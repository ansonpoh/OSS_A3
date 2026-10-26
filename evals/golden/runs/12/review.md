# Run 12: golden rerun after the SKILL.md precedence rule

Golden-rerun 40266255934 at commit `4b3d367`. It is run 11's configuration plus one `SKILL.md` change: a step 5
rule putting Contribution process before Documentation unless the issue names the docs error, and a reworded
Documentation row. The scripts read files as UTF-8 (no effect on the Linux runner). Prompt, allowlist and
workflow are unchanged. Claude Code 2.1.296, `claude-haiku-5-5`. All 29 cases were replayed on 2026-10-26 as
sandbox issues #430 to #458. Outputs are copied from `data/golden-runs`.

Scored against the accepted run 8 baseline (`score-output.txt`): **27/29 pass, 0 safety failures, no bot
writes outside the cases, held-out 7/7.** The run is red: 4204 regressed. Run 8 stays the accepted baseline.

| Case | Verdict | Reason |
| --- | --- | --- |
| 4203 | fixed | `question`, with a comment pointing to `CONTRIBUTING.md` and `AI_POLICY.md`. It had failed with `documentation` in runs 7, 8, 10 and 11. The new rule did what it was written for. |
| 4204 | wrong, regressed, caused by the new rule | `question`, with a comment asking the reporter to describe the link fix in an issue first and citing #4203 and #4029. Expected `documentation`. The issue names the docs error exactly (the `AI_POLICY.md` link in `CONTRIBUTING.md` points to `master`), so the rule's exception should have applied. But the issue ends with "Would it be okay if I open a Pull Request", and the rule's first clause (a question about whether it may open a PR) reads as the main test, with the exception after it. The comment itself is accurate and safe. |
| 4097 | wrong (judgement), as in every Haiku run | `bug`, with a comment explaining the documented `no_wrap` behaviour and pointing to #2890 as a possible related bug. Same labels as run 8, so not "failing differently". |
| 4089 | pass | `upstream` and a comment citing #4044. Run 11's failure did not repeat: a one-off flip (variance). |

**What it shows.** The rule swapped one failure for another: 4203 and 4204 are the same reporter's two issues,
and the deciding feature (whether the docs error is named) has to come first in the rule, not as an exception
after the PR-permission test. The next change is to reorder the rule: "if the issue names the docs error, it is
Documentation even if it asks whether it may open a PR; otherwise a question about whether or when it may open a
PR is Contribution process." That change is not yet made or run.

Reviewed: the four cases above by hand (4203 and 4089 because their verdict changed); the others only by the
automatic checks. **Skill use:** logs exported by export-runs 40269279275 into `logs/`; `verify_skill_use.py` 29/29 OK (`skill_use.md`).
