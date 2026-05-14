# Sepsis GitHub Upgrade Audit

## Executive Summary

This audit prepares a safe plan to upgrade the existing public GitHub repository:

```text
https://github.com/mdabir-hossain/sepsis-early-warning-system
```

The current local folder is not a Git repository. Because there is no `.git` metadata here, the local folder is not currently connected to the GitHub repository, has no local remote, has no current branch, and cannot report tracked files.

Recommendation: clone the existing GitHub repository into a fresh folder, then copy only the public-safe Phase 1-6 files from this local project into that clone. This is safer than initializing Git in the current folder because the current folder contains raw clinical data, generated feature tables, saved result artifacts, and generated figures that must not be accidentally staged.

No `git add`, `git commit`, `git push`, destructive Git command, training command, notebook command, or model-generation command was run.

## Git/Remote Status

Source-of-truth note:

- Root `SKILL.md` was not present in this local folder.
- `SEPSIS_SKILL.md` was present and read fully as the project source of truth.

Read-only Git commands were attempted exactly as requested.

`git status`:

```text
fatal: not a git repository (or any of the parent directories): .git
```

`git remote -v`:

```text
fatal: not a git repository (or any of the parent directories): .git
```

`git branch --show-current`:

```text
fatal: not a git repository (or any of the parent directories): .git
```

Remote verification:

- No remote exists in this local folder because this local folder is not a Git repository.
- Therefore this folder does not currently point to `https://github.com/mdabir-hossain/sepsis-early-warning-system`.

## Currently Tracked Safety Review

`git ls-files` was attempted:

```text
fatal: not a git repository (or any of the parent directories): .git
```

Because this folder is not a Git repository, there is no local tracked-file index to inspect. I could not verify whether the existing GitHub repository currently tracks unsafe files from this folder.

The tracked safety review must be repeated inside a fresh clone of the existing GitHub repository before adding or pushing anything.

High-risk patterns to check in the cloned repository:

- `*.psv`
- `training/`
- `data/raw/`
- `data/interim/`
- `data/processed/`
- `features_windowed_6h_12h_24h.csv`
- `results/*.parquet`
- large generated `results/*.csv`
- raw prediction dumps
- `models/`
- `*.pkl`
- `*.pickle`
- `*.joblib`
- `*.onnx`
- `*.pt`
- `*.pth`
- `*.h5`
- `*.sav`
- `.env`
- `.env.*`
- cache folders such as `__pycache__/`, `.pytest_cache/`, `.ruff_cache/`, `.ipynb_checkpoints/`

## Ignored/Untracked Safety Review

`git status --short --ignored` was attempted:

```text
fatal: not a git repository (or any of the parent directories): .git
```

Because this folder is not a Git repository, Git cannot report ignored or untracked status here. The filesystem inspection still found the following important local state.

Current public-safe project files and folders present:

- `.gitignore`
- `.python-version`
- `README.md`
- `pyproject.toml`
- `requirements.txt`
- `requirements-dev.txt`
- `data/README.md`
- `docs/`
- `reports/final_operating_point.md`
- `src/sepsis_ews/`
- `scripts/`
- `tests/`
- Phase reports: `SEPSIS_PHASE_1_REPORT.md` through `SEPSIS_PHASE_6_PORTFOLIO_REPORT.md`
- `SEPSIS_PROJECT_AUDIT.md`
- `SEPSIS_SKILL.md`

Current local unsafe or generated artifacts present:

- `training/` with 40,336 raw `.psv` files
- `features_windowed_6h_12h_24h.csv` at 45,813,457 bytes
- `results/` containing JSON/CSV/parquet artifacts, including generated parquet files and sample processed data
- `figures/` containing generated PNG figures

Additional scan result:

- No model artifact or local environment-secret filenames were found by the scan for `*.pkl`, `*.pickle`, `*.joblib`, `*.onnx`, `*.pt`, `*.pth`, `*.h5`, `*.sav`, `.env`, or `.env.*`.
- No cache/environment directories were found by the scan for `__pycache__`, `.pytest_cache`, `.mypy_cache`, `.ruff_cache`, `.ipynb_checkpoints`, `.venv`, `venv`, `env`, `build`, `dist`, or `*.egg-info`.

## Safe Files To Add

These files are appropriate candidates to copy into a fresh clone and stage after review:

