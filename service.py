#!/usr/bin/python2.7
from hosted import device

while True:
  device.gpio.setup_pin(26, direction="out")
  time.sleep(1)
  device.gpio.set_pin_value(26, high=True)
  time.sleep(1)
