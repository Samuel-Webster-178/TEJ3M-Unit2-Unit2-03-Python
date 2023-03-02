#!/usr/bin/env python3

# Created by Samuel Webster
# Created on Feb 2023

import time
import board
from digitalio import DigitalInOut, Direction

# LED setup for onboard LED
led = DigitalInOut(board.GP13)
led.direction = Direction.OUTPUT

while True:
    led.value = not led.value
    time.sleep(1)
