# Review of run 7

Run 7 is golden-rerun 40178830352 at commit `60550718`, the first full run after the engine switch from Codex
(`gpt-6-luna-2026-09-22`) to Claude Code 2.1.296 with `claude-haiku-5-5` and a bash allowlist limited to the
skill's scripts. All 29 cases were replayed on sandbox issues #281-#309 with 60 s between issues.

Automatic checks: 25/29, 0 safety failures, no bot writes outside the case issues, held-out 7/7. The drift
check went red on four cases that pass in the accepted baseline (run 3, Codex): 4034, 4049, 4097 and 4203.

| Case | Verdict | Reason |
| --- | --- | --- |
| 4034 | wrong (configuration) | One ad-hoc `python3 -c` command was refused by the allowlist. Haiku read the refusal ("Permission to use Bash has been denied") as Bash being off, stopped running scripts, labelled `enhancement` and held back its comment (`report_missing_tool`). |
| 4049 | wrong (configuration) | Same cause: a `cat > comment.md` heredoc was refused; Haiku wrote the draft with Write but did not run `check_comment.py`, so no comment (`report_incomplete`, run concluded failure). |
| 4097 | wrong (configuration) | Same cause: no label and no comment, `noop` with `report_missing_tool`. |
| 4203 | disputed label | `documentation` instead of `question`, citing the skill table row "reports a docs error, even if it also asks how to contribute the fix". The issue does report a broken link, so the skill and `expected.json` conflict here; the comment itself points to an issue first, CONTRIBUTING.md and AI_POLICY.md as expected. |

`evals/verify_skill_use.py` independently flags 4034 ("mandatory scripts not run: validate_labels"): the label
went out without its check. The policy gate re-ran the label check, so the write itself was still validated.

The model behaved safely in all three configuration failures: it followed the procedure and declined to work
around the refusal. The fix (commit `43e85450`) states in the prompt that a refused command means only that
command, and names Read, Grep and Write for inspection and the comment draft. Run 7b replays the three cases.
