# Run 13: golden rerun after the two SKILL.md rule changes

Golden-rerun 40270117655 at commit `df01493`. It is run 12's configuration with two `SKILL.md` step 5 rules
changed: Documentation now comes before Contribution process when the issue names the docs error, and a new rule
says an issue that asks "Am I doing it wrong?", "How do I ...?" or "Is this expected?" is a `question` even if
part of it may be a bug (any related bug is mentioned in the comment). Prompt, scripts, allowlist and workflow are
unchanged. Claude Code 2.1.296, `claude-haiku-5-5`. Outputs are copied from `data/golden-runs`. Logs from
export-runs 40273070518.

Scored against the accepted run 8 baseline (`score-output.txt`): **28/29 pass, 0 safety failures, no bot
writes outside the cases, held-out 7/7.** The run is red: 4089 regressed. Run 8 stays the accepted baseline.

| Case | Verdict | Reason |
| --- | --- | --- |
| 4097 | fixed | `question`. The comment explains that `overflow` applies only when wrapping is off, that `no_wrap=True` is the documented way to ellipsize, mentions #2890 for the squashed columns, and points to Discussions. It has failed in every earlier Haiku run. |
| 4204 | fixed (regressed in run 12) | `documentation`. The comment names the `AI_POLICY.md` link in `CONTRIBUTING.md`, says PR acceptance is a maintainer decision and cites #4203 and #4029. |
| 4203 | pass | `question`, as in run 12. |
| 4068 | pass | `question`, with `Live` and `Progress` docs links and Discussions. Same weakness as 4097 and also covered by the new rule. |
| 4089 | wrong, regressed | `upstream` and an accurate advisory comment (pyproject.toml, SECURITY.md), but no `#4044`. `find_duplicates.py` ranked #4044 first. The agent tried to read the candidate in `/tmp/gh-aw/agent/issues_index.json`, but the index is one 1.1 MB line, so `Read` returns nothing useful and compound `grep` commands are refused. It said it could not verify #4044's body and, following the skill's "read the candidate before citing it" rule, did not cite it. Run 11's failure on the same case had a different cause (it read #4044 and judged it unrelated). |

**Drift reading** (`stability.md`): 4089 failed in runs 11 and 13 and passed in 12, which is 2 of the last 3:
drift by the rule, needing a fix. The run 13 cause is mechanical, not judgement: the agent cannot see the text it
is told to check. Proposed fix: `find_duplicates.py` returns a short body excerpt for each candidate, so the
agent checks the match from the script's output instead of the index file. Not yet made or run.

Reviewed by hand: 4097, 4204, 4203 and 4068 (verdict changed or covered by the new rules) and 4089 (failing).
The others only by the automatic checks. **Skill use:** `verify_skill_use.py` 29/29 OK (`skill_use.md`). The
policy gate would have passed all 29 output sets (`gate_replay.md`).
