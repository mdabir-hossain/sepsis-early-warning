# Data Setup

This project uses PhysioNet-style sepsis patient time-series files in pipe-separated `.psv` format.

Raw clinical data is not committed to Git. Keep all raw patient files local.

## Expected Local Layout

Place the original dataset files under:

```text
data/raw/
|-- training_setA/
|   |-- p000001.psv
|   `-- ...
`-- training_setB/
    |-- p100001.psv
    `-- ...
```

The current working folder may also contain a legacy local layout:

```text
training/
|-- training_setA/
`-- training_setB/
```

That folder is ignored by `.gitignore` and must not be committed or pushed.

## What Must Stay Out of Git

Do not commit:

- raw `.psv` patient files
- `training/`
- `data/raw/`
- `data/interim/`
- `data/processed/`
- generated feature tables
- out-of-fold prediction dumps
- fitted model artifacts

## Public-Safe Data

Only tiny synthetic or public-safe sample fixtures should be placed in:

```text
data/sample/
```

Any sample data must avoid exposing patient-level private information and must be clearly documented as sample or synthetic.

## Reproducibility Note

Future pipeline scripts should read from `data/raw/`, write parsed/intermediate files to `data/interim/`, and write generated feature tables to `data/processed/`. Those generated folders are ignored so the repository remains safe and lightweight.

## Dataset Citation

Add the official dataset citation and access link before public release. Do not claim ownership of the raw clinical dataset.
