# Leakage Review

This is a first-pass leakage checklist for the Sepsis Early-Warning ML project. It documents known risks and unresolved checks before future retraining or public claims.

## Current Status

- Patient-grouped cross-validation is reported in the existing notebook workflow.
- Out-of-fold predictions are saved and used for calibration and alert-policy analysis.
- A full source-code leakage test suite does not exist yet.
- A final untouched holdout test set has not been confirmed in Phase 1.
- Existing metrics should be treated as retrospective development artifact metrics, not clinical validation.

## Known Leakage Risks

High-risk column names or patterns:

```text
SepsisLabel
event_iculos
use_row
future_*
target_*
label_*
sepsis_time
onset_time
```

The existing feature manifest preview includes mechanically generated missingness-style names such as:

```text
SepsisLabel__miss
event_iculos__miss
use_row__miss
```

These may be accidental byproducts of broad feature generation, but they are high-risk because they are derived from target/event workflow fields. They must be reviewed and excluded before any future training pipeline is considered trustworthy.

## Required Checks Before Retraining

- Confirm all rows for one patient stay in the same fold or split.
- Confirm no row-level random split is used for model evaluation.
- Confirm target labels and future-event metadata are excluded from features.
- Confirm rolling-window features use only past and current observations within each patient.
- Confirm calibration is evaluated on patient-separated predictions.
- Confirm threshold/policy selection is not reported as independent test performance unless a separate test split exists.

## Proposed Feature Blocklist

Future feature-building code should reject columns matching:

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

The code should fail loudly if any matching column enters the model matrix.

## Proposed Tests

- `test_patient_group_split_has_no_overlap`
- `test_feature_builder_blocks_target_columns`
- `test_rolling_features_do_not_use_future_rows`
- `test_calibrated_probabilities_are_between_zero_and_one`
- `test_policy_lockout_alert_counts_are_possible`

## Phase 4 Update

Added lightweight guardrails in `src/sepsis_ews/`:

- `features.find_blocked_feature_names(...)`
- `features.validate_feature_names(...)`
- `split.assert_no_patient_overlap(...)`
- `split.assert_patient_time_sorted(...)`

Added synthetic-data tests for:

- safe feature names passing validation
- exact risky names being detected
- derived risky names such as `SepsisLabel__miss` and `future_lactate_mean` being detected
- case-insensitive blocked-name detection
- patient overlap detection
- empty patient groups
- per-patient temporal ordering

These checks do not read raw clinical data and do not audit the existing notebooks end to end.

## Unresolved Items

- Automated leakage and split guard tests now exist for tiny synthetic fixtures only.
- No explicit feature allowlist exists yet.
- The source package now includes guard utilities, but the notebook pipeline has not yet been wired to use them.
- No independent final holdout test set has been documented.
- Notebook 07 references explainability outputs that were not found in `results/` during the audit.
- The real feature manifest and notebook-generated feature matrix still need an end-to-end leakage audit.

## Phase Recommendation

Phase 5 should keep the existing metrics unchanged while preparing a reproducible model/evaluation pipeline. Before any retraining, the real feature-generation path must call the Phase 4 guard utilities and fail loudly on blocked columns.
