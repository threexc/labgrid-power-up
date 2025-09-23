# qemu_example

This is an example of how labgrid could be used to approximate a boot-and-test
flow for an image built with the Yocto Project. More specifically, it was tested
with a recent build from the `master` branch with the following customizations:

- `MACHINE = "qemuriscv64"` in local.conf
- `meta/conf/distro/include/ptest-packagelists.inc` modified to remove `python3`
  from the slow lists (so that you can do `bitbake core-image-ptest-python3` for
  that MACHINE)

The parameters entered in the QEMUDriver definition were captured by running
`runqemu nographic snapshot` and saving the output of the underlying call to
`qemu-system-riscv64`, then hard-coding the networking details for simplicity
(so it may fail to start if the specified tap device is already in use).

It assumes you've run the build and copied the following files to the current
directory:

1. core-image-ptest-python3.rootfs.ext4
2. fw_jump.elf
3. uImage

To run it:

1. python3 -m venv venv
2. source venv/bin/activate
3. pip install labgrid
4. labgrid-client -p qemuriscv64 create
5. labgrid-client -p qemuriscv64 acquire
6. pytest
