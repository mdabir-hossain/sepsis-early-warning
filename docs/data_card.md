# Data Card

## Dataset Source Context

This project uses local PhysioNet-style sepsis patient time-series files in pipe-separated `.psv` format. The raw data is expected to come from the original dataset provider and should be downloaded by the user according to that provider's terms.

Exact citation, license, and access URL details are not fully documented in the local project files reviewed during Phase 6.

TODO: Add the official dataset citation, access link, and license/terms summary before public release.

## Expected Local File Layout

Raw patient files should be placed locally under:

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

That legacy folder is raw clinical data and must not be committed or published.

See [data/README.md](../data/README.md) for local setup notes.

## Raw Data Is Not Committed

Raw patient data is intentionally excluded from the public repository. The following should remain local and ignored:

- `training/`
- `data/raw/`
- `data/interim/`
- `data/processed/`
- raw `.psv` patient files
- generated feature tables
- raw prediction dumps
- fitted model artifacts

## File Format Overview

The expected raw files are pipe-separated value files (`.psv`) with one file per patient. The project treats observations as patient time-series records. Local saved artifacts indicate that downstream feature engineering uses patient identifiers, an ICU time index, rolling windows, missingness indicators, and engineered temporal summaries.

Do not copy raw patient rows into documentation, issues, commits, examples, or public reports.

## Label And Case Definition Caveat

The project studies retrospective sepsis early-warning labels derived from the dataset workflow. Exact clinical label construction should be documented from the official dataset description and the project notebooks before public release.

High-level caveat: label timing and case definition choices strongly affect early-warning performance, lead time, and alert burden. Any future modelling claims should state the prediction horizon, label definition, exclusion rules, and whether labels are used only as outcomes rather than features.

TODO: Add a concise, source-backed label definition once the official citation and local notebook logic are reviewed.

## Missingness And Temporal-Data Caveats

Healthcare time-series data is often sparse and irregular. Missingness can reflect clinical measurement practice, patient severity, site workflow, or documentation behavior.

Project artifacts indicate temporal rolling windows over 6, 12, and 24 hours, forward fill within patient, and missingness indicators. These design choices should be reviewed carefully because temporal imputation and missingness features can introduce leakage or encode site-specific workflow patterns if not constrained.

Future feature generation should ensure that only past and current observations are used for each prediction time.

## Privacy And Publication Constraints

This repository must not publish raw patient rows, patient-level examples, raw `.psv` files, large generated feature tables, or raw prediction dumps. Public documentation should use aggregate metrics and high-level descriptions only.

Before public release, verify that any curated figures or metrics are small, aggregate, non-sensitive, and permitted by the dataset license and terms.

## Licensing And Citation Notes

TODO: Add official dataset citation.

TODO: Add dataset access URL.

TODO: Add license or data-use terms summary.

Do not guess citation or license terms. If exact details are unavailable locally, leave them as TODOs until verified from the official source.

## Public-Safe Usage Notes

- Keep raw data local.
- Do not commit `.psv` files.
- Do not include patient-level examples in docs.
- Use only aggregate, saved-artifact metrics in public-facing documentation.
- Clearly distinguish retrospective development metrics from independent validation.
- Do not make clinical deployment claims from this dataset alone.
