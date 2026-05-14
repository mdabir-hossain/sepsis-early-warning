"""Alert-policy simulation boundaries for sepsis early-warning analysis.

Future responsibilities:
- apply threshold and lockout policies to calibrated probabilities
- estimate alert burden, detection rate, and lead time
- support retrospective policy sweeps without clinical deployment claims
"""

from sepsis_ews.placeholders import not_implemented


def run_policy_sweep(config_path: str | None = None) -> None:
    """Run alert-policy sweeps from a future configuration file."""
    not_implemented("Policy sweep")
