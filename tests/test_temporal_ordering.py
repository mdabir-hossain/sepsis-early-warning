import pytest

from sepsis_ews.split import assert_patient_time_sorted


pd = pytest.importorskip("pandas")


def test_patient_time_sorted_passes() -> None:
    frame = pd.DataFrame(
        {
            "patient_id": ["p1", "p1", "p2", "p2"],
            "iculos": [1, 2, 1, 3],
        }
    )

    assert_patient_time_sorted(frame)


def test_decreasing_patient_time_raises_value_error() -> None:
    frame = pd.DataFrame(
        {
            "patient_id": ["p1", "p1", "p2", "p2"],
            "iculos": [2, 1, 1, 3],
        }
    )

    with pytest.raises(ValueError, match="Time order decreases"):
        assert_patient_time_sorted(frame)
