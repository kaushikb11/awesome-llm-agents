"""Tests for the README generator.

History worth keeping in mind: the previous script edited README.md in place.
An entry whose repo returned 404 was written back without the blank line that
separated it from its neighbour, the next run could no longer see the entry
boundary, and neighbours merged into one blob -- 35 of 59 entries corrupted
over nine months of green CI. Generating the file from data/ removes that class
of bug entirely, and the tests below pin the properties that keep it removed.

Runs standalone (`python3 tests/test_update_metrics.py`) or under pytest. All
network calls are stubbed, so no token or dependencies are required.
"""
import importlib.util
import os
import re
import sys
import types

_requests = types.ModuleType("requests")
_requests.get = lambda *a, **k: (_ for _ in ()).throw(
    AssertionError("test attempted a real network call")
)
sys.modules.setdefault("requests", _requests)
_dotenv = types.ModuleType("dotenv")
_dotenv.load_dotenv = lambda *a, **k: None
sys.modules.setdefault("dotenv", _dotenv)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_spec = importlib.util.spec_from_file_location(
    "um", os.path.join(ROOT, "update_metrics.py")
)
um = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(um)


def write_entry(d, slug, **kw):
    fields = {
        "name": kw.get("name", slug),
        "repo": kw.get("repo", f"https://github.com/acme/{slug}"),
        "section": kw.get("section", "Core Frameworks"),
        "description": kw.get("description", f"Does {slug} things"),
    }
    path = os.path.join(d, f"{slug}.yml")
    with open(path, "w") as f:
        for k in ("name", "repo", "section", "description"):
            f.write(f"{k}: {fields[k]}\n")
    return path


def metrics(stars=100, archived=False):
    return {
        "stars": stars,
        "language": "Python",
        "license": "MIT",
        "updated": "2026-08",
        "archived": archived,
        "full_name": "acme/x",
    }


def _render(d, live=None, extra=None):
    """Render entries in dir d. `live` names the slugs that resolve."""
    entries = um.load_entries(d)
    live = live if live is not None else {e["name"] for e in entries}
    m = {}
    for i, e in enumerate(entries):
        m[e["repo"]] = metrics(stars=1000 - i * 10) if e["name"] in live else None
    if extra:
        m.update(extra)
    return um.render(entries, m, "2026-08-14")


# --- the original bug class, now structurally impossible -------------------

def test_failed_lookup_keeps_entry_and_neighbours(tmp_path):
    d = str(tmp_path)
    write_entry(d, "alive-one", name="AliveOne")
    write_entry(d, "dead-repo", name="DeadRepo")
    write_entry(d, "alive-two", name="AliveTwo")
    out = _render(d, live={"AliveOne", "AliveTwo"})
    for n in ("AliveOne", "DeadRepo", "AliveTwo"):
        assert f"[{n}](" in out, f"{n} vanished when a neighbour failed"
    assert out.count("| [") == 3, "entries merged or were dropped"


def test_generation_is_idempotent(tmp_path):
    d = str(tmp_path)
    write_entry(d, "alive-one", name="AliveOne")
    write_entry(d, "dead-repo", name="DeadRepo")
    runs = [_render(d, live={"AliveOne"}) for _ in range(3)]
    assert runs[0] == runs[1] == runs[2], "output changes between runs"


def test_output_does_not_depend_on_previous_readme(tmp_path):
    """The old script fed the README back into itself; this one must not."""
    d = str(tmp_path)
    write_entry(d, "only", name="Only")
    a = _render(d)
    b = _render(d)
    assert a == b
    assert a.count("[Only](") == 1, "entry duplicated across runs"


# --- validation ------------------------------------------------------------

def test_unknown_section_is_rejected(tmp_path):
    d = str(tmp_path)
    write_entry(d, "x", section="Made Up Section")
    try:
        um.load_entries(d)
    except um.EntryError as e:
        assert "unknown section" in str(e)
    else:
        raise AssertionError("expected EntryError")


def test_overlong_description_is_rejected(tmp_path):
    d = str(tmp_path)
    write_entry(d, "x", description="y" * (um.MAX_DESCRIPTION + 1))
    try:
        um.load_entries(d)
    except um.EntryError as e:
        assert "description" in str(e)
    else:
        raise AssertionError("expected EntryError")


