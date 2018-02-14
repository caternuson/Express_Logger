# Circuit Playground Express Basic Logger - Count Based
#
# Author: Carter Nelson
# MIT License (https://opensource.org/licenses/MIT)
import time
import random
from adafruit_circuitplayground.express import cpx

# Configure the data logger
LOG_COUNT  = 10    # total points
LOG_RATE   = 0.5   # seconds delay between data collects
LOG_FILE   = 'data.txt'

try:
    # Start logging
    with open("/"+LOG_FILE, "w") as f:
        for _ in range(LOG_COUNT):
            f.write("{}\n".format(random.random()))
            cpx.red_led = not cpx.red_led
            time.sleep(LOG_RATE)
except OSError as e:
    # Something happened with file access
    # Flash LED forever
    while True:
        cpx.red_led = not cpx.red_led
        time.sleep(0.1)
