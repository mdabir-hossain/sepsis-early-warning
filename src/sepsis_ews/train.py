"""Model training boundaries for the sepsis EWS project.

Future responsibilities:
- define baseline and stronger model pipelines
- train with patient-grouped validation
- generate out-of-fold predictions
- save model metadata without exposing raw data
"""

from sepsis_ews.placeholders import not_implemented


def train_model(config_path: str | None = None) -> None:
    """Train a model from a future configuration file."""
    not_implemented("Model training")
