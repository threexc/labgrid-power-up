#!/bin/bash

cd ~/workspace/zephyrproject
source .venv/bin/activate
cd zephyr
west build -p always -b nucleo_f446ze samples/basic/blinky
west flash --runner openocd
deactivate
