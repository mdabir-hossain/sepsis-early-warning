"""Evaluation boundaries for model and alert-policy reporting.

Future responsibilities:
- compute classification, calibration, and alert-policy metrics
- distinguish cross-validation, OOF, validation, and holdout results
- produce report-ready metric tables with provenance
"""

from collections.abc import Iterable
from numbers import Real

from sepsis_ews.placeholders import not_implemented


def safe_rate(numerator: Real, denominator: Real) -> float:
    """Return numerator / denominator, raising clearly for invalid denominators."""
    if denominator == 0:
        raise ValueError("Cannot compute rate with denominator equal to zero.")
    return float(numerator) / float(denominator)


def validate_probability_values(values: Iterable[Real]) -> None:
    """Raise if any probability is outside the inclusive [0, 1] range."""
    invalid_values = [value for value in values if value < 0 or value > 1]
    if invalid_values:
        raise ValueError(f"Probability values must be within [0, 1]. Invalid values: {invalid_values}")


def validate_binary_labels(values: Iterable[object]) -> None:
    """Raise if labels contain values other than 0 or 1."""
    invalid_values = [value for value in values if value not in (0, 1)]
    if invalid_values:
        raise ValueError(f"Binary labels must contain only 0 or 1. Invalid values: {invalid_values}")


def evaluate_model(config_path: str | None = None) -> None:
    """Evaluate model and policy outputs in a future phase."""
    not_implemented("Model evaluation")
