"""Future CLI entry point for model training."""

from __future__ import annotations

import argparse

from sepsis_ews.train import train_model


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train a sepsis EWS model.")
    parser.add_argument("--config", help="Path to a future model training configuration file.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    train_model(config_path=args.config)


if __name__ == "__main__":
    main()
