import tkinter as tk
from tkinter import font

from game_logic import *


class Board(tk.Tk):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.title("Connect4")

    def create_main_window(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=display_frame,
            text="Ready?",
            font=font.Font(size=28, weight="bold"),
        )
        self.display.pack()