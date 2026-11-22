# SKILL.md — Sepsis Early-Warning ML Portfolio Project

## What this skill is for

Use this file every time you are asked to review, audit, improve, restructure, document, or prepare the Sepsis Early-Warning project for GitHub, job applications, interviews, or deployment demos.

This is the project source of truth. It defines how to think about the project, what must be protected, what should be improved, and how changes should be made safely.

---

## What this project is

This project is a **machine learning portfolio project for early sepsis warning using patient time-series data**.

The project is not meant to be a clinical product, medical device, or diagnostic tool. It is a portfolio-grade ML engineering and data science project that demonstrates how to work responsibly with temporal healthcare data, patient-level validation, calibration, operational alert policies, and clinical-risk communication.

**Core project story:**

1. Load patient time-series data.
2. Explore missingness, label timing, and cohort behaviour.
3. Engineer temporal features using rolling windows.
4. Train baseline and stronger models using patient-grouped validation.
5. Generate out-of-fold predictions.
6. Calibrate risk estimates.
7. Sweep alert policies and thresholds.
8. Select an operating point that balances detection, alert burden, and lead time.
9. Communicate limitations clearly and responsibly.

**Target audience:**

- UK Machine Learning Engineer recruiters.
- Data Scientist hiring managers.
- Technical reviewers.
- Interviewers who want evidence of reproducible ML work.
- People evaluating whether the project shows production-minded thinking.

**Immediate goal:**

Turn the existing notebook-first project into a clean, reproducible, recruiter-friendly GitHub portfolio project.

Every decision must be evaluated against:

- Can a reviewer understand the project in 60 seconds?
- Can a technical reviewer trust the validation and metrics?
- Can the project be rerun or at least smoke-tested?
- Are raw clinical data and sensitive/generated artifacts kept out of Git?
- Does the project communicate healthcare limitations responsibly?

---

## Current project state

The project already contains strong ML analysis ingredients:

- 7-notebook workflow.
- Patient-grouped cross-validation.
- Out-of-fold predictions.
- Calibration analysis.
- Threshold and policy sweeps.
- Alarm-burden analysis.
- Lead-time analysis.
- Final operating-point artifact.
- Figures and results artifacts.

The current main weakness is professionalism and reproducibility:

- Notebook-first workflow.
- No source-code package yet.
- No training/evaluation scripts yet.
- No tests yet.
- No saved model bundle yet.
- Raw clinical data and generated features are currently present in the working tree.
- README is too thin for a serious portfolio project.
- Requirements are minimal and unpinned.
- Leakage checks need to be made explicit.

---

## Non-negotiable safety rules

### 1. Do not publish raw clinical data

Never commit or push:

```text
training/
data/raw/
data/interim/
data/processed/
*.psv
features_windowed_6h_12h_24h.csv
large generated feature tables
raw prediction dumps
```

Raw data should be obtained by the user from the original dataset source and placed locally according to `data/README.md`.

### 2. Do not invent results

Never fabricate metrics, plots, model performance, calibration values, or clinical claims.

If a metric is already present in saved artifacts, it may be reported with provenance. If it has not been rerun, say it is taken from existing artifacts rather than independently reproduced.

### 3. Do not overclaim clinical value

This project must not claim to diagnose, treat, prevent, or replace clinicians.

Use language such as:

- early-warning modelling
- risk estimation
- retrospective analysis
- alert-policy simulation
- portfolio demonstration
- research-style prototype

Avoid language such as:

- clinically validated
- production-ready for hospitals
- saves lives
- detects sepsis perfectly
- medical-grade
- deployable diagnostic system

### 4. Patient-level leakage protection comes first

All modelling changes must protect against leakage across patients and through future/target-derived variables.

Never allow obvious target or future-event fields into model features.

Examples of high-risk columns or patterns:

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

If any of these appear in feature manifests, add a leakage review before training.

### 5. Keep changes phase-by-phase

Never do a full rewrite in one step.

Prefer small, reviewable phases:

1. Repository hygiene.
2. Environment setup.
3. Source package skeleton.
4. Feature and split extraction.
5. Training/evaluation scripts.
6. Leakage tests.
7. Model card and README polish.
8. Optional deployment demo.

---

## Recommended project identity

Preferred public repo name:

```text
sepsis-early-warning
```

Alternative names:

```text
sepsis-risk-ml
sepsis-ews-ml
patient-time-series-sepsis
```

Recommended tagline:

```text
Patient-grouped, calibrated sepsis early-warning modelling with alert-burden-aware threshold analysis.
```

Recommended one-sentence portfolio pitch:

