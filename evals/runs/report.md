# Audit Report — Cross-Run Analysis

## Executive Summary

| Metric | Value |
|--------|-------|
| Runs analyzed | 103 |
| Runs with firewall data | 63 |
| Runs without firewall data | 40 |
| Total requests | 1911 |
| Allowed requests | 1911 |
| Blocked requests | 0 |
| Overall denial rate | 0.0% |
| Unique domains | 1 |

## Metrics Trends

| Metric | Total | Avg/run | Min | Max | Spikes |
|--------|-------|---------|-----|-----|--------|
| Token Trend | 19758956 | 191834 | 0 | 527469 | ⚠ #40164480420, #40163544464, #40162834306, #40158635774, #40158624147, #40158612803, #40156004734, #40154889723, #40154845387, #40154815346, #40154795541, #40154770396, #40154764299, #40154752490, #40154740346, #40154714837 |
| Turns | 63 | 0.6 | — | 1 | — |
| Duration | — | 6.2m | 25.0s | 14.9m | — |

## MCP Server Health (103 runs)

| Server | Connected | Error Rate | Total Calls | Errors | Status |
|--------|-----------|------------|-------------|--------|--------|
| `safeoutputs` | 63/103 | 0.0% | 99 | 0 | ⚠ unreliable |

## Error Trend

| Metric | Value |
|--------|-------|
| Runs with errors | 40/103 (39%) |
| Total errors | 40 |
| Avg errors/run | 0.39 |

## Domain Inventory

| Domain | Status | Seen In | Allowed | Blocked |
|--------|--------|---------|---------|--------|
| `api.openai.com:443` | ✅ allowed | 63/103 runs | 1911 | 0 |

## Agent Event Pattern Analysis

| Severity | Category | Title | Summary |
|----------|----------|-------|--------|
| ℹ info | execution | Cross-run log template patterns | Mined 2 distinct event templates across 6 pipeline stages from 166 events in 103 runs. (finish=1 plan=1) |

## Cluster Patterns

| Severity | Kind | Title | Description |
|----------|------|-------|-------------|
| 🔴 high | failure_correlation | All runs with execution_style=directed failed | Every run classified as execution_style="directed" ended in failure (40 runs). This suggests the execution_style dimension strongly predicts failure. |
| 🔴 high | failure_correlation | All runs with resource_profile=lean failed | Every run classified as resource_profile="lean" ended in failure (36 runs). This suggests the resource_profile dimension strongly predicts failure. |
| 🔴 high | failure_correlation | All runs with graders=absent failed | Every run classified as graders="absent" ended in failure (26 runs). This suggests the graders dimension strongly predicts failure. |

## Run Clusters

| Dimension | Value | Runs | Avg Tokens | Avg Turns | Avg Duration | Success Rate |
|-----------|-------|------|------------|-----------|--------------|-------------|
| conclusion | failure | 40 | 0 | 0.0 | 1.8m | 0% |
| conclusion | success | 63 | 313634 | 1.0 | 9.0m | 100% |
| execution_style | adaptive | 6 | 120602 | 1.0 | 8.8m | 100% |
| execution_style | directed | 40 | 0 | 0.0 | 1.8m | 0% |
| execution_style | exploratory | 57 | 333953 | 1.0 | 9.0m | 100% |
| resource_profile | heavy | 57 | 333953 | 1.0 | 9.0m | 100% |
| resource_profile | lean | 36 | 0 | 0.0 | 1.4m | 0% |
| resource_profile | moderate | 10 | 72361 | 0.6 | 7.4m | 60% |
| graders | absent | 26 | 0 | 0.0 | 50.3s | 0% |
| graders | mixed | 15 | 12313 | 0.1 | 3.8m | 7% |
| graders | pass | 62 | 315713 | 1.0 | 9.0m | 100% |

## Suggested Failure Investigations

Unique failed runs: **40** (40 observed, 0 metadata-only, 0 confirmed jobless; 0 intentional). Inspect these 2 runs first; they span 2/2 eligible symptom clusters. 0 clusters remain. Shared symptoms do not prove a common cause.

| Run | Workflow | Engine / Model | Clusters | Cached audit | Audit command |
|---|---|---|---|---|---|
| 40158756153 | Rich issue triage | codex / gpt-6-luna-2026-09-22 | failure-ccf6bfe72ce3cbab |  | gh aw audit 'https://github.com/ansonpoh/OSS_A3/actions/runs/40158756153' |
| 40158724350 | Rich issue triage | codex / gpt-6-luna-2026-09-22 | failure-9511af7bce6c66f0 |  | gh aw audit 'https://github.com/ansonpoh/OSS_A3/actions/runs/40158724350' |

