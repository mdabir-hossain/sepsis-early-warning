# Sepsis New Public Repo Prep Report

## Executive Summary

A new clean local folder was prepared for a future public GitHub repository named `sepsis-early-warning`. The folder was created outside the raw-data-containing Phase 1-6 project folder and populated only with allowlisted public-safe files.

Unsafe local artifacts were not copied. No raw clinical data, generated feature tables, generated results, generated figures, model artifacts, environment files, caches, notebooks, training commands, notebook execution, commits, pushes, remotes, or GitHub repo creation steps were performed.

Git was initialized in the clean folder only after the safety scan found no unsafe files or folders.

## New Folder Path

```text
F:\Project 3 Folder\sepsis-early-warning-public
```

Recommended future GitHub repository name:

```text
sepsis-early-warning
```

## Files Copied

Top-level files copied:

- `.gitignore`
- `.python-version`
- `README.md`
- `pyproject.toml`
- `requirements.txt`
- `requirements-dev.txt`
- `SEPSIS_PHASE_1_REPORT.md`
- `SEPSIS_PHASE_2_ENV_REPORT.md`
- `SEPSIS_PHASE_3_SOURCE_REPORT.md`
- `SEPSIS_PHASE_4_LEAKAGE_VALIDATION_REPORT.md`
- `SEPSIS_PHASE_5_MODEL_EVAL_REPORT.md`
- `SEPSIS_PHASE_6_PORTFOLIO_REPORT.md`
- `SEPSIS_GITHUB_UPGRADE_AUDIT.md`
- `SEPSIS_SKILL.md`
- `SEPSIS_PROJECT_AUDIT.md`

Folders/files copied:

- `data/README.md`
- `docs/`
- `reports/final_operating_point.md`
- `src/`
- `scripts/`
- `tests/`

## Files Intentionally Excluded

The following unsafe or generated local artifacts were not copied:

- `training/`
- `data/raw/`
- `data/interim/`
- `data/processed/`
- raw `.psv` files
- `features_windowed_6h_12h_24h.csv`
- `results/`
- `figures/`
- `models/`
- model artifact patterns: `*.pkl`, `*.pickle`, `*.joblib`, `*.onnx`, `*.pt`, `*.pth`, `*.h5`, `*.sav`
- `.env`
- `.env.*`
- cache/environment folders: `__pycache__/`, `.pytest_cache/`, `.ruff_cache/`, `.ipynb_checkpoints/`, `.venv/`, `venv/`, `env/`

Notebooks were also not copied in this preparation pass. They should only be added later if they are manually reviewed for output size, raw patient rows, local paths, stale claims, and public-safety issues.

## Safety Scan Results

Safety scans were run from inside the clean folder before Git initialization.

Checked for unsafe files:

- `.psv`
- `features_windowed_6h_12h_24h.csv`
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

Result: no matching unsafe files were found.

Checked for unsafe/cache folders:

- `training/`
- `results/`
- `figures/`
- `models/`
- `.venv/`
- `venv/`
- `env/`
- `__pycache__/`
- `.pytest_cache/`
- `.ruff_cache/`
- `.ipynb_checkpoints/`

Result: no matching unsafe folders were found.

Checked copied data/report folders:

- `data/` contains only `README.md`.
- `reports/` contains only `final_operating_point.md`.

## Git Status

Initial `git status` before initialization returned:

```text
fatal: not a git repository (or any of the parent directories): .git
```

Because the clean folder passed the safety scan, Git was initialized in the clean folder only:

```text
Initialized empty Git repository in F:/Project 3 Folder/sepsis-early-warning-public/.git/
```

Current Git state after initialization:

