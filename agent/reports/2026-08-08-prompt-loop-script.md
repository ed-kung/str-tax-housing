# 2026-08-08 — prompt_loop script

Wrote `agent/scripts/prompt_loop.py` to sequentially spawn fresh local Cursor SDK agents that execute `agent/prompts/regulations_prompt.txt` against `AGENT_DATA_PATH/str_regulations.json`.

## Summary

The loop creates one agent at a time (no parallelism) so agents do not race on the shared regulations JSON. Auth and model come from root `.env` (`CURSOR_API_KEY`, `CURSOR_MODEL`). Project setting sources are enabled so `.cursor/rules` apply (including writing reports under `agent/reports/`). After each finished run, `agent/reports/` is `git add`ed but not committed. The loop stops when no unchecked cities remain, or when `--max-runs` is hit.

## Usage

```bash
source .venv/bin/activate
python agent/scripts/prompt_loop.py --max-runs 1
python agent/scripts/prompt_loop.py --stream
```

## Artifacts

- `agent/scripts/prompt_loop.py`
