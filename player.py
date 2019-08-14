class Player:
    def __init__(self, color, turn):
        self.color = color
        self.turn = turn    # boolean
        self.pieces_on_board = []   # list of pieces
        self.blocked_spaces = []
        self.in_check = False
        self.checkmate = False

    def start_turn(self):
        if self.turn is False:
            self.turn = True

    def end_turn(self):
        self.turn = False

    def get_pieces_on_board(self):
        return self.pieces_on_board
