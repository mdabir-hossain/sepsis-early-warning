import importlib

import pytest


MODULE_NAMES = [
    "sepsis_ews.calibrate",
    "sepsis_ews.data",
    "sepsis_ews.evaluate",
    "sepsis_ews.explain",
    "sepsis_ews.features",
    "sepsis_ews.inference",
    "sepsis_ews.metadata",
    "sepsis_ews.policies",
    "sepsis_ews.reporting",
    "sepsis_ews.split",
    "sepsis_ews.train",
]


def test_core_modules_import() -> None:
    for module_name in MODULE_NAMES:
        importlib.import_module(module_name)


@pytest.mark.parametrize(
    ("module_name", "function_name"),
    [
        ("sepsis_ews.calibrate", "calibrate_model"),
        ("sepsis_ews.data", "build_dataset"),
        ("sepsis_ews.evaluate", "evaluate_model"),
        ("sepsis_ews.explain", "explain_model"),
        ("sepsis_ews.features", "build_features"),
        ("sepsis_ews.inference", "predict"),
        ("sepsis_ews.policies", "run_policy_sweep"),
        ("sepsis_ews.split", "make_patient_group_split"),
        ("sepsis_ews.train", "train_model"),
    ],
)
def test_placeholder_functions_fail_clearly(module_name: str, function_name: str) -> None:
    module = importlib.import_module(module_name)
    function = getattr(module, function_name)

    with pytest.raises(NotImplementedError, match="not implemented yet"):
        function(config_path=None)
