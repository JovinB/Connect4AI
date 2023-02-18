import random

class Game:
    def __init__(self):
        self.player_turn = True
        self.num_rows = 6
        self.num_columns = 7
        self.board = []
        self.setup_board()

    def setup_board(self):
        self.board = [["" for i in range(self.num_columns)] for j in range(self.num_rows)]

    def is_move_valid(self, row, col):
        if self.board[row][col] == "":
            return True
        return False

    def player_move(self, row, col):
        if self.is_move_valid(row, col):
            self.board[row][col] = "R"
            self.ai_move()

    def ai_move(self):
        row = random.randint(0, self.num_rows - 1)
        col = random.randint(0, self.num_columns - 1)

        while True:
            if self.is_move_valid(row, col):
                break
            else:
                row = random.randint(0, self.num_rows - 1)
                col = random.randint(0, self.num_columns - 1)

        self.board[row][col] = "Y"
        # update game screen


    def print_info(self):
        print(self.board)


game = Game()
game.print_info()
