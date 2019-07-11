__ALL__ = ['log_console', 'LogFileHandler']

import logging
import logging.handlers
import sys
from pathlib import Path
from datetime import time
# import pytz

log_formatter = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s')
log_console = logging.StreamHandler(sys.stdout)
log_console.setFormatter(log_formatter)


class LogFileHandler(logging.handlers.TimedRotatingFileHandler):
    """docstring for LogFile"""

    def __init__(
            self, log_file, when='midnight', interval=1, backupCount=30,
            atTime=time(
                0, 0, 0,
                # tzinfo=pytz.timezone('ROC')
            )):

        # Ensure log folder existst
        log_file = Path(log_file).resolve()
        log_file.parent.mkdir(parents=True, exist_ok=True)

        super().__init__(
            log_file,
            when=when, interval=interval, backupCount=backupCount, encoding='utf-8',
            atTime=atTime
        )

        self.setFormatter(log_formatter)
