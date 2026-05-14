import pytest

from sepsis_ews.split import assert_no_patient_overlap


def test_no_patient_overlap_passes() -> None:
    assert_no_patient_overlap(["p1", "p2"], ["p3", "p4"])


def test_patient_overlap_raises_value_error() -> None:
    with pytest.raises(ValueError, match="Patient overlap detected"):
        assert_no_patient_overlap(["p1", "p2"], ["p2", "p3"])


def test_empty_patient_groups_are_handled() -> None:
    assert_no_patient_overlap([], [])
    assert_no_patient_overlap(["p1"], [])
    assert_no_patient_overlap(set(), {"p2"})
