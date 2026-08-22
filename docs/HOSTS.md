# Hosts

Five-host packaging (no UI):

| Host | Path |
|---|---|
| Universal | `plugin.json` (agent-plugins.org) |
| Claude Code | `.claude-plugin/` |
| Grok Build | `.grok-plugin/` (Claude-compatible, zero-config) |
| Codex | `.codex-plugin/` |
| Cursor | `.cursor-plugin/` + `.cursor/rules/` |

No Claude `hooks/hooks.json` in this plugin, so Codex/Cursor hook files are not required.

## WikiTicket SDD

See [WORKLOG.md](WORKLOG.md).
