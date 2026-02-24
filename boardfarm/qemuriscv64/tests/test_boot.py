class TestBoot:
    def test_system_booted(self, command):
        stdout, stderr, rc = command("echo hello")
        assert rc == 0
        assert "hello" in stdout

    def test_kernel_version(self, command):
        stdout, stderr, rc = command("uname -r")
        assert rc == 0
        assert len(stdout) > 0
        print(f"Kernel version: {stdout[0]}")

    def test_architecture(self, command):
        stdout, stderr, rc = command("uname -m")
        assert rc == 0
        assert "riscv64" in stdout[0]
