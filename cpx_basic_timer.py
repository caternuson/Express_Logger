# Circuit Playground Express Basic Logger - Time Based
#
# Author: Carter Nelson
# MIT License (https://opensource.org/licenses/MIT)
import time
import random
from adafruit_circuitplayground.express import cpx

# Configure the data logger
LOG_TIME   = 5     # seconds total
LOG_RATE   = 0.5   # seconds delay between data collects
LOG_FILE   = 'data.txt'

try:
    # Start logging
    with open("/"+LOG_FILE, "w") as f:
        start_time = time.monotonic()
        delta_time = time.monotonic() - start_time
        while delta_time < LOG_TIME:
            f.write("{}\n".format(random.random()))
            cpx.red_led = not cpx.red_led
            time.sleep(LOG_RATE)
            delta_time = time.monotonic() - start_time
except OSError as e:
    # Something happened with file access
    # Flash LED forever
    while True:
        cpx.red_led = not cpx.red_led
        time.sleep(0.1)
