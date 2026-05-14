import pytest

from sepsis_ews.features import find_blocked_feature_names, validate_feature_names


def test_safe_feature_names_pass() -> None:
    validate_feature_names(["HR_mean_6", "lactate_delta_12", "age", "iculos"])


def test_blocked_exact_names_fail() -> None:
    blocked = find_blocked_feature_names(["HR_mean_6", "SepsisLabel", "event_iculos", "use_row"])

    assert blocked == ["SepsisLabel", "event_iculos", "use_row"]


def test_blocked_derived_names_fail() -> None:
    feature_names = [
        "SepsisLabel__miss",
        "event_iculos__miss",
        "future_lactate_mean",
        "target_score_rolling",
    ]

    with pytest.raises(ValueError, match="Blocked target/future-derived feature names"):
        validate_feature_names(feature_names)


def test_blocked_detection_is_case_insensitive() -> None:
    blocked = find_blocked_feature_names(["sepsislabel__MISS", "FUTURE_lactate_mean"])

    assert blocked == ["sepsislabel__MISS", "FUTURE_lactate_mean"]
