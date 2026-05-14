# Clinical Limitations

## Not A Diagnostic Tool

This project is not a diagnostic tool. It must not be used to diagnose, treat, prevent, triage, monitor, or manage sepsis or any other condition.

The model outputs should be understood only as retrospective risk-estimation artifacts within a portfolio ML project.

## Retrospective Analysis Only

The reported results come from saved retrospective development artifacts. They were not independently rerun in Phase 6 and do not represent prospective validation.

Retrospective performance can differ substantially from real-world performance because of data collection patterns, workflow differences, label timing, missingness, treatment effects, and population shift.

## No Clinical Deployment Claim

This repository does not claim clinical validation, clinical utility, patient benefit, regulatory readiness, or hospital deployment readiness.

Any real-world use would require formal clinical governance, prospective validation, privacy review, safety review, workflow integration assessment, monitoring plans, and regulatory assessment.

## Dataset-Specific Limitations

Results may depend on:

- the source cohort and inclusion criteria
- local measurement and documentation practices
- label definition and sepsis timing logic
- missingness patterns
- feature-engineering choices
- patient-grouped validation design
- calibration and threshold selection on development artifacts

The saved feature manifest preview also contains unresolved high-risk feature names derived from target or workflow fields. These must be audited before retraining or stronger claims.

## Alert Fatigue Considerations

Early-warning tools can increase cognitive and operational burden. False positives may create alert fatigue, unnecessary clinical review, or workflow disruption. False negatives may create false reassurance if users overtrust the system.

Alert burden metrics in this project are retrospective simulations and should not be interpreted as evidence that a real clinical alert would be safe, usable, or accepted.

## Calibration And Threshold Limitations

Calibration and threshold choices are dataset-specific and may degrade under population shift, measurement changes, or workflow changes. A threshold selected retrospectively may not maintain the same detection, false-alert, or lead-time profile in another setting.

Any threshold used in a real care environment would need prospective validation, local calibration review, continuous monitoring, and clear escalation governance.

## Need For Prospective Validation

Before any real-world use, the model would need prospective validation in the intended setting. That validation should assess discrimination, calibration, alert burden, lead time, subgroup performance, workflow impact, clinician interaction, safety risks, and downstream patient outcomes.

## Human Oversight And Governance

Any clinical ML system would require human oversight and governance. This includes clear ownership, audit trails, incident review, model monitoring, data drift checks, recalibration plans, privacy controls, and processes for stopping use if safety concerns arise.

## Clinical Disclaimer

This project is a public-safe ML portfolio artifact only. It is not clinically validated and is not deployment-ready. It must not be used for patient care or clinical decision-making.
