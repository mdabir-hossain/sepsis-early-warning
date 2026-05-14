"""Future CLI entry point for model and policy evaluation."""

from __future__ import annotations

import argparse

from sepsis_ews.evaluate import evaluate_model


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Evaluate sepsis EWS model outputs.")
    parser.add_argument("--config", help="Path to a future evaluation configuration file.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    evaluate_model(config_path=args.config)


if __name__ == "__main__":
    main()
