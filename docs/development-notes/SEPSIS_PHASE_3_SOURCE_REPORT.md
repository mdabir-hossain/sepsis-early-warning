# Sepsis Phase 3 Source Report

## Executive Summary

Phase 3 created a safe source-package and script skeleton so the project can start moving away from notebook-only structure. The new modules define future package boundaries for data loading, feature engineering, patient-grouped splitting, training, calibration, policy sweeps, evaluation, explainability, and inference.

All new source functions are lightweight placeholders and raise clear `NotImplementedError` messages. No notebook logic was extracted yet. No raw data was read, moved, or deleted. No training was rerun. No saved metrics, figures, generated artifacts, or model outputs were changed.

Tests were added for importability and placeholder failure behaviour, but they could not be executed in this shell because `python`, `py`, and `pytest` are not available on PATH.

## Files Changed

Added source modules:

- `src/sepsis_ews/placeholders.py`
- `src/sepsis_ews/data.py`
- `src/sepsis_ews/features.py`
- `src/sepsis_ews/split.py`
- `src/sepsis_ews/train.py`
- `src/sepsis_ews/calibrate.py`
- `src/sepsis_ews/policies.py`
- `src/sepsis_ews/evaluate.py`
- `src/sepsis_ews/explain.py`
- `src/sepsis_ews/inference.py`

Added script placeholders:

- `scripts/build_dataset.py`
- `scripts/train_model.py`
- `scripts/evaluate_model.py`
- `scripts/run_policy_sweep.py`

Added tests:

- `tests/test_skeleton_modules.py`

Updated:

- `README.md`

## Source Package Skeleton

The package now contains these Phase 3 boundaries:

- `data.py`: future raw file discovery, parsing, and dataset assembly.
- `features.py`: future patient-grouped temporal feature engineering and feature manifest work.
- `split.py`: future patient-level split and no-overlap validation utilities.
- `train.py`: future model training and out-of-fold prediction workflow.
- `calibrate.py`: future calibration workflow and reliability reporting.
- `policies.py`: future threshold, lockout, and alert-policy sweep logic.
- `evaluate.py`: future classification, calibration, and policy metric reporting.
- `explain.py`: future global/local explainability outputs.
- `inference.py`: future sample inference/demo boundary once a model bundle exists.
- `placeholders.py`: shared helper for consistent `NotImplementedError` messages.

Each module has a docstring explaining its future responsibility. The placeholder functions do not read raw data, do not depend on `training/` or `results/`, do not hardcode local paths, and do not implement modelling logic.

## Script Placeholders

The following scripts were added as future CLI entry points:

- `scripts/build_dataset.py`
- `scripts/train_model.py`
- `scripts/evaluate_model.py`
- `scripts/run_policy_sweep.py`

Each script:

- uses `argparse`
- accepts a `--config` argument
- calls the matching package-level placeholder function
- raises a clear `NotImplementedError` through the package placeholder path
- does not silently succeed
- does not run notebooks
- does not load raw data
- does not train models
- does not modify files

## Tests Added

Existing test retained:

- `tests/test_package_import.py`

New test added:

- `tests/test_skeleton_modules.py`

The new test checks:

- all core Phase 3 modules can be imported
- placeholder functions raise `NotImplementedError` with a clear "not implemented yet" message

The tests do not require:

- raw `.psv` files
- `training/`
- `results/`
- `figures/`
- `notebooks/`
- generated features
- model artifacts

Test execution attempted:

```text
python -m pytest
py -m pytest
pytest
```

All attempts failed because the commands were not available on PATH in this shell.

## Git Status

This folder is still not a Git repository. Running `git status --short` returned:

```text
fatal: not a git repository (or any of the parent directories): .git
```

Git was not initialised because this phase explicitly avoids doing so unless instructed later.

## Public Safety Notes

No public-safety-sensitive files were touched.

The following remain ignored by `.gitignore`:

- `training/`
- `data/raw/`
- `data/interim/`
- `data/processed/`
- `*.psv`
- generated feature tables
- `results/`
- `figures/`
- model artifacts
- virtual environments
- local secrets

The new source and script files are safe to publish because they contain no raw data, no local absolute paths, no generated metrics, and no clinical claims.

## Reproducibility Notes

This phase improves the project structure by creating package and CLI boundaries, but the project is not fully reproducible yet.

Current state:

- package skeleton exists
- script skeletons exist
- minimal tests exist
- no real pipeline logic exists yet
- tests could not be run locally because Python tooling is unavailable on PATH

The README now notes that `src/sepsis_ews/` modules and `scripts/` entry points are skeletons that raise `NotImplementedError` until later phases.

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
- raw clinical data
- model artifacts

No training was rerun. No notebook was modified. No model artifact was created. No metrics were invented or changed.

## Remaining Risks

- Python is not available on PATH, so the package and test suite could not be validated locally.
- The scripts are placeholders only and intentionally raise `NotImplementedError`.
- The source modules do not yet contain real data, feature, split, training, calibration, policy, or evaluation logic.
- No leakage tests exist yet beyond placeholder import/failure tests and the documentation checklist.
- No CI exists yet.
- The folder is still not a Git repository.
- Raw/generated data remains physically present locally and must be checked before any future public GitHub push.

## Next Recommended Phase

Begin Phase 4: leakage and validation hardening.

Recommended Phase 4 tasks:

1. Add a feature-name blocklist utility that rejects target/future-derived fields.
2. Add patient-group split validation helpers.
3. Add tests for patient overlap, blocked feature names, and temporal ordering using tiny synthetic fixtures only.
4. Keep raw data, notebooks, results, metrics, and model artifacts untouched.
5. Do not retrain models or change reported performance.
