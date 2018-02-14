# Circuit Playground Express Basic Logger - Wait For Button
#
# Author: Carter Nelson
# MIT License (https://opensource.org/licenses/MIT)
import time
import random
from adafruit_circuitplayground.express import cpx

# Configure the data logger
LOG_TIME   = 5   # seconds total
LOG_RATE   = 0.5 # seconds delay between data collects
LOG_FILE   = 'data.txt'

# Wait for button press
while not cpx.button_a and not cpx.button_b:
    pass

try:
    # Start logging
    with open("/"+LOG_FILE, "w") as f:
        start_time = time.monotonic()
        delta_time = time.monotonic() - start_time
        while  delta_time < LOG_TIME:
            # Write data to file
            f.write("{}\n".format(random.random()))
            # Blink LED
            cpx.red_led = not cpx.red_led
            # Pause
            time.sleep(LOG_RATE)
            # Keep track of time
            delta_time = time.monotonic() - start_time
except OSError as e:
    # Something happened with file access
    # Flash LED forever
    while True:
        cpx.red_led = not cpx.red_led
        time.sleep(0.1)
