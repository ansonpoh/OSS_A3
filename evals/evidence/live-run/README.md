# Live public-user run

Every golden run replays cases from the owner's account through the replay path (replay marker, restored author
role, rewound index). This run checks the path a real reporter takes: an issue opened in the browser by a second
GitHub account with no role on the repository.

- `input.json`: upstream Textualize/rich#4029 as fetched on 2026-10-26 (never edited after filing). Not a golden
  case.
- `body.txt`: its body exactly as filed. The original was posted with literal `\n` sequences, so it is one line.
  Paste it unchanged.
- `expected.json`: the expected outcome, written at 2026-10-26T12:47:06Z, before the issue was opened.

## Steps (second account)

1. New issue → "Open a blank issue" (the original used no template, so it had no `Needs triage` label).
2. Title: `Request: Enable PRs from forks for contributors`
3. Body: the contents of `body.txt`.
4. Submit, and send the issue number to the owner. Do not edit the issue afterwards.

## Result: PASS

Opened as #636 by `a-p-j-e` (association `NONE`) at 12:48:46Z, 1 min 40 s after `expected.json` was written.
Triage run 40325420907 at `b12aa19`: all six jobs succeeded. The prep step built the live index from this
repository's own issues (3 indexed, #29 quarantined). The agent saw `author_association: NONE`, ran all six
skill scripts (`verify_skill_use.py` OK) and proposed `question` plus one comment pointing to CONTRIBUTING.md,
AI_POLICY.md and Discussions. The policy gate passed (2 items, 0 problems). github-actions[bot] wrote the label
and the comment on #636 and nothing elsewhere. Every check in `expected.json` passes (`result.json`).

One wording point: the comment asks for the change to be described "in a new issue first", though this issue
already does part of that. Not a failure. The route it gives is right.

`logs/` holds the transcript, safe outputs, skill trace, `aw_info.json`, `skill_inventory.json` and usage.
