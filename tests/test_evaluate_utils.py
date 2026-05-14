import pytest

from sepsis_ews.evaluate import safe_rate, validate_binary_labels, validate_probability_values


def test_safe_rate_computes_fraction() -> None:
    assert safe_rate(1, 2) == 0.5


def test_safe_rate_rejects_zero_denominator() -> None:
    with pytest.raises(ValueError, match="denominator"):
        safe_rate(1, 0)


def test_validate_probability_values_accepts_valid_values() -> None:
    validate_probability_values([0, 0.25, 1.0])


def test_validate_probability_values_rejects_out_of_range_values() -> None:
    with pytest.raises(ValueError, match="within \\[0, 1\\]"):
        validate_probability_values([0.1, 1.2])


def test_validate_binary_labels_accepts_binary_values() -> None:
    validate_binary_labels([0, 1, 1, 0])


def test_validate_binary_labels_rejects_non_binary_values() -> None:
    with pytest.raises(ValueError, match="0 or 1"):
        validate_binary_labels([0, 2, 1])
