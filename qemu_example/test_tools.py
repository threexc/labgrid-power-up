import json
import pytest
import re

from labgrid.driver import ShellDriver, SSHDriver, ExecutionError

def test_tools_available(default_shell: ShellDriver) -> None:
    tools = ['/bin/bash', '/bin/ls']
    missing = []

    for tool in tools:
        stdout, stderr, code = default_shell.run(f"test -x {tool}")

        if code != 0:
            missing.append(tool)

    assert(missing == [])

def test_uname_a(default_shell: ShellDriver) -> None:
    try:
        state = default_shell.run_check('/bin/uname -a', timeout=60.0)

        assert("6.16" in state[0])
    except ExecutionError:
        default_shell.run('ls /bin/uname')
        raise