```text
A reproducible sepsis early-warning ML project using patient time-series data, grouped validation, calibrated risk estimates, and alert-policy analysis to study detection, lead time, and alarm burden.
```

---

## Target folder structure

Use this as the target structure for the cleaned project:

```text
sepsis-early-warning/
├── README.md
├── LICENSE
├── .gitignore
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
├── configs/
│   ├── default.yaml
│   └── model_hgb.yaml
├── data/
│   ├── README.md
│   ├── raw/                 # ignored; original .psv files
│   ├── interim/             # ignored; parsed intermediate files
│   ├── processed/           # ignored; generated feature tables
│   └── sample/              # tiny synthetic or public-safe fixture only
├── docs/
│   ├── data_card.md
│   ├── model_card.md
│   ├── leakage_review.md
│   ├── clinical_limitations.md
│   └── reproducibility.md
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
├── models/                  # ignored unless metadata-only
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

---

## Files and folders that should usually be public

Safe to commit after review:

```text
README.md
LICENSE
.gitignore
pyproject.toml
requirements.txt
requirements-dev.txt
configs/
src/
scripts/
tests/
docs/
notebooks/                  # if cleaned and not too large
reports/figures/            # curated figures only
reports/metrics/            # curated final metrics only
data/README.md
data/sample/                # tiny synthetic/sample fixture only
```

Curated result files are allowed only if they are small, non-sensitive, and clearly documented.

---

## Files and folders that must be ignored

Use this as the baseline `.gitignore` direction:

```gitignore
# Raw and generated data
training/
data/raw/
data/interim/
data/processed/
features_windowed_6h_12h_24h.csv
*.psv
*.parquet

