import pytest
import re
import traceback

@pytest.fixture(scope='module')
def emmc(strategy, target):
    try:
        strategy.transition('emmc')
    except Exception as e:
        traceback.print_exc()
        pytest.exit(f"Transition into emmc boot shell failed: {e}", returncode=3)

    return target.get_driver('ShellDriver')

@pytest.fixture(scope='module')
def tftp(strategy, target):
    try:
        strategy.transition('tftp')
    except Exception as e:
        traceback.print_exc()
        pytest.exit(f"Transition into tftp boot shell failed: {e}", returncode=3)

    return target.get_driver('ShellDriver')
