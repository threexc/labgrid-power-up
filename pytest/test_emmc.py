import json
import pytest
import re

from labgrid.driver import ExecutionError

def test_tools_available(emmc):
    tools = ['/bin/bash', '/usr/bin/ls']
    missing = []

    for tool in tools:
        stdout, stderr, code = emmc.run(f"test -x {tool}")

        if code != 0:
            missing.append(tool)

    assert(missing == [])

def test_uname_a(emmc):
    try:
        state = emmc.run_check('/usr/bin/uname -a', timeout=60.0)

        assert("6.12.13-ti" in state[0])
    except ExecutionError:
        emmc.run('ls /usr/bin/uname')
        raise
