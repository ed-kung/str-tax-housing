#!/usr/bin/env python3
"""Sequentially spawn Cursor agents to fill STR regulation research.

Each iteration creates a fresh local agent that executes
``agent/prompts/regulations_prompt.txt`` against
``AGENT_DATA_PATH/str_regulations.json``. Agents run one at a time so they
do not race on that shared file. After each finished run, new/updated files
under ``agent/reports/`` are staged (``git add``) but not committed.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

from cursor_sdk import Agent, CursorAgentError, LocalAgentOptions, close_default_client
from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parents[2]
PROMPT_PATH = REPO_ROOT / "agent" / "prompts" / "regulations_prompt.txt"
REPORTS_DIR = REPO_ROOT / "agent" / "reports"
REGULATIONS_FILENAME = "str_regulations.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Spawn Cursor agents sequentially to research STR regulations "
            "for unchecked cities in AGENT_DATA_PATH/str_regulations.json."
        )
    )
    parser.add_argument(
        "--max-runs",
        type=int,
        default=None,
        help="Maximum number of agents to spawn (default: until no unchecked cities remain).",
    )
    parser.add_argument(
        "--stream",
        action="store_true",
        help="Print assistant text as it streams.",
    )
    return parser.parse_args()


def load_env() -> tuple[str, str, Path]:
    load_dotenv(REPO_ROOT / ".env")
    api_key = os.environ.get("CURSOR_API_KEY", "").strip()
    model = os.environ.get("CURSOR_MODEL", "").strip()
    agent_data = os.environ.get("AGENT_DATA_PATH", "").strip()

    missing = [
        name
        for name, value in (
            ("CURSOR_API_KEY", api_key),
            ("CURSOR_MODEL", model),
            ("AGENT_DATA_PATH", agent_data),
        )
        if not value
    ]
    if missing:
        raise SystemExit(f"Missing required .env values: {', '.join(missing)}")

    return api_key, model, Path(agent_data)


def read_prompt() -> str:
    if not PROMPT_PATH.is_file():
        raise SystemExit(f"Prompt file not found: {PROMPT_PATH}")
    return PROMPT_PATH.read_text(encoding="utf-8").strip()


def regulations_path(agent_data: Path) -> Path:
    return agent_data / REGULATIONS_FILENAME


def count_unchecked(path: Path) -> int:
    if not path.is_file():
        raise SystemExit(f"Regulations file not found: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise SystemExit(f"Expected a list in {path}, got {type(data).__name__}")
    return sum(1 for item in data if not item.get("agent_checked"))


def next_unchecked_label(path: Path) -> str | None:
    data = json.loads(path.read_text(encoding="utf-8"))
    for item in data:
        if not item.get("agent_checked"):
            city = item.get("city", "?")
            state = item.get("state", "?")
            return f"{city}, {state}"
    return None


def stage_reports() -> list[str]:
    """Stage agent/reports changes without committing. Returns staged paths."""
    subprocess.run(
        ["git", "add", "--", str(REPORTS_DIR.relative_to(REPO_ROOT))],
        cwd=REPO_ROOT,
        check=True,
    )
    listed = subprocess.run(
        [
            "git",
            "diff",
            "--cached",
            "--name-only",
            "--",
            str(REPORTS_DIR.relative_to(REPO_ROOT)),
        ],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return [line for line in listed.stdout.splitlines() if line.strip()]


def run_one_agent(
    *,
    api_key: str,
    model: str,
    prompt: str,
    run_index: int,
    city_label: str,
    stream: bool,
) -> None:
    name = f"str-regulations-{run_index:03d}"
    print(f"\n=== Run {run_index}: {city_label} (agent name={name}) ===", flush=True)

    with Agent.create(
        model=model,
        api_key=api_key,
        name=name,
        local=LocalAgentOptions(
            cwd=str(REPO_ROOT),
            # Load repo .cursor/rules and AGENTS.md so the agent writes reports.
            setting_sources=["project"],
        ),
    ) as agent:
        run = agent.send(prompt)
        print(f"agent_id={agent.agent_id} run_id={run.id}", flush=True)

        if stream:
            for message in run.messages():
                if message.type == "assistant":
                    for block in message.message.content:
                        if block.type == "text":
                            print(block.text, end="", flush=True)
            print(flush=True)

        result = run.wait()

    if result.status == "error":
        raise SystemExit(
            f"Run failed: id={result.id} agent_id={result.agent_id} "
            f"status={result.status}"
        )

    print(
        f"Finished status={result.status} duration_ms={result.duration_ms}",
        flush=True,
    )
    if result.result:
        preview = result.result if len(result.result) <= 500 else result.result[:500] + "…"
        print(f"Result preview:\n{preview}", flush=True)

    staged = stage_reports()
    if staged:
        print("Staged (not committed):", flush=True)
        for path in staged:
            print(f"  {path}", flush=True)
    else:
        print("No agent/reports changes to stage.", flush=True)


def main() -> int:
    args = parse_args()
    api_key, model, agent_data = load_env()
    prompt = read_prompt()
    regs_path = regulations_path(agent_data)

    print(f"Repo: {REPO_ROOT}")
    print(f"Model: {model}")
    print(f"Regulations: {regs_path}")
    print(f"Prompt: {PROMPT_PATH}")

    run_index = 0
    try:
        while True:
            if args.max_runs is not None and run_index >= args.max_runs:
                print(f"\nReached --max-runs={args.max_runs}. Stopping.")
                break

            remaining = count_unchecked(regs_path)
            city_label = next_unchecked_label(regs_path)
            if remaining == 0 or city_label is None:
                print("\nNo unchecked cities remaining. Done.")
                break

            print(f"\nUnchecked cities remaining: {remaining}")
            run_index += 1
            try:
                run_one_agent(
                    api_key=api_key,
                    model=model,
                    prompt=prompt,
                    run_index=run_index,
                    city_label=city_label,
                    stream=args.stream,
                )
            except CursorAgentError as err:
                print(
                    f"Startup/API failure: {err.message} "
                    f"(retryable={err.is_retryable})",
                    file=sys.stderr,
                )
                return 1
    finally:
        close_default_client()

    print(f"\nCompleted {run_index} agent run(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
