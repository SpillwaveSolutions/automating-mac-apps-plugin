# Automating Mac Apps Workspace (meta)

This folder hosts:
- `plugins/automating-mac-apps-plugin/`: the Claude plugin payload (skills/agents/commands).
- `tests/`: local test suite (unit + integration) that is **not** shipped with the plugin.
- `pyproject.toml`: Poetry config for the test harness only.

## Run tests (Poetry)
```bash
poetry install --with test
poetry run pytest
```

This is not ready for prime time.
Do not use unless you are a developer and want to help fix it. 

More details: see `README-tests.md`.
