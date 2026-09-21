from importlib import import_module

import pytest

PUBLIC_MODULES = (
    "funbattle",
    "funbattle.battles",
    "funbattle.battles.datafountain",
    "funbattle.battles.datafountain.bt557",
    "funbattle.battles.datafountain.bt557.evalution",
    "funbattle.battles.datafountain.bt557.model",
    "funbattle.battles.datafountain.bt557.utils",
)


@pytest.mark.parametrize("module_name", PUBLIC_MODULES)
def test_import_public_module(module_name):
    assert import_module(module_name).__name__ == module_name


def test_missing_competition_module_is_not_silently_provided():
    with pytest.raises(ModuleNotFoundError):
        import_module("funbattle.battles.missing_competition")
