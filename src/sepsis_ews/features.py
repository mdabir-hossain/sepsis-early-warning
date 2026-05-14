"""Temporal feature engineering boundaries for patient time-series data.

Future responsibilities:
- create patient-grouped rolling-window features
- enforce feature allowlists and leakage blocklists
- save feature manifests with clear provenance
- ensure features use past and current observations only
"""

from collections.abc import Sequence

from sepsis_ews.placeholders import not_implemented

BLOCKED_FEATURE_PATTERNS: tuple[str, ...] = (
    "SepsisLabel",
    "event_iculos",
    "use_row",
    "future_",
    "target_",
    "label_",
    "sepsis_time",
    "onset_time",
)


def find_blocked_feature_names(feature_names: Sequence[str]) -> list[str]:
    """Return feature names that look target-derived or future-derived.

    Matching is case-insensitive and intentionally conservative. It catches exact
    risky fields as well as derived names such as ``SepsisLabel__miss`` or
    ``future_lactate_mean``. The function only reports names; it never drops
    columns silently.
    """
    blocked_patterns = tuple(pattern.casefold() for pattern in BLOCKED_FEATURE_PATTERNS)
    blocked_names: list[str] = []

    for feature_name in feature_names:
        normalized_name = str(feature_name).casefold()
        if any(pattern in normalized_name for pattern in blocked_patterns):
            blocked_names.append(str(feature_name))

    return blocked_names


def validate_feature_names(feature_names: Sequence[str]) -> None:
    """Raise if any feature names appear target-derived or future-derived."""
    blocked_names = find_blocked_feature_names(feature_names)
    if blocked_names:
        blocked_display = ", ".join(blocked_names)
        raise ValueError(
            "Blocked target/future-derived feature names detected: "
            f"{blocked_display}. Review feature engineering before training."
        )


def build_features(config_path: str | None = None) -> None:
    """Build temporal features from future configured inputs."""
    not_implemented("Feature engineering")
