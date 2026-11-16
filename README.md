# Claude MCP Telemetry & Usage Starter

A lightweight, open-source Python starter kit for inspecting Claude API usage, auditing organizational activity logs, and exposing telemetry metrics via the **Model Context Protocol (MCP)**.

Built for developers and platform engineers who want clean visibility into token consumption, project activity, and API rate limits without heavy enterprise overhead.

## Key Features
- **Usage & Activity Poller:** Clean Python client wrapper for fetching and structuring Claude workspace activity and usage metrics.
- **MCP Server Ready:** Exposes usage summaries as standard MCP resources so you can query your own API health directly inside Claude Desktop or Claude Code.
- **Zero-Blocker Local Storage:** Exports structured JSON/CSV logs ready for local dashboards or lightweight observability pipelines.
- **Privacy-First Design:** Metadata-only mode strips prompt and completion payloads by default, logging only timestamps, token counts, and model IDs.

## Quick Start

### 1. Clone the repository
```bash
git clone https://github.com
cd claude-mcp-telemetry-starter
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure environment variables
```bash
cp .env.example .env
# Add your ANTHROPIC_API_KEY or ANTHROPIC_ADMIN_KEY
```

### 4. Run a sample usage check
```bash
python src/fetch_metrics.py --mode metadata-only
```

## Roadmap
- [x] Basic Python client wrapper & metadata-only log formatter
- [ ] Full MCP server tool definitions for real-time usage queries
- [ ] Docker Compose template for local Prometheus/Grafana visualization
- [ ] GitHub Action for automated weekly token-spend summaries

## Contributing
Contributions, issues, and feature requests are welcome! Feel free to open a pull request or start a discussion to help make Claude observability simpler for the open-source community.

## License
Distributed under the **MIT License**. See `LICENSE` for more information.
