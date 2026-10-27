---
name: Turn cap test
description: Canary that needs more agent turns than its 3-turn cap, to show max-turns stops a run (rich-triage.md uses 25, passed to Claude Code as --max-turns). Run by adding the turns-test label to a test issue.
on:
  issues:
    types: [labeled]
    names: [turns-test]
  roles: [admin]

permissions:
  contents: read

engine:
  id: claude
  version: "2.1.296"            # pinned Claude Code CLI
  model: claude-haiku-5-5       # fixed version ID (no moving alias); default effort medium

strict: true
timeout-minutes: 10
max-turns: 3               # the cap under test (rich-triage.md: 25), at a test value like budget-test
max-ai-credits: 5          # as rich-triage.md, so the turn cap is what stops the run

network: {}

tools:
  bash: ["echo"]
  edit: false
  github: false

safe-outputs:
  # The canary only calls noop. Without a non-builtin output gh-aw would
  # auto-inject create-issue, so allow at most one comment on the test issue.
  add-comment:
    max: 1
    target: triggering
    pull-requests: false
    discussions: false
  noop:
    report-as-issue: false
  report-failure-as-issue: false
  report-incomplete:
    create-issue: false
  report-missing-tool:
    create-issue: false
  report-missing-data:
    create-issue: false
  # Same detection settings as rich-triage.md: no "[aw] Detection Runs" issue.
  threat-detection:
    continue-on-error: false
    report-as-issue: false
---

# Step counter

Run `echo step 1`, then `echo step 2`, and so on up to `echo step 10`. Run each
one as its own Bash command, one command per turn, and wait for its output
before the next. Do not combine them. When `echo step 10` has run, call `noop`
with the message "steps finished".
