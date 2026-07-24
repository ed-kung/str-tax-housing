# Permits Data Research Agent

You are a research assistant helping out with data preparation and analysis for the economics research project contained in this repo. This file is a living document to help you get up to speed on the current state of the project.

## Project 

Understand how short term rental regulations impacted municipal taxes.  The scope of the project may change over time.

## Stack

- **Python**: use the repo-local `.venv` (`python3 -m venv .venv` then `pip install -r requirements.txt`)
- Default packages: numpy, pandas, matplotlib, pyarrow, scikit-learn (and others as needed)
- **R**: available for econometric / statistical work

## Data paths

Paths are set in `.env` (see `.env.example`):

| Variable | Role |
| --- | --- |
| `RAW_DATA_PATH` | Local directory with raw data (**read-only**) |
| `MY_DATA_PATH` | Local directory for additional datasets processed by the human user (**read-only**) |
| `AGENT_DATA_PATH` | Local directory for files and artifacts stored by the agent |

Never overwrite, modify, or delete anything under `RAW_DATA_PATH` or `MY_DATA_PATH`. Write all derived artifacts to `AGENT_DATA_PATH`.

## Important data files

- `RAW_DATA_PATH/sales-analysis-redfin/data/best_treatment_dates_2026-0y.csv`: Passage and enforcement dates for 50 cities.
- `RAW_DATA_PATH/lincoln-institute/FiSC-Full-Dataset-2023-Update.xlsx`: Lincoln Institute Fiscally Standardized Cities data. Data is on sheet "Data".
- `RAW_DATA_PATH/zhvi/City_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv`: City-level Zillow Home Value Index historical. 

## Repo layout

- `scripts/` — reproducible analysis scripts (created by human user)
- `notebooks/` - exploratory jupyter notebooks by human user
- `reports/` - reports created by human user
- `agent/scripts/` - reproducible analysis scripts created by agent
- `agent/reports/` - post-task summaries of work and findings by agent
- `.cursor/rules/` — agent rules (data protection, workflow, stack)

## Environment notes

- `.venv` is set up; core packages present except `scikit-learn` (not installed yet). No `requirements.txt` in repo currently.

## Agent conventions

- After finishing a task, write a dated entry under `agent/reports/` (e.g. `diary/YYYY-MM-DD-short-slug.md`).
