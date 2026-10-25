"""The canary workflows must test the same limits the triage workflow uses."""
import os
import re

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WF = os.path.join(REPO, ".github", "workflows")


def frontmatter_block(name, key):
    text = open(os.path.join(WF, name), encoding="utf-8").read().split("---")[1]
    m = re.search(r"^" + key + r":\n(?:(?:  .*|\s*)\n)+", text, re.M)
    return m.group(0) if m else None


def test_cap_test_uses_the_triage_safe_outputs_unchanged():
    assert frontmatter_block("cap-test.md", "safe-outputs") == frontmatter_block("rich-triage.md", "safe-outputs")


def test_policy_gate_is_in_threat_detection():
    block = frontmatter_block("rich-triage.md", "safe-outputs")
    assert "threat-detection:" in block and ".github/triage/policy_gate.py" in block


def test_writes_use_only_the_workflow_token():
    block = frontmatter_block("rich-triage.md", "safe-outputs")
    assert re.search(r"^  github-token: \$\{\{ secrets\.GITHUB_TOKEN \}\}$", block, re.M)


def test_lock_file_has_no_personal_token_fallback_for_writes():
    lock = open(os.path.join(WF, "rich-triage.lock.yml"), encoding="utf-8").read()
    assert "github-token: ${{ secrets.GH_AW_GITHUB_TOKEN || secrets.GITHUB_TOKEN }}" not in lock


def test_budget_test_has_a_one_credit_cap():
    text = open(os.path.join(WF, "budget-test.md"), encoding="utf-8").read()
    assert re.search(r"^max-ai-credits: 1\b", text, re.M)
    assert re.search(r"^max-daily-ai-credits: 1\b", text, re.M)


def test_canaries_run_only_on_owner_labels():
    for name, label in (("cap-test.md", "cap-test"), ("budget-test.md", "budget-test")):
        text = open(os.path.join(WF, name), encoding="utf-8").read()
        assert f"names: [{label}]" in text and "roles: [admin]" in text
