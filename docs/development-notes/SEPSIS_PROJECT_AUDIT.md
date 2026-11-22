# Sepsis Project Audit

## Executive Summary

This project already contains a meaningful sepsis early-warning analysis: a 7-notebook workflow, patient-grouped cross-validation, out-of-fold predictions, calibration, threshold/policy sweeps, alarm-burden analysis, lead-time analysis, and a final operating-point artifact. Those are strong ingredients for a UK Machine Learning Engineer / Data Scientist portfolio project.

The main blocker is professionalism and reproducibility. The current repository is notebook-first, stores raw clinical data and generated artifacts directly in the project tree, has no source-code package, no training/evaluation scripts, no tests, no saved model artifact, no pinned environment, and only a short README. This makes the project harder for recruiters and technical reviewers to trust or rerun.

Priority recommendation: convert the notebook work into a clean, reproducible project with `src/` pipelines, a small public sample dataset or documented data download path, pinned dependencies, a stronger README, a model card, clear metrics tables, leakage checks, tests, and a deployment/demo layer.

Important caveat: this audit does not verify metric correctness by rerunning the notebooks. Metrics below are reported from existing files only and should be treated as saved project artifacts, not independently reproduced results.

## Current Project Structure

Observed root contents:

```text
.
├── .gitignore
├── README.md
├── requirements.txt
├── features_windowed_6h_12h_24h.csv
├── figures/
├── notebooks/
├── results/
└── training/
```

File inventory:

| Category | Observed files |
|---|---:|
| Raw patient `.psv` files | 40,336 |
| Notebook files | 7 |
| Figures | 22 PNGs |
| CSV artifacts | 13 |
| JSON artifacts | 6 |
| Parquet artifacts | 5 |
| Markdown docs | 1 README |
| Requirements files | 1 |
| Python scripts | 0 |
| Saved model files (`.pkl`, `.joblib`, `.onnx`, `.pt`, etc.) | 0 |

Dataset files:

| Path | Notes |
|---|---|
| `training/training_setA/` | 20,336 `.psv` files, about 125.3 MB |
| `training/training_setB/` | 20,000 `.psv` files, about 117.94 MB |
| `features_windowed_6h_12h_24h.csv` | 45.8 MB feature table in repo root |
| `results/features_02b.parquet` | Generated feature matrix, 9.8 MB |
| `results/sample_long_table.parquet` | Intermediate sample table |
| `results/patient_events.parquet` | Patient-level event metadata |
| `results/oof_predictions.parquet` | Out-of-fold predictions |
| `results/oof_with_calibration.parquet` | Calibrated out-of-fold predictions |
| `results/sample_500_processed.csv` | Processed sample CSV, 2.0 MB |

Notebooks:

| Notebook | Purpose inferred from name/content |
|---|---|
| `01_eda_problem_definition.ipynb` | EDA, cohort summary, missingness, label timing, figures |
| `02_feature_engineering_temporal.ipynb` | Temporal feature engineering with 6/12/24-hour windows |
| `03_groupcv_modeling_oof.ipynb` | GroupKFold modelling and out-of-fold predictions |
| `04_calibration_policyA_sweep.ipynb` | Calibration, Policy A threshold sweep, lead time, alarm burden |
| `05_policyB_persistence_sweep.ipynb` | Policy B persistence sweep and comparison |
| `06_final_decision_and_utility.ipynb` | Final operating-point selection and utility framing |
| `07_uncertainty_instability_explainability.ipynb` | Instability and explainability analysis, but expected output files are not currently present |

Training/evaluation scripts:

- No standalone `.py` training scripts were found.
- No standalone evaluation scripts were found.
- The executable workflow appears to live inside notebooks.

Saved models:

- No saved model artifacts were found.
- There is no `models/` directory.
- Existing results identify `hgb` with isotonic calibration as the selected approach, but the fitted model/calibrator object is not persisted.

Requirements/environment files:

- `requirements.txt` exists, but it is minimal and unpinned:

