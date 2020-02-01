import time

class Board:
    def __init__(self):
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.is_board_full = ""

    def init_board(self):
        print("Welcome to Tic-Tac-Toe game:")
        time.sleep(2)
        print("| 1 | 2 | 3 |")
        print("| 4 | 5 | 6 |")
        print("| 7 | 8 | 9 |")
        print("Please take 5 seconds to study board locations...")
        time.sleep(5)
        print("| - | - | - |")
        print("| - | - | - |")
        print("| - | - | - |")
        time.sleep(1)
        print("OK, now lets play :)")


    def display_board(self, board_list):
        print("|" + self.board[0][0] + "|" + self.board[0][1] + "|" + self.board[0][2] + "|")
        print("|" + self.board[1][0] + "|" + self.board[1][1] + "|" + self.board[1][2] + "|")
        print("|" + self.board[2][0] + "|" + self.board[2][1] + "|" + self.board[2][2] + "|")

    def position_converter(self, position):
        if position == 1:
            return self.board[0][0]
        elif position == 2:
            return self.board[0][1]
        elif position == 3:
            return self.board[0][2]
        elif position == 4:
            return self.board[1][0]
        elif position == 5:
            return self.board[1][1]
        elif position == 6:
            return self.board[1][2]
        elif position == 7:
            return self.board[2][0]
        elif position == 8:
            return self.board[2][1]
        elif position == 9:
            return self.board[2][2]

    def is_position_valid(self, position):
        if self.position_converter(position) == '-':
            return True
        else:
            return False

    def set_board(self, position, symbol):
        board_position = self.position_converter(position)
        board_position = symbol

    def check_rows(self):
        if self.board[0][0] == self.board[0][1] == self.board[0][2] and self.board[0][0] != '-':
            winner_symbol = self.board[0][0]
            return winner_symbol
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] and self.board[1][0] != '-':
            winner_symbol = self.board[1][0]
            return winner_symbol
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] and self.board[2][0] != '-':
            winner_symbol = self.board[2][0]
            return winner_symbol
        else:
            return False

    def check_columns(self):
        if self.board[0][0] == self.board[1][0] == self.board[2][0] and self.board[0][0] != '-':
            winner_symbol = self.board[0][0]
            return winner_symbol
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] and self.board[0][1] != '-':
            winner_symbol = self.board[0][1]
            return winner_symbol
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] and self.board[0][2] != '-':
            winner_symbol = self.board[0][2]
            return winner_symbol
        else:
            return False

    def check_diagonals(self):
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != '-':
            winner_symbol = self.board[0][0]
            return winner_symbol
        elif self.board[0][2] == self.board[1][0] == self.board[2][0] and self.board[0][2] != '-':
            winner_symbol = self.board[0][2]
            return winner_symbol
        else:
            return False

    def check_sequence(self):
        if self.check_rows() != False:
            return self.check_rows()
        elif self.check_columns() != False:
            return self.check_columns()
        elif self.check_diagonals() != False:
            return self.check_diagonals()
        else:
            return False

    def check_full_board(self):
        if '-' in self.board[0]:
            self.is_board_full = False
        elif '-' in self.board[1]:
            self.is_board_full = False
        elif '-' in self.board[2]:
            self.is_board_full = False
        else:
            self.is_board_full = True