- `.gitignore`
- `.python-version`
- `README.md`
- `pyproject.toml`
- `requirements.txt`
- `requirements-dev.txt`
- `data/README.md`
- `docs/leakage_review.md`
- `docs/reproducibility.md`
- `docs/model_card.md`
- `docs/data_card.md`
- `docs/clinical_limitations.md`
- `reports/final_operating_point.md`
- `src/sepsis_ews/__init__.py`
- `src/sepsis_ews/calibrate.py`
- `src/sepsis_ews/data.py`
- `src/sepsis_ews/evaluate.py`
- `src/sepsis_ews/explain.py`
- `src/sepsis_ews/features.py`
- `src/sepsis_ews/inference.py`
- `src/sepsis_ews/metadata.py`
- `src/sepsis_ews/placeholders.py`
- `src/sepsis_ews/policies.py`
- `src/sepsis_ews/reporting.py`
- `src/sepsis_ews/split.py`
- `src/sepsis_ews/train.py`
- `scripts/build_dataset.py`
- `scripts/evaluate_model.py`
- `scripts/generate_report.py`
- `scripts/run_policy_sweep.py`
- `scripts/train_model.py`
- `tests/test_evaluate_utils.py`
- `tests/test_feature_leakage.py`
- `tests/test_metadata.py`
- `tests/test_package_import.py`
- `tests/test_reporting.py`
- `tests/test_skeleton_modules.py`
- `tests/test_split_validation.py`
- `tests/test_temporal_ordering.py`
- `SEPSIS_PHASE_1_REPORT.md`
- `SEPSIS_PHASE_2_ENV_REPORT.md`
- `SEPSIS_PHASE_3_SOURCE_REPORT.md`
- `SEPSIS_PHASE_4_LEAKAGE_VALIDATION_REPORT.md`
- `SEPSIS_PHASE_5_MODEL_EVAL_REPORT.md`
- `SEPSIS_PHASE_6_PORTFOLIO_REPORT.md`
- `SEPSIS_GITHUB_UPGRADE_AUDIT.md`

Files that may be safe but should receive a final manual review before staging:

- `SEPSIS_PROJECT_AUDIT.md`
- `SEPSIS_SKILL.md`
- `notebooks/*.ipynb`

Notebook caution: notebooks can contain outputs, local paths, hidden large embedded data, or stale claims. Only stage notebooks after verifying they do not include raw patient rows, private paths, large outputs, or overclaims.

## Files To Keep Ignored

These files and folders must remain ignored and must not be added:

- `training/`
- `data/raw/`
- `data/interim/`
- `data/processed/`
- `*.psv`
- `features_windowed_6h_12h_24h.csv`
- `results/`
- `figures/`
- `*.parquet`
- generated `*.csv` files except explicitly curated files under `reports/metrics/` or `data/sample/`
- `models/`
- `*.pkl`
- `*.pickle`
- `*.joblib`
- `*.onnx`
- `*.pt`
- `*.pth`
- `*.h5`
- `*.sav`
- `.env`
- `.env.*`
- notebook/runtime caches
- virtual environments
- editor and OS metadata

Current `.gitignore` already covers these categories:

- raw clinical data and `.psv` files
- generated feature tables and parquet files
- `results/` and `figures/`
- model artifacts
- runtime caches
- build outputs
- virtual environments and local secrets
- OS/editor files

## Files Requiring Untracking If Already Tracked

Because this local folder is not a Git repository, I could not determine whether any unsafe files are already tracked in the public GitHub repository.

If any of the following are tracked in the fresh clone, remove them from Git tracking with `git rm --cached` only. Do not delete local raw data unless explicitly instructed.

Patterns requiring untracking if tracked:

- `training/`
- `data/raw/`
- `data/interim/`
- `data/processed/`
- `features_windowed_6h_12h_24h.csv`
- raw `.psv` files
- `results/`
- `figures/`
- `models/`
- model artifact files
- `.env` files
- cache folders

Before untracking, inspect the exact tracked matches. Do not run broad removal commands blindly.

## README Upgrade Plan

The current Phase 6 README is safe to use as the replacement public README because it:

- opens with a concise recruiter-friendly project pitch
- frames the project as retrospective ML engineering work
- explains dataset access without publishing raw data
- links to model card, data card, leakage review, reproducibility notes, clinical limitations, and data setup
- reports saved metrics only with provenance and caveats
- avoids clinical validation and deployment claims
- explains that scripts are placeholders or scaffolding where appropriate
- lists limitations and next steps conservatively

Before staging the README in the fresh clone:

1. Confirm relative links resolve in the GitHub repository.
2. Confirm no linked file is missing from the staged set.
3. Confirm metrics still match saved artifacts and Phase 5/6 reports.
4. Keep clinical disclaimer language visible.

## Public Safety Risks

Primary risk: accidentally staging local raw/generated artifacts from the current folder.

Specific local risks:

- `training/` contains 40,336 raw `.psv` files.
- `features_windowed_6h_12h_24h.csv` is a large generated feature table.
- `results/` contains generated parquet files, raw-ish processed samples, prediction/calibration artifacts, and metric outputs.
- `figures/` contains generated images that should only be published if intentionally curated and license/public-safety reviewed.

Process risks:

- Initializing Git in this raw-data-containing folder increases the chance of accidental staging.
- Copying the entire folder into a clone would bring unsafe artifacts along with safe docs/source files.
- Existing GitHub history may already contain unsafe files; that must be checked inside the clone.

