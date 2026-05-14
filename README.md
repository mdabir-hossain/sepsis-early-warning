# Sepsis Early-Warning ML

A reproducible sepsis early-warning ML portfolio project using patient time-series data, patient-grouped validation, calibrated risk estimates, and alert-policy analysis to study detection, lead time, and alarm burden.

This repository is a research-style and portfolio-grade machine learning project. It is not a clinical product, diagnostic system, medical device, or deployment-ready hospital tool.

## Problem Framing

Sepsis early-warning models are challenging because patient observations are temporal, sparse, and clinically high-stakes. This project studies a retrospective early-warning workflow that estimates sepsis risk from patient time-series data, then evaluates how model thresholds and alert policies affect detection, lead time, and alarm burden.

The main engineering story is:

1. Load patient time-series data from local `.psv` files.
2. Explore cohort size, missingness, label timing, and length of stay.
3. Engineer rolling-window temporal features.
4. Evaluate baseline and stronger models with patient-grouped validation.
5. Use out-of-fold predictions for calibration and policy analysis.
6. Compare calibration methods.
7. Simulate alert policies and threshold trade-offs.
8. Communicate limitations conservatively and publicly safely.

## Dataset Access

Raw patient files are not committed to this repository. The project expects a PhysioNet-style sepsis dataset in pipe-separated `.psv` format, placed locally under:

```text
data/raw/
|-- training_setA/
|   |-- p000001.psv
|   `-- ...
`-- training_setB/
    |-- p100001.psv
    `-- ...
```

This working folder may also contain a legacy local `training/` directory. That folder is treated as raw clinical data, is ignored by `.gitignore`, and must not be published.

See [data/README.md](data/README.md) and [docs/data_card.md](docs/data_card.md) for data layout, privacy, citation, and public-safety notes. Exact dataset citation and licensing details should be completed before public release if they are not already present locally.

## Workflow Overview

The existing analysis is notebook-first and is being converted phase by phase into a reusable package and command-line workflow.

```text
Raw patient files
  -> exploratory analysis and cohort summaries
  -> temporal feature engineering
  -> patient-grouped cross-validation
  -> out-of-fold predictions
  -> calibration comparison
  -> threshold and policy sweeps
  -> final operating-point summary
  -> public-safe documentation
```

## Validation Strategy

The saved modelling artifacts report 5-fold patient-grouped cross-validation over 493 patients and 19,145 rows after feature-building filters. Patient grouping is essential because random row-level splitting could leak information across observations from the same patient.

The saved artifacts also report out-of-fold predictions used for calibration and alert-policy analysis. No independent final holdout test set has been confirmed in the current documentation. These results should therefore be read as retrospective development artifact metrics, not independent validation and not clinical validation.

Known unresolved leakage risks are documented in [docs/leakage_review.md](docs/leakage_review.md). In particular, the saved feature manifest preview includes missingness-derived names from target/workflow fields, such as `SepsisLabel__miss`, `event_iculos__miss`, and `use_row__miss`. These must be reviewed and excluded before any future retraining or stronger performance claims.

## Headline Saved Metrics

The following values are copied from existing saved artifacts in `results/` and from prior phase reports. They were not independently rerun during this documentation phase.

These metrics are retrospective development artifact metrics and should not be interpreted as clinical validation, deployment readiness, or evidence of patient benefit.

### Model Comparison

Source: `results/model_metrics_cv.json`

| Model | AUROC mean | AUROC std | AUPRC mean | AUPRC std |
| --- | ---: | ---: | ---: | ---: |
| Logistic Regression | 0.8767 | 0.0827 | 0.1400 | 0.0900 |
| HistGradientBoosting | 0.9405 | 0.0276 | 0.1786 | 0.0847 |

### Calibration

Source: `results/calibration_report.json`

| Calibration | Brier | ECE@10 |
| --- | ---: | ---: |
| Uncalibrated | 0.0196 | 0.0202 |
| Platt | 0.0134 | 0.0050 |
| Isotonic | 0.0133 | 0.0008 |

The saved artifact marks isotonic calibration as the selected calibrator for the final operating-point analysis.

### Final Operating Point

Source: `results/final_decision.json` and `results/final_operating_point.csv`

| Field | Saved value |
| --- | ---: |
| Model | `hgb` |
| Calibrator | `isotonic` |
| Policy | `A_first_crossing_lockout` |
| Threshold | 0.0854430379746835 |
| Lockout | 6 hours |
| Sepsis detection rate | 0.8974 |
| Non-sepsis alert rate | 0.0000 |
| Alerts per 100 patient hours | 0.8671 |
| Median lead time | 40.0 hours |

See [reports/final_operating_point.md](reports/final_operating_point.md) for the public-safe operating-point note.

## Documentation

- [Model card](docs/model_card.md)
- [Data card](docs/data_card.md)
- [Clinical limitations](docs/clinical_limitations.md)
- [Leakage review](docs/leakage_review.md)
- [Reproducibility notes](docs/reproducibility.md)
- [Data setup](data/README.md)

## Project Structure

```text
.
|-- configs/                 # Future experiment configuration
|-- data/                    # Data layout docs; raw data stays local and ignored
|-- docs/                    # Model/data cards, leakage review, reproducibility notes
|-- figures/                 # Existing generated figures; not modified in Phase 6
|-- notebooks/               # Existing notebook analysis; not modified in Phase 6
|-- reports/                 # Public-safe reports and future curated metrics/figures
|-- results/                 # Existing saved artifacts; read-only for Phase 6
|-- scripts/                 # Planned command-line entry points
|-- src/sepsis_ews/          # Source package skeleton and utility scaffolding
|-- tests/                   # Synthetic/unit tests for guardrails and utilities
|-- training/                # Local raw data; ignored and not for publication
|-- README.md
|-- pyproject.toml
|-- requirements.txt
`-- requirements-dev.txt
```

