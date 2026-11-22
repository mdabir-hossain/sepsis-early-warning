# Sepsis Phase 1 Report

## Executive Summary

Phase 1 focused on repository hygiene and public safety. The project folder was inspected, Git status was checked, a safe target folder skeleton was created, `.gitignore` was expanded, and public-facing documentation was added.

No raw data was moved or deleted. No commits or pushes were made. No metrics were invented. README metrics are copied only from existing saved artifacts in `results/` and are clearly caveated as retrospective development artifact metrics.

This folder is not currently a Git repository. Running `git status --short` returned:

```text
fatal: not a git repository (or any of the parent directories): .git
```

## Files Changed

Updated:

- `README.md`
- `.gitignore`

Added:

- `data/README.md`
- `docs/leakage_review.md`
- `SEPSIS_PHASE_1_REPORT.md`

Created folder skeleton:

- `data/`
- `data/raw/`
- `data/interim/`
- `data/processed/`
- `data/sample/`
- `docs/`
- `reports/`
- `reports/figures/`
- `reports/metrics/`
- `src/sepsis_ews/`
- `scripts/`
- `tests/`
- `configs/`

## Public Safety Notes

The expanded `.gitignore` now covers:

- raw clinical `.psv` files
- legacy `training/` raw-data folder
- `data/raw/`, `data/interim/`, and `data/processed/`
- generated feature table `features_windowed_6h_12h_24h.csv`
- parquet intermediates
- large/intermediate `results/` and `figures/` folders
- model artifacts such as `.pkl`, `.joblib`, `.onnx`, `.pt`, `.h5`, and `.sav`
- notebook/runtime caches
- virtual environments
- editor and OS files

Important: `.gitignore` prevents future accidental tracking, but it does not untrack files that are already committed. This folder is not currently a Git repository, so before any future GitHub push, run a clean `git status` after `git init` and verify that raw data and generated artifacts are untracked.

Raw clinical data remains in the local `training/` folder. It was not moved or deleted.

## Reproducibility Notes

The README now describes the current notebook-first state and the planned command interface. Current reproducibility remains limited because:

- dependencies are minimal and unpinned
- no source package implementation exists yet
- no command-line training/evaluation scripts exist yet
- no tests exist yet
- no saved model bundle exists yet

The README reports only existing saved artifact metrics:

- model comparison from `results/model_metrics_cv.json`
- calibration from `results/calibration_report.json`
- final operating point from `results/final_decision.json`

The README explicitly states these values were not independently rerun during Phase 1 and should not be treated as clinical validation.

## Remaining Risks

- This folder is not a Git repository yet.
- Raw data is still physically present in the working tree under `training/`.
- Existing generated artifacts remain physically present under `results/`, `figures/`, and the root feature CSV.
- No automated leakage tests exist yet.
- The feature manifest preview includes high-risk derived names such as `SepsisLabel__miss`, `event_iculos__miss`, and `use_row__miss`; these require review before retraining.
- No independent final holdout test set has been confirmed.
- Notebook 07 references explainability outputs that were not found in `results/` during the audit.
- `requirements.txt` is still unpinned.

## Next Recommended Phase

Begin Phase 2: reproducible environment.

Recommended Phase 2 tasks:

1. Pin the Python version.
2. Add `pyproject.toml`.
3. Add pinned runtime and development requirements.
4. Add formatter/linter/test configuration.
5. Add a minimal CI workflow if the project is ready for GitHub.
6. Do not train new models or change reported metrics in Phase 2.
