import enum

import attr
import time

import boardfarm_common.helpers as helpers

from labgrid.factory import target_factory
from labgrid.strategy.common import Strategy, StrategyError


class Status(enum.Enum):
    unknown = 0
    off = 1
    uboot = 2
    emmc = 3
    tftp = 4


@target_factory.reg_driver
@attr.s(eq=False)
class MusePiProBootStrategy(Strategy):
    """MusePiProBootStrategy - Strategy to switch to uboot or shell"""
    bindings = {
        "power": "PowerProtocol",
        "console": "ConsoleProtocol",
        "uboot": "UBootDriver",
        "shell": "ShellDriver",
        "tftp": "TFTPProviderDriver",
    }

    status = attr.ib(default=Status.unknown)

    def __attrs_post_init__(self):
        super().__attrs_post_init__()
        self.staged = False

    def _stage(self):
        helpers.uboot_stage(self)

    def transition(self, status):
        if not isinstance(status, Status):
            status = Status[status]
        if status == Status.unknown:
            raise StrategyError(f"can not transition to {status}")
        elif status == self.status:
            return # nothing to do
        elif status == Status.off:
            self.target.deactivate(self.console)
            self.target.activate(self.power)
            self.power.off()
        elif status == Status.uboot:
            self.transition(Status.off)
            self.target.activate(self.console)
            # cycle power
            self.power.cycle()
            # interrupt uboot
            self.target.activate(self.uboot)
            self._stage()
        elif status == Status.emmc:
            # transition to uboot
            self.transition(Status.uboot)
            self.uboot.boot("emmc")
            self.uboot.await_boot()
            self.target.activate(self.shell)
        elif status == Status.tftp:
            # transition to uboot
            self.transition(Status.uboot)
            helpers.uboot_set_server_ip(self)
            helpers.uboot_set_bootargs(self)
            helpers.uboot_tftpboot_file(self, "$kernel_addr_r", "muse-pi-pro", "Image")
            helpers.uboot_tftpboot_file(self, "$dtb_addr", "muse-pi-pro", "k1-musepi-pro.dtb")
            self.uboot.boot("tftp")
            self.uboot.await_boot()
            self.target.activate(self.shell)
        else:
            raise StrategyError(f"no transition found from {self.status} to {status}")
        self.status = status

    def force(self, status):
        if not isinstance(status, Status):
            status = Status[status]
        if status == Status.off:
            self.target.activate(self.power)
        elif status == Status.uboot:
            self.target.activate(self.uboot)
        elif status == Status.emmc:
            self.target.activate(self.shell)
        elif status == Status.tftp:
            self.target.activate(self.shell)
        else:
            raise StrategyError("can not force state {}".format(status))
        self.status = status

