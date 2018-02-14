
# Circuit Playground Express Acceleration Logger
#
# Author: Carter Nelson
# MIT License (https://opensource.org/licenses/MIT)
import time
from adafruit_circuitplayground.express import cpx

TOTAL_TIME = 10  # seconds
COLORS = {
    'RED'     : ( 80,   0,   0),
    'GREEN'   : (  0,  80,   0),
    'BLUE'    : (  0,   0,  80),
    'BLACK'   : (  0,   0,   0),
}

count = 0

try:
    cpx.pixels.fill(COLORS['BLUE'])
    # Wait for button press
    while not cpx.button_a and not cpx.button_b:
        pass
    cpx.pixels.fill(COLORS['GREEN'])
    # Start logging
    with open("/data.txt", "w") as f:
        start_time = time.monotonic()
        delta_time = time.monotonic() - start_time
        while  < TOTAL_TIME:
            x, y, z = cpx.acceleration
            f.write("{},{},{},{}\n".format(delta_time, x, y, z))
            count += 1
            delta_time = time.monotonic() - start_time
    with open("/info.txt", "w") as f:
        f.write("Total Points = {}\n".format(count))
        f.write("Total Time = {} secs\n".format(current_time - start_time))
        f.write("Avg. Rate = {} Hz\n".format(count/(current_time - start_time)))
    cpx.pixels.fill(COLORS['RED'])
    while True:
        pass
except OSError as e:
    # Blink NeoPixels to indicate something happened.
    while True:
        cpx.pixels.fill(COLORS['RED'])
        time.sleep(0.5)
        cpx.pixels.fill(COLORS['BLACK'])
        time.sleep(0.5)
