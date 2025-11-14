# orangepi-rv2

## Setup Notes

- This setup assumes you're using the Debian image found
  [here](https://romanrm.net/rv-debian), with it flashed onto the eMMC module
- The U-Boot included with the image boots quickly and uses a 's' to interrupt
  the boot process. Manual testing was done to identify the match string that
  the UBootDriver should watch for before sending that interrupt character.
- Includes the same general setup logic as the boardfarm/beagleplay content
  otherwise, although no TFTP functionality will be usable until fitImages are
  generated for the OrangePi RV2 config using meta-riscv.

## Usage

### export

`labgrid-exporter boardfarm/orangepi-rv2/orangepi-rv2-exporter.yaml`

### create a place

`labgrid-client -p bf-orangepi-rv2 create`

### add the resource match

`labgrid-client -p bf-orangepi-rv2 add-match */orangepi-rv2-setup-1/*/*`

### acquire the place

`labgrid-client -p bf-orangepi-rv2 acquire`

### boot it to the default shell (via uboot)

`labgrid-client -c boardfarm/orangepi-rv2/orangepi-rv2-client.yaml -s emmc con`
