# systemd services

These are designed to be run as a normal user, and located in
`~/.config/systemd/user/`. Once they are placed, they can be enabled with e.g.:

1. `systemctl --user enable labgrid-coordinator.service`
2. `systemctl --user start labgrid-coordinator.service`
