"""Generate a Markdown report from existing metrics artifacts."""

from __future__ import annotations

import argparse
from pathlib import Path

from sepsis_ews.reporting import (
    build_artifact_metrics_report,
    load_json_artifact,
    write_markdown_report,
)

EXPECTED_ARTIFACTS = {
    "model_metrics": "model_metrics_cv.json",
    "calibration_report": "calibration_report.json",
    "final_decision": "final_decision.json",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a Markdown report from existing saved metrics artifacts."
    )
    parser.add_argument("--metrics-dir", required=True, help="Directory containing existing JSON artifacts.")
    parser.add_argument("--output", required=True, help="Markdown report path to create.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    metrics_dir = Path(args.metrics_dir)
    if not metrics_dir.exists():
        raise FileNotFoundError(f"Metrics directory not found: {metrics_dir}")

    model_metrics = load_json_artifact(metrics_dir / EXPECTED_ARTIFACTS["model_metrics"])
    calibration_report = load_json_artifact(metrics_dir / EXPECTED_ARTIFACTS["calibration_report"])
    final_decision = load_json_artifact(metrics_dir / EXPECTED_ARTIFACTS["final_decision"])

    report = build_artifact_metrics_report(
        model_metrics=model_metrics,
        calibration_report=calibration_report,
        final_decision=final_decision,
    )
    write_markdown_report(report, args.output)


if __name__ == "__main__":
    main()
