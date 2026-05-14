"""Inference boundaries for future demonstration workflows.

Future responsibilities:
- load a saved model bundle when one exists
- score public-safe sample rows
- expose prediction outputs for a future demo without clinical claims
"""

from sepsis_ews.placeholders import not_implemented


def predict(config_path: str | None = None) -> None:
    """Run future sample inference once a model bundle exists."""
    not_implemented("Inference")
