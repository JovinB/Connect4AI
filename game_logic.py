import random


class Game:
    def __init__(self):
        # self.human_turn = True
        self.num_rows = 6
        self.num_columns = 7
        self.board = []
        self.setup_board()
        self.game_over = False
        self.winner = ""

    def setup_board(self):
        self.board = [["" for i in range(self.num_columns)] for j in range(self.num_rows)]

    def is_move_valid(self, row, col):
        if self.board[row][col] == "":
            return True
        return False

    def is_a_tie(self):
        for row in range(self.num_rows):
            for col in range(self.num_columns):
                if self.board[row][col] == "":
                    return False
        return True

    def is_a_winner(self, row, col, player_colour):
        # check for horizontal 4 in a row
        if self.check_for_row_winner(row, player_colour):
            return True

        # check for vertical 4 in a row
        if self.check_for_col_winner(col, player_colour):
            return True

        # check for diagonal 4 in a row
        if self.check_for_diagonal_winner(row, col, player_colour):
            return True

        return False

    def check_for_row_winner(self, row, player_colour):
        player_pieces_count = 0
        for col in range(self.num_columns):
            if self.board[row][col] == player_colour:
                if player_pieces_count == 3:
                    return True
                player_pieces_count += 1
            else:
                player_pieces_count = 0
        return False

    def check_for_col_winner(self, col, player_colour):
        player_pieces_count = 0
        for row in range(self.num_rows):
            if self.board[row][col] == player_colour:
                if player_pieces_count == 3:
                    return True
                player_pieces_count += 1
            else:
                player_pieces_count = 0
        return False

    def check_for_diagonal_winner(self, row, col, player_colour):
        og_row = row
        og_col = col

        # start at the top-most and left-most spot that is on the same diagonal as the most recent move
        while True:
            if row - 1 >= 0 and col - 1 >= 0:
                row -= 1
                col -= 1
            else:
                break

        player_pieces_count = 0
        while row < self.num_rows and col < self.num_columns:
            if self.board[row][col] == player_colour:
                if player_pieces_count == 3:
                    return True
                player_pieces_count += 1
                row += 1
                col += 1
            else:
                player_pieces_count = 0
                row += 1
                col += 1

        # start at the top-most and right-most spot that is on the same diagonal as the most recent move
        row = og_row
        col = og_col
        while True:
            if row - 1 >= 0 and col + 1 < self.num_columns:
                row -= 1
                col += 1
            else:
                break

        player_pieces_count = 0
        while row < self.num_rows and col >= 0:
            if self.board[row][col] == player_colour:
                if player_pieces_count == 3:
                    return True
                player_pieces_count += 1
                row += 1
                col -= 1
            else:
                player_pieces_count = 0
                row += 1
                col -= 1
        return False

    def human_move(self, row, col):
        if self.is_move_valid(row, col) and not self.game_over:
            self.board[row][col] = "R"
            # update UI

            if self.is_a_winner(row, col, "R"):
                self.game_over = True
                self.winner = "R"
            elif self.is_a_tie():
                self.game_over = True
                self.winner = "T"
            else:
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
        # update UI

        if self.is_a_winner(row, col, "Y"):
            self.game_over = True
            self.winner = "Y"
        elif self.is_a_tie():
            self.game_over = True
            self.winner = "T"

    def reset_game(self):
        self.setup_board()
        self.game_over = False
        self.winner = ""

    def print_info(self):
        print(self.board)