Clinical communication risks:

- Saved metrics are retrospective development artifact metrics only.
- No independent final holdout test set has been confirmed.
- The saved feature manifest preview contains unresolved high-risk leakage indicators.
- The repository must not imply clinical validation, deployment readiness, diagnosis, treatment, or patient benefit.

## Exact Recommended Commands For Later

Do not run these commands until you are ready to work in a Git-connected clone and have reviewed the plan.

Recommended safer workflow:

```powershell
cd "F:\Project 3 Folder"
git clone https://github.com/mdabir-hossain/sepsis-early-warning-system.git sepsis-early-warning-system-upgrade
cd "F:\Project 3 Folder\sepsis-early-warning-system-upgrade"
git status
git remote -v
git branch --show-current
git ls-files
git status --short --ignored
```

Safety inspection commands inside the fresh clone:

```powershell
git ls-files "*.psv"
git ls-files "training/*"
git ls-files "data/raw/*"
git ls-files "data/interim/*"
git ls-files "data/processed/*"
git ls-files "features_windowed_6h_12h_24h.csv"
git ls-files "results/*"
git ls-files "figures/*"
git ls-files "models/*"
git ls-files "*.pkl" "*.pickle" "*.joblib" "*.onnx" "*.pt" "*.pth" "*.h5" "*.sav"
git ls-files ".env" ".env.*"
```

Copy only safe files from this local Phase 1-6 folder into the clone. Example paths to copy manually or with a carefully scoped file copy:

```text
.gitignore
.python-version
README.md
pyproject.toml
requirements.txt
requirements-dev.txt
data/README.md
docs/
reports/final_operating_point.md
src/
scripts/
tests/
SEPSIS_PHASE_1_REPORT.md
SEPSIS_PHASE_2_ENV_REPORT.md
SEPSIS_PHASE_3_SOURCE_REPORT.md
SEPSIS_PHASE_4_LEAKAGE_VALIDATION_REPORT.md
SEPSIS_PHASE_5_MODEL_EVAL_REPORT.md
SEPSIS_PHASE_6_PORTFOLIO_REPORT.md
SEPSIS_GITHUB_UPGRADE_AUDIT.md
```

After copying safe files into the fresh clone, inspect before staging:

```powershell
git status --short --ignored
git diff -- README.md
git diff -- docs
git diff -- src
git diff -- scripts
git diff -- tests
git diff -- reports
```

If unsafe files are already tracked in the cloned repository, inspect first:

```powershell
git ls-files "training/*" "*.psv" "data/raw/*" "data/interim/*" "data/processed/*" "features_windowed_6h_12h_24h.csv" "results/*" "figures/*" "models/*"
```

Only after confirming the exact tracked unsafe files, untrack them without deleting local copies:

```powershell
git rm --cached -r -- training data/raw data/interim data/processed results figures models
git rm --cached -- features_windowed_6h_12h_24h.csv
```

If individual raw `.psv` files or model artifacts are tracked outside those folders, untrack those exact paths only after reviewing `git ls-files` output.

When ready to stage public-safe files later:

```powershell
git add .gitignore .python-version README.md pyproject.toml requirements.txt requirements-dev.txt data/README.md docs reports/final_operating_point.md src scripts tests SEPSIS_PHASE_1_REPORT.md SEPSIS_PHASE_2_ENV_REPORT.md SEPSIS_PHASE_3_SOURCE_REPORT.md SEPSIS_PHASE_4_LEAKAGE_VALIDATION_REPORT.md SEPSIS_PHASE_5_MODEL_EVAL_REPORT.md SEPSIS_PHASE_6_PORTFOLIO_REPORT.md SEPSIS_GITHUB_UPGRADE_AUDIT.md
git status --short
```

Before committing later, run tests if Python is available:

```powershell
python -m pytest
```

If `python` is not available, try:

```powershell
py -m pytest
pytest
```

Only commit after the staged file list is clean and public-safe:

```powershell
git commit -m "Upgrade sepsis early-warning portfolio structure"
```

Only push after final review:

```powershell
git push
```

## Do Not Run Yet

Do not run these yet:

- `git add`
- `git commit`
- `git push`
- `git init` in the current raw-data-containing folder
- broad copy commands that copy the whole current folder into the clone
- `git rm` without `--cached`
- model training commands
- notebook execution commands
- commands that regenerate metrics, figures, predictions, or model artifacts

Before any later push, verify:

- the working folder is a clone of `https://github.com/mdabir-hossain/sepsis-early-warning-system`
- no raw `.psv` files are tracked
- no generated feature tables are tracked
- no raw/generated prediction dumps are tracked
- no model artifacts are tracked
- no secrets or local environment files are tracked
- README/docs preserve retrospective-development and clinical-disclaimer caveats
