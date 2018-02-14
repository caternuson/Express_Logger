# Feather M0 Express Basic Logger
#
# Author: Carter Nelson
# MIT License (https://opensource.org/licenses/MIT)
import time
import random

# Configure the data logger
LOG_COUNT  = 60   # total points (only used if LOG_MODE = 1)
LOG_RATE   = 10   # seconds delay between data collects
LOG_FILE   = 'data.txt'

try:
    # Start logging
    with open("/"+LOG_FILE, "w") as f:
        for _ in range(LOG_COUNT):
            f.write("{}\n".format(random.random()))
            time.sleep(LOG_RATE)

except OSError as e:
    # Something happened with file access
    pass
