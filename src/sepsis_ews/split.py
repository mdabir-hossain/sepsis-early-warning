"""Patient-level split utilities for leakage-safe validation.

Future responsibilities:
- create patient-grouped train/validation/test splits
- wrap GroupKFold-style cross-validation
- assert no patient overlap across splits
- reject row-level random splitting for model evaluation
"""

from collections.abc import Iterable
from typing import Any

from sepsis_ews.placeholders import not_implemented


def _to_patient_id_set(patient_ids: Iterable[Any]) -> set[Any]:
    """Convert common patient-id iterables to a set without requiring pandas."""
    return set(patient_ids)


def assert_no_patient_overlap(train_patient_ids: Iterable[Any], validation_patient_ids: Iterable[Any]) -> None:
    """Raise if any patient ID appears in both train and validation groups."""
    train_ids = _to_patient_id_set(train_patient_ids)
    validation_ids = _to_patient_id_set(validation_patient_ids)
    overlap = train_ids.intersection(validation_ids)

    if overlap:
        overlap_display = ", ".join(str(patient_id) for patient_id in sorted(overlap, key=str))
        raise ValueError(
            "Patient overlap detected between train and validation groups: "
            f"{overlap_display}. Use patient-grouped splitting before evaluation."
        )


def assert_patient_time_sorted(frame: Any, patient_col: str = "patient_id", time_col: str = "iculos") -> None:
    """Raise if time decreases within any patient group.

    The function supports pandas-like frames with ``sort=False`` groupby semantics
    and avoids importing pandas directly, keeping the guard lightweight for tests
    and future pipeline code.
    """
    missing_cols = [column for column in (patient_col, time_col) if column not in frame]
    if missing_cols:
        raise ValueError(f"Missing required columns for temporal ordering check: {missing_cols}")

    for patient_id, patient_frame in frame.groupby(patient_col, sort=False):
        times = list(patient_frame[time_col])
        if any(current_time > next_time for current_time, next_time in zip(times, times[1:])):
            raise ValueError(
                "Time order decreases within patient "
                f"{patient_id!r} for column {time_col!r}. Sort by patient and time before feature engineering."
            )


def make_patient_group_split(config_path: str | None = None) -> None:
    """Create leakage-safe patient-grouped splits in a future phase."""
    not_implemented("Patient-grouped splitting")
