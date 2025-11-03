# labgrid-power-up
Configs and guides for setting up labgrid-based automation

## basic_setup

Files used for my talk co-presented with Tim Orling at Open Source Summit Europe
2025 in Amsterdam. Watch the talk
[here](https://www.youtube.com/watch?v=_QQmoT5rQOA).

These files may no longer be totally in-sync with the content provided in the
presentation (in an attempt to make them easier to understand and use by
others), but they should be close.

## boardfarm

Configuration files for boards and devices in my boardfarm, meant mostly for
automated testing.

## docker_example

A simple set of examples for using docker with labgrid, similar to the ones
upstream.

## helper_scripts

Scripts that help make use of labgrid. Right now, the only one is an example of
how to use the Python interpreter to manually control a labgrid environment and
transition to a 'shell' state.

## qemu_example

Similar to docker_example, this consists of some files to show how QEMU could be
used with the Yocto Project. A much more extensive example can be found in
Joschka Seydell's [talk](https://www.youtube.com/watch?v=FVUEJnYgbxY) and
[repository](https://github.com/JSydll/emulated-yocto-linux-testing.git).

## udev

Some udev configuration files I've used for enabling usage of gpios and BayLibre
Copilot devices.

## workbench

Configuration files for devices on my workbench, meant for more of a hands-on,
manual control flow.
