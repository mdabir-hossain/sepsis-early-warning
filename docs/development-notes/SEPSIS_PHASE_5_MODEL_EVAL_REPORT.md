# Sepsis Phase 5 Model and Evaluation Report

## Executive Summary

Phase 5 prepared model/evaluation reporting scaffolding without rerunning models, executing notebooks, changing metrics, or creating model artifacts. The project now has small utilities for explicit run metadata, artifact-derived Markdown reporting, and deterministic evaluation validation helpers.

This is a preparation phase only. The new code does not train models, read raw clinical data, infer unknown results, or modify existing `results/` artifacts.

Tests were added using tiny synthetic data and temporary JSON files only. They could not be executed in this shell because `python`, `py`, and `pytest` are not available on PATH.

## Files Changed

Added:

- `src/sepsis_ews/metadata.py`
- `src/sepsis_ews/reporting.py`
- `scripts/generate_report.py`
- `tests/test_metadata.py`
- `tests/test_evaluate_utils.py`
- `tests/test_reporting.py`
- `docs/reproducibility.md`
- `SEPSIS_PHASE_5_MODEL_EVAL_REPORT.md`

Updated:

- `src/sepsis_ews/evaluate.py`
- `tests/test_skeleton_modules.py`
- `README.md`

## Metadata Utilities Added

Added `src/sepsis_ews/metadata.py` with:

- `REQUIRED_METADATA_FIELDS`
- `build_run_metadata(...)`

The metadata helper requires caller-provided values for:

- `project_name`
- `run_name`
- `data_version`
- `feature_schema_version`
- `model_family`
- `calibrator`
- `policy`
- `threshold`
- `lockout_hours`
- `metrics_provenance`

It also records:

- `created_at_utc`
- `notes`

The helper validates required fields and does not read raw data, inspect results, infer metrics, or fabricate a `metrics` object by default.

## Reporting Utilities Added

Added `src/sepsis_ews/reporting.py` with:

- `load_json_artifact(path)`
- `markdown_table(headers, rows)`
- `model_metrics_to_markdown(model_metrics)`
- `calibration_report_to_markdown(calibration_report)`
- `final_decision_to_markdown(final_decision)`
- `build_artifact_metrics_report(...)`
- `write_markdown_report(content, output_path)`

These utilities format existing or caller-provided artifacts only. They fail clearly when:

- a JSON artifact path is missing
- a non-JSON path is supplied
- a loaded JSON file is not an object
- expected artifact sections are absent
- a Markdown table is malformed
- report content is empty

They do not read raw clinical data, do not hardcode local absolute paths, and do not modify existing `results/`.

## Evaluation Utilities Added

Updated `src/sepsis_ews/evaluate.py` with:

- `safe_rate(numerator, denominator)`
- `validate_probability_values(values)`
- `validate_binary_labels(values)`

These helpers are deterministic and do not depend on notebooks, raw data, saved artifacts, or generated features.

Behaviour:

- `safe_rate` raises `ValueError` for zero denominator.
- `validate_probability_values` raises `ValueError` for values outside `[0, 1]`.
- `validate_binary_labels` raises `ValueError` for labels other than `0` or `1`.

Full model metric pipelines were not implemented in this phase.

## Script Changes

Added `scripts/generate_report.py`.

The script accepts:

- `--metrics-dir`
- `--output`

It expects the metrics directory to contain:

- `model_metrics_cv.json`
- `calibration_report.json`
- `final_decision.json`

It generates a Markdown report stating that metrics are copied from existing saved artifacts and were not independently rerun.

The script does not:

- run notebooks
- train models
- read raw data
- create model artifacts
- modify existing result files

It writes only to the caller-provided `--output` path.

## Tests Added

Added `tests/test_metadata.py`:

- required fields are present
- missing required values raise `ValueError`
- metadata does not fabricate metrics by default

Added `tests/test_evaluate_utils.py`:

- `safe_rate(1, 2) == 0.5`
- zero denominator raises `ValueError`
- valid probabilities pass
- probabilities outside `[0, 1]` raise
- binary labels pass
- non-binary labels raise

Added `tests/test_reporting.py`:

- loading a tiny temporary JSON file works
- missing JSON artifact raises `FileNotFoundError`
- Markdown table generation uses only supplied data
- artifact report generation formats supplied temporary dictionaries

Updated `tests/test_skeleton_modules.py` to include imports for:

- `sepsis_ews.metadata`
- `sepsis_ews.reporting`

Tests do not require:

- raw `.psv` files
- `training/`
- `data/raw/`
- existing `results/`
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

Therefore, tests were added but not executed locally. The package should not be described as validated until these tests pass in a Python environment.

## Git Status

This folder is still not a Git repository. Running `git status --short` returned:

```text
fatal: not a git repository (or any of the parent directories): .git
```

Git was not initialised because this phase explicitly avoids doing so unless instructed later.

## Public Safety Notes

No raw data or generated artifacts were touched.

The reporting utilities only read paths supplied by a caller. The tests use temporary files only. The new script writes only to a caller-provided output path and does not modify existing results.

Protected paths remain untouched:

- `training/`
- `data/raw/`
- `data/interim/`
- `data/processed/`
- `features_windowed_6h_12h_24h.csv`
- existing `results/`
- existing `figures/`
- `notebooks/`
- saved metrics
- model artifacts

## Reproducibility Notes

Phase 5 improves reproducibility structure by separating:

- explicit run metadata
- artifact-derived report formatting
- small evaluation input validators

Added `docs/reproducibility.md` to clarify that current README metrics are copied from existing saved artifacts and have not yet been independently rerun by the source package.

This phase does not make the full project reproducible yet. The training/evaluation pipeline still needs controlled implementation, guardrail wiring, and successful test execution.

## What Was Not Changed

The following were not modified:

- raw clinical data
- `training/`
- `data/raw/`
- `data/interim/`
- `data/processed/`
- `features_windowed_6h_12h_24h.csv`
- existing `results/`
- existing `figures/`
- `notebooks/`
- saved metrics
- model artifacts

No model was trained. No notebook was run. No metrics were invented, recreated, or changed.

## Remaining Risks

- Python and pytest are not available on PATH, so tests could not be executed.
- `scripts/generate_report.py` has not been locally run.
- The report-generation script can read existing artifacts when invoked, but it has not been integrated into CI.
- The metadata helper records caller-provided values only; it does not validate against real training runs yet.
- The evaluation helpers are small validators only, not a full metric pipeline.
- Existing notebook outputs and feature manifests still need end-to-end reproducibility and leakage review before any new model claims.
- The folder is still not a Git repository.

## Next Recommended Phase

Begin Phase 6: portfolio documentation.

Recommended Phase 6 tasks:

1. Add concise model card, data card, and clinical limitations docs.
2. Keep metrics artifact-derived unless a controlled rerun is explicitly requested later.
3. Curate README sections around problem framing, validation caveats, and project limitations.
4. Do not train models or alter saved artifacts.
5. Keep public-safety and leakage caveats visible.
