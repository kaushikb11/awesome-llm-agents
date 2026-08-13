"""Regression tests for update_metrics.py.

The bug these guard against: entries were joined by whatever trailing newlines
each entry happened to carry, and only entries with a successful GitHub lookup
were rebuilt with them. So a framework whose repo 404'd silently lost its blank
line and got glued onto its predecessor. The next weekly run could no longer see
it as an entry boundary, so neighbours merged into one blob and the damage
compounded -- 35 of 59 entries over nine months of green CI.

Runs standalone (`python3 tests/test_update_metrics.py`) or under pytest. Every
network call is stubbed, so no token or dependencies are needed.
"""
import argparse
import os
import re
import sys
import types

# requests/dotenv are only needed for the real network path, which these tests
# never touch. Stub them so the suite runs on a bare interpreter.
_requests = types.ModuleType("requests")
_requests.get = lambda *a, **k: (_ for _ in ()).throw(
    AssertionError("test attempted a real network call")
)
sys.modules.setdefault("requests", _requests)
_dotenv = types.ModuleType("dotenv")
_dotenv.load_dotenv = lambda *a, **k: None
sys.modules.setdefault("dotenv", _dotenv)

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import update_metrics  # noqa: E402

FIXTURE = """# Awesome LLM Agent Frameworks

A curated list. (Last updated: 2020-01-01)

## Frameworks

- [Alive One](https://github.com/acme/alive-one) - First framework

  10 stars · 1 forks · 1 contributors · 0 issues · Python · MIT

  - Feature A
  - Feature B


- [Dead Repo](https://github.com/acme/dead-repo) - This repo 404s

  - Feature C
  - Feature D


- [Alive Two](https://github.com/acme/alive-two) - Third framework

  20 stars · 2 forks · 2 contributors · 0 issues · Go · Apache-2.0

  - Feature E
  - Feature F
"""

FAKE_METRICS = {
    "stars": 999,
    "forks": 99,
    "open_issues": 9,
    "contributors": 9,
    "language": "Python",
    "license": "MIT",
}


def _fake_lookup(url):
    """Mimic the real function: None for a repo that 404s."""
    return None if "dead-repo" in url else dict(FAKE_METRICS)


def _run(tmp_path, times=1):
    """Write the fixture, run the updater N times, return each run's output."""
    readme = os.path.join(str(tmp_path), "README.md")
    with open(readme, "w") as f:
        f.write(FIXTURE)

    original = update_metrics.get_repo_metrics
    update_metrics.get_repo_metrics = _fake_lookup
    try:
        outputs = []
        args = argparse.Namespace(url=None, name=None)
        for _ in range(times):
            update_metrics.update_readme_with_metrics(readme, args)
            with open(readme) as f:
                outputs.append(f.read())
        return outputs
    finally:
        update_metrics.get_repo_metrics = original


def _entry_starts(text):
    """Entries that begin at column 0 -- i.e. still parseable as entries."""
    return len(re.findall(r"^- \[", text.split("## Frameworks", 1)[1], re.M))


def _links(text):
    return re.findall(r"- \[[^\]]+\]\(https://github[^)\s]+\)", text)


def test_failed_lookup_does_not_merge_entries(tmp_path):
    """A repo that 404s must not swallow the entry after it."""
    out = _run(tmp_path)[0]
    assert _entry_starts(out) == 3, "an entry lost its separator and got merged"
    assert len(_links(out)) == 3


def test_corruption_does_not_compound_across_runs(tmp_path):
    """The original bug only showed up on the third run -- check several."""
    outs = _run(tmp_path, times=3)
    for i, out in enumerate(outs, 1):
        assert _entry_starts(out) == 3, f"entries merged by run {i}"
        assert len(_links(out)) == 3, f"a link was lost by run {i}"


def test_is_idempotent(tmp_path):
    """Repeated runs must converge, not keep rewriting the file."""
    outs = _run(tmp_path, times=3)
    assert outs[0] == outs[1] == outs[2], "output still changing between runs"


def test_failed_lookup_preserves_entry_content(tmp_path):
    """A 404 must leave the entry untouched, not drop it."""
    out = _run(tmp_path, times=3)[-1]
    assert "This repo 404s" in out
    assert "- Feature C" in out and "- Feature D" in out


def test_live_entries_get_refreshed_metrics(tmp_path):
    out = _run(tmp_path, times=3)[-1]
    assert out.count("999 stars") == 2, "live entries were not refreshed"


def test_trailing_section_survives(tmp_path):
    """Anything after the last entry (e.g. ## License) rides along inside the
    final chunk. It must stay a top-level heading, not get folded into the
    last framework's bullets."""
    readme = os.path.join(str(tmp_path), "README.md")
    with open(readme, "w") as f:
        f.write(FIXTURE + "\n\n## License\n\n[CC0 1.0](LICENSE)\n")

    original = update_metrics.get_repo_metrics
    update_metrics.get_repo_metrics = _fake_lookup
    try:
        args = argparse.Namespace(url=None, name=None)
        outs = []
        for _ in range(3):
            update_metrics.update_readme_with_metrics(readme, args)
            with open(readme) as f:
                outs.append(f.read())
    finally:
        update_metrics.get_repo_metrics = original

    assert outs[0] == outs[1] == outs[2], "trailing section not stable"
    assert re.search(r"^## License", outs[-1], re.M), "License heading was mangled"
    assert "[CC0 1.0](LICENSE)" in outs[-1]


if __name__ == "__main__":
    import shutil
    import tempfile
    import traceback

    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    failed = 0
    for test in tests:
        tmp = tempfile.mkdtemp()
        try:
            test(tmp)
            print(f"PASS  {test.__name__}")
        except Exception:
            failed += 1
            print(f"FAIL  {test.__name__}")
            traceback.print_exc()
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    sys.exit(1 if failed else 0)
