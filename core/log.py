import logging
import settings


class Log:

    _log: logging = None

    blue = "\x1b[34;20m"
    green = "\x1b[32;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    def __init__(self, name: str):
        self.name = name
        self._log = self._create_python_logger()

    def _create_python_logger(self):
        # create a logger object to have our own log
        logger = logging.getLogger(name=self.name)

        # set the level to the lowest since we want to log everything
        logger.setLevel(logging.DEBUG)

        # the information will go to the console
        console_handler = logging.StreamHandler()
        logger.addHandler(console_handler)

        formatter = self._create_formatter()

        console_handler.setFormatter(formatter)

        return logger

    def _create_formatter(self):

        formatter = logging.Formatter(
            "{asctime} - {levelname} - {message}",
            style="{",
            datefmt=settings.STANDARD_LOG_DATE_FORMAT,
        )

        return formatter

    # public methods
    def debug(self, message: str):
        self._log.log(logging.DEBUG, f'{self.blue}{message}{self.reset}') # pylint: disable=logging-fstring-interpolation

    def info(self, message: str):
        self._log.log(logging.INFO, message)

    def warning(self, message: str):
        self._log.log(logging.WARNING, f'{self.yellow}{message}{self.reset}') # pylint: disable=logging-fstring-interpolation

    def error(self, message: str):
        self._log.log(logging.ERROR, f'{self.red}{message}{self.reset}') # pylint: disable=logging-fstring-interpolation

    def critical(self, message: str):
        self._log.log(logging.CRITICAL, f'{self.bold_red}{message}{self.reset}') # pylint: disable=logging-fstring-interpolation
