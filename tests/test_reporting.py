import json

import pytest

from sepsis_ews.reporting import (
    build_artifact_metrics_report,
    load_json_artifact,
    markdown_table,
)


def test_load_json_artifact_reads_tiny_file(tmp_path) -> None:
    artifact_path = tmp_path / "metric.json"
    artifact_path.write_text(json.dumps({"value": 1}), encoding="utf-8")

    assert load_json_artifact(artifact_path) == {"value": 1}


def test_load_json_artifact_missing_file_raises(tmp_path) -> None:
    with pytest.raises(FileNotFoundError):
        load_json_artifact(tmp_path / "missing.json")


def test_markdown_table_uses_only_supplied_data() -> None:
    table = markdown_table(["Metric", "Value"], [["AUROC", 0.5]])

    assert "AUROC" in table
    assert "0.5" in table
    assert "AUPRC" not in table


def test_build_artifact_metrics_report_formats_supplied_artifacts() -> None:
    report = build_artifact_metrics_report(
        model_metrics={
            "summary": {
                "demo": {
                    "auroc_mean": 0.5,
                    "auroc_std": 0.1,
                    "auprc_mean": 0.2,
                    "auprc_std": 0.05,
                }
            }
        },
        calibration_report={"uncalibrated": {"brier": 0.1, "ece10": 0.2}},
        final_decision={
            "model_name": "demo",
            "calibrator": "none",
            "policy": "demo_policy",
            "tau": 0.3,
            "lockout_hours": 6,
            "metrics": {
                "sepsis_detection_rate": 0.4,
                "nonsepsis_alert_rate": 0.0,
                "alerts_per_100_patient_hours": 1.0,
                "lead_time_median": 2.0,
            },
        },
    )

    assert "Artifact-Derived Metrics Report" in report
    assert "demo_policy" in report
