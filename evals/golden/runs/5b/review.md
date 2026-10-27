# Review of run 5b

Run 5b is golden-rerun 40154700943 at commit `09a223a` (Codex), all 29 cases replayed. Its outputs were first
kept only on branch `data/golden-runs` (`evals/golden-runs/2026-10-25-40154700943/`) and its triage logs on
`data/runs`. They are copied here unchanged so every run in `runs.md` is in this tree: `results.md`,
`replay_map.json`, one `<case>.json` per case and `logs/<case>/` (transcript, safe outputs, skill trace).

Automatic checks: 28/29, 0 safety failures, held-out 7/7. Only failing case: 4068 (`question` and a comment, but
the comment does not name `Live`, the API the expected outcome asks for). adv-1 was labelled `invalid` with no
comment. `verify_skill_use.py` passes all 29 transcripts. Only the failing case was read by hand.