## Failure Investigation Clusters

Clusters overlap and describe observed symptoms, not proven root causes. Shares use the returned failed population, separated by intentional status. Wilson 95% bounds assume independent runs, not fleet incidence; retries and missing evidence limit interpretation.

| Cluster | Runs | Failed population | Share (Wilson 95%) | Role | Symptom | Conclusion / Kind | Evidence | Intentional | Representatives |
|---|---:|---:|---|---|---|---|---|---|---|
| failure-ccf6bfe72ce3cbab | 26 | 40 | 65.0% [49.5%, 77.9%] | failure_boundary | activation / Restore daily AIC scan observations | failure / driver_exit | observed_symptom | false | 40158756153, 40158749503, 40158743049 |
| failure-9511af7bce6c66f0 | 14 | 40 | 35.0% [22.1%, 50.5%] | failure_boundary | activation / Check daily workflow token guardrail | failure / driver_exit | observed_symptom | false | 40158724350, 40158718705, 40158713755 |

<details><summary>Full cluster membership</summary>

```text
failure-ccf6bfe72ce3cbab runs=40156017810,40156024042,40156031280,40156036801,40156041885,40156047554,40156052705,40156058864,40156063978,40156069199,40156076188,40156081777,40156089206,40156096412,40156102581,40156108929,40156115475,40156121169,40156126591,40156132493,40156137561,40158730744,40158736428,40158743049,40158749503,40158756153
failure-9511af7bce6c66f0 runs=40155980114,40155985705,40155991815,40155997998,40158666547,40158678398,40158684593,40158689826,40158695843,40158701965,40158707926,40158713755,40158718705,40158724350
```

</details>

## Per-Run Breakdown

