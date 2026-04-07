# muse-pi-pro

## Usage

### export

`labgrid-exporter boardfarm/muse-pi-pro/muse-pi-pro-exporter.yaml`

### create a place

`labgrid-client -p bf-muse-pi-pro create`

### add the resource match

`labgrid-client -p bf-muse-pi-pro add-match */muse-pi-pro-setup-1/*/*`

### acquire the place

`labgrid-client -p bf-muse-pi-pro acquire`

### boot it to the default shell (via uboot)

`labgrid-client -c boardfarm/muse-pi-pro/muse-pi-pro-client.yaml -s emmc con`
