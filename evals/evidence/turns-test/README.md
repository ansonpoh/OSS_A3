# Turn cap test (`max-turns`)

`rich-triage.md` sets `max-turns: 25`, which gh-aw passes to Claude Code as `--max-turns 25`. `turns-test.md` uses
the same mechanism at 3 (as `budget-test` tests the credit caps at 1), with the 5-credit run cap so that only the
turn cap can stop it, and asks for ten `echo` commands, one per turn, then `noop`.

- `expected.json`: written and committed (`c05d2fe`) before the run.
- `issue-27-before.json`, `issue-27-after.json`: labels and comments on #27.
- `turns-test-run-40449918646.json`: jobs and timings. `agent-stop-40449918646.log`: the stop and error lines.

## Result: PASS

Run 40449918646: `echo step 1` to `echo step 3` ran, then Claude Code stopped (`error_max_turns`, terminal reason
`max_turns`, it reports `num_turns` 4, counting the turn it was stopped in). The harness did not retry ("not
retriable via --continue"), the agent job failed with "max-turns limit reached" and the run concluded failure.
`noop` was never called. safe_outputs processed only gh-aw's own `report_incomplete` signal, which creates no issue.
#27 gained only the owner's `turns-test` trigger label. Agent: 0.58 credits.

The detection job runs its own agent with `max_turns=50` (gh-aw's default), outside the workflow's `max-turns`.
