import logging
from typing import Callable


class InterceptingLogFilter(logging.Filter):
    """Intercepts log records and passes them to the provided callback"""

    def __init__(self, on_intercept: Callable):
        super().__init__()
        self.on_intercept = on_intercept

    def filter(self, record) -> bool:
        self.on_intercept(record.getMessage())

        return True