```text
pandas
numpy
scikit-learn
matplotlib
pyarrow
jupyter
```

README/docs:

- `README.md` exists but is very short.
- No `docs/`, model card, data card, experiment notes, reproducibility guide, or deployment guide were found.
- README has a visible encoding issue: the project structure bullets render `â€”` instead of an em dash.

Outputs/figures/reports:

- `figures/` contains useful plots for missingness, distributions, ROC/PR baselines, calibration reliability, policy trade-offs, and lead-time histograms.
- `results/` contains metrics, feature manifests, threshold sweeps, and final operating-point files.
- Existing saved model comparison in `results/model_metrics_cv.json`:

| Model | AUROC mean | AUROC std | AUPRC mean | AUPRC std |
|---|---:|---:|---:|---:|
| Logistic Regression | 0.8767 | 0.0827 | 0.1400 | 0.0900 |
| HistGradientBoosting | 0.9405 | 0.0276 | 0.1786 | 0.0847 |

- Existing calibration report in `results/calibration_report.json`:

| Calibration | Brier | ECE@10 |
|---|---:|---:|
| Uncalibrated | 0.0196 | 0.0202 |
| Platt | 0.0134 | 0.0050 |
| Isotonic | 0.0133 | 0.0008 |

- Existing final decision in `results/final_decision.json`:

| Field | Value |
|---|---|
| Model | `hgb` |
| Calibrator | `isotonic` |
| Policy | `A_first_crossing_lockout` |
| Threshold | `0.0854430379746835` |
| Lockout | 6 hours |
| Sepsis detection rate | 0.8974 |
| Non-sepsis alert rate | 0.0 |
| Alerts per 100 patient hours | 0.8671 |
| Median lead time | 40.0 hours |

Note: the older `results/baseline_metrics.csv` reports much weaker baseline scores than `model_metrics_cv.json`. The README should explain which result set is current and why older baseline files remain.

## What Works Well

- The project addresses a realistic, high-impact clinical ML problem with temporal data, class imbalance, missingness, and operational alert fatigue.
- The notebook sequence tells a coherent analysis story: EDA, temporal features, grouped validation, calibration, policy selection, and explainability.
- Patient-grouped validation is explicitly used in the modelling notebook via `GroupKFold`, which is the right direction for avoiding patient-level leakage.
- Out-of-fold predictions are saved and used for calibration/policy work, which is stronger than evaluating on in-sample predictions.
- The project already contains recruiter-friendly concepts: AUROC/AUPRC, calibration, Brier score, expected calibration error, lead time, alert burden, threshold sweeps, and final operating-point selection.
- Results artifacts and figures are already available, so a polished README can show concrete tables and plots without inventing results.
- The work shows awareness of deployment-facing trade-offs, especially false alerts and alert lockout policies.

## Critical Issues

1. No Git repository detected in the current folder.

   `git status --short` failed with `fatal: not a git repository`. For a GitHub portfolio project, this folder must be initialised or copied into a real Git repo before publishing.

2. Raw clinical data is inside the project tree.

   `training/` contains 40,336 patient `.psv` files. The existing `.gitignore` ignores `training/`, which is good, but if the project is not currently a Git repo there is no guarantee these files are not accidentally published later. The README also needs explicit data-access instructions rather than shipping full raw data.

3. The project is not reproducible from scripts.

   There are no `src/` modules, no `train.py`, no `evaluate.py`, no pipeline entry point, and no tests. A reviewer cannot easily run `make train`, `python -m sepsis_ews.train`, or `pytest`.

4. No saved model artifact exists.

   The project selects `hgb` plus isotonic calibration, but no fitted pipeline/calibrator file is saved. This prevents inference demos, deployment, model-card validation, and reliable handoff.

5. Environment is under-specified.

   `requirements.txt` has only six unpinned packages. It omits versions, Python version, development tools, testing tools, notebook execution tooling, and likely explainability dependencies if Notebook 07 is completed.

