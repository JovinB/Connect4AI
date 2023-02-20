import tkinter as tk
from tkinter import font

from game_logic import *


class Board(tk.Tk):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.title("Connect4")
        self.display = None
        self.buttons = {}

        self.default_img = tk.PhotoImage(file="circle.png")
        self.yellow_img = tk.PhotoImage(file="circle_yellow.png")
        self.red_img = tk.PhotoImage(file="circle_red.png")

        self.create_main_window()
        self.create_board()

    def create_main_window(self):
        main_frame = tk.Frame(master=self)
        main_frame.pack(fill=tk.X)

        self.display = tk.Label(
            master=main_frame,
            text="Good Luck",
            font=font.Font(size=28, weight="bold"),
        )
        self.display.pack()

    def create_board(self):
        board_frame = tk.Frame(master=self)
        board_frame.pack()
        board_frame.config(background="deep sky blue")

        for row in range(6):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(7):
                button = tk.Button(
                    master=board_frame,
                    image=self.default_img,
                    width=100,
                    height=100,
                    borderwidth=0,
                )
                self.buttons[button] = (row, col)
                button.bind("<ButtonPress-1>", self.human_move_played)
                button.grid(
                    row=row,
                    column=col,
                    sticky="nsew"
                )

    def update_button(self, button, colour):
        if colour == "yellow":
            button.config(image=self.yellow_img)
        else:
            button.config(image=self.red_img)

    def update_header(self):
        if self.game.winner == "R":
            self.display["text"] = "You Won!"
            self.display["fg"] = "red"
        elif self.game.winner == "Y":
            self.display["text"] = "You Lost"
            self.display["fg"] = "yellow"
        else:
            self.display["text"] = "Tie Game"
            self.display["fg"] = "black"


    def human_move_played(self, event):
        button = event.widget
        row, col = self.buttons[button]

        if not self.game.game_over and self.game.is_move_valid(row, col):
            self.game.human_move(row, col)
            self.update_button(button, "red")

            if self.game.is_a_winner(row, col, "R"):
                self.game.game_over = True
                self.game.winner = "R"
                self.update_header()

            elif self.game.is_a_tie():
                self.game.game_over = True
                self.game.winner = "T"
                self.update_header()

            else:
                self.ai_move_played()


    def ai_move_played(self):
        move = self.game.ai_move()
        row = move[0]
        col = move[1]

        button = [b for b, coords in self.buttons.items() if coords == (row, col)][0]
        self.update_button(button, "yellow")

        if self.game.is_a_winner(row, col, "Y"):
            self.game.game_over = True
            self.game.winner = "Y"
            self.update_header()

        elif self.game.is_a_tie():
            self.game.game_over = True
            self.game.winner = "T"
            self.update_header()

