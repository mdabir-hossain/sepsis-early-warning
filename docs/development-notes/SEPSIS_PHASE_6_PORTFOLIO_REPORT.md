# Sepsis Phase 6 Portfolio Documentation Report

## Executive Summary

Phase 6 made the project more recruiter-friendly and technically reviewable through public-safe documentation only. No training was run, no notebooks were executed, no saved metrics were changed, and no model artifacts were created.

The documentation now presents the project as a retrospective portfolio ML project with patient-grouped validation, calibration, alert-policy analysis, and conservative clinical limitations.

## Files Changed

Added:

- `docs/model_card.md`
- `docs/data_card.md`
- `docs/clinical_limitations.md`
- `reports/final_operating_point.md`
- `SEPSIS_PHASE_6_PORTFOLIO_REPORT.md`

Updated:

- `README.md`

## Documentation Added

`docs/model_card.md` documents intended use, non-intended use, dataset summary, feature overview, model family, validation method, saved-artifact metrics, calibration, threshold/policy decision, limitations, ethical considerations, and clinical disclaimer.

`docs/data_card.md` documents dataset source context, expected local layout, raw-data exclusion, file format, label/case-definition caveats, missingness and temporal-data caveats, privacy constraints, citation/license TODOs, and public-safe usage notes.

`docs/clinical_limitations.md` documents that the project is not a diagnostic tool, is retrospective only, has no deployment claim, has dataset-specific limitations, may create alert fatigue concerns, has calibration/threshold limitations, requires prospective validation, and would need human oversight and governance.

`reports/final_operating_point.md` safely summarizes the saved final operating point from existing artifacts only.

## README Changes

The README was rewritten to include:

- a stronger one-sentence project pitch
- problem framing
- dataset access instructions
- explicit raw-data non-publication guidance
- workflow overview
- validation strategy
- headline saved metrics with caveats
- links to model card, data card, leakage review, reproducibility notes, and clinical limitations
- project structure
- setup commands
- planned command interface with placeholder caveats
- limitations
- clinical disclaimer
- next steps

## Metrics Provenance

All reported metrics were copied from existing saved artifacts and prior phase documentation:

- `results/model_metrics_cv.json`
- `results/calibration_report.json`
- `results/final_decision.json`
- `results/final_operating_point.csv`
- `SEPSIS_PHASE_5_MODEL_EVAL_REPORT.md`
- `SEPSIS_SKILL.md`

Metrics were not independently rerun in Phase 6. They are documented as retrospective development artifact metrics, not clinical validation.

## Public Safety Notes

No raw patient rows were copied into documentation. No raw `.psv` files were read for content or modified. No generated feature tables, prediction dumps, figures, saved results, notebooks, or model artifacts were changed.

The data card leaves citation and license details as TODOs because exact citation/license metadata was not present in the local docs reviewed during this phase.

## Clinical Safety Notes

The new documentation explicitly states that the project is not a diagnostic tool, not clinically validated, and not deployment-ready. It discusses retrospective-only evaluation, alert fatigue, calibration and threshold limitations, prospective validation requirements, and human governance needs.

No clinical benefit, treatment, diagnosis, patient outcome, or deployment claims were added.

## Reproducibility Notes

The README now distinguishes planned commands from implemented functionality. The current scripts are described as placeholders or scaffolding unless their docstrings say otherwise.

The existing source package and tests remain part of the phased conversion from notebooks to a reproducible pipeline, but Phase 6 did not implement new pipeline behavior.

## Test/Check Results

Documentation-safe checks performed:

- `git status --short --branch` was attempted and reported that the folder is not a Git repository.
- Project structure was inspected with `Get-ChildItem`.
- Existing docs and saved JSON/CSV artifacts were read for provenance.

Test commands attempted after documentation edits:

- `python -m pytest`
- `py -m pytest`
- `pytest`

Results:

- `python -m pytest` failed because `python` is not available on PATH.
- `py -m pytest` failed because `py` is not available on PATH.
- `pytest` failed because `pytest` is not available on PATH.

No tests were executed successfully in this shell, so this phase does not claim that tests passed.

## Git Status

`git status --short --branch` returned:

```text
fatal: not a git repository (or any of the parent directories): .git
```

Git was not initialized because the user explicitly instructed not to initialize Git unless instructed later.

## What Was Not Changed

The following were not modified:

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

No models were trained. No notebooks were run. No metrics were fabricated, recreated, changed, or improved.

## Remaining Risks

- The folder is not currently a Git repository.
- Python/pytest availability still needs to be checked after Phase 6 edits.
- No independent final holdout test set has been confirmed.
- The real feature manifest preview still contains high-risk target/workflow-derived missingness names.
- The notebook-generated feature matrix and training workflow still need end-to-end leakage review.
- The command-line training/evaluation workflow is not fully implemented.
- Exact dataset citation and licensing details remain TODOs until verified from the official source.

## Next Recommended Phase

Begin a Phase 7-style reproducibility hardening phase before any demo work:

1. Run the test suite in a working Python environment.
2. Wire leakage guard utilities into the actual feature-building path.
3. Add an explicit feature allowlist.
4. Document a confirmed patient-level holdout strategy or clearly keep all metrics framed as development-only.
5. Complete dataset citation and license documentation before public release.
