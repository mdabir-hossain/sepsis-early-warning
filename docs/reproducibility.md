# Reproducibility Notes

This project is being converted from a notebook-first analysis into a reproducible ML portfolio project in phases.

Current metrics in the README are copied from existing saved artifacts. They have not been independently rerun by the source package yet.

Phase 5 adds utilities for metadata and artifact-derived Markdown reporting. These utilities are scaffolding only:

- they do not train models
- they do not run notebooks
- they do not read raw clinical data
- they do not invent missing metrics
- they fail if expected JSON artifacts are missing

Before any new model results are reported, the pipeline should be rerun in a controlled environment with leakage guards enabled and clear metric provenance.
