"""Data loading and dataset assembly boundaries for the sepsis EWS project.

Future responsibilities:
- locate raw PhysioNet-style patient files from configured paths
- parse pipe-separated patient time-series files
- write public-safe intermediate datasets
- avoid hardcoded local paths and avoid committing raw clinical data
"""

from sepsis_ews.placeholders import not_implemented


def build_dataset(config_path: str | None = None) -> None:
    """Build the analysis dataset from a future configuration file."""
    not_implemented("Dataset building")
