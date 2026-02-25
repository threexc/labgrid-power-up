class TestPtests:
    def test_system_booted(self, command):
        stdout, stderr, rc = command("echo hello")
        assert rc == 0
        assert "hello" in stdout

    def test_kernel_version(self, command):
        stdout, stderr, rc = command("uname -r")
        assert rc == 0
        assert len(stdout) > 0
        print(f"Kernel version: {stdout[0]}")

    def test_ptests(self, command):
        stdout, stderr, rc = command("ptest-runner", 1200)
        assert rc == 0
