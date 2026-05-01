# Helper functions for the boardfarm's test suites and strategies

default_bootargs = (
    "$bootargs "
    "console=ttyS0,115200n8 "
    "root=/dev/nfs "
    "rw "
    "nfsroot=$serverip:/srv/nfs3/rv2_1,nfsvers=3,tcp "
    "ip=dhcp "
    "rootdelay=5"
)

default_serverip = "192.168.40.134"

def uboot_stage(strategy):
    if strategy.staged:
        return
    strategy.target.activate(strategy.tftp)

    for name, image in strategy.target.env.config.get_images().items():
        if name.startswith('tftp-'):
            strategy.tftp.stage(image)

    strategy.target.deactivate(strategy.tftp)   
    strategy.staged = True

def uboot_set_server_ip(strategy, serverip=default_serverip):
    tftpdir = strategy.tftp.get_export_vars()['internal']
    strategy.uboot.run(f"setenv autoload no")
    try:
        strategy.uboot.run(f"dhcp", timeout=10)
    except Exception as e:
        strategy.uboot.run(f"dhcp")
    
    strategy.uboot.run(f"setenv serverip {serverip}")

def uboot_set_bootargs(strategy, bootargs=default_bootargs):
    strategy.uboot.run(f"setenv bootargs {bootargs}")
    strategy.uboot.run(f" echo $bootargs")

def uboot_tftpboot_file(strategy, loadaddr, board_name, file_name):
    strategy.uboot.run(f"tftpboot {loadaddr} {board_name}/{file_name}")
    strategy.uboot.run(f"tftpboot $kernel_addr_r orangepi-rv2/Image")
    strategy.uboot.run(f"tftpboot $fdt_addr_r orangepi-rv2/k1-orangepi-rv2.dtb")
