import tkinter as tk

from gui.color import Color


class TextEntry:

    @staticmethod
    def build():
        text = tk.Text(
            bg = Color.GRAY,
            relief = tk.FLAT,
        )

        text.grid(
            padx = 15,
            pady = 15,
            ipadx = 1,
            ipady = 1,
            row = 1,
            column = 0,
            columnspan = 4,
            sticky = tk.W + tk.E + tk.N + tk.S
        )

        return text
