import logging


class QueueHandler(logging.Handler):
    """
    Queue handler intended for queuing log messages.

    Queuing and polling are required to facilitate communication between the main thread that is occupied by
    tkinter's GUI and any other worker thread that needs its logging output to be displayed by the GUI.
    """

    def __init__(self, log_queue):
        super().__init__()
        self.log_queue = log_queue

    def emit(self, record):
        self.log_queue.put(record)
