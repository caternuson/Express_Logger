# Circuit Playground Express Basic Logger
#
# Author: Carter Nelson
# MIT License (https://opensource.org/licenses/MIT)
import time
from adafruit_circuitplayground.express import cpx

# Configure the data logger
LOG_MODE   = 0    # log based on 0 = LOG_TIME, 1 = LOG_COUNT
LOG_TIME   = 10   # seconds (only used if LOG_MODE = 0)
LOG_COUNT  = 1000 # total points (only used if LOG_MODE = 1)
LOG_RATE   = 0    # seconds delay between data collects
LOG_FILE   = 'data.txt'
LOG_INFO   = 'info.txt'

# NeoPixel status colors
COLORS = {
    'RED'     : ( 10,   0,   0),
    'GREEN'   : (  0,  10,   0),
    'BLUE'    : (  0,   0,  10),
    'BLACK'   : (  0,   0,   0),
}

# Wait for button press
cpx.pixels.fill(COLORS['BLUE'])
while not cpx.button_a and not cpx.button_b:
    pass
cpx.pixels.fill(COLORS['GREEN'])

count = 0
try:
    # Start logging
    with open("/"+LOG_FILE, "w") as f:
        start_time = time.monotonic()
        delta_time = time.monotonic() - start_time
        keep_logging = True
        while  keep_logging:
            # Collect some data
            data = cpx.temperature
            # Write it to the file
            f.write("{},{}\n".format(delta_time, data))
            # Pause
            time.sleep(LOG_RATE)
            # Keep track of how many
            count += 1
            # Keep track of time
            delta_time = time.monotonic() - start_time
            # Should we continue
            if LOG_MODE == 0:
                keep_logging = delta_time < LOG_TIME
            elif LOG_MODE == 1:
                keep_logging = count < LOG_COUNT
            else:
                raise RunTimeError("Unknown log mode {}.".format(LOG_MODE))
    # Write some meta info
    with open("/"+LOG_INFO, "w") as f:
        f.write("Total Points = {}\n".format(count))
        f.write("Total Time = {} secs\n".format(delta_time))
        f.write("Avg. Rate = {} Hz\n".format(count/delta_time))
except OSError as e:
    # Blink NeoPixels to indicate something happened.
    while True:
        cpx.pixels.fill(COLORS['RED'])
        time.sleep(0.5)
        cpx.pixels.fill(COLORS['BLACK'])
        time.sleep(0.5)
# Done. Wait for reset.
cpx.pixels.fill(COLORS['RED'])
while True:
    pass
