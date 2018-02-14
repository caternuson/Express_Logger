# Circuit Playground Express Basic Logger - Wait For Button
#
# Author: Carter Nelson
# MIT License (https://opensource.org/licenses/MIT)
import time
import random
from adafruit_circuitplayground.express import cpx

# Configure the data logger
LOG_TIME   = 5   # seconds (only used if LOG_MODE = 0)
LOG_RATE   = 0.5 # seconds delay between data collects
LOG_FILE   = 'data.txt'

def wait_for_start():
    """Put code here that waits until some form of user input."""
    while not cpx.button_a and not cpx.button_b:
        pass

def heart_beat():
    """Put code here that provides some form of logging indication."""
    cpx.red_led = not cpx.red_led

def get_data():
    """Put code here that collects data and returns it in a tuple."""
    data = (random.random(), random.random())
    return data

def write_data(file, data):
    """Put code here that writes formatted data to file."""
    if len(data) > 1:
        for d in data[:-1]:
            file.write("{},".format(d))
    file.write("{}\n".format(data[-1]))

wait_for_start()
try:
    # Start logging
    with open("/"+LOG_FILE, "w") as f:
        start_time = time.monotonic()
        delta_time = time.monotonic() - start_time
        while  delta_time < LOG_TIME:
            # Write data to file
            write_data(f, get_data())
            # Blink LED
            heart_beat()
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
