import pytest
import re
import traceback

@pytest.fixture(scope='module')
def my_tftp(strategy, target):
    try:
        strategy.transition('shell')
    except Exception as e:
        traceback.print_exc()
        pytest.exit(f"Transition into tftp boot shell failed: {e}", returncode=3)

    return target.get_driver('ShellDriver')
