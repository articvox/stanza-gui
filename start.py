import logging
import tkinter as tk

from gui.gui import GUI
from nlp.nlphandler import NLPHandler


def start():
    logger = logging.getLogger('stanza')
    nlp_handler = NLPHandler(logger)

    gui_root = tk.Tk()
    gui_root.resizable(0, 0)

    app = GUI(gui_root, logger)
    app.on_start = nlp_handler.start
    app.on_analyze = nlp_handler.process

    gui_root.mainloop()


if __name__ == '__main__':
    start()
