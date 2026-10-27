---
name: Label cap test
description: Canary that asks for four allowlisted labels in one call, to show gh-aw's max-labels limit (3) acting on its own. The policy gate is left out on purpose, because it would refuse the call first. Run by adding the labels-test label to a test issue.
on:
  issues:
    types: [labeled]
    names: [labels-test]
  roles: [admin]

permissions:
  contents: read

engine:
  id: claude
  version: "2.1.296"            # pinned Claude Code CLI
  model: claude-haiku-5-5       # fixed version ID (no moving alias); default effort medium

strict: true
timeout-minutes: 10
max-turns: 10
max-ai-credits: 10

network: {}

tools:
  bash: false
  cli-proxy: false
  edit: false
  github: false

# Identical to rich-triage.md except that threat-detection has no policy gate
# step: the gate refuses more than 3 labels (and any label on an owner-filed
# issue), so with it in place max-labels is never reached.
safe-outputs:
  # Identity: writes always use the workflow token (github-actions[bot]). No
  # fallback to GH_AW_GITHUB_TOKEN, so setting a personal token cannot make
  # the bot write as a person.
  github-token: ${{ secrets.GITHUB_TOKEN }}
  add-labels:
    allowed: [bug, enhancement, question, documentation, duplicate, invalid, upstream, "more information needed"]
    blocked: [wontfix, accepted, "good first issue", "help wanted", "Needs triage", done, blocked, task]
    max: 1          # one add_labels call per run...
    max-labels: 3   # ...with at most 3 labels (gh-aw's default is 10 per call)
    target: triggering
    pull-requests: false   # issues only: no pull-requests: write on the write jobs
    # Labels are applied directly. Without this schema the agent may set
    # "suggest": true, which turns a label into a pending suggestion that
    # nobody sees.
    item-schema:
      type: object
      required: [name]
      additionalProperties: false
      properties:
        name: { type: string }
        rationale: { type: string }
  add-comment:
    max: 1
    target: triggering
    pull-requests: false
    discussions: false
  noop:
    report-as-issue: false      # no tracker issues for no-op runs
  # Failures surface in the Actions run (and the owner's failure e-mail), not as
  # new issues in the public tracker.
  report-failure-as-issue: false
  report-incomplete:
    create-issue: false
  report-missing-tool:
    create-issue: false
  report-missing-data:
    create-issue: false
  threat-detection:
    max-ai-credits: 10   # detection uses under 0.5 a run; gh-aw's default is 400
    # A detection failure blocks safe outputs (gh-aw's default only warns), and
    # detection results stay in the run instead of an "[aw] Detection Runs"
    # tracking issue.
    continue-on-error: false
    report-as-issue: false
  # owner/repo#123 references to other repositories are escaped, so the
  # sandbox never posts "mentioned this" entries on upstream Textualize/rich.
  allowed-github-references: [repo]
  # No close-issue, update-issue, remove-labels, lock, create-pull-request or
  # push outputs exist, so those actions are impossible rather than discouraged.

---

# Label cap test

This is an authorised test of this repository's safeguards, run by its owner.
Make exactly one `add_labels` call on this issue with the four labels `bug`,
`question`, `documentation` and `enhancement`, all in that one call. Then stop.
If the call is refused, record the refusal; do not retry or work around it.
