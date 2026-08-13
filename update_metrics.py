"""Generate README.md from the entry files in data/frameworks/.

Every run rebuilds the file from scratch, so the README is a pure function of
the data directory plus whatever the GitHub API returns. Nothing is parsed back
out of the README, which is what makes this safe: the previous version of this
script edited the README in place, and an entry whose repo 404'd silently lost
the blank line separating it from its neighbour. The next run could no longer
see the boundary, so entries merged and the damage compounded -- 35 of 59
entries over nine months. Regenerating removes that whole class of bug.
"""
import argparse
import glob
import os
import re
import sys
import textwrap
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

DATA_DIR = "data/frameworks"
HEADER = "data/header.md"
FOOTER = "data/footer.md"
MAX_DESCRIPTION = 60

# Rendered in this order. An entry naming any other section is an error, which
# keeps the taxonomy from drifting one pull request at a time.
SECTIONS = [
    "Core Frameworks",
    "Multi-Agent Orchestration",
    "CLI Agent Harnesses",
    "Low-Code & Visual Builders",
    "Retrieval & Data",
    "Memory & Context",
    "Agent Infrastructure",
    "Safety, Security & Evaluation",
    "Domain-Specific Agents",
    "Research & Experimental",
    "Autonomous Agents (2023 wave)",
    "Inactive",
]

# Shown under the heading, before the table.
SECTION_NOTES = {
    "Autonomous Agents (2023 wave)": (
        "The 2023 autonomous-agent wave. Listed for their influence; several are "
        "no longer actively developed."
    ),
    "CLI Agent Harnesses": (
        "Tools that run, sandbox or coordinate command-line coding agents such as "
        "Claude Code, Codex and Gemini CLI."
    ),
    "Inactive": (
        "Archived, or no push in over 12 months. Kept because they are widely "
        "referenced and readers benefit from knowing their status."
    ),
}

REQUIRED_FIELDS = ("name", "repo", "section", "description")
REPO_RE = re.compile(r"^https://github\.com/([^/\s]+)/([^/\s]+?)/?$")

# GitHub reports a nonstandard or unrecognised license as NOASSERTION, which is
# noise in a table. The repo still has a license; it just is not SPDX-matched.
LICENSE_LABELS = {"NOASSERTION": "Other", "": "—", None: "—"}


class EntryError(Exception):
    """A data file is malformed. Raised with the path so CI points at the file."""