| Run ID | Workflow | Conclusion | Duration | Firewall | Tokens | Turns | MCP Err | Errors |
|--------|----------|------------|----------|----------|--------|-------|---------|--------|
| 40164480420 | Rich issue triage | success | 5.5m | 38/0 | 429.2K ⚠ | 1 | 0 | 0 |
| 40164444792 | Rich issue triage | success | 5.3m | 24/0 | 233.1K | 1 | 0 | 0 |
| 40164319969 | Rich issue triage | success | 6.0m | 27/0 | 234.6K | 1 | 0 | 0 |
| 40164188084 | Rich issue triage | success | 5.3m | 26/0 | 297.5K | 1 | 0 | 0 |
| 40164054215 | Rich issue triage | success | 5.5m | 35/0 | 329.8K | 1 | 0 | 0 |
| 40163917692 | Rich issue triage | success | 5.2m | 28/0 | 229.3K | 1 | 0 | 0 |
| 40163797946 | Rich issue triage | success | 4.5m | 11/0 | 80.6K | 1 | 0 | 0 |
| 40163669581 | Rich issue triage | success | 4.4m | 15/0 | 115.0K | 1 | 0 | 0 |
| 40163544464 | Rich issue triage | success | 5.4m | 46/0 | 524.4K ⚠ | 1 | 0 | 0 |
| 40163415075 | Rich issue triage | success | 5.3m | 31/0 | 297.5K | 1 | 0 | 0 |
| 40163257727 | Rich issue triage | success | 4.7m | 26/0 | 217.5K | 1 | 0 | 0 |
| 40163137419 | Rich issue triage | success | 4.7m | 23/0 | 338.9K | 1 | 0 | 0 |
| 40162963584 | Rich issue triage | success | 4.2m | 30/0 | 258.4K | 1 | 0 | 0 |
| 40162834306 | Rich issue triage | success | 5.2m | 32/0 | 419.6K ⚠ | 1 | 0 | 0 |
| 40162707501 | Rich issue triage | success | 4.9m | 35/0 | 360.4K | 1 | 0 | 0 |
| 40162519154 | Rich issue triage | success | 7.0m | 37/0 | 380.2K | 1 | 0 | 0 |
| 40158756153 | Rich issue triage | failure | 1.8m | — | — | — | 0 | 1 |
| 40158749503 | Rich issue triage | failure | 1.9m | — | — | — | 0 | 1 |
| 40158743049 | Rich issue triage | failure | 2.0m | — | — | — | 0 | 1 |
| 40158736428 | Rich issue triage | failure | 2.1m | — | — | — | 0 | 1 |
| 40158730744 | Rich issue triage | failure | 2.1m | — | — | — | 0 | 1 |
| 40158724350 | Rich issue triage | failure | 5.1m | — | — | — | 0 | 1 |
| 40158718705 | Rich issue triage | failure | 3.0m | — | — | — | 0 | 1 |
| 40158713755 | Rich issue triage | failure | 3.5m | — | — | — | 0 | 1 |
| 40158707926 | Rich issue triage | failure | 4.2m | — | — | — | 0 | 1 |
| 40158701965 | Rich issue triage | failure | 2.8m | — | — | — | 0 | 1 |
| 40158695843 | Rich issue triage | failure | 5.8m | — | — | — | 0 | 1 |
| 40158689826 | Rich issue triage | failure | 4.2m | — | — | — | 0 | 1 |
| 40158684593 | Rich issue triage | failure | 5.4m | — | — | — | 0 | 1 |
| 40158678398 | Rich issue triage | failure | 3.5m | — | — | — | 0 | 1 |
| 40158671967 | Rich issue triage | success | 8.2m | 25/0 | 342.8K | 1 | 0 | 0 |
| 40158666547 | Rich issue triage | failure | 5.2m | — | — | — | 0 | 1 |
| 40158659972 | Rich issue triage | success | 10.5m | 35/0 | 361.7K | 1 | 0 | 0 |
| 40158653943 | Rich issue triage | success | 9.6m | 32/0 | 327.7K | 1 | 0 | 0 |
| 40158647644 | Rich issue triage | success | 10.1m | 35/0 | 343.8K | 1 | 0 | 0 |
| 40158641685 | Rich issue triage | success | 9.6m | 35/0 | 362.3K | 1 | 0 | 0 |
| 40158635774 | Rich issue triage | success | 11.2m | 37/0 | 483.2K ⚠ | 1 | 0 | 0 |
| 40158629724 | Rich issue triage | success | 11.7m | 35/0 | 350.5K | 1 | 0 | 0 |
| 40158624147 | Rich issue triage | success | 9.3m | 34/0 | 514.6K ⚠ | 1 | 0 | 0 |
| 40158618417 | Rich issue triage | success | 8.3m | 24/0 | 192.0K | 1 | 0 | 0 |
| 40158612803 | Rich issue triage | success | 10.9m | 39/0 | 413.4K ⚠ | 1 | 0 | 0 |
| 40158608022 | Rich issue triage | success | 8.2m | 17/0 | 184.7K | 1 | 0 | 0 |
| 40158602103 | Rich issue triage | success | 8.0m | 18/0 | 144.4K | 1 | 0 | 0 |
| 40158596478 | Rich issue triage | success | 9.0m | 25/0 | 246.0K | 1 | 0 | 0 |
| 40158590355 | Rich issue triage | success | 7.8m | 34/0 | 315.1K | 1 | 0 | 0 |
| 40156137561 | Rich issue triage | failure | 41.0s | — | — | — | 0 | 1 |
| 40156132493 | Rich issue triage | failure | 32.0s | — | — | — | 0 | 1 |
| 40156126591 | Rich issue triage | failure | 32.0s | — | — | — | 0 | 1 |
| 40156121169 | Rich issue triage | failure | 33.0s | — | — | — | 0 | 1 |
| 40156115475 | Rich issue triage | failure | 28.0s | — | — | — | 0 | 1 |
| 40156108929 | Rich issue triage | failure | 30.0s | — | — | — | 0 | 1 |
| 40156102581 | Rich issue triage | failure | 45.0s | — | — | — | 0 | 1 |
| 40156096412 | Rich issue triage | failure | 29.0s | — | — | — | 0 | 1 |
| 40156089206 | Rich issue triage | failure | 31.0s | — | — | — | 0 | 1 |
| 40156081777 | Rich issue triage | failure | 31.0s | — | — | — | 0 | 1 |
| 40156076188 | Rich issue triage | failure | 33.0s | — | — | — | 0 | 1 |
| 40156069199 | Rich issue triage | failure | 25.0s | — | — | — | 0 | 1 |
| 40156063978 | Rich issue triage | failure | 27.0s | — | — | — | 0 | 1 |
| 40156058864 | Rich issue triage | failure | 52.0s | — | — | — | 0 | 1 |
| 40156052705 | Rich issue triage | failure | 39.0s | — | — | — | 0 | 1 |
| 40156047554 | Rich issue triage | failure | 29.0s | — | — | — | 0 | 1 |
| 40156041885 | Rich issue triage | failure | 48.0s | — | — | — | 0 | 1 |
| 40156036801 | Rich issue triage | failure | 35.0s | — | — | — | 0 | 1 |
| 40156031280 | Rich issue triage | failure | 29.0s | — | — | — | 0 | 1 |
| 40156024042 | Rich issue triage | failure | 37.0s | — | — | — | 0 | 1 |
| 40156017810 | Rich issue triage | failure | 32.0s | — | — | — | 0 | 1 |
| 40156010270 | Rich issue triage | success | 4.9m | 31/0 | 289.3K | 1 | 0 | 0 |
| 40156004734 | Rich issue triage | success | 5.8m | 46/0 | 485.5K ⚠ | 1 | 0 | 0 |
| 40155997998 | Rich issue triage | failure | 1.1m | — | — | — | 0 | 1 |
| 40155991815 | Rich issue triage | failure | 2.1m | — | — | — | 0 | 1 |
| 40155985705 | Rich issue triage | failure | 1.6m | — | — | — | 0 | 1 |
| 40155980114 | Rich issue triage | failure | 2.0m | — | — | — | 0 | 1 |
| 40155974545 | Rich issue triage | success | 5.2m | 29/0 | 256.1K | 1 | 0 | 0 |
| 40155968471 | Rich issue triage | success | 5.9m | 34/0 | 329.4K | 1 | 0 | 0 |
| 40154889723 | Rich issue triage | success | 14.4m | 44/0 | 520.0K ⚠ | 1 | 0 | 0 |
| 40154883575 | Rich issue triage | success | 11.4m | 24/0 | 303.8K | 1 | 0 | 0 |
| 40154876691 | Rich issue triage | success | 11.2m | 17/0 | 150.7K | 1 | 0 | 0 |
| 40154870509 | Rich issue triage | success | 14.9m | 31/0 | 292.5K | 1 | 0 | 0 |
| 40154863950 | Rich issue triage | success | 11.0m | 25/0 | 211.9K | 1 | 0 | 0 |
| 40154857513 | Rich issue triage | success | 14.6m | 12/0 | 80.2K | 1 | 0 | 0 |
| 40154851937 | Rich issue triage | success | 13.0m | 12/0 | 118.7K | 1 | 0 | 0 |
| 40154845387 | Rich issue triage | success | 14.2m | 40/0 | 412.7K ⚠ | 1 | 0 | 0 |
| 40154839485 | Rich issue triage | success | 12.9m | 34/0 | 363.4K | 1 | 0 | 0 |
| 40154834116 | Rich issue triage | success | 12.5m | 27/0 | 239.8K | 1 | 0 | 0 |
| 40154827994 | Rich issue triage | success | 14.7m | 29/0 | 303.1K | 1 | 0 | 0 |
| 40154821303 | Rich issue triage | success | 11.4m | 28/0 | 239.0K | 1 | 0 | 0 |
| 40154815346 | Rich issue triage | success | 13.9m | 42/0 | 408.0K ⚠ | 1 | 0 | 0 |
| 40154809244 | Rich issue triage | success | 14.3m | 26/0 | 224.5K | 1 | 0 | 0 |
| 40154802435 | Rich issue triage | success | 11.1m | 24/0 | 224.1K | 1 | 0 | 0 |
| 40154795541 | Rich issue triage | success | 9.9m | 38/0 | 387.0K ⚠ | 1 | 0 | 0 |
| 40154790733 | Rich issue triage | success | 8.1m | 32/0 | 295.4K | 1 | 0 | 0 |
| 40154783537 | Rich issue triage | success | 10.8m | 33/0 | 332.5K | 1 | 0 | 0 |
| 40154777474 | Rich issue triage | success | 9.9m | 31/0 | 307.7K | 1 | 0 | 0 |
| 40154770396 | Rich issue triage | success | 11.9m | 37/0 | 407.2K ⚠ | 1 | 0 | 0 |
| 40154764299 | Rich issue triage | success | 11.4m | 35/0 | 501.6K ⚠ | 1 | 0 | 0 |
| 40154757797 | Rich issue triage | success | 9.6m | 35/0 | 322.2K | 1 | 0 | 0 |
| 40154752490 | Rich issue triage | success | 11.0m | 43/0 | 527.5K ⚠ | 1 | 0 | 0 |
| 40154746665 | Rich issue triage | success | 9.4m | 28/0 | 256.4K | 1 | 0 | 0 |
| 40154740346 | Rich issue triage | success | 8.3m | 37/0 | 387.6K ⚠ | 1 | 0 | 0 |
| 40154733687 | Rich issue triage | success | 9.3m | 33/0 | 321.7K | 1 | 0 | 0 |
| 40154727664 | Rich issue triage | success | 7.9m | 25/0 | 249.2K | 1 | 0 | 0 |
| 40154721311 | Rich issue triage | success | 6.6m | 24/0 | 201.0K | 1 | 0 | 0 |
| 40154714837 | Rich issue triage | success | 9.1m | 36/0 | 481.3K ⚠ | 1 | 0 | 0 |