# Large/intermediate results
results/
figures/
*.csv
!reports/metrics/*.csv
!data/sample/*.csv

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

# Environments and secrets
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
```

Important: `.gitignore` does not remove files that are already tracked. If raw data or generated artifacts were already tracked, use safe untracking commands and verify before pushing.

---

## Existing metrics that may be referenced carefully

Existing saved artifacts report the following values. These should be described as values from existing project artifacts unless independently rerun.

Model comparison artifact:

```text
Logistic Regression:
- AUROC mean: 0.8767
- AUROC std: 0.0827
- AUPRC mean: 0.1400
- AUPRC std: 0.0900

HistGradientBoosting:
- AUROC mean: 0.9405
- AUROC std: 0.0276
- AUPRC mean: 0.1786
- AUPRC std: 0.0847
```

Calibration artifact:

```text
Uncalibrated:
- Brier: 0.0196
- ECE@10: 0.0202

Platt:
- Brier: 0.0134
- ECE@10: 0.0050

Isotonic:
- Brier: 0.0133
- ECE@10: 0.0008
```

Final operating-point artifact:

```text
Model: hgb
Calibrator: isotonic
Policy: A_first_crossing_lockout
Threshold: 0.0854430379746835
Lockout: 6 hours
Sepsis detection rate: 0.8974
Non-sepsis alert rate: 0.0
Alerts per 100 patient hours: 0.8671
Median lead time: 40.0 hours
```

Caveat to include near metrics:

```text
These metrics are reported from saved project artifacts and should be interpreted as retrospective development results, not clinical validation.
```

---

## Validation standards

### Required validation principles

- Use patient-level grouping.
- Avoid random row-level splitting.
- Keep all rows from the same patient in the same fold/split.
- Use out-of-fold predictions for calibration and policy analysis where possible.
- Clearly distinguish cross-validation development performance from final holdout performance.
- If no untouched test set exists, say so plainly.

### Preferred split utilities

`src/sepsis_ews/split.py` should eventually include:

- patient-grouped train/validation split
- GroupKFold helper
- patient ID integrity checks
- no-overlap assertions

### Required tests

Add tests that fail if:

- the same patient appears in both train and validation
- target/future columns enter the feature matrix
- rolling features use future rows
- policy lockout rules produce impossible alert counts
- calibrated probabilities fall outside `[0, 1]`

---

## Feature engineering standards

Temporal features should be:

- computed using past and current observations only
- grouped by patient
- sorted by time
- explicit about window lengths
- reproducible from scripts
- documented in a feature manifest

Recommended feature module responsibilities:

```text
features.py
- parse time-series rows
- create rolling windows
- create missingness indicators
- create deltas/trends
- enforce feature allowlist/blocklist
- save feature manifest
```

Do not let feature code silently include all columns. Prefer explicit feature selection.

---

## Calibration and policy standards

This project is strongest when it shows deployment-aware thinking.

Calibration work should report:

- Brier score
- ECE
- reliability curve
- calibration method
- calibration data provenance

Policy work should report:

- threshold
- lockout period
- detection rate
- non-sepsis alert rate
- alerts per 100 patient-hours
- median lead time
- trade-off curves

All policy outputs should be framed as retrospective simulation, not a clinical deployment claim.

---

## Documentation standards

### README must include

- One-sentence project pitch.
- Problem framing.
- Dataset source and data-access instructions.
- Clear statement that raw data is not committed.
- Workflow diagram or bullet flow.
- Validation strategy.
- Headline metrics with caveat.
- Key figures.
- Reproducibility commands.
- Folder structure.
- Limitations.
- Clinical disclaimer.
- Next steps.

### `docs/model_card.md` must include

- Intended use.
- Non-intended use.
- Dataset summary.
- Features overview.
- Model family.
- Validation method.
- Metrics.
- Calibration.
- Threshold/policy decision.
- Limitations.
- Ethical and clinical considerations.

### `docs/data_card.md` must include

- Dataset source.
- Access instructions.
- File layout.
- Label definition.
- Missingness.
- Cohort caveats.
- Licensing/citation notes.
- Privacy/publication constraints.

### `docs/leakage_review.md` must include

- Known leakage risks.
- Blocked columns.
- Feature allowlist strategy.
- Validation split checks.
- Status of unresolved issues.
- Tests added or still needed.

### `docs/clinical_limitations.md` must include

- Not a diagnostic tool.
- Retrospective analysis only.
- No clinical deployment claim.
- Dataset-specific limitations.
- Alert fatigue considerations.
- Need for prospective validation before any real use.

---

## Code quality standards

New Python code should be:

- small and modular
- readable
- type-hinted where practical
- tested with tiny fixtures
- deterministic where possible
- configured through YAML or CLI arguments
- free of hardcoded local machine paths
- safe around missing files and empty inputs

Avoid:

- giant notebook-only logic
- hidden state
- absolute Windows paths
- committing heavy artifacts
- result overwrites without metadata
- unlabelled experiment outputs

---

## Recommended command interface

Aim for commands like:

```bash
python scripts/build_dataset.py --config configs/default.yaml
python scripts/train_model.py --config configs/model_hgb.yaml
python scripts/evaluate_model.py --config configs/model_hgb.yaml
python scripts/run_policy_sweep.py --config configs/model_hgb.yaml
pytest
```

Optional later:

```bash
streamlit run app.py
uvicorn sepsis_ews.api:app --reload
```

Only add deployment/demo commands after the core pipeline is reproducible.

---

## Phase-by-phase roadmap

### Phase 1 — Repository hygiene and public safety

Goal: make the repo safe for GitHub.

Tasks:

- Initialise Git if needed.
- Expand `.gitignore`.
- Create target folders.
- Add `data/README.md`.
- Move or ignore raw/generated data safely.
- Fix README encoding issue.
- Identify which results are current.
- Do not delete raw data.

Deliverable:

```text
SEPSIS_PHASE_1_REPORT.md
```

### Phase 2 — Reproducible environment

Goal: make setup credible.

Tasks:

- Pin Python version.
- Add `pyproject.toml`.
- Add pinned requirements or lockfile.
- Add dev requirements.
- Add formatting/lint/test config.
- Add basic CI if ready.

Deliverable:

```text
SEPSIS_PHASE_2_ENV_REPORT.md
```

### Phase 3 — Source package skeleton

Goal: move from notebook-only to maintainable code.

Tasks:

- Create `src/sepsis_ews/`.
- Add modules for data, features, split, train, calibrate, policies, evaluate, inference.
- Add scripts that call package functions.
- Keep notebooks as narrative reports.

Deliverable:

```text
SEPSIS_PHASE_3_SOURCE_REPORT.md
```

### Phase 4 — Leakage and validation hardening

Goal: make the results trustworthy.

Tasks:

- Add feature allowlist/blocklist.
- Add patient split assertions.
- Add tests for leakage and temporal ordering.
- Document unresolved risks.

Deliverable:

```text
SEPSIS_PHASE_4_LEAKAGE_VALIDATION_REPORT.md
```

### Phase 5 — Model and evaluation pipeline

Goal: make training/evaluation rerunnable.

Tasks:

- Save model/calibrator bundle.
- Save metadata.
- Recreate key metrics.
- Generate final reports from scripts.
- Clearly mark old baseline artifacts.

Deliverable:

```text
SEPSIS_PHASE_5_MODEL_EVAL_REPORT.md
```

### Phase 6 — Portfolio documentation

Goal: make it recruiter-ready.

Tasks:

- Rewrite README.
- Add model card.
- Add data card.
- Add clinical limitations.
- Add key figures.
- Add reproducibility commands.
- Add final operating-point explanation.

Deliverable:

```text
SEPSIS_PHASE_6_PORTFOLIO_REPORT.md
```

### Phase 7 — Optional deployment/demo

Goal: make it interview-demo ready.

Tasks:

- Add Streamlit or FastAPI demo using sample/synthetic rows.
- Add clinical disclaimer.
- Add simple inference explanation.
- Add Docker only if it stays clean and lightweight.

Deliverable:

```text
SEPSIS_PHASE_7_DEMO_REPORT.md
```

---

## Review checklist

Run this checklist for every review or code change.

### Public safety

- [ ] Raw clinical data is not tracked.
- [ ] Generated large feature tables are not tracked.
- [ ] Model artifacts are not tracked unless intentionally released.
- [ ] No local paths or secrets are committed.
- [ ] `.gitignore` covers data, models, caches, and environments.
- [ ] No patient-level private data appears in README/docs/figures beyond approved public dataset context.

### Reproducibility

- [ ] Setup instructions exist.
- [ ] Dependencies are pinned or controlled.
- [ ] Scripts exist for key workflow stages.
- [ ] Notebooks are not the only executable workflow.
- [ ] Small fixture tests can run quickly.
- [ ] Results have provenance.

### ML correctness

- [ ] Splits are patient-grouped.
- [ ] No patient overlap across folds/splits.
- [ ] Target/future columns are excluded.
- [ ] Temporal features do not use future observations.
- [ ] Calibration is evaluated honestly.
- [ ] Policy thresholds are not overclaimed.
- [ ] Metrics distinguish CV, OOF, validation, and test performance.

### Portfolio quality

- [ ] README has a strong opening.
- [ ] Headline metrics are clear and caveated.
- [ ] Figures are curated and readable.
- [ ] Limitations are visible.
- [ ] Clinical disclaimer is included.
- [ ] Project can be understood quickly by a recruiter.
- [ ] Project can withstand deeper technical review.

### Healthcare communication

- [ ] No diagnostic claims.
- [ ] No treatment recommendations.
- [ ] No claim of clinical deployment readiness.
- [ ] Limitations and alert fatigue are discussed.
- [ ] Prospective validation is mentioned as necessary before real-world use.

---

## Change safety rules

Before suggesting or applying any change, ask:

1. **Will this risk publishing raw clinical data?**
2. **Will this create data leakage?**
3. **Will this make metrics look better than they really are?**
4. **Will this break reproducibility?**
5. **Will this overclaim clinical usefulness?**
6. **Will this make the repo look less professional to a recruiter?**

If any answer is yes or uncertain, stop and report the risk before changing files.

---

## How to use this skill

When the user asks for Sepsis project help:

1. Read this `SKILL.md` fully first.
2. Inspect the current project structure before assuming files exist.
3. Work phase by phase.
4. Prefer reports in Markdown.
5. Do not invent missing results.
6. Keep raw data and generated artifacts out of Git.
7. Convert notebooks into reusable source code gradually.
8. Preserve the project story: temporal ML, patient-grouped validation, calibration, alert burden, and responsible healthcare communication.

---

## First Codex prompt for a new project folder

Use this when starting work in a fresh Sepsis project folder:

```text
You are acting as a senior ML engineer, data scientist, and GitHub portfolio maintainer.

Read SKILL.md fully before making any recommendation.

Goal:
Begin Phase 1 for the Sepsis Early-Warning ML portfolio project.

Rules:
- Do not delete raw data.
- Do not commit or push.
- Do not invent results.
- Do not change model metrics.
- Keep raw clinical data untracked/ignored.
- Make small, reviewable edits only.
- Save all output as Markdown reports.

Tasks:
1. Inspect the current project structure.
2. Create or update a professional target folder skeleton:
   - data/
   - docs/
   - reports/
   - src/sepsis_ews/
   - scripts/
   - tests/
   - configs/
3. Expand `.gitignore` for raw data, generated features, model artifacts, caches, and environments.
4. Draft `data/README.md` explaining where the PhysioNet sepsis files should live and that raw data is not committed.
5. Draft or improve `README.md` into a recruiter-friendly portfolio README using only metrics already present in saved artifacts.
6. Add `docs/leakage_review.md` as a first-pass checklist, clearly flagging unresolved leakage checks.
7. Do not move or delete raw data unless explicitly instructed.
8. Save a report as:

SEPSIS_PHASE_1_REPORT.md

Include:
- Executive Summary
- Files Changed
- Public Safety Notes
- Reproducibility Notes
- Remaining Risks
- Next Recommended Phase
```
