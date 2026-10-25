# Audit Report — Cross-Run Analysis

## Executive Summary

| Metric | Value |
|--------|-------|
| Runs analyzed | 29 |
| Runs with firewall data | 29 |
| Runs without firewall data | 0 |
| Total requests | 837 |
| Allowed requests | 837 |
| Blocked requests | 0 |
| Overall denial rate | 0.0% |
| Unique domains | 1 |

## Metrics Trends

| Metric | Total | Avg/run | Min | Max | Spikes |
|--------|-------|---------|-----|-----|--------|
| Token Trend | 8686558 | 299536 | 96203 | 552272 | — |
| Turns | 29 | 1.0 | — | 1 | — |
| Duration | — | 5.7m | 4.5m | 8.9m | — |

## MCP Server Health (29 runs)

| Server | Connected | Error Rate | Total Calls | Errors | Status |
|--------|-----------|------------|-------------|--------|--------|
| `safeoutputs` | 29/29 | 0.0% | 45 | 0 | ✅ ok |

## Domain Inventory

| Domain | Status | Seen In | Allowed | Blocked |
|--------|--------|---------|---------|--------|
| `api.openai.com:443` | ✅ allowed | 29/29 runs | 837 | 0 |

## Agent Event Pattern Analysis

| Severity | Category | Title | Summary |
|----------|----------|-------|--------|
| ℹ info | execution | Cross-run log template patterns | Mined 2 distinct event templates across 6 pipeline stages from 58 events in 29 runs. (finish=1 plan=1) |

## Cluster Patterns

| Severity | Kind | Title | Description |
|----------|------|-------|-------------|
| 🟡 low | style_skew | Dominant resource_profile: heavy | 90% of runs share resource_profile="heavy" (26/29). Low diversity may indicate homogeneous workload or classification bias. |
| 🟡 low | style_skew | Dominant execution_style: exploratory | 90% of runs share execution_style="exploratory" (26/29). Low diversity may indicate homogeneous workload or classification bias. |

## Run Clusters

| Dimension | Value | Runs | Avg Tokens | Avg Turns | Avg Duration | Success Rate |
|-----------|-------|------|------------|-----------|--------------|-------------|
| execution_style | adaptive | 3 | 124355 | 1.0 | 4.7m | 100% |
| execution_style | exploratory | 26 | 319749 | 1.0 | 5.8m | 100% |
| resource_profile | heavy | 26 | 319749 | 1.0 | 5.8m | 100% |
| resource_profile | moderate | 3 | 124355 | 1.0 | 4.7m | 100% |

## Per-Run Breakdown

| Run ID | Workflow | Conclusion | Duration | Firewall | Tokens | Turns | MCP Err | Errors |
|--------|----------|------------|----------|----------|--------|-------|---------|--------|
| 40171676399 | Rich issue triage | success | 5.1m | 30/0 | 396.2K | 1 | 0 | 0 |
| 40171613493 | Rich issue triage | success | 4.9m | 30/0 | 257.9K | 1 | 0 | 0 |
| 40171552493 | Rich issue triage | success | 5.4m | 30/0 | 273.4K | 1 | 0 | 0 |
| 40171488539 | Rich issue triage | success | 5.3m | 34/0 | 309.4K | 1 | 0 | 0 |
| 40171422745 | Rich issue triage | success | 5.2m | 26/0 | 313.8K | 1 | 0 | 0 |
| 40171358839 | Rich issue triage | success | 4.5m | 14/0 | 96.8K | 1 | 0 | 0 |
| 40171296246 | Rich issue triage | success | 4.7m | 14/0 | 96.2K | 1 | 0 | 0 |
| 40171235061 | Rich issue triage | success | 5.4m | 40/0 | 428.1K | 1 | 0 | 0 |
| 40171166529 | Rich issue triage | success | 5.6m | 36/0 | 333.3K | 1 | 0 | 0 |
| 40171095323 | Rich issue triage | success | 4.8m | 21/0 | 180.0K | 1 | 0 | 0 |
| 40171035296 | Rich issue triage | success | 4.7m | 17/0 | 221.9K | 1 | 0 | 0 |
| 40170974939 | Rich issue triage | success | 5.2m | 24/0 | 256.0K | 1 | 0 | 0 |
| 40170914424 | Rich issue triage | success | 4.9m | 36/0 | 323.2K | 1 | 0 | 0 |
| 40170851646 | Rich issue triage | success | 5.6m | 30/0 | 293.6K | 1 | 0 | 0 |
| 40170787210 | Rich issue triage | success | 5.1m | 32/0 | 309.3K | 1 | 0 | 0 |
| 40170725830 | Rich issue triage | success | 5.2m | 32/0 | 307.4K | 1 | 0 | 0 |
| 40170663712 | Rich issue triage | success | 5.3m | 18/0 | 215.7K | 1 | 0 | 0 |
| 40170601227 | Rich issue triage | success | 5.2m | 28/0 | 272.4K | 1 | 0 | 0 |
| 40170539541 | Rich issue triage | success | 5.2m | 22/0 | 286.9K | 1 | 0 | 0 |
| 40170475429 | Rich issue triage | success | 6.0m | 37/0 | 395.3K | 1 | 0 | 0 |
| 40170415441 | Rich issue triage | success | 5.8m | 42/0 | 552.3K | 1 | 0 | 0 |
| 40170355433 | Rich issue triage | success | 5.4m | 27/0 | 276.7K | 1 | 0 | 0 |
| 40170293944 | Rich issue triage | success | 6.1m | 42/0 | 533.5K | 1 | 0 | 0 |
| 40170231687 | Rich issue triage | success | 5.4m | 30/0 | 248.8K | 1 | 0 | 0 |
| 40170165711 | Rich issue triage | success | 5.2m | 20/0 | 215.8K | 1 | 0 | 0 |
| 40170104352 | Rich issue triage | success | 8.9m | 38/0 | 374.7K | 1 | 0 | 0 |
| 40170043055 | Rich issue triage | success | 8.1m | 26/0 | 214.3K | 1 | 0 | 0 |
| 40169980504 | Rich issue triage | success | 8.6m | 32/0 | 278.4K | 1 | 0 | 0 |
| 40169918098 | Rich issue triage | success | 8.3m | 29/0 | 425.2K | 1 | 0 | 0 |

