import sys
import time

import ntwork

from .fuctions.config import load_config
from .utils.loader import load_plugins_from_local


def forever():
    try:
        load_config()
        load_plugins_from_local()
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        ntwork.exit_()
        sys.exit()
