"""Run metadata helpers for artifact-derived reporting.

These helpers record caller-provided run information only. They do not inspect
raw data, infer model performance, or fabricate metric values.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

REQUIRED_METADATA_FIELDS: tuple[str, ...] = (
    "project_name",
    "run_name",
    "data_version",
    "feature_schema_version",
    "model_family",
    "calibrator",
    "policy",
    "threshold",
    "lockout_hours",
    "metrics_provenance",
)


def _require_non_empty(field_name: str, value: Any) -> None:
    if value is None or value == "":
        raise ValueError(f"Missing required metadata field: {field_name}")


def build_run_metadata(
    *,
    project_name: str,
    run_name: str,
    data_version: str,
    feature_schema_version: str,
    model_family: str,
    calibrator: str,
    policy: str,
    threshold: float,
    lockout_hours: int,
    metrics_provenance: str,
    notes: str | None = None,
    created_at_utc: str | None = None,
) -> dict[str, Any]:
    """Build explicit run metadata from caller-provided values."""
    values = {
        "project_name": project_name,
        "run_name": run_name,
        "data_version": data_version,
        "feature_schema_version": feature_schema_version,
        "model_family": model_family,
        "calibrator": calibrator,
        "policy": policy,
        "threshold": threshold,
        "lockout_hours": lockout_hours,
        "metrics_provenance": metrics_provenance,
    }
    for field_name in REQUIRED_METADATA_FIELDS:
        _require_non_empty(field_name, values[field_name])

    if not isinstance(threshold, int | float):
        raise ValueError("threshold must be numeric and caller-provided.")
    if not isinstance(lockout_hours, int):
        raise ValueError("lockout_hours must be an integer number of hours.")

    return {
        **values,
        "created_at_utc": created_at_utc or datetime.now(timezone.utc).isoformat(),
        "notes": notes or "",
    }