6. README is far too thin for a portfolio project.

   It currently gives a brief description and project highlights, but lacks installation steps, data setup, commands, reproducibility notes, metrics tables, figures, limitations, leakage controls, project structure, and clinical disclaimer.

7. Missing expected explainability/instability output files.

   Notebook 07 says it saves outputs such as `explainability_global_perm_importance.csv` and `explainability_local_alert_examples.csv`, but those files are not present in `results/`. Either Notebook 07 was not run to completion or its outputs were not saved/kept.

8. Potential leakage risk needs explicit review.

   `results/feature_manifest.json` includes fields such as `SepsisLabel__miss`, `event_iculos__miss`, and `use_row__miss` in the feature preview. They may be harmless missingness indicators created mechanically, but labels/event metadata should not enter the feature matrix. This needs an explicit leakage audit and an allowlist/blocklist of feature columns.

9. Metrics need provenance and a final holdout story.

   The current metrics are cross-validation/OOF artifacts. That is useful, but the project should clearly state whether there is a final untouched test set. If there is no holdout, say so and explain the limitation.

## Important Improvements

- Convert core notebook logic into source modules under `src/sepsis_ews/`.
- Add CLI scripts or module entry points for data building, feature generation, training, calibration, policy sweep, evaluation, and inference.
- Add a locked environment using `requirements-lock.txt`, `uv.lock`, `poetry.lock`, or `conda-lock`.
- Add `pyproject.toml` with package metadata, formatting, linting, and test configuration.
- Add `tests/` with fast unit tests for:
  - patient-level group splitting
  - feature leakage blocklist
  - temporal rolling-window behaviour
  - calibration transform shape/range
  - policy alert lockout logic
  - metric calculation on a tiny fixture
- Save a final model bundle, for example `models/sepsis_hgb_isotonic.joblib`, but keep it out of Git unless it is small and intended for release.
- Add `data/README.md` explaining how to obtain the dataset and where to place raw files.
- Move raw/generated data out of the repo root into `data/raw/`, `data/interim/`, and `data/processed/`.
- Create a clear experiment registry file, such as `reports/metrics/model_comparison.csv`, identifying the current selected run.
- Rerun or complete Notebook 07, or remove claims about missing explainability outputs.
- Add model interpretability outputs that are suitable for clinical discussion: global permutation importance, local alert examples, limitations, and what should not be inferred.
- Add a deployment demo only after the model bundle is reproducible: Streamlit/FastAPI inference demo using sample rows, with clinical disclaimer.
- Add CI with `pytest`, linting, and optionally notebook smoke tests on a tiny sample.

## Portfolio Readiness

Current readiness: promising analysis project, not yet polished portfolio project.

Estimated portfolio score today: 5.5/10.

What a recruiter will like:

- The problem is serious and relevant.
- The project uses temporal patient data instead of a toy tabular dataset.
- There is attention to calibration and operational alert burden, which is mature.
- Figures and results already exist.
- The notebook titles communicate a full ML workflow.

What a technical hiring manager may question:

- Can this be rerun from scratch?
- Are the reported metrics from a clean validation strategy?
- Are labels or future event fields leaking into features?
- Where is the trained model?
- Where is the code quality: package structure, tests, type hints, CI?
- Why are raw data and generated features mixed into the root folder?
- Which metrics are final when baseline CSV and CV JSON differ substantially?
- Is the project safe to publish with clinical data files present?

Target readiness after improvements: 8.5/10.

To reach that level, the project should present itself as:

> A reproducible sepsis early-warning ML system trained on patient time-series data, evaluated with patient-grouped validation, calibrated for reliable risk estimates, and tuned for alarm-fatigue-aware deployment trade-offs.

## Recommended Folder Structure

