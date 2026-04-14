# bananapi-f3

## Usage

### export

`labgrid-exporter boardfarm/bananapi-f3/exporter.yaml`

### create a place

`labgrid-client -p bf-bananapi-f3 create`

### add the resource match

`labgrid-client -p bf-bananapi-f3 add-match */bananapi-f3-setup-1/*/*`

### acquire the place

`labgrid-client -p bf-bananapi-f3 acquire`

### boot it to the default shell (via uboot)

`labgrid-client -c boardfarm/bananapi-f3/client.yaml -s emmc con`
