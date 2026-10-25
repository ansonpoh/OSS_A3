# Audit Report — Cross-Run Analysis

## Executive Summary

| Metric | Value |
|--------|-------|
| Runs analyzed | 27 |
| Runs with firewall data | 27 |
| Runs without firewall data | 0 |
| Total requests | 747 |
| Allowed requests | 747 |
| Blocked requests | 0 |
| Overall denial rate | 0.0% |
| Unique domains | 1 |

## Metrics Trends

| Metric | Total | Avg/run | Min | Max | Spikes |
|--------|-------|---------|-----|-----|--------|
| Token Trend | 7501339 | 277827 | 79763 | 592492 | ⚠ #40148673866 |
| Turns | 27 | 1.0 | — | 1 | — |
| Duration | — | 9.2m | 5.4m | 12.5m | — |

## MCP Server Health (27 runs)

| Server | Connected | Error Rate | Total Calls | Errors | Status |
|--------|-----------|------------|-------------|--------|--------|
| `safeoutputs` | 27/27 | 0.0% | 43 | 0 | ✅ ok |

## Domain Inventory

| Domain | Status | Seen In | Allowed | Blocked |
|--------|--------|---------|---------|--------|
| `api.openai.com:443` | ✅ allowed | 27/27 runs | 747 | 0 |

## Agent Event Pattern Analysis

| Severity | Category | Title | Summary |
|----------|----------|-------|--------|
| ℹ info | execution | Cross-run log template patterns | Mined 2 distinct event templates across 6 pipeline stages from 54 events in 27 runs. (finish=1 plan=1) |

## Cluster Patterns

| Severity | Kind | Title | Description |
|----------|------|-------|-------------|
| 🟡 low | style_skew | Dominant execution_style: exploratory | 89% of runs share execution_style="exploratory" (24/27). Low diversity may indicate homogeneous workload or classification bias. |
| 🟡 low | style_skew | Dominant resource_profile: heavy | 89% of runs share resource_profile="heavy" (24/27). Low diversity may indicate homogeneous workload or classification bias. |

## Run Clusters

| Dimension | Value | Runs | Avg Tokens | Avg Turns | Avg Duration | Success Rate |
|-----------|-------|------|------------|-----------|--------------|-------------|
| execution_style | adaptive | 3 | 126567 | 1.0 | 10.9m | 100% |
| execution_style | exploratory | 24 | 296734 | 1.0 | 9.0m | 100% |
| resource_profile | heavy | 24 | 296734 | 1.0 | 9.0m | 100% |
| resource_profile | moderate | 3 | 126567 | 1.0 | 10.9m | 100% |

## Per-Run Breakdown

| Run ID | Workflow | Conclusion | Duration | Firewall | Tokens | Turns | MCP Err | Errors |
|--------|----------|------------|----------|----------|--------|-------|---------|--------|
| 40148786961 | Rich issue triage | success | 12.5m | 28/0 | 253.0K | 1 | 0 | 0 |
| 40148780906 | Rich issue triage | success | 12.3m | 35/0 | 413.0K | 1 | 0 | 0 |
| 40148773695 | Rich issue triage | success | 11.7m | 27/0 | 229.4K | 1 | 0 | 0 |
| 40148768023 | Rich issue triage | success | 12.2m | 11/0 | 79.8K | 1 | 0 | 0 |
| 40148761099 | Rich issue triage | success | 11.1m | 13/0 | 97.0K | 1 | 0 | 0 |
| 40148754795 | Rich issue triage | success | 10.9m | 19/0 | 255.0K | 1 | 0 | 0 |
| 40148747682 | Rich issue triage | success | 11.8m | 27/0 | 237.2K | 1 | 0 | 0 |
| 40148740534 | Rich issue triage | success | 10.8m | 28/0 | 241.6K | 1 | 0 | 0 |
| 40148735050 | Rich issue triage | success | 10.2m | 35/0 | 356.2K | 1 | 0 | 0 |
| 40148729091 | Rich issue triage | success | 9.6m | 28/0 | 233.5K | 1 | 0 | 0 |
| 40148722277 | Rich issue triage | success | 9.4m | 17/0 | 202.9K | 1 | 0 | 0 |
| 40148717236 | Rich issue triage | success | 9.2m | 17/0 | 228.0K | 1 | 0 | 0 |
| 40148711936 | Rich issue triage | success | 8.8m | 28/0 | 256.8K | 1 | 0 | 0 |
| 40148705777 | Rich issue triage | success | 11.0m | 42/0 | 403.9K | 1 | 0 | 0 |
| 40148699812 | Rich issue triage | success | 10.4m | 21/0 | 220.5K | 1 | 0 | 0 |
| 40148694128 | Rich issue triage | success | 8.3m | 23/0 | 254.8K | 1 | 0 | 0 |
| 40148687687 | Rich issue triage | success | 8.9m | 41/0 | 446.4K | 1 | 0 | 0 |
| 40148681253 | Rich issue triage | success | 7.5m | 33/0 | 351.7K | 1 | 0 | 0 |
| 40148673866 | Rich issue triage | success | 8.2m | 47/0 | 592.5K ⚠ | 1 | 0 | 0 |
| 40148667678 | Rich issue triage | success | 6.4m | 23/0 | 223.4K | 1 | 0 | 0 |
| 40148661342 | Rich issue triage | success | 8.1m | 37/0 | 393.8K | 1 | 0 | 0 |
| 40148653882 | Rich issue triage | success | 6.9m | 17/0 | 137.0K | 1 | 0 | 0 |
| 40148648449 | Rich issue triage | success | 7.3m | 36/0 | 342.1K | 1 | 0 | 0 |
| 40148642828 | Rich issue triage | success | 7.8m | 34/0 | 317.3K | 1 | 0 | 0 |
| 40148637290 | Rich issue triage | success | 5.4m | 20/0 | 159.9K | 1 | 0 | 0 |
| 40148630929 | Rich issue triage | success | 6.1m | 25/0 | 221.6K | 1 | 0 | 0 |
| 40148626523 | Rich issue triage | success | 6.7m | 35/0 | 353.1K | 1 | 0 | 0 |

