import json
import pytest
import re

from labgrid.driver import ExecutionError

def test_tools_available(tftp):
    tools = ['/bin/bash', '/usr/bin/ls']
    missing = []

    for tool in tools:
        stdout, stderr, code = tftp.run(f"test -x {tool}")

        if code != 0:
            missing.append(tool)

    assert(missing == [])

def test_uname_a(tftp):
    try:
        state = tftp.run_check('/usr/bin/uname -a', timeout=60.0)

        assert("6.16.0" in state[0])
    except ExecutionError:
        tftp.run('ls /usr/bin/uname')
        raise
