<details>
<summary>MCP Gateway</summary>

- ✓ **startup** MCPG Gateway version: v0.4.36
- ✓ **startup** Starting MCPG with config: stdin, listen: 0.0.0.0:8080, log-dir: /tmp/gh-aw/mcp-logs/
- ✓ **startup** WASM compilation cache directory: /tmp/gh-aw/wazero-cache
- ✓ **startup** Environment validation passed
- ✓ **startup** Loaded 1 MCP server(s): [safeoutputs]
- ✓ **startup** Guards sink server ID logging enrichment disabled (no sink server IDs configured)
- ✓ **startup** OpenTelemetry tracing disabled (no OTLP endpoint configured)
- ✓ **backend**
  ```
  Successfully connected to MCP backend server, command=docker
  ```
- 🔍 rpc **safeoutputs**→`tools/list`
- 🔍 rpc **safeoutputs**←`resp` `{"jsonrpc":"2.0","id":1,"result":{"ttlMs":0,"cacheScope":"","tools":[{"description":"WRITE-ONCE: do NOT probe this tool with empty or placeholder arguments. If not ready to post a real comment, call noop. Adds a comment to an existing GitHub issue, pull request, or discussion; use create_issue, create_discussion, or create_pull_request for new items. Input is limited to 524288 characters, 10 mentions, and configured max-links URL occurrences (default: 50). Oversized agent content is automatically replaced b...`
- ✓ **startup** Starting MCPG in ROUTED mode on 0.0.0.0:8080
- ✓ **startup** Routes: /mcp/<server> where <server> is one of: [safeoutputs]
- ✓ **startup** TLS not configured — listening on http://0.0.0.0:8080 (set --tls-cert/--tls-key to enable)
- ✓ **backend**
  ```
  Successfully connected to MCP backend server, command=docker
  ```
- 🔍 rpc **safeoutputs**→`tools/call` `add_labels`
  
  ```json
  {"params":{"arguments":{"item_number":"708","labels":[{"name":"upstream","rationale":"Dependency advisory: the CVE concerns Pygments, a Rich dependency, not Rich itself."}]},"name":"add_labels"}}
  ```
- 🔍 rpc **safeoutputs**←`resp`
  
  ```json
  {"id":1,"result":{"content":[{"text":"{\"result\":\"success\"}","type":"text"}]}}
  ```
- 🔍 rpc **safeoutputs**→`tools/call` `{"jsonrpc":"2.0","method":"tools/call","params":{"arguments":{"body":"The advisory in this report concerns the Pygments dependency (CVE-2026-4539 in Pygments 2.19.2), not Rich itself. The `requests` entry in the pip-audit output is also outside Rich, which does not depend on `requests`. Rich is labelled `upstream` so a maintainer can follow up with the Pygments project.\n\nFor private vulnerability reports about Rich, see [SECURITY.md](https://github.com/Textualize/rich/blob/master/SECURITY.md). Please do n...`
- 🔍 rpc **safeoutputs**←`resp`
  
  ```json
  {"id":1,"result":{"content":[{"text":"{\"result\":\"success\",\"temporary_id\":\"aw_Nhfv22rS\",\"comment\":\"#aw_Nhfv22rS\"}","type":"text"}]}}
  ```
- ✓ **shutdown** Shutting down gateway...

</details>