Protected local artifacts include `training/`, `data/raw/`, `data/interim/`, `data/processed/`, `features_windowed_6h_12h_24h.csv`, existing `results/`, existing `figures/`, notebooks, saved metrics, and model artifacts.

## Setup

The project metadata currently specifies Python `>=3.10,<3.13`.

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

For development checks:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest
ruff check .
```

If `python` is not available on PATH, use the appropriate local Python launcher for your system.

## Planned Command Interface

The scripts are currently placeholders or scaffolding unless their module docstrings say otherwise. They should not be presented as a complete production training pipeline yet.

Planned commands:

```bash
python scripts/build_dataset.py --config configs/default.yaml
python scripts/train_model.py --config configs/model_hgb.yaml
python scripts/evaluate_model.py --config configs/model_hgb.yaml
python scripts/run_policy_sweep.py --config configs/model_hgb.yaml
python scripts/generate_report.py --metrics-dir results --output reports/artifact_metrics.md
```

The reporting script formats existing saved artifacts only. It does not train models, run notebooks, or create new metrics.

## Limitations

- Current metrics come from saved project artifacts and were not rerun in Phase 6.
- The current pipeline is still partly notebook-first.
- The source package and CLI are not a complete retraining workflow yet.
- No independent final holdout test set has been confirmed.
- The real notebook-generated feature matrix still needs an end-to-end leakage audit.
- Calibration and threshold choices are retrospective development analyses, not prospective clinical evidence.
- Alert burden, lead time, and detection trade-offs would need site-specific evaluation before any real-world consideration.
- Dataset source, license, and citation details should be finalized before public release if not already present locally.

## Clinical Disclaimer

This project is not a diagnostic tool and is not intended to diagnose, treat, prevent, or manage sepsis. It is not clinically validated and is not deployment-ready. Any real-world healthcare use would require prospective validation, clinical safety review, privacy and governance review, human oversight, workflow evaluation, and regulatory assessment.

## Next Steps

- Wire the source package to a controlled feature-building and evaluation pipeline.
- Add an explicit feature allowlist and enforce leakage guards in the real pipeline.
- Confirm or create a documented patient-level holdout strategy before making stronger claims.
- Run the test suite in a working Python environment and report exact results.
- Complete dataset citation/license metadata before public release.