```text
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.gitignore
	.python-version
	README.md
	SEPSIS_GITHUB_UPGRADE_AUDIT.md
	SEPSIS_PHASE_1_REPORT.md
	SEPSIS_PHASE_2_ENV_REPORT.md
	SEPSIS_PHASE_3_SOURCE_REPORT.md
	SEPSIS_PHASE_4_LEAKAGE_VALIDATION_REPORT.md
	SEPSIS_PHASE_5_MODEL_EVAL_REPORT.md
	SEPSIS_PHASE_6_PORTFOLIO_REPORT.md
	SEPSIS_PROJECT_AUDIT.md
	SEPSIS_SKILL.md
	data/
	docs/
	pyproject.toml
	reports/
	requirements-dev.txt
	requirements.txt
	scripts/
	src/
	tests/

nothing added to commit but untracked files present (use "git add" to track)
```

Remote status:

- `git remote -v` returned no remotes.
- No GitHub remote was connected.
- No GitHub repository was created from CLI.

Current branch:

```text
master
```

## Public Safety Notes

The clean folder is intentionally separated from the raw-data-containing source folder. The source folder still contains raw/generated local artifacts and should not be initialized or copied wholesale.

The clean folder excludes raw patient data, generated features, saved result artifacts, generated figures, model artifacts, local environment files, and caches.

The README and documentation preserve conservative healthcare framing:

- retrospective development artifact metrics only
- no clinical validation claim
- no deployment readiness claim
- no diagnostic or treatment use
- leakage risks documented
- citation/license TODOs not guessed

## Remaining Risks

- Tests were not run in this task.
- No files were staged or committed yet.
- No GitHub remote has been added yet.
- The current branch is `master`; GitHub default may be `main`.
- `SEPSIS_PROJECT_AUDIT.md` and `SEPSIS_SKILL.md` were copied as requested, but should receive one final public-readiness review before staging.
- Notebooks were not copied. If notebooks are added later, they need manual safety review.
- Dataset citation/license details remain TODOs in the data card until verified from the official source.
- The old public repository was not changed and was not made private.

## Recommended Next Commands

Run from the clean folder:

```powershell
cd "F:\Project 3 Folder\sepsis-early-warning-public"
git status --short --ignored
```

Optional branch rename before first commit:

```powershell
git branch -M main
git status
```

Before staging, run one more safety scan:

```powershell
Get-ChildItem -Recurse -Force -File -Include *.psv,features_windowed_6h_12h_24h.csv,*.pkl,*.pickle,*.joblib,*.onnx,*.pt,*.pth,*.h5,*.sav,.env,.env.* | Select-Object FullName,Length
Get-ChildItem -Recurse -Force -Directory -Include training,results,figures,models,.venv,venv,env,__pycache__,.pytest_cache,.ruff_cache,.ipynb_checkpoints | Select-Object FullName
```

When ready to stage later:

```powershell
git add .gitignore .python-version README.md pyproject.toml requirements.txt requirements-dev.txt data/README.md docs reports/final_operating_point.md src scripts tests SEPSIS_PHASE_1_REPORT.md SEPSIS_PHASE_2_ENV_REPORT.md SEPSIS_PHASE_3_SOURCE_REPORT.md SEPSIS_PHASE_4_LEAKAGE_VALIDATION_REPORT.md SEPSIS_PHASE_5_MODEL_EVAL_REPORT.md SEPSIS_PHASE_6_PORTFOLIO_REPORT.md SEPSIS_GITHUB_UPGRADE_AUDIT.md SEPSIS_NEW_PUBLIC_REPO_PREP_REPORT.md SEPSIS_SKILL.md SEPSIS_PROJECT_AUDIT.md
git status --short
```

If Python is available, run tests before committing:

```powershell
python -m pytest
```

If the new GitHub repository is created manually in GitHub settings later, add the remote only after review:

```powershell
git remote add origin https://github.com/mdabir-hossain/sepsis-early-warning.git
git remote -v
```

## Do Not Run Yet

Do not run these yet:

- `git add`
- `git commit`
- `git push`
- `git remote add`
- GitHub CLI repo creation
- commands that make the old repository private
- commands that copy the whole raw-data-containing folder
- notebook execution
- model training
- metric regeneration
- figure/result generation

Before any future commit or push, verify again that no raw clinical data, generated feature table, generated result artifact, generated figure, model artifact, local secret, or cache file is staged.
