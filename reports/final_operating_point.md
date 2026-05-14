# Final Operating Point

This report is copied from existing saved artifacts. The values were not independently rerun during Phase 6.

Source artifacts:

- `results/final_decision.json`
- `results/final_operating_point.csv`

## Saved Operating Point

| Field | Saved value |
|---|---:|
| Model | `hgb` |
| Calibrator | `isotonic` |
| Policy | `A_first_crossing_lockout` |
| Threshold | 0.0854430379746835 |
| Lockout | 6 hours |
| Detection rate | 0.8974 |
| Non-sepsis alert rate | 0.0000 |
| Alerts per 100 patient hours | 0.8671 |
| Median lead time | 40.0 hours |

## Interpretation

This operating point is a retrospective development artifact. It summarizes one saved threshold/policy decision for a HistGradientBoosting model with isotonic calibration and a first-crossing alert policy with a 6-hour lockout.

It should be used only to understand the project's saved analysis and reporting workflow. It is not a clinical operating threshold.

## Limitations

- The values were copied from saved artifacts and were not rerun in Phase 6.
- No independent final holdout test set has been confirmed.
- The feature-generation path still needs end-to-end leakage review.
- Alert burden and lead time are retrospective simulations.
- Calibration and threshold behavior may not transfer to other settings.

## Clinical Disclaimer

This operating point is not clinically validated and is not deployment-ready. It must not be used for diagnosis, treatment, triage, monitoring, or any patient-care decision.
