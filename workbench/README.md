# workbench

This is a labgrid configuration intended for more manual control on a
developer's desk. Assuming you have modified the exporter configuration file to
correct the match patterns for the serial port and GPIO (and have the right
permissions + udev rules to access them), you can do the following to make use
of it. Note that this also assumes that the labgrid-coordinator is already
running, either on the same machine or elsewhere (in which case `LG_COORDINATOR`
must be set in the environment to point at the hostname):

1. `python3 -m venv venv`
2. `source venv/bin/activate`
3. `pip install --upgrade pip labgrid`
4. Run the exporter with `labgrid-exporter wb-exporter.yaml&`
5. Create a place with `labgrid-client -p workbench create`
6. Add a resource match with `labgrid-client -p workbench add-match */wb-setup/*/*`
7. Acquire the place for use with `labgrid-client -p workbench acquire`

Now you can attach to the console with:

`labgrid-client -p workbench -c workbench/wb-client.yaml con`

And control the power with:

`labgrid-client -p workbench -c workbench/wb-client.yaml pw on|off|cycle|get`
