import tkinter as tk

from gui.color import Color


class Console:

    @staticmethod
    def build():
        text = tk.Text(
            bg = Color.BLACK,
            fg = Color.WHITE,
            relief = tk.FLAT,
        )

        text.grid(
            padx = 15,
            pady = 15,
            ipadx = 1,
            ipady = 1,
            row = 1,
            rowspan = 2,
            column = 5,
            columnspan = 4,
            sticky = tk.E + tk.W + tk.N + tk.S
        )

        return text
