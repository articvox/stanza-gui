import logging
from typing import Callable


class InterceptingLogFilter(logging.Filter):
    """
    Filter that is intended for intercepting log messages and passing them to the provided callback method.
    """

    def __init__(self, on_intercept: Callable):
        super().__init__()
        self.on_intercept = on_intercept

    def filter(self, record) -> bool:
        self.on_intercept(record.getMessage())

        return True
