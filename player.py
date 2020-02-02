import board

class Players:
    def __init__(self, symbol, position, is_turn, board):
        self.name = ""
        self.symbol = ""
        self.position = position
        self.is_turn = is_turn
        self.type = ""
        self.board = board

    def set_name(self, name):
        self.name = name

    def set_symbol(self, symbol):
        self.symbol = symbol

    def set_position(self, position, symbol, type):
        game_board = board.Board()
        game_board.set_board(position, symbol)
        game_board.is_position_valid(position)
        self.type = type
        print("?")

