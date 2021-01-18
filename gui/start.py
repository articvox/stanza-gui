from typing import Callable
import tkinter as tk

from gui.color import Color


class StartBtn:

    @staticmethod
    def build(root, on_click: Callable):
        button = tk.Button(
            root,
            text = "START NLP",
            command = on_click,
            bg = Color.BLUE,
            fg = Color.WHITE,
            bd = 2,
            relief = tk.FLAT
        )
        button.grid(
            padx = 15,
            pady = 15,
            ipadx = 24,
            ipady = 6,
            row = 2,
            column = 0,
            columnspan = 2,
            sticky = tk.W + tk.E + tk.N + tk.S
        )
        return button
