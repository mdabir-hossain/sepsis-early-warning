import pytest

from sepsis_ews.metadata import build_run_metadata


def _valid_metadata_kwargs() -> dict[str, object]:
    return {
        "project_name": "sepsis-early-warning",
        "run_name": "artifact-report",
        "data_version": "existing-artifacts",
        "feature_schema_version": "not-rerun",
        "model_family": "hgb",
        "calibrator": "isotonic",
        "policy": "A_first_crossing_lockout",
        "threshold": 0.085,
        "lockout_hours": 6,
        "metrics_provenance": "existing saved artifacts",
        "created_at_utc": "2026-05-14T00:00:00+00:00",
    }


def test_build_run_metadata_contains_required_fields() -> None:
    metadata = build_run_metadata(**_valid_metadata_kwargs())

    assert metadata["project_name"] == "sepsis-early-warning"
    assert metadata["model_family"] == "hgb"
    assert metadata["created_at_utc"] == "2026-05-14T00:00:00+00:00"


def test_build_run_metadata_rejects_missing_required_field() -> None:
    kwargs = _valid_metadata_kwargs()
    kwargs["model_family"] = ""

    with pytest.raises(ValueError, match="model_family"):
        build_run_metadata(**kwargs)


def test_build_run_metadata_does_not_fabricate_metrics_by_default() -> None:
    metadata = build_run_metadata(**_valid_metadata_kwargs())

    assert "metrics" not in metadata
