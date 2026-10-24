# Audit Report — Cross-Run Analysis

## Executive Summary

| Metric | Value |
|--------|-------|
| Runs analyzed | 27 |
| Runs with firewall data | 27 |
| Runs without firewall data | 0 |
| Total requests | 804 |
| Allowed requests | 804 |
| Blocked requests | 0 |
| Overall denial rate | 0.0% |
| Unique domains | 1 |

## Metrics Trends

| Metric | Total | Avg/run | Min | Max | Spikes |
|--------|-------|---------|-----|-----|--------|
| Token Trend | 8182169 | 303043 | 96672 | 506283 | — |
| Turns | 27 | 1.0 | — | 1 | — |
| Duration | — | 9.3m | 5.8m | 12.9m | — |

## MCP Server Health (27 runs)

| Server | Connected | Error Rate | Total Calls | Errors | Status |
|--------|-----------|------------|-------------|--------|--------|
| `safeoutputs` | 27/27 | 0.0% | 42 | 0 | ✅ ok |

## Domain Inventory

| Domain | Status | Seen In | Allowed | Blocked |
|--------|--------|---------|---------|--------|
| `api.openai.com:443` | ✅ allowed | 27/27 runs | 804 | 0 |

## Agent Event Pattern Analysis

| Severity | Category | Title | Summary |
|----------|----------|-------|--------|
| ℹ info | execution | Cross-run log template patterns | Mined 2 distinct event templates across 6 pipeline stages from 54 events in 27 runs. (finish=1 plan=1) |

## Cluster Patterns

| Severity | Kind | Title | Description |
|----------|------|-------|-------------|
| 🟡 low | style_skew | Dominant execution_style: exploratory | 93% of runs share execution_style="exploratory" (25/27). Low diversity may indicate homogeneous workload or classification bias. |
| 🟡 low | style_skew | Dominant resource_profile: heavy | 93% of runs share resource_profile="heavy" (25/27). Low diversity may indicate homogeneous workload or classification bias. |

## Run Clusters

| Dimension | Value | Runs | Avg Tokens | Avg Turns | Avg Duration | Success Rate |
|-----------|-------|------|------------|-----------|--------------|-------------|
| execution_style | adaptive | 2 | 114200 | 1.0 | 8.3m | 100% |
| execution_style | exploratory | 25 | 318150 | 1.0 | 9.4m | 100% |
| resource_profile | heavy | 25 | 318150 | 1.0 | 9.4m | 100% |
| resource_profile | moderate | 2 | 114200 | 1.0 | 8.3m | 100% |

## Per-Run Breakdown

| Run ID | Workflow | Conclusion | Duration | Firewall | Tokens | Turns | MCP Err | Errors |
|--------|----------|------------|----------|----------|--------|-------|---------|--------|
| 40106854365 | Rich issue triage | success | 12.3m | 25/0 | 224.6K | 1 | 0 | 0 |
| 40106847992 | Rich issue triage | success | 12.9m | 35/0 | 342.5K | 1 | 0 | 0 |
| 40106841553 | Rich issue triage | success | 12.2m | 24/0 | 193.1K | 1 | 0 | 0 |
| 40106834550 | Rich issue triage | success | 10.8m | 14/0 | 96.7K | 1 | 0 | 0 |
| 40106827266 | Rich issue triage | success | 11.4m | 14/0 | 97.5K | 1 | 0 | 0 |
| 40106821246 | Rich issue triage | success | 11.7m | 37/0 | 372.9K | 1 | 0 | 0 |
| 40106813507 | Rich issue triage | success | 12.2m | 27/0 | 232.4K | 1 | 0 | 0 |
| 40106805701 | Rich issue triage | success | 10.3m | 27/0 | 240.3K | 1 | 0 | 0 |
| 40106798377 | Rich issue triage | success | 11.0m | 23/0 | 300.9K | 1 | 0 | 0 |
| 40106790761 | Rich issue triage | success | 8.3m | 24/0 | 281.0K | 1 | 0 | 0 |
| 40106783338 | Rich issue triage | success | 10.9m | 38/0 | 370.7K | 1 | 0 | 0 |
| 40106774957 | Rich issue triage | success | 9.4m | 35/0 | 329.0K | 1 | 0 | 0 |
| 40106768948 | Rich issue triage | success | 8.8m | 26/0 | 306.0K | 1 | 0 | 0 |
| 40106761076 | Rich issue triage | success | 10.4m | 33/0 | 506.3K | 1 | 0 | 0 |
| 40106754435 | Rich issue triage | success | 10.1m | 38/0 | 379.5K | 1 | 0 | 0 |
| 40106748128 | Rich issue triage | success | 7.5m | 31/0 | 299.7K | 1 | 0 | 0 |
| 40106741212 | Rich issue triage | success | 9.5m | 38/0 | 408.7K | 1 | 0 | 0 |
| 40106734286 | Rich issue triage | success | 8.8m | 36/0 | 372.0K | 1 | 0 | 0 |
| 40106727489 | Rich issue triage | success | 8.1m | 35/0 | 475.1K | 1 | 0 | 0 |
| 40106718850 | Rich issue triage | success | 7.5m | 29/0 | 263.4K | 1 | 0 | 0 |
| 40106713819 | Rich issue triage | success | 8.6m | 41/0 | 488.7K | 1 | 0 | 0 |
| 40106703083 | Rich issue triage | success | 6.5m | 28/0 | 228.0K | 1 | 0 | 0 |
| 40106696184 | Rich issue triage | success | 7.4m | 32/0 | 314.0K | 1 | 0 | 0 |
| 40106690013 | Rich issue triage | success | 7.0m | 38/0 | 364.3K | 1 | 0 | 0 |
| 40106681303 | Rich issue triage | success | 5.8m | 15/0 | 131.7K | 1 | 0 | 0 |
| 40106674835 | Rich issue triage | success | 6.2m | 28/0 | 238.8K | 1 | 0 | 0 |
| 40106667550 | Rich issue triage | success | 6.7m | 33/0 | 324.4K | 1 | 0 | 0 |

