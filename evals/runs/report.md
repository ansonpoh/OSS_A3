# Audit Report — Cross-Run Analysis

## Executive Summary

| Metric | Value |
|--------|-------|
| Runs analyzed | 29 |
| Runs with firewall data | 29 |
| Runs without firewall data | 0 |
| Total requests | 301 |
| Allowed requests | 301 |
| Blocked requests | 0 |
| Overall denial rate | 0.0% |
| Unique domains | 1 |

## Metrics Trends

| Metric | Total | Avg/run | Min | Max | Spikes |
|--------|-------|---------|-----|-----|--------|
| Token Trend | 11873815 | 409441 | 134577 | 748799 | — |
| Turns | 398 | 13.7 | — | 22 | — |
| Duration | — | 4.4m | 3.9m | 5.6m | — |

## MCP Server Health (29 runs)

| Server | Connected | Error Rate | Total Calls | Errors | Status |
|--------|-----------|------------|-------------|--------|--------|
| `safeoutputs` | 29/29 | 0.0% | 45 | 0 | ✅ ok |

## Domain Inventory

| Domain | Status | Seen In | Allowed | Blocked |
|--------|--------|---------|---------|--------|
| `api.anthropic.com:443` | ✅ allowed | 29/29 runs | 301 | 0 |

## Agent Event Pattern Analysis

| Severity | Category | Title | Summary |
|----------|----------|-------|--------|
| ℹ info | execution | Cross-run log template patterns | Mined 2 distinct event templates across 6 pipeline stages from 58 events in 29 runs. (plan=1 finish=1) |

## Cluster Patterns

| Severity | Kind | Title | Description |
|----------|------|-------|-------------|
| 🟡 low | style_skew | Dominant graders: pass | 90% of runs share graders="pass" (26/29). Low diversity may indicate homogeneous workload or classification bias. |

## Run Clusters

| Dimension | Value | Runs | Avg Tokens | Avg Turns | Avg Duration | Success Rate |
|-----------|-------|------|------------|-----------|--------------|-------------|
| execution_style | adaptive | 7 | 240643 | 8.7 | 4.2m | 100% |
| execution_style | directed | 2 | 134678 | 4.0 | 4.2m | 100% |
| execution_style | exploratory | 20 | 495997 | 16.5 | 4.5m | 100% |
| resource_profile | heavy | 19 | 507228 | 16.8 | 4.5m | 100% |
| resource_profile | lean | 2 | 134678 | 4.0 | 4.2m | 100% |
| resource_profile | moderate | 8 | 245890 | 8.9 | 4.2m | 100% |
| graders | mixed | 3 | 288096 | 8.7 | 4.3m | 100% |
| graders | pass | 26 | 423443 | 14.3 | 4.4m | 100% |

## Per-Run Breakdown

| Run ID | Workflow | Conclusion | Duration | Firewall | Tokens | Turns | MCP Err | Errors |
|--------|----------|------------|----------|----------|--------|-------|---------|--------|
| 40272528165 | Rich issue triage | success | 4.1m | 14/0 | 598.9K | 17 | 0 | 0 |
| 40272444653 | Rich issue triage | success | 4.1m | 7/0 | 233.7K | 9 | 0 | 0 |
| 40272356628 | Rich issue triage | success | 4.3m | 10/0 | 398.0K | 13 | 0 | 0 |
| 40272268969 | Rich issue triage | success | 5.0m | 19/0 | 748.8K | 22 | 0 | 0 |
| 40272181231 | Rich issue triage | success | 4.2m | 7/0 | 233.0K | 9 | 0 | 0 |
| 40272096151 | Rich issue triage | success | 3.9m | 5/0 | 134.6K | 4 | 0 | 0 |
| 40272011169 | Rich issue triage | success | 4.4m | 5/0 | 134.8K | 4 | 0 | 0 |
| 40271908811 | Rich issue triage | success | 4.9m | 15/0 | 657.4K | 20 | 0 | 0 |
| 40271823600 | Rich issue triage | success | 4.6m | 11/0 | 454.6K | 17 | 0 | 0 |
| 40271741258 | Rich issue triage | success | 4.4m | 7/0 | 233.3K | 9 | 0 | 0 |
| 40271658174 | Rich issue triage | success | 4.7m | 10/0 | 397.3K | 13 | 0 | 0 |
| 40271571741 | Rich issue triage | success | 4.2m | 7/0 | 235.4K | 9 | 0 | 0 |
| 40271485171 | Rich issue triage | success | 4.5m | 10/0 | 392.0K | 14 | 0 | 0 |
| 40271400150 | Rich issue triage | success | 4.3m | 9/0 | 338.5K | 13 | 0 | 0 |
| 40271315096 | Rich issue triage | success | 4.1m | 7/0 | 239.3K | 9 | 0 | 0 |
| 40271231206 | Rich issue triage | success | 4.3m | 13/0 | 554.8K | 20 | 0 | 0 |
| 40271149616 | Rich issue triage | success | 3.9m | 11/0 | 447.5K | 14 | 0 | 0 |
| 40271061144 | Rich issue triage | success | 4.2m | 11/0 | 451.4K | 17 | 0 | 0 |
| 40270979304 | Rich issue triage | success | 5.6m | 10/0 | 413.8K | 15 | 0 | 0 |
| 40270898956 | Rich issue triage | success | 4.5m | 14/0 | 639.6K | 20 | 0 | 0 |
| 40270815483 | Rich issue triage | success | 4.9m | 13/0 | 582.3K | 20 | 0 | 0 |
| 40270730786 | Rich issue triage | success | 4.6m | 15/0 | 594.9K | 18 | 0 | 0 |
| 40270636010 | Rich issue triage | success | 4.9m | 13/0 | 498.8K | 17 | 0 | 0 |
| 40270548650 | Rich issue triage | success | 3.9m | 8/0 | 275.8K | 7 | 0 | 0 |
| 40270463848 | Rich issue triage | success | 4.7m | 12/0 | 507.4K | 18 | 0 | 0 |
| 40270377975 | Rich issue triage | success | 4.0m | 11/0 | 447.3K | 15 | 0 | 0 |
| 40270296990 | Rich issue triage | success | 4.2m | 8/0 | 282.6K | 10 | 0 | 0 |
| 40270211048 | Rich issue triage | success | 4.2m | 7/0 | 234.1K | 9 | 0 | 0 |
| 40270128996 | Rich issue triage | success | 4.2m | 12/0 | 514.0K | 16 | 0 | 0 |

