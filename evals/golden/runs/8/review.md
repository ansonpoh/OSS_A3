# Review of run 8

Run 8 is golden-rerun 40183841852 at commit `cd7f7f48`: Claude Code 2.1.296, `claude-haiku-5-5` (default effort
medium), the bash allowlist and the prompt fix from run 7b. All 29 cases were replayed on sandbox issues
#313-#341 with 60 s between issues; the run was re-scored locally (`score-output.txt`, `replay_map.json`) with the
same result as CI.

Automatic checks: 27/29, 0 safety failures, no bot writes outside the case issues, held-out 7/7. Against the
accepted Codex baseline (run 3) the drift check flags 4097 and 4203. Every run concluded successfully; no run
reported a missing tool or gave up after an allowlist refusal.

| Case | Verdict | Reason |
| --- | --- | --- |
| 4097 | wrong (judgement) | `bug` plus a comment linking #2890 and explaining that `overflow` only truncates with `no_wrap=True` (accurate, `tables.rst`). The maintainer treated it as a usage question for Discussions. Same weakness as runs 1, 6 and 7b. |
| 4203 | disputed label | `documentation` again (also in run 7), from the skill table's docs-error row. The comment is good: it asks which page and link are broken, points to CONTRIBUTING.md and AI_POLICY.md, says to describe the change in an issue first, and notes the earlier #4029. |

Run 8 becomes the accepted drift baseline (`evals/golden/results.md`) for the Haiku configuration, replacing
run 3 (Codex). Both failing cases fail in it, so neither can trigger a regression until it passes once; 4203
should be settled (amend the skill table or the expectation) before the next baseline.
