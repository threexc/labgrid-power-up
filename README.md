# labgrid-power-up
Configs and guides for setting up labgrid-based automation

## Using the Example in the **basic_setup** directory

### Setup

1. `python3 -m venv venv`
2. `source venv/bin/activate`
3. `pip install labgrid`
4. In one shell, do `labgrid-coordinator` to start the coordinator
5. In another shell, do `labgrid-exporter basic_setup/ecogrid-exporter.yaml`
6. In a third shell, do `labgrid-client -v -p beagleplay create`
7. `labgrid-client -p beagleplay add-match */beagleplay/*`
8. `labgrid-client -c basic_setup/ecogrid-client.yaml acquire`

You should now be able to run commands like `labgrid-client -p beagleplay
console` to get the serial console, and `labgrid-client -p beagleplay pw cycle`
to reset the board.

To use the strategy for testing:

1. Run `python3`
2. `from labgrid import Environment`
3. `e = Environment("basic_setup/ecogrid-client.yaml")`
4. `t = e.get_target("main")`
5. `s = t.get_driver("BeagleplayBootStrategy")`

From here you should be able to run commands like `s.transition("off")`
and `s.transition("shell")` to boot with the existing rootfs but the
tftp'd kernel and dtb. The shell script `basic_setup/uboot_test.py`
captures the five steps from above, but adds `s.transition("shell")` at
the end for testing.

**NOTE:** In this case the "environment" we load is the client file
because that's where the drivers are - if we try to load
`ecogrid-exporter.yaml` instead, we'll get an error.

### Transition to a State, With Console

```
labgrid-client -c basic_setup/ecogrid-client.yaml -p beagleplay -s shell -v con
```

## Using the Docker Examples

Under construction

## Using QEMU

Under construction
