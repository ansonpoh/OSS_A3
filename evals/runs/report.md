# Audit Report — Cross-Run Analysis

## Executive Summary

| Metric | Value |
|--------|-------|
| Runs analyzed | 30 |
| Runs with firewall data | 29 |
| Runs without firewall data | 1 |
| Total requests | 239 |
| Allowed requests | 239 |
| Blocked requests | 0 |
| Overall denial rate | 0.0% |
| Unique domains | 1 |

## Metrics Trends

| Metric | Total | Avg/run | Min | Max | Spikes |
|--------|-------|---------|-----|-----|--------|
| Token Trend | 8916641 | 297221 | 0 | 478581 | — |
| Turns | 319 | 10.6 | — | 17 | — |
| Duration | — | 4.4m | 52.0s | 5.6m | — |

## MCP Server Health (30 runs)

| Server | Connected | Error Rate | Total Calls | Errors | Status |
|--------|-----------|------------|-------------|--------|--------|
| `safeoutputs` | 29/30 | 0.0% | 46 | 0 | ✅ ok |

## Error Trend

| Metric | Value |
|--------|-------|
| Runs with errors | 1/30 (3%) |
| Total errors | 1 |
| Avg errors/run | 0.03 |

## Domain Inventory

| Domain | Status | Seen In | Allowed | Blocked |
|--------|--------|---------|---------|--------|
| `api.anthropic.com:443` | ✅ allowed | 29/30 runs | 239 | 0 |

## Agent Event Pattern Analysis

| Severity | Category | Title | Summary |
|----------|----------|-------|--------|
| ℹ info | execution | Cross-run log template patterns | Mined 2 distinct event templates across 6 pipeline stages from 59 events in 30 runs. (finish=1 plan=1) |

## Cluster Patterns

| Severity | Kind | Title | Description |
|----------|------|-------|-------------|
| 🟡 low | style_skew | Dominant graders: pass | 90% of runs share graders="pass" (27/30). Low diversity may indicate homogeneous workload or classification bias. |

## Run Clusters

| Dimension | Value | Runs | Avg Tokens | Avg Turns | Avg Duration | Success Rate |
|-----------|-------|------|------------|-----------|--------------|-------------|
| conclusion | failure | 1 | 0 | 0.0 | 52.0s | 0% |
| conclusion | success | 29 | 307470 | 11.0 | 4.5m | 100% |
| execution_style | adaptive | 7 | 237795 | 9.0 | 4.4m | 100% |
| execution_style | directed | 3 | 89968 | 2.7 | 3.1m | 67% |
| execution_style | exploratory | 20 | 349108 | 12.4 | 4.6m | 100% |
| resource_profile | heavy | 15 | 365211 | 13.1 | 4.5m | 100% |
| resource_profile | lean | 3 | 89968 | 2.7 | 3.1m | 67% |
| resource_profile | moderate | 12 | 264047 | 9.5 | 4.6m | 100% |
| graders | absent | 1 | 0 | 0.0 | 52.0s | 0% |
| graders | mixed | 2 | 134952 | 4.0 | 4.2m | 100% |
| graders | pass | 27 | 320249 | 11.5 | 4.5m | 100% |

## Suggested Failure Investigations

Unique failed runs: **1** (1 observed, 0 metadata-only, 0 confirmed jobless; 0 intentional). Inspect these 1 runs first; they span 1/1 eligible symptom clusters. 0 clusters remain. Shared symptoms do not prove a common cause.

| Run | Workflow | Engine / Model | Clusters | Cached audit | Audit command |
|---|---|---|---|---|---|
| 40291830850 | Rich issue triage | claude / claude-haiku-5-5 | failure-17888dfee9f531fe |  | gh aw audit 'https://github.com/ansonpoh/OSS_A3/actions/runs/40291830850' |

## Failure Investigation Clusters

Clusters overlap and describe observed symptoms, not proven root causes. Shares use the returned failed population, separated by intentional status. Wilson 95% bounds assume independent runs, not fleet incidence; retries and missing evidence limit interpretation.

