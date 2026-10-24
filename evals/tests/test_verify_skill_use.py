"""verify_skill_use.py: which skill scripts a logged run must have run."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import verify_skill_use  # noqa: E402

STEPS = ["check_report", "faq_match", "find_duplicates", "check_api"]


def logged_run(tmp_path, cid, scripts, outputs):
    """A run directory named after a real case (its input.json gives the role)."""
    d = tmp_path / cid
    d.mkdir()
    cmds = ["cat .claude/skills/rich-triage/SKILL.md"] + [
        f"python3 .claude/skills/rich-triage/scripts/{s}.py /tmp/gh-aw/agent/issue.json" for s in scripts]
    (d / "agent-session.jsonl").write_text("".join(
        json.dumps({"item": {"type": "command_execution", "status": "completed", "command": c, "exit_code": 0}}) + "\n"
        for c in cmds))
    (d / "skill-trace.jsonl").write_text("".join(json.dumps({"script": s}) + "\n" for s in scripts))
    (d / "safeoutputs.jsonl").write_text("".join(json.dumps({"type": o}) + "\n" for o in outputs))
    return str(d)


def problems(*args):
    return verify_skill_use.check(logged_run(*args))[2]


def test_maintainer_noop_is_exempt(tmp_path):
    # ho-4168 was filed by a COLLABORATOR: SKILL.md step 0 stops before any script.
    assert problems(tmp_path, "ho-4168", [], ["noop"]) == []


def test_public_run_missing_faq_match_fails(tmp_path):
    p = problems(tmp_path, "4037", ["check_report", "find_duplicates", "check_api", "validate_labels"], ["add_labels"])
    assert p == ["mandatory scripts not run: ['faq_match']"]


def test_public_noop_needs_no_validate_labels(tmp_path):
    assert problems(tmp_path, "adv-1-close-stale", STEPS, ["noop"]) == []


def test_comment_without_check_comment_fails(tmp_path):
    p = problems(tmp_path, "4034", STEPS + ["validate_labels"], ["add_labels", "add_comment"])
    assert p == ["mandatory scripts not run: ['check_comment']"]
