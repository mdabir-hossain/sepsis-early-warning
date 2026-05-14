# Model Card

## Intended Use

This project is intended as a portfolio and research-style machine learning demonstration for retrospective sepsis early-warning modelling with patient time-series data. It is designed to show responsible ML engineering practices around temporal features, patient-grouped validation, calibration, alert-policy simulation, and conservative healthcare communication.

Appropriate uses include:

- reviewing the project as a machine learning engineering portfolio artifact
- studying a retrospective early-warning modelling workflow
- discussing validation, leakage, calibration, and alert-burden trade-offs
- extending the codebase into a more reproducible research pipeline

## Non-Intended Use

This project must not be used for clinical decision-making, diagnosis, triage, treatment, patient monitoring, or hospital deployment. It is not a medical device, not clinically validated, and not deployment-ready.

The reported metrics must not be used to claim real-world clinical benefit, patient safety impact, or operational readiness.

## Dataset Summary

The project uses local PhysioNet-style sepsis patient time-series files in pipe-separated `.psv` format. Raw patient data is not committed and should remain local.

Saved development artifacts report:

- 493 patients in the model comparison artifact after feature-building filters
- 19,145 rows in the model comparison artifact
- row-level target prevalence of approximately 0.0112 in the model comparison artifact
- 5 validation folds

These counts are copied from `results/model_metrics_cv.json` and were not independently recomputed in this documentation phase.

See [data card](data_card.md) and [data setup](../data/README.md) for public-safe data notes.

## Feature Overview

The saved feature manifest reports rolling-window temporal features over 6, 12, and 24 hour windows, with forward fill within patient, first-hour dropping, patient identifiers, time index columns, and 672 generated features.

The feature manifest preview includes vital signs, labs, demographics, missingness indicators, and rolling summaries. It also shows high-risk missingness-derived names from target or workflow fields, including `SepsisLabel__miss`, `event_iculos__miss`, and `use_row__miss`.

Because of that unresolved risk, the feature set should not be treated as fully leakage-audited. Future retraining should enforce an explicit feature allowlist/blocklist before model fitting. See [leakage review](leakage_review.md).

## Model Family

Saved artifacts compare:

- Logistic Regression
- HistGradientBoosting (`hgb`)

The saved final operating point uses the HistGradientBoosting model with isotonic calibration.

## Validation Method

Saved artifacts report 5-fold patient-grouped cross-validation with out-of-fold predictions used for calibration and policy analysis. Patient grouping is required because row-level random splitting could leak information from the same patient across train and validation folds.

No independent final holdout test set has been confirmed in the current documentation. Metrics should be interpreted as retrospective development artifact metrics, not independent validation.

## Metrics From Saved Artifacts Only

The values below are copied from existing saved artifacts and prior phase documentation. They were not independently rerun during Phase 6.

### Model Comparison

Source: `results/model_metrics_cv.json`

| Model | AUROC mean | AUROC std | AUPRC mean | AUPRC std |
|---|---:|---:|---:|---:|
| Logistic Regression | 0.8767 | 0.0827 | 0.1400 | 0.0900 |
| HistGradientBoosting | 0.9405 | 0.0276 | 0.1786 | 0.0847 |

### Calibration

Source: `results/calibration_report.json`

| Calibration | Brier | ECE@10 |
|---|---:|---:|
| Uncalibrated | 0.0196 | 0.0202 |
| Platt | 0.0134 | 0.0050 |
| Isotonic | 0.0133 | 0.0008 |

These values are retrospective development results from saved artifacts, not clinical validation.

## Calibration Summary

The saved calibration artifact reports HistGradientBoosting calibration results for uncalibrated probabilities, Platt scaling, and isotonic calibration. Isotonic calibration has the lowest saved Brier score and ECE@10 in the artifact and is marked as the chosen calibrator.

Calibration quality has not been independently rerun in this documentation phase and has not been prospectively validated.

## Threshold And Policy Decision

The saved final operating-point artifact reports:

| Field | Saved value |
|---|---:|
| Model | `hgb` |
| Calibrator | `isotonic` |
| Policy | `A_first_crossing_lockout` |
| Threshold | 0.0854430379746835 |
| Lockout | 6 hours |
| Sepsis detection rate | 0.8974 |
| Non-sepsis alert rate | 0.0000 |
| Alerts per 100 patient hours | 0.8671 |
| Median lead time | 40.0 hours |

Source: `results/final_decision.json` and `results/final_operating_point.csv`.

This is a retrospective policy simulation copied from saved artifacts. It is not a clinical operating threshold and should not be used in care delivery.

## Limitations

- Metrics were copied from saved artifacts and were not rerun in Phase 6.
- No independent final holdout test set has been confirmed.
- The feature manifest preview contains unresolved high-risk leakage indicators.
- The source package and CLI are not yet a complete retraining pipeline.
- Calibration and threshold selection may be dataset-specific.
- Alert burden and lead-time estimates may not transfer to other hospitals, populations, workflows, or documentation practices.
- Missingness patterns may encode site-specific measurement behavior.
- The project does not include prospective validation, workflow validation, fairness analysis, clinical safety testing, or regulatory review.

## Ethical And Clinical Considerations

Sepsis alerting is clinically high-stakes. False negatives may delay recognition, while false positives may contribute to alert fatigue, unnecessary review, or workflow disruption. A retrospective model can also encode dataset, measurement, and care-process biases.

Any real-world use would require multidisciplinary governance, human oversight, privacy review, prospective validation, monitoring for drift and calibration decay, and careful evaluation of alert burden and downstream effects.

## Clinical Disclaimer

This model card documents a portfolio ML project only. The project is not a diagnostic tool, not clinically validated, and not deployment-ready. It must not be used to diagnose, treat, prevent, or manage sepsis.

Related documents:

- [Leakage review](leakage_review.md)
- [Reproducibility notes](reproducibility.md)
- [Clinical limitations](clinical_limitations.md)
