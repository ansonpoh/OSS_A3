# Review of run 7b

Run 7b is a local replay of the three cases run 7 lost to the allowlist misreading (sandbox issues #310-#312,
runs 40181475862, 40181543484, 40181615251), at commit `43e85450` with the prompt fix. Scored locally with
`evals/score.py`. The accepted baseline was not changed.

| Case | Verdict | Reason |
| --- | --- | --- |
| 4034 | correct | `enhancement` and a comment pointing to Discussions, `TaskProgressColumn(show_speed=True)` and a `ProgressColumn` subclass. Related #3835. All six scripts ran. |
| 4049 | correct | `enhancement` and a comment pointing to Discussions and a `RegexHighlighter` subclass. Related #3318. One wording slip: "feature template" links to Discussions. |
| 4097 | wrong (judgement) | The fix worked: after a refused command Haiku wrote "Bash is restricted for that command", switched to Grep and ran every script. It then labelled `bug` with no comment, the usage-question-versus-bug confusion that also failed 4097 on Codex in runs 1 and 6. |
