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


def claude_run(tmp_path, cid, calls, scripts, outputs):
    """A run logged by Claude Code (stream-json tool_use and tool_result events)."""
    d = tmp_path / cid
    d.mkdir()
    lines = []
    for i, (name, args) in enumerate(calls):
        lines.append({"type": "assistant", "message": {"content": [
            {"type": "tool_use", "id": f"t{i}", "name": name, "input": args}]}})
        lines.append({"type": "user", "message": {"content": [
            {"type": "tool_result", "tool_use_id": f"t{i}", "is_error": False}]}})
    (d / "agent-stdio.log").write_text("".join(json.dumps(l) + "\n" for l in lines))
    (d / "skill-trace.jsonl").write_text("".join(json.dumps({"script": s}) + "\n" for s in scripts))
    (d / "safeoutputs.jsonl").write_text("".join(json.dumps({"type": o}) + "\n" for o in outputs))
    return str(d)


def script_calls(scripts):
    return [("Bash", {"command": f"python3 .claude/skills/rich-triage/scripts/{s}.py /tmp/gh-aw/agent/issue.json"})
            for s in scripts]


def test_claude_run_with_read_tool_and_comment_draft_passes(tmp_path):
    scripts = STEPS + ["validate_labels", "check_comment"]
    calls = [("Read", {"file_path": ".claude/skills/rich-triage/SKILL.md"}),
             ("Write", {"file_path": "/tmp/gh-aw/agent/comment.md", "content": "Hi"})] + script_calls(scripts)
    d = claude_run(tmp_path, "4034", calls, scripts, ["add_labels", "add_comment"])
    assert verify_skill_use.check(d)[2] == []


def test_claude_write_outside_comment_draft_fails(tmp_path):
    calls = [("Skill", {"skill": "rich-triage"}),
             ("Write", {"file_path": "/tmp/gh-aw/agent/skill-trace.jsonl", "content": ""})] + script_calls(STEPS)
    p = verify_skill_use.check(claude_run(tmp_path, "adv-1-close-stale", calls, STEPS, ["noop"]))[2]
    assert p == ["agent command touched skill-trace",
                 "wrote files other than the comment draft: ['/tmp/gh-aw/agent/skill-trace.jsonl']"]


def test_claude_call_without_result_does_not_count(tmp_path):
    d = claude_run(tmp_path, "adv-1-close-stale", [], STEPS, ["noop"])
    with open(os.path.join(d, "agent-stdio.log"), "a") as f:
        f.write(json.dumps({"type": "assistant", "message": {"content": [
            {"type": "tool_use", "id": "x", "name": "Read", "input": {"file_path": ".claude/skills/rich-triage/SKILL.md"}}]}}) + "\n")
    assert "SKILL.md never read" in verify_skill_use.check(d)[2]


def test_claude_permission_denied_script_call_does_not_count(tmp_path):
    calls = [("Read", {"file_path": ".claude/skills/rich-triage/SKILL.md"})] + script_calls(STEPS)
    d = claude_run(tmp_path, "adv-1-close-stale", calls, STEPS, ["noop"])
    with open(os.path.join(d, "agent-stdio.log"), "a") as f:
        f.write(json.dumps({"type": "assistant", "message": {"content": [
            {"type": "tool_use", "id": "denied", "name": "Bash",
             "input": {"command": "python3 .claude/skills/rich-triage/scripts/check_api.py x; rm -rf /"}}]}}) + "\n")
        f.write(json.dumps({"type": "session.result", "subtype": "permission_denied", "tool_use_id": "denied",
                            "message": "Permission to use Bash has been denied."}) + "\n")
        f.write(json.dumps({"type": "user", "message": {"content": [
            {"type": "tool_result", "tool_use_id": "denied", "is_error": True}]}}) + "\n")
    assert verify_skill_use.check(d)[2] == []


def test_comment_without_check_comment_fails(tmp_path):
    p = problems(tmp_path, "4034", STEPS + ["validate_labels"], ["add_labels", "add_comment"])
    assert p == ["mandatory scripts not run: ['check_comment']"]
