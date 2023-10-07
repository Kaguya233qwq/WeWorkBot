import sys
import time

import ntwork

from .fuctions.config import load_config


def forever():
    try:
        load_config()
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        ntwork.exit_()
        sys.exit()
