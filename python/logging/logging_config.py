__ALL__ = ["ConsoleHandler", "LogFileHandler", "get_logger_console_file"]

import logging
import logging.handlers
import sys
from pathlib import Path

LOG_FORMATTER = logging.Formatter("[%(asctime)s][%(levelname)s] %(message)s")


class LogFileHandler(logging.handlers.TimedRotatingFileHandler):
    def __init__(
        self, log_file, when="midnight", interval=1, backupCount=30, atTime=None
    ):
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
            when=when,
            interval=interval,
            backupCount=backupCount,
            encoding="utf-8",
            atTime=atTime,
        )

        self.setFormatter(LOG_FORMATTER)


class LessThanFilter(logging.Filter):
    """
    Log higher level to stderr.
    https://stackoverflow.com/a/31459386/3744499
    """

    def __init__(self, exclusive_maximum, name=""):
        super(LessThanFilter, self).__init__(name)
        self.max_level = exclusive_maximum

    def filter(self, record):
        # non-zero return means we log this message
        return 1 if record.levelno < self.max_level else 0


class ConsoleHandler(logging.StreamHandler):
    def __init__(self, stream=sys.stdout):
        super().__init__(stream)
        self.setFormatter(LOG_FORMATTER)


def register_console_file_handler(logger, log_file, level=logging.DEBUG):
    logger.setLevel(level)  # better to have too much log than not enough

    logging_handler_out = ConsoleHandler(sys.stdout)
    logging_handler_out.setLevel(logging.DEBUG)
    logging_handler_out.addFilter(LessThanFilter(logging.WARNING))

    logging_handler_err = ConsoleHandler(sys.stderr)
    logging_handler_err.setLevel(logging.WARNING)
    logger.addHandler(logging_handler_err)

    logger.addHandler(logging_handler_out)
    logger.addHandler(logging_handler_err)
    logger.addHandler(LogFileHandler(log_file))

    # with this pattern, it's rarely necessary to propagate the error up to parent
    logger.propagate = False

    return None


if __name__ == "__main__":
    LOG_FILE = "log/my_app.log"

    default_logger = logging.getLogger(__name__)
    register_console_file_handler(default_logger, LOG_FILE)
    default_logger.warning("hihi ---------------")