```text
sepsis-early-warning/
├── README.md
├── LICENSE
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
├── .gitignore
├── .github/
│   └── workflows/
│       └── ci.yml
├── configs/
│   ├── default.yaml
│   └── model_hgb.yaml
├── data/
│   ├── README.md
│   ├── raw/                 # ignored; PhysioNet .psv files
│   ├── interim/             # ignored; parsed/long tables
│   ├── processed/           # ignored or small sample only
│   └── sample/              # public tiny synthetic/sample fixture
├── docs/
│   ├── data_card.md
│   ├── model_card.md
│   ├── leakage_review.md
│   └── clinical_limitations.md
├── notebooks/
│   ├── 01_eda_problem_definition.ipynb
│   ├── 02_feature_engineering_temporal.ipynb
│   ├── 03_groupcv_modeling_oof.ipynb
│   ├── 04_calibration_policyA_sweep.ipynb
│   ├── 05_policyB_persistence_sweep.ipynb
│   ├── 06_final_decision_and_utility.ipynb
│   └── 07_uncertainty_instability_explainability.ipynb
├── src/
│   └── sepsis_ews/
│       ├── __init__.py
│       ├── data.py
│       ├── features.py
│       ├── split.py
│       ├── train.py
│       ├── calibrate.py
│       ├── policies.py
│       ├── evaluate.py
│       ├── explain.py
│       └── inference.py
├── scripts/
│   ├── build_dataset.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   └── run_policy_sweep.py
├── models/                  # ignored, except optional small metadata
├── reports/
│   ├── figures/
│   ├── metrics/
│   └── final_operating_point.md
└── tests/
    ├── test_features.py
    ├── test_split.py
    ├── test_policies.py
    └── test_metrics.py
```

## Recommended .gitignore

Suggested public files:

- `README.md`
- `requirements.txt`, lockfile, `pyproject.toml`
- `src/`, `scripts/`, `tests/`, `configs/`
- cleaned notebooks, ideally with heavy embedded outputs stripped or controlled
- selected lightweight figures in `reports/figures/`
- selected metrics in `reports/metrics/`
- `docs/` model/data cards
- tiny sample or synthetic fixture data only

Suggested ignored files:

```gitignore
# Raw and generated data
data/raw/
data/interim/
data/processed/
training/
features_windowed_6h_12h_24h.csv
*.parquet

# Model artifacts
models/
*.pkl
*.pickle
*.joblib
*.onnx
*.pt
*.pth
*.h5
*.sav

# Notebook/runtime cache
.ipynb_checkpoints/
__pycache__/
*.py[cod]
.pytest_cache/
.mypy_cache/
.ruff_cache/

# Environment
.venv/
venv/
env/
.env
.env.*

# OS/editor
.DS_Store
Thumbs.db
.vscode/
.idea/

# Large generated outputs, keep curated copies under reports/
results/
figures/
```

Suggested removed or relocated before public GitHub release:

- Move `training/` out of the tracked project or keep ignored with a `data/README.md`.
- Move `features_windowed_6h_12h_24h.csv` out of root; it is generated and too large for a clean portfolio root.
- Move `results/` to `reports/metrics/` only for curated, final artifacts; ignore bulky intermediate predictions.
- Move `figures/` to `reports/figures/` and keep only the strongest plots.
- Remove stale or contradictory metrics unless clearly labelled as old baseline experiments.

Do not delete raw data locally until the replacement structure and `.gitignore` have been verified. The immediate public-safety step is to ensure raw data and generated intermediates are untracked.

## Phase-by-Phase Improvement Plan

### Phase 1: Repository Hygiene and Public Safety

- Initialise or move this work into a real Git repository.
- Expand `.gitignore` before adding files.
- Create `data/README.md` with dataset source, access instructions, expected folder layout, and licensing/citation notes.
- Relocate raw data and generated feature files into ignored `data/` locations.
- Decide which result artifacts are current and archive or label older baselines.
- Fix README encoding issue.

Deliverable: a safe GitHub-ready repository skeleton with no raw clinical data tracked.

### Phase 2: Reproducible Environment

- Pin Python version.
- Replace loose requirements with pinned runtime and dev requirements.
- Add `pyproject.toml`.
- Add commands such as:

