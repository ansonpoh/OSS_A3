# Audit Report — Cross-Run Analysis

## Executive Summary

| Metric | Value |
|--------|-------|
| Runs analyzed | 26 |
| Runs with firewall data | 26 |
| Runs without firewall data | 0 |
| Total requests | 743 |
| Allowed requests | 743 |
| Blocked requests | 0 |
| Overall denial rate | 0.0% |
| Unique domains | 1 |

## Metrics Trends

| Metric | Total | Avg/run | Min | Max | Spikes |
|--------|-------|---------|-----|-----|--------|
| Token Trend | 7236165 | 278314 | 79955 | 441388 | — |
| Turns | 26 | 1.0 | — | 1 | — |
| Duration | — | 9.2m | 5.6m | 12.6m | — |

## MCP Server Health (26 runs)

| Server | Connected | Error Rate | Total Calls | Errors | Status |
|--------|-----------|------------|-------------|--------|--------|
| `safeoutputs` | 26/26 | 0.0% | 40 | 0 | ✅ ok |

## Domain Inventory

| Domain | Status | Seen In | Allowed | Blocked |
|--------|--------|---------|---------|--------|
| `api.openai.com:443` | ✅ allowed | 26/26 runs | 743 | 0 |

## Agent Event Pattern Analysis

| Severity | Category | Title | Summary |
|----------|----------|-------|--------|
| ℹ info | execution | Cross-run log template patterns | Mined 2 distinct event templates across 6 pipeline stages from 52 events in 26 runs. (finish=1 plan=1) |

## Cluster Patterns

| Severity | Kind | Title | Description |
|----------|------|-------|-------------|
| 🟡 low | style_skew | Dominant execution_style: exploratory | 92% of runs share execution_style="exploratory" (24/26). Low diversity may indicate homogeneous workload or classification bias. |
| 🟡 low | style_skew | Dominant resource_profile: heavy | 92% of runs share resource_profile="heavy" (24/26). Low diversity may indicate homogeneous workload or classification bias. |
| 🟡 low | style_skew | Dominant graders: pass | 96% of runs share graders="pass" (25/26). Low diversity may indicate homogeneous workload or classification bias. |

## Run Clusters

| Dimension | Value | Runs | Avg Tokens | Avg Turns | Avg Duration | Success Rate |
|-----------|-------|------|------------|-----------|--------------|-------------|
| execution_style | adaptive | 1 | 79955 | 1.0 | 11.2m | 100% |
| execution_style | directed | 1 | 92741 | 1.0 | 10.7m | 100% |
| execution_style | exploratory | 24 | 294311 | 1.0 | 9.0m | 100% |
| resource_profile | heavy | 24 | 294311 | 1.0 | 9.0m | 100% |
| resource_profile | moderate | 2 | 86348 | 1.0 | 10.9m | 100% |
| graders | mixed | 1 | 92741 | 1.0 | 10.7m | 100% |
| graders | pass | 25 | 285736 | 1.0 | 9.1m | 100% |

## Per-Run Breakdown

| Run ID | Workflow | Conclusion | Duration | Firewall | Tokens | Turns | MCP Err | Errors |
|--------|----------|------------|----------|----------|--------|-------|---------|--------|
| 40068948938 | Rich issue triage | success | 12.6m | 28/0 | 254.4K | 1 | 0 | 0 |
| 40068942640 | Rich issue triage | success | 12.3m | 19/0 | 245.7K | 1 | 0 | 0 |
| 40068935062 | Rich issue triage | success | 12.1m | 28/0 | 232.9K | 1 | 0 | 0 |
| 40068929007 | Rich issue triage | success | 10.7m | 9/0 | 92.7K | 1 | 0 | 0 |
| 40068921980 | Rich issue triage | success | 11.2m | 12/0 | 80.0K | 1 | 0 | 0 |
| 40068916312 | Rich issue triage | success | 11.9m | 32/0 | 270.4K | 1 | 0 | 0 |
| 40068909402 | Rich issue triage | success | 10.0m | 24/0 | 198.6K | 1 | 0 | 0 |
| 40068903512 | Rich issue triage | success | 11.7m | 28/0 | 235.8K | 1 | 0 | 0 |
| 40068897888 | Rich issue triage | success | 10.5m | 26/0 | 214.4K | 1 | 0 | 0 |
| 40068891302 | Rich issue triage | success | 9.2m | 30/0 | 278.3K | 1 | 0 | 0 |
| 40068886111 | Rich issue triage | success | 10.0m | 38/0 | 347.4K | 1 | 0 | 0 |
| 40068880103 | Rich issue triage | success | 7.4m | 15/0 | 150.0K | 1 | 0 | 0 |
| 40068873795 | Rich issue triage | success | 9.8m | 40/0 | 413.7K | 1 | 0 | 0 |
| 40068867899 | Rich issue triage | success | 8.9m | 21/0 | 241.2K | 1 | 0 | 0 |
| 40068860447 | Rich issue triage | success | 7.9m | 34/0 | 311.7K | 1 | 0 | 0 |
| 40068853610 | Rich issue triage | success | 8.7m | 34/0 | 365.1K | 1 | 0 | 0 |
| 40068847364 | Rich issue triage | success | 8.4m | 36/0 | 388.4K | 1 | 0 | 0 |
| 40068841034 | Rich issue triage | success | 7.5m | 35/0 | 441.4K | 1 | 0 | 0 |
| 40068834137 | Rich issue triage | success | 7.3m | 34/0 | 307.3K | 1 | 0 | 0 |
| 40068828191 | Rich issue triage | success | 5.9m | 34/0 | 349.2K | 1 | 0 | 0 |
| 40068822605 | Rich issue triage | success | 7.2m | 28/0 | 227.1K | 1 | 0 | 0 |
| 40068815329 | Rich issue triage | success | 7.0m | 38/0 | 376.9K | 1 | 0 | 0 |
| 40068809273 | Rich issue triage | success | 12.3m | 29/0 | 381.1K | 1 | 0 | 0 |
| 40068801861 | Rich issue triage | success | 5.9m | 26/0 | 213.3K | 1 | 0 | 0 |
| 40068794586 | Rich issue triage | success | 7.0m | 30/0 | 259.4K | 1 | 0 | 0 |
| 40068787689 | Rich issue triage | success | 5.6m | 35/0 | 359.9K | 1 | 0 | 0 |