def test_duplicate_repo_is_rejected(tmp_path):
    d = str(tmp_path)
    write_entry(d, "a", name="A", repo="https://github.com/acme/same")
    write_entry(d, "b", name="B", repo="https://github.com/acme/same")
    try:
        um.load_entries(d)
    except um.EntryError as e:
        assert "duplicate repo" in str(e)
    else:
        raise AssertionError("expected EntryError")


def test_bad_repo_url_is_rejected(tmp_path):
    d = str(tmp_path)
    write_entry(d, "x", repo="https://gitlab.com/acme/x")
    try:
        um.load_entries(d)
    except um.EntryError:
        pass
    else:
        raise AssertionError("expected EntryError")


def test_missing_field_is_rejected(tmp_path):
    d = str(tmp_path)
    path = os.path.join(d, "x.yml")
    with open(path, "w") as f:
        f.write("name: X\nrepo: https://github.com/acme/x\n")
    try:
        um.load_entries(d)
    except um.EntryError as e:
        assert "missing field" in str(e)
    else:
        raise AssertionError("expected EntryError")


def test_description_may_contain_a_colon(tmp_path):
    d = str(tmp_path)
    write_entry(d, "x", name="X", description="Agents: the good kind")
    out = _render(d)
    assert "Agents: the good kind" in out


# --- rendering -------------------------------------------------------------

def test_rows_sort_by_stars_within_section(tmp_path):
    d = str(tmp_path)
    write_entry(d, "small", name="Small")
    write_entry(d, "big", name="Big")
    entries = um.load_entries(d)
    m = {e["repo"]: metrics(stars=5 if e["name"] == "Small" else 5000) for e in entries}
    out = um.render(entries, m, "2026-08-14")
    assert out.index("[Big](") < out.index("[Small](")


def test_unranked_entries_sort_last(tmp_path):
    d = str(tmp_path)
    write_entry(d, "ranked", name="Ranked")
    write_entry(d, "unranked", name="Unranked")
    out = _render(d, live={"Ranked"})
    assert out.index("[Ranked](") < out.index("[Unranked](")


def test_archived_is_marked(tmp_path):
    d = str(tmp_path)
    write_entry(d, "old", name="Old", section="Inactive")
    entries = um.load_entries(d)
    out = um.render(entries, {entries[0]["repo"]: metrics(archived=True)}, "2026-08-14")
    assert "(archived)" in out


def test_pipe_in_description_is_escaped(tmp_path):
    """An unescaped pipe would silently split the table row."""
    d = str(tmp_path)
    write_entry(d, "x", name="X", description="Either a | or b")
    out = _render(d)
    row = [ln for ln in out.split("\n") if "[X](" in ln][0]
    assert "\\|" in row, "pipe in description was not escaped"
    # Only unescaped pipes delimit columns; 6 columns means 7 delimiters.
    unescaped = len(re.findall(r"(?<!\\)\|", row))
    assert unescaped == 7, f"row has {unescaped} delimiters, expected 7"


def test_empty_sections_are_omitted(tmp_path):
    d = str(tmp_path)
    write_entry(d, "x", section="Core Frameworks")
    out = _render(d)
    assert "## Core Frameworks" in out
    assert "## Inactive" not in out


def test_contents_links_match_section_anchors(tmp_path):
    d = str(tmp_path)
    write_entry(d, "a", name="A", section="Safety, Security & Evaluation")
    write_entry(d, "b", name="B", section="Low-Code & Visual Builders")
    out = _render(d)
    for section in ("Safety, Security & Evaluation", "Low-Code & Visual Builders"):
        assert f"(#{um.anchor(section)})" in out
    assert "#safety-security-evaluation" in out
    assert "#low-code-visual-builders" in out


# --- the real data ---------------------------------------------------------

def test_shipped_entries_are_valid(tmp_path):
    """The entries actually in this repo must pass validation."""
    entries = um.load_entries(os.path.join(ROOT, um.DATA_DIR))
    assert len(entries) > 0
    for e in entries:
        assert e["section"] in um.SECTIONS
        assert len(e["description"]) <= um.MAX_DESCRIPTION


if __name__ == "__main__":
    import shutil
    import tempfile
    import traceback

    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    failed = 0
    for t in tests:
        tmp = tempfile.mkdtemp()
        try:
            t(tmp)
            print(f"PASS  {t.__name__}")
        except Exception:
            failed += 1
            print(f"FAIL  {t.__name__}")
            traceback.print_exc()
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    sys.exit(1 if failed else 0)
