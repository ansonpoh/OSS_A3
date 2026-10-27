# Label cap test (`max-labels`)

`rich-triage.md` limits `add_labels` to one call with at most 3 labels (`max-labels: 3`). In the triage workflow
the policy gate refuses more than 3 labels first, so `cap-test` never reached this limit. `labels-test.md` uses the
same `safe-outputs` block without the gate step and asks for four allowlisted labels on owner test issue #27.

- `expected.json`: written and committed (`b24bc50`) before the run.
- `issue-27-before.json`, `issue-27-after.json`: labels and comments on #27.
- `labels-test-run-40439379566.json`: jobs and timings. `safe_outputs-40439379566.log`: the handler's output.

## Result: PASS

Run 40439379566: the agent made one `add_labels` call with `bug, question, documentation, enhancement`. The
safe-outputs MCP accepted it and detection passed it. The `safe_outputs` job refused the whole call ("E003: Cannot
add more than 3 labels (received 4)"), so no label was written. The limit refuses rather than truncates, and the
failed write fails the run. #27 gained only the owner's `labels-test` trigger label. Agent: 0.56 credits.

`labels-test.md` stays in the triage agent's checkout (the prep step deletes only `cap-test.*` and
`budget-test.*`). Its prompt asks only for allowlisted labels.
