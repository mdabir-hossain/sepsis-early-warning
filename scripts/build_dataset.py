"""Future CLI entry point for building project datasets."""

from __future__ import annotations

import argparse

from sepsis_ews.data import build_dataset


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the sepsis EWS dataset.")
    parser.add_argument("--config", help="Path to a future dataset configuration file.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    build_dataset(config_path=args.config)


if __name__ == "__main__":
    main()
