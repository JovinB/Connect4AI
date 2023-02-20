import tkinter as tk
from tkinter import font

from game_logic import *


class Board(tk.Tk):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.title("Connect4")
        self.display = None
        self.create_main_window()
        self.create_board()

    def create_main_window(self):
        main_frame = tk.Frame(master=self)
        main_frame.pack(fill=tk.X)
        """
        self.display = tk.Label(
            master=main_frame,
            # text="Ready?",
            # font=font.Font(size=28, weight="bold"),
        )
        self.display.pack()
        """

    def create_board(self):
        global button_image

        board_frame = tk.Frame(master=self)
        board_frame.pack()
        board_frame.config(background="deep sky blue")

        button_image = tk.PhotoImage(file="circle.png")

        for row in range(6):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(7):
                button = tk.Button(
                    master=board_frame,
                    image=button_image,
                    width=100,
                    height=100,
                    borderwidth=0,
                )
                # self.tiles[button] = (row, col)
                # button.bind("<ButtonPress-1>", self.play)
                button.grid(
                    row=row,
                    column=col,
                    sticky="nsew"
                )

