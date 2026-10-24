"""The policy gate that runs in the threat-detection job before any write."""
import os
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(REPO, ".github", "triage"))
os.environ.setdefault("RICH_TRIAGE_TRACE", os.devnull)
os.chdir(REPO)

import policy_gate  # noqa: E402

FOOTER = "<sub>Automated first-response triage (rich-triage skill). A maintainer will review.</sub>"
PUBLIC = {"author_association": "NONE", "body": "report"}


def labels(*names):
    return {"type": "add_labels", "labels": [{"name": n} for n in names]}


def comment(text):
    return {"type": "add_comment", "body": f"{text}\n\n{FOOTER}"}


def test_clean_output_passes():
    assert policy_gate.gate([labels("bug"), comment("Thanks, reproduced.")], PUBLIC) == []


def test_noop_passes_for_maintainer():
    assert policy_gate.gate([{"type": "noop", "message": "maintainer"}],
                            {"author_association": "COLLABORATOR", "body": ""}) == []


def test_blocks_off_list_and_too_many_labels():
    p = policy_gate.gate([labels("wontfix", "bug", "question", "documentation")], PUBLIC)
    assert any("wontfix" in x for x in p) and any("maximum is 3" in x for x in p)


def test_blocks_second_comment_and_second_label_call():
    p = policy_gate.gate([labels("bug"), labels("question"), comment("a"), comment("b")], PUBLIC)
    assert "more than one add_labels call" in p and "2 comments; at most 1" in p


def test_blocks_upstream_issue_url_and_missing_footer():
    p = policy_gate.gate([{"type": "add_comment",
                           "body": "See https://github.com/Textualize/rich/issues/1"}], PUBLIC)
    assert any("by URL" in x for x in p) and any("footer" in x for x in p)


def test_blocks_duplicate_without_issue_number():
    p = policy_gate.gate([labels("question", "duplicate"), comment("Asked before.")], PUBLIC)
    assert "duplicate label without a comment naming the earlier issue" in p


def test_blocks_any_write_on_maintainer_issue_including_replayed_role():
    replay = {"author_association": "OWNER",
              "body": "x\n\n<!-- golden-case: c filed: 2026-01-01T00:00:00Z as: COLLABORATOR -->"}
    assert policy_gate.gate([labels("bug")], replay)
    public_replay = {**replay, "body": replay["body"].replace("COLLABORATOR", "NONE")}
    assert policy_gate.gate([labels("bug")], public_replay) == []


def test_cli_exits_nonzero_on_violation(tmp_path):
    out = tmp_path / "agent_output.json"
    ev = tmp_path / "event.json"
    out.write_text('{"items": [{"type": "add_labels", "labels": [{"name": "wontfix"}]}]}')
    ev.write_text('{"issue": {"author_association": "NONE", "body": ""}}')
    gate = os.path.join(REPO, ".github", "triage", "policy_gate.py")
    r = subprocess.run([sys.executable, gate, str(out), str(ev)], cwd=REPO, capture_output=True, text=True)
    assert r.returncode == 1 and '"ok": false' in r.stdout
