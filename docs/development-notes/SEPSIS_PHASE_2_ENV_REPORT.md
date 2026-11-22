# Sepsis Phase 2 Environment Report

## Executive Summary

Phase 2 focused only on making the Python environment and project metadata more professional and reproducible. The project now has a `pyproject.toml`, constrained runtime requirements, separate development requirements, a lightweight package placeholder under `src/sepsis_ews/`, and a minimal import smoke test.

No raw data, notebooks, generated artifacts, saved metrics, figures, model results, or model artifacts were moved, deleted, rerun, or modified.

Local verification is limited because neither `python`, `py`, nor `pytest` is available on PATH in this shell. The new test infrastructure is present, but tests were not executed successfully in this environment.

## Files Changed

Added:

- `.python-version`
- `pyproject.toml`
- `requirements-dev.txt`
- `src/sepsis_ews/__init__.py`
- `tests/test_package_import.py`
- `SEPSIS_PHASE_2_ENV_REPORT.md`

Updated:

- `README.md`
- `requirements.txt`
- `.gitignore`

## Environment Changes

Added `pyproject.toml` with:

- project name: `sepsis-early-warning`
- package layout: `src/sepsis_ews`
- Python support range: `>=3.10,<3.13`
- setuptools build backend
- package discovery from `src`
- pytest configuration
- ruff linting and formatting configuration

Added `.python-version` with:

```text
3.11
```

This records the intended local Python version for tools that support `.python-version`. It was not verified locally because Python is not available on PATH in this shell.

Added minimal package placeholder:

```text
src/sepsis_ews/__init__.py
```

Added minimal smoke test:

```text
tests/test_package_import.py
```

The test only checks that the package imports and exposes the expected placeholder version. It does not touch raw data or model artifacts.

## Dependency Decisions

The previous `requirements.txt` contained unpinned package names:

```text
pandas
numpy
scikit-learn
matplotlib
pyarrow
jupyter
```

Because local package versions could not be inspected, exact pins were not fabricated. Instead, `requirements.txt` now uses constrained ranges for the existing notebook workflow:

```text
numpy>=1.24,<3.0
pandas>=2.0,<3.0
scikit-learn>=1.3,<2.0
matplotlib>=3.7,<4.0
pyarrow>=12,<18
jupyterlab>=4.0,<5.0
```

Rationale:

- `numpy`, `pandas`, and `pyarrow` are needed for tabular/parquet workflows.
- `scikit-learn` is needed for the saved Logistic Regression, HistGradientBoosting, GroupKFold, and calibration workflow.
- `matplotlib` is needed for existing figures.
- `jupyterlab` supports the current notebook-first workflow.
- Heavy deployment dependencies such as Streamlit, FastAPI, Uvicorn, Docker tooling, SHAP, MLflow, and cloud SDKs were intentionally not added in Phase 2.

Added `requirements-dev.txt` with:

```text
pytest>=8.0,<9.0
ruff>=0.6,<1.0
```

Rationale:

- `pytest` supports the new test harness.
- `ruff` provides lightweight linting and formatting configuration.

This is not a full lockfile. A future phase should produce an exact lockfile after Python is available and dependencies can be installed/tested.

## Git Status

This folder is still not a Git repository. Running `git status --short` returned:

```text
fatal: not a git repository (or any of the parent directories): .git
```

Git was not initialised because this phase explicitly avoids doing so unless instructed later.

## Public Safety Notes

`.gitignore` was extended to cover packaging and test outputs:

- `build/`
- `dist/`
- `*.egg-info/`
- `.coverage`
- `htmlcov/`

Existing public-safety ignores remain in place for:

- raw clinical data
- `.psv` files
- `training/`
- `data/raw/`
- `data/interim/`
- `data/processed/`
- generated feature tables
- parquet files
- `results/`
- `figures/`
- model artifacts
- virtual environments
- local secret files

No raw clinical data was moved or deleted.

## Reproducibility Notes

README setup instructions now include:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```

Development checks are documented as:

```bash
pip install -r requirements-dev.txt
pytest
ruff check .
```

The planned pipeline scripts are still documented as planned and not implemented. The project is more structured than before, but it is not fully reproducible yet.

Verification attempted:

- `python` was not found on PATH.
- `py` was not found on PATH.
- `pytest` was not found on PATH.

Therefore, the new smoke test has not been executed in this shell.

## What Was Not Changed

The following were not modified:

- `training/`
- `data/raw/`
- `data/interim/`
- `data/processed/`
- `features_windowed_6h_12h_24h.csv`
- `results/`
- `figures/`
- `notebooks/`
- saved metrics
- model results
- raw clinical data

No training was rerun. No model artifacts were created. No clinical claims were added.

## Remaining Risks

- Python is not available on PATH in the current shell, so setup and tests could not be validated.
- Dependency ranges are constrained but not fully locked.
- No CI exists yet.
- No real pipeline scripts exist yet.
- No source modules beyond `__init__.py` exist yet.
- No leakage tests exist yet beyond the documentation checklist.
- The folder is still not a Git repository.
- Raw/generated data remains physically present locally and must be checked carefully before any future GitHub push.

## Next Recommended Phase

Begin Phase 3: source package skeleton.

Recommended Phase 3 tasks:

1. Add empty or lightly stubbed modules for `data`, `features`, `split`, `train`, `calibrate`, `policies`, `evaluate`, `explain`, and `inference`.
2. Add script placeholders that fail clearly with "not implemented yet" rather than silently doing nothing.
3. Keep notebooks unchanged.
4. Do not retrain models or modify metrics.
5. Add only tiny tests that do not require raw data.
