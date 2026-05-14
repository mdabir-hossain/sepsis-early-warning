# Sepsis Phase 4 Leakage and Validation Report

## Executive Summary

Phase 4 added small, public-safe leakage and validation guardrails using only source utilities and tiny synthetic-test patterns. The project now has utilities to detect target/future-derived feature names, fail clearly when blocked feature names are present, assert no patient overlap between train and validation groups, and check per-patient time ordering.

No raw data was read, moved, or deleted. No notebooks were modified. No training was rerun. No saved metrics, results, figures, generated artifacts, or model artifacts were changed.

Tests were added, but they could not be executed in this shell because `python`, `py`, and `pytest` are not available on PATH.

## Files Changed

Updated:

- `src/sepsis_ews/features.py`
- `src/sepsis_ews/split.py`
- `docs/leakage_review.md`
- `README.md`

Added:

- `tests/test_feature_leakage.py`
- `tests/test_split_validation.py`
- `tests/test_temporal_ordering.py`
- `SEPSIS_PHASE_4_LEAKAGE_VALIDATION_REPORT.md`

## Leakage Guardrails Added

Added feature-name blocklist utilities in `src/sepsis_ews/features.py`:

- `BLOCKED_FEATURE_PATTERNS`
- `find_blocked_feature_names(feature_names)`
- `validate_feature_names(feature_names)`

Blocked patterns are conservative and case-insensitive:

```text
SepsisLabel
event_iculos
use_row
future_
target_
label_
sepsis_time
onset_time
```

The guard catches exact risky names and derived names such as:

```text
SepsisLabel__miss
event_iculos__miss
future_lactate_mean
target_score_rolling
```

`validate_feature_names(...)` raises `ValueError` listing blocked feature names. It does not silently drop, rename, or alter columns.

## Patient Split Validation Added

Added patient-overlap validation in `src/sepsis_ews/split.py`:

- `assert_no_patient_overlap(train_patient_ids, validation_patient_ids)`

The function accepts common iterable inputs such as lists and sets. It should also work with pandas Series because pandas Series are iterable. It raises a clear `ValueError` if any patient ID appears in both groups.

This is not a full split generator. It is a validation guard only.

## Temporal Ordering Guard Added or Deferred

Added temporal-ordering validation in `src/sepsis_ews/split.py`:

- `assert_patient_time_sorted(frame, patient_col="patient_id", time_col="iculos")`

The guard expects a pandas-like frame passed into the function. It does not import pandas directly and does not read project data. It checks each patient group and raises `ValueError` if time decreases within a patient.

This is intentionally lightweight and does not implement feature generation.

## Tests Added

Added `tests/test_feature_leakage.py`:

- safe feature names pass
- exact blocked names are detected
- derived blocked names raise `ValueError`
- blocked-name detection is case-insensitive

Added `tests/test_split_validation.py`:

- no patient overlap passes
- overlapping patient IDs raise `ValueError`
- empty groups are handled

Added `tests/test_temporal_ordering.py`:

- sorted patient-time rows pass
- decreasing time for one patient raises `ValueError`

The temporal-ordering tests use `pytest.importorskip("pandas")`, so they skip if pandas is unavailable.

Tests do not require:

- raw `.psv` files
- `training/`
- `results/`
- `figures/`
- `notebooks/`
- generated features
- model artifacts

## Test Results

Test commands were attempted exactly as requested:

```text
python -m pytest
py -m pytest
pytest
```

Results:

- `python -m pytest` failed because `python` is not available on PATH.
- `py -m pytest` failed because `py` is not available on PATH.
- `pytest` failed because `pytest` is not available on PATH.

Therefore, tests were added but did not run locally. Do not treat the new test suite as validated until Python and pytest are available and the tests pass.

## Git Status

This folder is still not a Git repository. Running `git status --short` returned:

```text
fatal: not a git repository (or any of the parent directories): .git
```

Git was not initialised because this phase explicitly avoids doing so unless instructed later.

## Public Safety Notes

No raw clinical data or generated artifacts were touched.

The new tests use tiny synthetic values only. They do not read from protected local paths and do not depend on real patient files.

Protected paths remain untouched:

- `training/`
- `data/raw/`
- `data/interim/`
- `data/processed/`
- `features_windowed_6h_12h_24h.csv`
- `results/`
- `figures/`
- `notebooks/`

No model artifacts were created.

## Reproducibility Notes

This phase improves reproducibility safety by making several validation assumptions executable:

- risky feature-name detection
- patient train/validation overlap checks
- per-patient time-order checks

However, the project is not fully reproducible yet. The guardrails are not wired into the existing notebook pipeline, and the tests could not be run in this shell.

## What Was Not Changed

The following were not modified:

- raw clinical data
- `training/`
- `data/raw/`
- `data/interim/`
- `data/processed/`
- `features_windowed_6h_12h_24h.csv`
- `results/`
- `figures/`
- `notebooks/`
- saved metrics
- model artifacts

No training was rerun. No notebook was executed. No metrics were invented or changed.

## Remaining Risks

- Python and pytest are not available on PATH, so tests could not be executed.
- The real notebook feature-generation path has not yet been wired to `validate_feature_names(...)`.
- The real feature manifest and generated feature matrix still need an end-to-end leakage audit.
- No feature allowlist exists yet.
- No independent final holdout test set has been documented.
- The temporal-order guard is lightweight and only validates a supplied pandas-like frame.
- The folder is still not a Git repository.

## Next Recommended Phase

Begin Phase 5: model and evaluation pipeline preparation.

Recommended Phase 5 tasks:

1. Wire guardrails into future feature-building code before any retraining.
2. Add small, explicit pipeline functions for loading safe inputs and validating schema.
3. Keep existing saved metrics unchanged unless the user explicitly requests a controlled rerun.
4. Add metadata/report-generation scaffolding without creating model artifacts yet.
5. Continue using tiny synthetic tests only until raw-data access and environment validation are sorted.