```bash
pip install -r requirements.txt
python scripts/build_dataset.py --config configs/default.yaml
python scripts/train_model.py --config configs/model_hgb.yaml
python scripts/evaluate_model.py --config configs/model_hgb.yaml
```

- Add CI that runs linting and tests on a small fixture.

Deliverable: a reviewer can install the project and run basic checks without opening notebooks.

### Phase 3: Convert Notebook Logic to Source Code

- Extract data loading into `src/sepsis_ews/data.py`.
- Extract temporal features into `features.py`.
- Extract patient-grouped split logic into `split.py`.
- Extract model definitions/training into `train.py`.
- Extract calibration into `calibrate.py`.
- Extract alert policies into `policies.py`.
- Extract metrics and operating-point selection into `evaluate.py`.
- Keep notebooks as narrative reports that call the package code.

Deliverable: notebooks become readable demonstrations, not the only executable implementation.

### Phase 4: Leakage and Validation Hardening

- Add a documented feature allowlist and leakage blocklist.
- Explicitly exclude label/event/future fields from model features.
- Add tests that fail if columns like `SepsisLabel`, `event_iculos`, future labels, or target-derived fields enter `X`.
- Decide whether validation should be:
  - GroupKFold only, clearly labelled as cross-validation, or
  - train/validation/test patient split plus nested CV/tuning.
- Ensure calibration and threshold selection are not evaluated on the same patients used to choose them unless clearly framed as OOF development performance.

Deliverable: a `docs/leakage_review.md` file and passing leakage tests.

### Phase 5: Model Artifacts and Evaluation Reports

- Save the final fitted preprocessing/model/calibrator bundle.
- Save metadata with:
  - training data version
  - feature schema
  - model parameters
  - package versions
  - threshold/policy settings
  - metric provenance
- Create final metrics tables in `reports/metrics/`.
- Create a concise model comparison section: Logistic Regression baseline vs HGB vs calibrated HGB/policy.
- Complete or rerun explainability artifacts, or remove claims until outputs exist.

Deliverable: a reproducible model bundle and trustworthy final report artifacts.

### Phase 6: Recruiter-Friendly Documentation

- Rewrite README with:
  - one-sentence project pitch
  - problem framing
  - dataset source and citation
  - method summary
  - validation strategy
  - headline metrics
  - selected figures
  - how to reproduce
  - repository structure
  - limitations and clinical disclaimer
  - next steps
- Add `docs/model_card.md` and `docs/data_card.md`.
- Add screenshots/figures directly to README.

Deliverable: a polished GitHub page understandable in 60 seconds and credible in 10 minutes.

### Phase 7: Optional Deployment/Demo

- Add a Streamlit or FastAPI demo using sample/synthetic rows.
- The demo should show:
  - risk score over time
  - calibrated probability
  - alert decision under selected policy
  - top contributing features or local explanation
  - clinical safety disclaimer
- Add Dockerfile only if it runs cleanly and does not bloat the project.

Deliverable: an interview-ready demo that supports the project story without pretending to be clinical software.

## Next Codex Prompt

```text
You are acting as a senior ML engineer and GitHub portfolio maintainer.

Use the audit in SEPSIS_PROJECT_AUDIT.md to begin Phase 1 only.

Rules:
- Do not delete raw data.
- Do not commit or push.
- Do not change model results.
- Keep raw clinical data untracked/ignored.
- Make small, reviewable edits.

Tasks:
1. Create a professional target folder skeleton: data/, docs/, reports/, src/sepsis_ews/, scripts/, tests/, configs/.
2. Expand .gitignore for raw data, generated features, model artifacts, caches, and environments.
3. Move only public-safe documentation/report copies if needed; do not move or delete raw data yet unless explicitly confirmed.
4. Draft data/README.md explaining where the PhysioNet sepsis files should live and that raw data is not committed.
5. Rewrite README.md into a recruiter-friendly portfolio README using only metrics already present in results/.
6. Add docs/leakage_review.md as a first-pass checklist, clearly flagging unresolved leakage checks.
7. Show a concise summary of changed files and any unresolved risks.
```