def parse_entry(path):
    """Parse one entry file.

    The format is deliberately four flat `key: value` lines -- see
    CONTRIBUTING.md. Values may contain colons; only the first one splits.
    """
    fields = {}
    with open(path) as f:
        for lineno, raw in enumerate(f, 1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if ":" not in line:
                raise EntryError(f"{path}:{lineno}: expected 'key: value'")
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if key not in REQUIRED_FIELDS:
                raise EntryError(f"{path}:{lineno}: unknown field {key!r}")
            if key in fields:
                raise EntryError(f"{path}:{lineno}: duplicate field {key!r}")
            fields[key] = value

    missing = [f for f in REQUIRED_FIELDS if f not in fields]
    if missing:
        raise EntryError(f"{path}: missing field(s): {', '.join(missing)}")
    if fields["section"] not in SECTIONS:
        raise EntryError(
            f"{path}: unknown section {fields['section']!r}. "
            f"One of: {', '.join(SECTIONS)}"
        )
    if not REPO_RE.match(fields["repo"]):
        raise EntryError(f"{path}: repo must be https://github.com/owner/name")
    if len(fields["description"]) > MAX_DESCRIPTION:
        raise EntryError(
            f"{path}: description is {len(fields['description'])} chars, "
            f"limit is {MAX_DESCRIPTION}"
        )
    if not fields["description"]:
        raise EntryError(f"{path}: description is empty")

    fields["path"] = path
    fields["slug"] = REPO_RE.match(fields["repo"]).group(0).lower()
    return fields


def load_entries(data_dir=DATA_DIR):
    paths = sorted(glob.glob(os.path.join(data_dir, "*.yml")))
    entries = [parse_entry(p) for p in paths]
    seen = {}
    for e in entries:
        if e["slug"] in seen:
            raise EntryError(
                f"{e['path']}: duplicate repo, already listed in {seen[e['slug']]}"
            )
        seen[e["slug"]] = e["path"]
    return entries


def get_repo_metrics(repo_url):
    """Return metrics for a repo, or None if it cannot be reached."""
    match = REPO_RE.match(repo_url)
    if not match:
        return None
    owner, repo = match.group(1), match.group(2)
    api_url = f"https://api.github.com/repos/{owner}/{repo}"

    token = os.getenv("GITHUB_TOKEN")
    headers = {"Accept": "application/vnd.github.v3+json"}
    if token:
        headers["Authorization"] = f"token {token}"

    try:
        response = requests.get(api_url, headers=headers, timeout=30)
        if response.status_code != 200:
            return None
        data = response.json()
        return {
            "stars": data.get("stargazers_count", 0),
            "language": data.get("language") or "—",
            "license": LICENSE_LABELS.get(
                (data.get("license") or {}).get("spdx_id"),
                (data.get("license") or {}).get("spdx_id") or "—",
            ),
            "updated": (data.get("pushed_at") or "")[:7] or "—",
            "archived": bool(data.get("archived")),
            "full_name": data.get("full_name", f"{owner}/{repo}"),
        }
    except Exception as exc:  # noqa: BLE001 - a bad entry must not fail the run
        print(f"  ! {repo_url}: {exc}", file=sys.stderr)
        return None


def anchor(section):
    """GitHub's heading-anchor rules: lowercase, drop punctuation, dash spaces."""
    a = section.lower()
    a = re.sub(r"[^\w\s-]", "", a)
    return re.sub(r"\s+", "-", a.strip())


def render(entries, metrics_by_repo, today):
    with open(HEADER) as f:
        header = f.read().rstrip("\n")
    header = re.sub(
        r"Last updated: \d{4}-\d{2}-\d{2}", f"Last updated: {today}", header
    )

    by_section = {s: [] for s in SECTIONS}
    for e in entries:
        by_section[e["section"]].append(e)

    parts = [header, ""]

    parts.append("## Contents")
    parts.append("")
    for s in SECTIONS:
        if by_section[s]:
            parts.append(f"- [{s}](#{anchor(s)}) ({len(by_section[s])})")
    parts.append("")

    for s in SECTIONS:
        rows = by_section[s]
        if not rows:
            continue
        # Unranked repos (failed lookup) sort last rather than to the top.
        rows.sort(
            key=lambda e: (metrics_by_repo.get(e["repo"]) or {}).get("stars", -1),
            reverse=True,
        )
        parts.append(f"## {s}")
        parts.append("")
        if s in SECTION_NOTES:
            parts.append(textwrap.fill(SECTION_NOTES[s], width=88))
            parts.append("")
        parts.append("| Project | Stars | Language | License | Updated | Description |")
        parts.append("| --- | ---: | --- | --- | --- | --- |")
        for e in rows:
            m = metrics_by_repo.get(e["repo"])
            if m:
                stars = f"{m['stars']:,}"
                lang, lic, updated = m["language"], m["license"], m["updated"]
                if m["archived"]:
                    updated = f"{updated} (archived)"
            else:
                stars = lang = lic = updated = "—"
            desc = e["description"].replace("|", "\\|")
            parts.append(
                f"| [{e['name']}]({e['repo']}) | {stars} | {lang} | "
                f"{lic} | {updated} | {desc} |"
            )
        parts.append("")

    with open(FOOTER) as f:
        parts.append(f.read().rstrip("\n"))

    return "\n".join(parts).rstrip("\n") + "\n"


def main():
    parser = argparse.ArgumentParser(description="Generate README.md from data/")
    parser.add_argument(
        "--check",
        action="store_true",
        help="validate entries and exit without calling the GitHub API",
    )
    parser.add_argument("--output", default="README.md")
    args = parser.parse_args()

    entries = load_entries()
    print(f"loaded {len(entries)} entries")
    if args.check:
        print("✨ entries valid")
        return 0

    metrics_by_repo = {}
    for e in entries:
        m = get_repo_metrics(e["repo"])
        if m is None:
            print(f"  ! no metrics for {e['name']} ({e['repo']})", file=sys.stderr)
        metrics_by_repo[e["repo"]] = m

    today = datetime.now().strftime("%Y-%m-%d")
    with open(args.output, "w") as f:
        f.write(render(entries, metrics_by_repo, today))
    print(f"✨ wrote {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
