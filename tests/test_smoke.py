# NOTE: This test is intentionally minimal.
#
# funbattle's top-level package and its `battles` / `battles.datafountain`
# packages all have empty __init__.py files, so importing them has no
# side effects. Deeper submodules (e.g. `battles.datafountain.bt557`)
# are competition-specific scratch code and are not exercised here.
import funbattle
import funbattle.battles
import funbattle.battles.datafountain


def test_import_funbattle():
    assert funbattle is not None


def test_import_funbattle_battles():
    assert funbattle.battles is not None


def test_import_funbattle_battles_datafountain():
    assert funbattle.battles.datafountain is not None
