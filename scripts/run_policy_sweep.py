"""Future CLI entry point for alert-policy threshold sweeps."""

from __future__ import annotations

import argparse

from sepsis_ews.policies import run_policy_sweep


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run sepsis EWS alert-policy sweeps.")
    parser.add_argument("--config", help="Path to a future policy sweep configuration file.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    run_policy_sweep(config_path=args.config)


if __name__ == "__main__":
    main()
