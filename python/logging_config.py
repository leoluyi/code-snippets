__ALL__ = ['ConsoleHandler', 'LogFileHandler', 'get_logger_console_file']

import logging
from logging import StreamHandler
from logging.handlers import TimedRotatingFileHandler
import sys
from pathlib import Path

LOG_FORMATTER = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s')


class LogFileHandler(TimedRotatingFileHandler):
    """docstring for LogFile"""

    def __init__(
            self, log_file, when='midnight', interval=1,
            backupCount=30, atTime=None):
        """
        Arguments:
            log_file {[type]} -- File path for logging output.

        Keyword Arguments:
            when {str} -- Argument passed to logging.handlers.TimedRotatingFileHandler (default: {'midnight'})
            interval {number} -- Argument passed to logging.handlers.TimedRotatingFileHandler (default: {1})
            backupCount {number} -- Argument passed to logging.handlers.TimedRotatingFileHandler (default: {30})
            atTime {[type]} -- Argument passed to logging.handlers.TimedRotatingFileHandler (default: {None})

        Details:

            One could use the folowing as `atTime` setting:

            ```
            from datetime import time
            import pytz

            time(0, 0, 0, tzinfo=pytz.timezone('ROC')))
            ```
        """

        # Ensure log folder existst
        log_file = Path(log_file).resolve()
        log_file.parent.mkdir(parents=True, exist_ok=True)

        super().__init__(
            log_file,
            when=when, interval=interval, backupCount=backupCount, encoding='utf-8',
            atTime=atTime
        )

        self.setFormatter(LOG_FORMATTER)


class ConsoleHandler(StreamHandler):
    def __init__(self, stream=sys.stdout):
        super().__init__(stream)
        self.setFormatter(LOG_FORMATTER)


def register_console_file_handler(logger, log_file, level=logging.DEBUG):

    logger.setLevel(level)  # better to have too much log than not enough

    logger.addHandler(ConsoleHandler())
    logger.addHandler(LogFileHandler(log_file))

    # with this pattern, it's rarely necessary to propagate the error up to parent
    logger.propagate = False

    return None


if __name__ == '__main__':
    LOG_FILE = 'log/my_app.log'

    default_logger = logging.getLogger(__name__)
    register_console_file_handler(default_logger, LOG_FILE)

    # with this pattern, it's rarely necessary to propagate the error up to parent
    default_logger.propagate = False
