import pytest
import re
import traceback

import pathlib

def pytest_configure(config):
    if not config.getoption("--lg-env", default=None):
        env = (pathlib.Path(__file__).parent.parent / "client.yaml").resolve()
        config.option.lg_env = str(env)

    config.addinivalue_line("markers", "orangepi-rv2: orangepi-rv2 specific tests")


@pytest.fixture(scope='module')
def tftp(strategy, target):
    try:
        strategy.transition('tftp')
    except Exception as e:
        traceback.print_exc()
        pytest.exit(f"Transition into tftp boot shell failed: {e}", returncode=3)

    return target.get_driver('ShellDriver')
