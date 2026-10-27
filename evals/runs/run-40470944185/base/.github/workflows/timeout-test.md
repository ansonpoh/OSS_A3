---
name: Timeout test
description: Canary whose agent step needs longer than its 1-minute timeout, to show timeout-minutes stops a run (rich-triage.md uses 10). Run by adding the timeout-test label to a test issue.
on:
  issues:
    types: [labeled]
    names: [timeout-test]
  roles: [admin]

permissions:
  contents: read

engine:
  id: claude
  version: "2.1.296"            # pinned Claude Code CLI
  model: claude-haiku-5-5       # fixed version ID (no moving alias); default effort medium

strict: true
timeout-minutes: 1         # the cap under test (rich-triage.md: 10), at a test value like budget-test
max-turns: 25              # as rich-triage.md, so the timeout is what stops the run
max-ai-credits: 5          # as rich-triage.md

network: {}

tools:
  bash: ["sleep"]
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

# Slow steps

Run `sleep 50` five times, each as its own Bash command, waiting for each to
finish before the next. Do not combine them or shorten them. When all five
have finished, call `noop` with the message "sleeps finished".
