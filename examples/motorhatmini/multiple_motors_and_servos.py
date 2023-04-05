import time
import math
from inventorhatmini import MotorHATMini

"""
Demonstrates how to control all of the servos on Inventor HAT Mini.
"""

# Create a new InventorHATMini
board = MotorHATMini()

# Enable all servos (this puts them at the middle)
for m in board.motors:
    m.enable()
for s in board.servos:
    s.enable()
time.sleep(2)

# Go to min
for m in board.motors:
    m.full_positive()
for s in board.servos:
    s.to_min()
time.sleep(2)

for m in board.motors:
    m.stop()
for s in board.servos:
    s.to_mid()
time.sleep(2)

# Go to max
for m in board.motors:
    m.full_negative()
for s in board.servos:
    s.to_max()
time.sleep(2)

# Go back to mid
for m in board.motors:
    m.coast()
for s in board.servos:
    s.to_mid()
time.sleep(2)

SWEEPS = 3              # How many sweeps of the servo to perform
STEPS = 10              # The number of discrete sweep steps
STEPS_INTERVAL = 0.5    # The time in seconds between each step of the sequence
SPEED_EXTENT = 1.0      # How far from zero to drive the motors when sweeping
SWEEP_EXTENT = 70.0     # How far from zero to move the servo when sweeping

# Do a sine sweep
for j in range(SWEEPS):
    for i in range(360):
        speed = math.sin(math.radians(i)) * SPEED_EXTENT
        for m in board.motors:
            m.speed(speed)
        value = math.sin(math.radians(i)) * SWEEP_EXTENT
        for s in board.servos:
            s.value(value)
        time.sleep(0.02)

# Do a stepped sweep
for j in range(SWEEPS):
    for i in range(0, STEPS):
        for m in board.motors:
            m.to_percent(i, 0, STEPS, 0.0 - SPEED_EXTENT, SPEED_EXTENT)
        for s in board.servos:
            s.to_percent(i, 0, STEPS, 0.0 - SWEEP_EXTENT, SWEEP_EXTENT)
        time.sleep(STEPS_INTERVAL)
    for i in range(0, STEPS):
        for m in board.motors:
            m.to_percent(i, STEPS, 0, 0.0 - SPEED_EXTENT, SPEED_EXTENT)
        for s in board.servos:
            s.to_percent(i, STEPS, 0, 0.0 - SWEEP_EXTENT, SWEEP_EXTENT)
        time.sleep(STEPS_INTERVAL)

# Disable the servos
for m in board.motors:
    m.disable()
for s in board.servos:
    s.disable()
