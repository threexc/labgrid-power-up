import json
import pytest
import re
import os

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
    version = os.environ.get("VERSION")
    try:
        state = emmc.run_check('/usr/bin/uname -a', timeout=60.0)

        assert(version in state[0])
    except ExecutionError:
        emmc.run('ls /usr/bin/uname')
        raise
