import shutil
import enum
import attr
from labgrid.step import step
from labgrid.strategy import Strategy, StrategyError
from labgrid.factory import target_factory


class Status(enum.Enum):
    unknown = 0
    off = 1
    booting = 2
    shell = 3

@target_factory.reg_driver
@attr.s(eq=False)
class QEMUYoctoStrategy(Strategy):
    bindings = {
        "qemu_driver": "QEMUDriver",
        "shell": "ShellDriver",
    }

    status = attr.ib(default=Status.unknown)

    @step(title="transition")
    def transition(self, status):
        if not isinstance(status, Status):
            status = Status[status]

        if status == Status.off:
            if self.status == Status.shell:
                self.target.deactivate(self.shell)
                self.qemu_driver.off()
                self.target.deactivate(self.qemu_driver)
            self.status = Status.off

        elif status == Status.shell:
            if self.status == Status.shell:
                return
            if self.status == Status.booting:
                raise StrategyError(
                    "Cannot go to shell directly from booting; turn off first."
                )

            self.target.activate(self.qemu_driver)
            self.qemu_driver.on()
            self.status = Status.booting

            self.target.activate(self.shell)
            self.status = Status.shell

        else:
            raise StrategyError(f"Unknown status {status}")
