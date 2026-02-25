import pytest
from labgrid.strategy import Strategy
from labgrid.driver import ShellDriver


@pytest.fixture(scope="session")
def strategy(target):
    """Get the strategy from the target.

    'target' is a built-in fixture provided by labgrid's pytest plugin
    when using --lg-env. No need to create Environment ourselves.
    """
    for driver in target.drivers:
        if isinstance(driver, Strategy):
            return driver
    raise RuntimeError("No strategy driver found on target")


@pytest.fixture(scope="session")
def boot_to_shell(target, strategy):
    """Boot the system and return the shell driver."""
    strategy.transition("shell")
    return target.get_driver(ShellDriver)


@pytest.fixture(scope="session")
def command(boot_to_shell, cmd_timeout=30):
    """Convenience fixture for running commands."""
    def _run(cmd, timeout=cmd_timeout):
        return boot_to_shell.run(cmd, timeout=timeout)
    return _run
