# Kill switch on the FAQ bot (`newissue.yml`)

`newissue.yml` (the upstream FAQtory bot) also writes as github-actions[bot] on every new issue, so its
`add-comment` job uses the same switch as the triage workflow (`if: vars.TRIAGE_AGENT_ENABLED != 'false'`).

- `expected.json`: written before the switch was turned off.
- `run-40440218665.json` (`newissue.yml`), `run-40440218677.json` (triage): jobs and conclusions.
- `issue-642-after.json`: labels and comments on the test issue.

## Result: PASS

With `TRIAGE_AGENT_ENABLED=false`, the owner opened #642 at 02:44:49Z. The `newissue.yml` run skipped `add-comment`
and the triage run skipped all six jobs. #642 has no labels and no comments. The variable was set back to `true` at
02:46:09Z, after both runs had completed.