| Cluster | Runs | Failed population | Share (Wilson 95%) | Role | Symptom | Conclusion / Kind | Evidence | Intentional | Representatives |
|---|---:|---:|---|---|---|---|---|---|---|
| failure-17888dfee9f531fe | 1 | 1 | 100.0% [20.7%, 100.0%] | failure_boundary | activation / Checkout .github and .agents folders | failure / driver_exit | observed_symptom | false | 40291830850 |

<details><summary>Full cluster membership</summary>

```text
failure-17888dfee9f531fe runs=40291830850
```

</details>

## Per-Run Breakdown

| Run ID | Workflow | Conclusion | Duration | Firewall | Tokens | Turns | MCP Err | Errors |
|--------|----------|------------|----------|----------|--------|-------|---------|--------|
| 40293587510 | Rich issue triage | success | 4.9m | 7/0 | 238.1K | 9 | 0 | 0 |
| 40292764943 | Rich issue triage | success | 4.5m | 8/0 | 293.9K | 13 | 0 | 0 |
| 40292640082 | Rich issue triage | success | 5.2m | 7/0 | 239.5K | 9 | 0 | 0 |
| 40292525832 | Rich issue triage | success | 4.5m | 9/0 | 346.2K | 11 | 0 | 0 |
| 40292409603 | Rich issue triage | success | 4.1m | 9/0 | 342.5K | 12 | 0 | 0 |
| 40292295225 | Rich issue triage | success | 4.2m | 7/0 | 234.4K | 9 | 0 | 0 |
| 40292181457 | Rich issue triage | success | 3.9m | 5/0 | 134.9K | 4 | 0 | 0 |
| 40292065327 | Rich issue triage | success | 4.5m | 5/0 | 135.0K | 4 | 0 | 0 |
| 40291946440 | Rich issue triage | success | 4.7m | 8/0 | 296.7K | 10 | 0 | 0 |
| 40291830850 | Rich issue triage | failure | 52.0s | — | — | — | 0 | 1 |
| 40291711402 | Rich issue triage | success | 4.6m | 8/0 | 287.5K | 10 | 0 | 0 |
| 40291593937 | Rich issue triage | success | 4.2m | 7/0 | 242.7K | 9 | 0 | 0 |
| 40291471111 | Rich issue triage | success | 4.8m | 8/0 | 286.7K | 10 | 0 | 0 |
| 40291354091 | Rich issue triage | success | 4.6m | 10/0 | 397.0K | 14 | 0 | 0 |
| 40291242265 | Rich issue triage | success | 4.9m | 9/0 | 344.4K | 12 | 0 | 0 |
| 40291126248 | Rich issue triage | success | 5.6m | 8/0 | 287.0K | 10 | 0 | 0 |
| 40291007611 | Rich issue triage | success | 5.1m | 11/0 | 446.1K | 15 | 0 | 0 |
| 40290887939 | Rich issue triage | success | 4.5m | 8/0 | 297.5K | 12 | 0 | 0 |
| 40290773517 | Rich issue triage | success | 4.5m | 9/0 | 338.8K | 12 | 0 | 0 |
| 40290658208 | Rich issue triage | success | 4.1m | 8/0 | 295.5K | 13 | 0 | 0 |
| 40290544425 | Rich issue triage | success | 4.4m | 9/0 | 355.0K | 12 | 0 | 0 |
| 40290431584 | Rich issue triage | success | 4.4m | 10/0 | 450.3K | 13 | 0 | 0 |
| 40290316552 | Rich issue triage | success | 4.9m | 9/0 | 341.4K | 12 | 0 | 0 |
| 40290207516 | Rich issue triage | success | 4.4m | 11/0 | 478.6K | 17 | 0 | 0 |
| 40290097824 | Rich issue triage | success | 4.7m | 7/0 | 235.8K | 9 | 0 | 0 |
| 40289985933 | Rich issue triage | success | 4.1m | 11/0 | 449.2K | 15 | 0 | 0 |
| 40289874110 | Rich issue triage | success | 4.1m | 9/0 | 347.5K | 12 | 0 | 0 |
| 40289757876 | Rich issue triage | success | 3.9m | 7/0 | 235.5K | 9 | 0 | 0 |
| 40289646965 | Rich issue triage | success | 3.9m | 7/0 | 238.5K | 9 | 0 | 0 |
| 40289536713 | Rich issue triage | success | 4.4m | 8/0 | 300.6K | 13 | 0 | 0 |

