# labgrid-power-up
Configs and guides for setting up labgrid-based automation

## Using the basic_setup Example

1. `git clone https://github.com/labgrid-project/labgrid.git`
2. `cd labgrid`
3. `python3 -m venv venv`
4. `source venv/bin/activate`
5. `pip install .`
6. In one shell, do `labgrid-coordinator` to start the coordinator
7. In another shell, do `labgrid-exporter ecogrid-env.yaml`
8. In a third shell, do `labgrid-client -v -p bp create`
9. `labgrid-client -p bp add-match */beagleplay/*`
10. `labgrid-client -c ecogrid-client.yaml acquire`

You should now be able to run commands like `labgrid-client -p bp
console` to get the serial console, and `labgrid-client -p bp pw cycle`
to reset the board.
