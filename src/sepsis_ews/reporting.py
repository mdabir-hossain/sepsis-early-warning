"""Artifact-derived reporting utilities.

The functions in this module only format caller-provided or explicitly loaded
artifacts. They do not rerun notebooks, train models, modify existing results,
or invent missing metrics.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_json_artifact(path: str | Path) -> dict[str, Any]:
    """Load a JSON artifact from a caller-provided path."""
    artifact_path = Path(path)
    if not artifact_path.exists():
        raise FileNotFoundError(f"JSON artifact not found: {artifact_path}")
    if artifact_path.suffix.lower() != ".json":
        raise ValueError(f"Expected a .json artifact, got: {artifact_path}")

    with artifact_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, dict):
        raise ValueError(f"Expected JSON object in artifact: {artifact_path}")
    return data


def markdown_table(headers: list[str], rows: list[list[object]]) -> str:
    """Format supplied values as a Markdown table."""
    if not headers:
        raise ValueError("Markdown table requires at least one header.")
    for row in rows:
        if len(row) != len(headers):
            raise ValueError("Every Markdown table row must match the header count.")

    header_line = "| " + " | ".join(headers) + " |"
    separator_line = "| " + " | ".join("---" for _ in headers) + " |"
    row_lines = ["| " + " | ".join(str(value) for value in row) + " |" for row in rows]
    return "\n".join([header_line, separator_line, *row_lines])


def model_metrics_to_markdown(model_metrics: dict[str, Any]) -> str:
    """Format existing model comparison artifact data as Markdown."""
    summary = model_metrics.get("summary")
    if not isinstance(summary, dict):
        raise ValueError("model_metrics artifact must contain a 'summary' object.")

    rows: list[list[object]] = []
    for model_name, metrics in summary.items():
        if not isinstance(metrics, dict):
            raise ValueError(f"Metrics for model {model_name!r} must be an object.")
        rows.append(
            [
                model_name,
                metrics.get("auroc_mean", ""),
                metrics.get("auroc_std", ""),
                metrics.get("auprc_mean", ""),
                metrics.get("auprc_std", ""),
            ]
        )

    return markdown_table(["Model", "AUROC mean", "AUROC std", "AUPRC mean", "AUPRC std"], rows)


def calibration_report_to_markdown(calibration_report: dict[str, Any]) -> str:
    """Format existing calibration artifact data as Markdown."""
    rows: list[list[object]] = []
    for calibrator_name in ("uncalibrated", "platt", "isotonic"):
        metrics = calibration_report.get(calibrator_name)
        if isinstance(metrics, dict):
            rows.append([calibrator_name, metrics.get("brier", ""), metrics.get("ece10", "")])

    if not rows:
        raise ValueError("calibration_report artifact does not contain known calibration entries.")
    return markdown_table(["Calibration", "Brier", "ECE@10"], rows)


def final_decision_to_markdown(final_decision: dict[str, Any]) -> str:
    """Format existing final decision artifact data as Markdown."""
    metrics = final_decision.get("metrics")
    if not isinstance(metrics, dict):
        raise ValueError("final_decision artifact must contain a 'metrics' object.")

    rows = [
        ["Model", final_decision.get("model_name", "")],
        ["Calibrator", final_decision.get("calibrator", "")],
        ["Policy", final_decision.get("policy", "")],
        ["Threshold", final_decision.get("tau", "")],
        ["Lockout hours", final_decision.get("lockout_hours", "")],
        ["Sepsis detection rate", metrics.get("sepsis_detection_rate", "")],
        ["Non-sepsis alert rate", metrics.get("nonsepsis_alert_rate", "")],
        ["Alerts per 100 patient hours", metrics.get("alerts_per_100_patient_hours", "")],
        ["Median lead time", metrics.get("lead_time_median", "")],
    ]
    return markdown_table(["Field", "Value"], rows)


def build_artifact_metrics_report(
    *,
    model_metrics: dict[str, Any],
    calibration_report: dict[str, Any],
    final_decision: dict[str, Any],
) -> str:
    """Build a Markdown report from already loaded artifact dictionaries."""
    return "\n\n".join(
        [
            "# Artifact-Derived Metrics Report",
            "These metrics are copied from existing saved artifacts and were not independently rerun.",
            "## Model Comparison",
            model_metrics_to_markdown(model_metrics),
            "## Calibration",
            calibration_report_to_markdown(calibration_report),
            "## Final Operating Point",
            final_decision_to_markdown(final_decision),
        ]
    )


def write_markdown_report(content: str, output_path: str | Path) -> None:
    """Write caller-provided Markdown content to a caller-provided output path."""
    if not content.strip():
        raise ValueError("Refusing to write an empty Markdown report.")

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
