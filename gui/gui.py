import logging
import queue
import tkinter as tk
from typing import Callable

from gui.analyze import AnalyzeBtn
from gui.color import Color

from gui.console import Console
from gui.start import StartBtn
from gui.textentry import TextEntry
from log.filter import InterceptingLogFilter
from log.queuehandler import QueueHandler


class GUI:
    __CONSOLE_REFRESH_MS = 100

    def __init__(self, root: tk.Tk, logger: logging.Logger):
        self.root = root
        self.logger = logger
        root.configure(bg = Color.WHITE)

        self.on_analyze = lambda text: None
        self.on_start = lambda: None

        self.__create_ui()
        self.__intercept_logging()

        self.root.after(
            self.__CONSOLE_REFRESH_MS,
            self.__log_poll_queue
        )

    def reload(self) -> None:
        self.__create_ui()

    def console_log(self, message: str) -> None:
        self.__access_console(lambda: self.console.insert(tk.END, message + '\n'))

    def console_clear(self) -> None:
        self.__access_console(lambda: self.console.delete('1.0', tk.END))

    def __start_and_disable(self) -> None:
        self.on_start()
        self.start_btn.config(state = tk.DISABLED)

    def __analyze(self) -> None:
        self.console_clear()
        self.on_analyze(self.text_entry.get('1.0', tk.END))

    def __access_console(self, action: Callable = lambda: None):
        self.console.config(state = tk.NORMAL)
        action()
        self.console.config(state = tk.DISABLED)

    def __create_ui(self) -> None:
        self.console = Console.build()
        self.text_entry = TextEntry.build()

        self.analyze_btn = AnalyzeBtn.build(self.root, self.__analyze)
        self.start_btn = StartBtn.build(self.root, self.__start_and_disable)

    def __intercept_logging(self) -> None:
        self.log_queue = queue.Queue()

        self.logger.addHandler(QueueHandler(self.log_queue))
        self.logger.addFilter(InterceptingLogFilter(self.console_log))

    def __log_poll_queue(self) -> None:
        try:
            record = self.log_queue.get(block = False)
        except queue.Empty:
            return
        else:
            self.console_log(record)

        self.root.after(self.__CONSOLE_REFRESH_MS, self.__log_poll_queue())
