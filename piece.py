board_map_alpha_to_index = {"a": 0, "b": 1, "c": 2, "d": 3,
                            "e": 4, "f": 5, "g": 6, "h": 7}

board_map_index_to_alpha = {0: "a", 1: "b", 2: "c", 3: "d",
                            4: "e", 5: "f", 6: "g", 7: "h"}

piece_key_to_name = {"x": "King", "X": "King", "q": "Queen", "Q": "Queen",
                     "r": "Rook", "R": "Rook", "b": "Bishop", "B": "Bishop",
                     "k": "Knight", "K": "Knight", "p": "Pawn", "P": "Pawn"}


class Piece:
    def __init__(self, key, color):
        self.key = key
        self.color = color

    def get_moves(self, position, board):
        pass

    def get_key(self):
        return self.key

    def get_color(self):
        return self.color

    def no_jumping(self, from_square, to_square, color, board):
        pass


class King(Piece):

    is_in_check = False

    def get_moves(self, position, board):
        file, rank = list(position.strip().lower())
        rank = int(rank)
        file = board_map_alpha_to_index[file]
        i, j = rank, file
        available_moves = []

        try:
            temp = board[i + 1][j]
            available_moves.append([i + 1, j])
        except:
            pass
        try:
            temp = board[i - 1][j]
            available_moves.append([i - 1, j])
        except:
            pass
        try:
            temp = board[i][j - 1]
            available_moves.append([i, j - 1])
        except:
            pass
        try:
            temp = board[i][j + 1]
            available_moves.append([i, j + 1])
        except:
            pass
        try:
            temp = board[i - 1][j - 1]
            available_moves.append([i - 1, j - 1])
        except:
            pass
        try:
            temp = board[i + 1][j + 1]
            available_moves.append([i + 1, j + 1])
        except:
            pass
        try:
            temp = board[i + 1][j - 1]
            available_moves.append([i + 1, j - 1])
        except:
            pass
        try:
            temp = board[i - 1][j + 1]
            available_moves.append([i - 1, j + 1])
        except:
            pass

        # filter negative values
        temp = [i for i in available_moves if i[0] >= 0 and i[1] >= 0]
        all_available_moves = ["".join([board_map_index_to_alpha[i[1]],
                                        str(i[0])]) for i in temp]
        all_available_moves.sort()
        return all_available_moves

    def no_jumping(self, from_square, to_square, color, board):
        blocked_spaces = []

        return blocked_spaces


class Queen(Piece):
    def get_moves(self, position, board):
        file, rank = list(position.strip().lower())
        rank = int(rank)
        file = board_map_alpha_to_index[file]
        available_moves = []

        # Vertical and horizontal
        for j in range(8):
            if j != file:
                try:
                    available_moves.append((rank, j))
                except:
                    pass

        for i in range(8):
            if i != rank:
                try:
                    available_moves.append((i, file))
                except:
                    pass

        # Diagonal
        for i, j in zip(range(rank + 1, 8, 1), range(file + 1, 8, 1)):
            try:
                available_moves.append((i, j))
            except:
                pass

        for i, j in zip(range(rank + 1, 8, 1), range(file - 1, 0 + -1, -1)):
            try:
                available_moves.append((i, j))
            except:
                pass

        for i, j in zip(range(rank - 1, 0 + -1, -1), range(file + 1, 8, 1)):
            try:
                available_moves.append((i, j))
            except:
                pass

        for i, j in zip(range(rank - 1, 0 + -1, -1), range(file - 1, 0 + -1, -1)):
            try:
                available_moves.append((i, j))
            except:
                pass

        # filter negative values
        temp = [i for i in available_moves if i[0] >= 0 and i[1] >= 0]
        all_available_moves = ["".join([board_map_index_to_alpha[i[1]],
                                        str(i[0])]) for i in temp]
        all_available_moves.sort()
        return all_available_moves


    def no_jumping(self, from_square, to_square, color, board):
        blocked = False
        blocked_spaces = []
        # get rank and file of current and target positions
        this_file, this_rank = list(from_square.strip().lower())
        this_rank = int(this_rank)
        this_color = color  # color of current piece
        target_file, target_rank = list(to_square.strip().lower())
        target_rank = int(target_rank)

        # Horizontals:
        # ==============================================================
        if this_rank == target_rank:
            if target_file > this_file:  # LEFT ====================================================================
                for i in range(board_map_alpha_to_index[this_file] + 1, board_map_alpha_to_index[target_file] + 1):
                    if blocked is True:
                        blocked_spaces.append(board_map_index_to_alpha[i] + str(this_rank))
                    elif (board[i][this_rank] != 0) and (board[i][this_rank].color == this_color):
                        blocked = True  # position is blocked by a friendly piece
                        position = (board_map_index_to_alpha[i]) + str(this_rank)
                        blocked_spaces.append(position)
                    elif (board[i][this_rank] != 0) and (board[i][this_rank].color != this_color):
                        # positions behind are blocked, but target can be captured
                        blocked = True
            else:  # RIGHT ===================================================================
                for i in reversed(range(board_map_alpha_to_index[target_file],
                                        board_map_alpha_to_index[this_file])):
                    if blocked is True:
                        blocked_spaces.append(board_map_index_to_alpha[i] + str(this_rank))
                    elif (board[i][this_rank] != 0) and (board[i][this_rank].color == this_color):
                        blocked = True  # position is blocked by a friendly piece
                        position = (board_map_index_to_alpha[i]) + str(this_rank)
                        blocked_spaces.append(position)
                    elif (board[i][this_rank] != 0) and (board[i][this_rank].color != this_color):
                        # positions behind are blocked, but target can be captured
                        blocked = True
        # Verticals:
        # ==============================================================
        if this_file == target_file:
            if target_rank > this_rank:  # DOWN ====================================================================
                for i in range(this_rank + 1, target_rank + 1):
                    if blocked is True:
                        blocked_spaces.append(this_file + str(i))
                    elif (board[board_map_alpha_to_index[this_file]][i] != 0) and \
                            (board[board_map_alpha_to_index[this_file]][i].color == this_color):
                        blocked = True  # position is blocked by a friendly piece
                        position = this_file + str(i)
                        blocked_spaces.append(position)
                    elif (board[board_map_alpha_to_index[this_file]][i] != 0) and \
                            (board[board_map_alpha_to_index[this_file]][i].color != this_color):
                        # positions behind are blocked, but target can be captured
                        blocked = True
            else:  # UP =======================================================================
                for i in reversed(range(target_rank, this_rank)):
                    if blocked is True:
                        blocked_spaces.append(this_file + str(i))
                    elif (board[board_map_alpha_to_index[this_file]][i] != 0) and \
                            (board[board_map_alpha_to_index[this_file]][i].color == this_color):
                        blocked = True  # position is blocked by a friendly piece
                        position = this_file + str(i)
                        blocked_spaces.append(position)
                    elif (board[board_map_alpha_to_index[this_file]][i] != 0) and \
                            (board[board_map_alpha_to_index[this_file]][i].color != this_color):
                        blocked = True  # positions behind are blocked, but target can be captured
        # Diagonals:
        # ==============================================================
        elif (target_rank < this_rank) and (
                board_map_alpha_to_index[target_file] > board_map_alpha_to_index[this_file]):
            # UP-RIGHT =====================================================================================
            j = board_map_alpha_to_index[this_file] + 1
            for i in range(this_rank - 1, target_rank - 1, -1):
                if blocked is True:
                    blocked_spaces.append(board_map_index_to_alpha[j] + str(i))
                elif (board[j][i] != 0) and (board[j][i].color == this_color):
                    blocked = True  # position is blocked by a friendly piece
                    blocked_spaces.append(board_map_index_to_alpha[j] + str(i))
                elif (board[j][i] != 0) and (board[j][i].color != this_color):
                    blocked = True  # positions behind are blocked, but target can be captured
                j += 1

        elif (target_rank < this_rank) and \
                (board_map_alpha_to_index[target_file] < board_map_alpha_to_index[this_file]):
            # UP-LEFT ======================================================================================
            j = board_map_alpha_to_index[this_file] - 1
            for i in range(this_rank - 1, target_rank - 1, -1):
                if blocked is True:
                    blocked_spaces.append(board_map_index_to_alpha[j] + str(i))
                elif (board[j][i] != 0) and (board[j][i].color == this_color):
                    blocked = True  # position is blocked by a friendly piece
                    blocked_spaces.append(board_map_index_to_alpha[j] + str(i))
                elif (board[j][i] != 0) and (board[j][i].color != this_color):
                    blocked = True  # positions behind are blocked, but target can be captured
                j -= 1

            # DOWN-RIGHT ===================================================================================
        elif (target_rank > this_rank) and board_map_alpha_to_index[target_file] > board_map_alpha_to_index[this_file]:
            j = board_map_alpha_to_index[this_file] + 1
            for i in range(this_rank + 1, target_rank + 1):
                if blocked is True:
                    blocked_spaces.append(board_map_index_to_alpha[j] + str(i))
                elif (board[j][i] != 0) and (board[j][i].color == this_color):
                    blocked = True  # position is blocked by a friendly piece
                    blocked_spaces.append(board_map_index_to_alpha[j] + str(i))
                elif (board[j][i] != 0) and (board[j][i].color != this_color):
                    blocked = True  # positions behind are blocked, but target can be captured
                j += 1

            # DOWN-LEFT ====================================================================================
        elif (target_rank > this_rank) and board_map_alpha_to_index[target_file] < board_map_alpha_to_index[this_file]:
            j = board_map_alpha_to_index[this_file] - 1
            for i in range(this_rank + 1, target_rank + 1):
                if blocked is True:
                    blocked_spaces.append(board_map_index_to_alpha[j] + str(i))
                elif (board[j][i] != 0) and (board[j][i].color == this_color):
                    blocked = True  # position is blocked by a friendly piece
                    blocked_spaces.append(board_map_index_to_alpha[j] + str(i))
                elif (board[j][i] != 0) and (board[j][i].color != this_color):
                    blocked = True  # positions behind are blocked, but target can be captured
                j -= 1

        return blocked_spaces


class Rook(Piece):
    def get_moves(self, position, board):
        file, rank = list(position.strip().lower())
        rank = int(rank)
        file = board_map_alpha_to_index[file]
        available_moves = []

        # rank moves
        for j in range(8):
            if j != file:
                try:
                    available_moves.append((rank, j))
                except:
                    pass

        # file moves
        for i in range(8):
            if i != rank:
                try:
                    available_moves.append((i, file))
                except:
                    pass

        available_moves = ["".join([board_map_index_to_alpha[i[1]],
                                    str(i[0])]) for i in available_moves]
        available_moves.sort()

        return available_moves

    def no_jumping(self, from_square, to_square, color, board):
        blocked = False
        blocked_spaces = []
        # get rank and file of current and target positions
        this_file, this_rank = list(from_square.strip().lower())
        this_rank = int(this_rank)
        this_color = color  # color of current piece
        target_file, target_rank = list(to_square.strip().lower())
        target_rank = int(target_rank)

        # Horizontals:
        # ==============================================================
        if this_rank == target_rank:
            if target_file > this_file:  # LEFT ====================================================================
                for i in range(board_map_alpha_to_index[this_file] + 1, board_map_alpha_to_index[target_file] + 1):
                    if blocked is True:
                        blocked_spaces.append(board_map_index_to_alpha[i] + str(this_rank))
                    elif (board[i][this_rank] != 0) and (board[i][this_rank].color == this_color):
                        blocked = True   # position is blocked by a friendly piece
                        position = (board_map_index_to_alpha[i]) + str(this_rank)
                        blocked_spaces.append(position)
                    elif (board[i][this_rank] != 0) and (board[i][this_rank].color != this_color):
                        # positions behind are blocked, but target can be captured
                        blocked = True
            else:                        # RIGHT ===================================================================
                for i in reversed(range(board_map_alpha_to_index[target_file],
                                        board_map_alpha_to_index[this_file])):
                    if blocked is True:
                        blocked_spaces.append(board_map_index_to_alpha[i] + str(this_rank))
                    elif (board[i][this_rank] != 0) and (board[i][this_rank].color == this_color):
                        blocked = True   # position is blocked by a friendly piece
                        position = (board_map_index_to_alpha[i]) + str(this_rank)
                        blocked_spaces.append(position)
                    elif (board[i][this_rank] != 0) and (board[i][this_rank].color != this_color):
                        # positions behind are blocked, but target can be captured
                        blocked = True
        # Verticals:
        # ==============================================================
        if this_file == target_file:
            if target_rank > this_rank:  # DOWN ====================================================================
                for i in range(this_rank + 1, target_rank + 1):
                    if blocked is True:
                        blocked_spaces.append(this_file + str(i))
                    elif (board[board_map_alpha_to_index[this_file]][i] != 0) and \
                            (board[board_map_alpha_to_index[this_file]][i].color == this_color):
                        blocked = True  # position is blocked by a friendly piece
                        position = this_file + str(i)
                        blocked_spaces.append(position)
                    elif (board[board_map_alpha_to_index[this_file]][i] != 0) and \
                            (board[board_map_alpha_to_index[this_file]][i].color != this_color):
                        # positions behind are blocked, but target can be captured
                        blocked = True
            else:                       # UP =======================================================================
                for i in reversed(range(target_rank, this_rank)):
                    if blocked is True:
                        blocked_spaces.append(this_file + str(i))
                    elif (board[board_map_alpha_to_index[this_file]][i] != 0) and \
                            (board[board_map_alpha_to_index[this_file]][i].color == this_color):
                        blocked = True  # position is blocked by a friendly piece
                        position = this_file + str(i)
                        blocked_spaces.append(position)
                    elif (board[board_map_alpha_to_index[this_file]][i] != 0) and \
                            (board[board_map_alpha_to_index[this_file]][i].color != this_color):
                        blocked = True  # positions behind are blocked, but target can be captured

        return blocked_spaces


class Bishop(Piece):
    def get_moves(self, position, board):
        file, rank = list(position.strip().lower())
        rank = int(rank)
        file = board_map_alpha_to_index[file]
        available_moves = []

        for i, j in zip(range(rank + 1, 8, 1), range(file + 1, 8, 1)):
            try:  # (+rank, +file)
                available_moves.append((i, j))
            except:
                pass

        for i, j in zip(range(rank + 1, 8, 1), range(file - 1, 0 + -1, -1)):
            try:  # (+rank, -file)
                available_moves.append((i, j))
            except:
                pass

        for i, j in zip(range(rank - 1, 0 + -1, -1), range(file + 1, 8, 1)):
            try:  # (-rank, +file)
                available_moves.append((i, j))
            except:
                pass

        for i, j in zip(range(rank - 1, 0 + -1, -1), range(file - 1, 0 + -1, -1)):
            try:  # (-rank, -file)
                available_moves.append((i, j))
            except:
                pass

        available_moves = ["".join([board_map_index_to_alpha[i[1]],
                                    str(i[0])]) for i in available_moves]
        available_moves.sort()

        return available_moves

    def no_jumping(self, from_square, to_square, color, board):
        blocked = False
        blocked_spaces = []
        # get rank and file of current and target positions
        this_file, this_rank = list(from_square.strip().lower())
        this_rank = int(this_rank)
        this_color = color  # color of current piece
        target_file, target_rank = list(to_square.strip().lower())
        target_rank = int(target_rank)

        # Diagonals:
        # ==============================================================
        if (target_rank < this_rank) and (board_map_alpha_to_index[target_file] > board_map_alpha_to_index[this_file]):
            # UP-RIGHT =====================================================================================
            j = board_map_alpha_to_index[this_file] + 1
            for i in range(this_rank - 1, target_rank - 1, -1):
                if blocked is True:
                    blocked_spaces.append(board_map_index_to_alpha[j] + str(i))
                elif (board[j][i] != 0) and (board[j][i].color == this_color):
                    blocked = True  # position is blocked by a friendly piece
                    blocked_spaces.append(board_map_index_to_alpha[j] + str(i))
                elif (board[j][i] != 0) and (board[j][i].color != this_color):
                    blocked = True  # positions behind are blocked, but target can be captured
                j += 1

        elif (target_rank < this_rank) and \
                (board_map_alpha_to_index[target_file] < board_map_alpha_to_index[this_file]):
            # UP-LEFT ======================================================================================
            j = board_map_alpha_to_index[this_file] - 1
            for i in range(this_rank - 1, target_rank - 1, -1):
                if blocked is True:
                    blocked_spaces.append(board_map_index_to_alpha[j] + str(i))
                elif (board[j][i] != 0) and (board[j][i].color == this_color):
                    blocked = True  # position is blocked by a friendly piece
                    blocked_spaces.append(board_map_index_to_alpha[j] + str(i))
                elif (board[j][i] != 0) and (board[j][i].color != this_color):
                    blocked = True  # positions behind are blocked, but target can be captured
                j -= 1

            # DOWN-RIGHT ===================================================================================
        elif (target_rank > this_rank) and board_map_alpha_to_index[target_file] > board_map_alpha_to_index[this_file]:
            j = board_map_alpha_to_index[this_file] + 1
            for i in range(this_rank + 1, target_rank + 1):
                if blocked is True:
                    blocked_spaces.append(board_map_index_to_alpha[j] + str(i))
                elif (board[j][i] != 0) and (board[j][i].color == this_color):
                    blocked = True  # position is blocked by a friendly piece
                    blocked_spaces.append(board_map_index_to_alpha[j] + str(i))
                elif (board[j][i] != 0) and (board[j][i].color != this_color):
                    blocked = True  # positions behind are blocked, but target can be captured
                j += 1

        elif (target_rank > this_rank) and board_map_alpha_to_index[target_file] < board_map_alpha_to_index[this_file]:
            # DOWN-LEFT ====================================================================================
                j = board_map_alpha_to_index[this_file] - 1
                for i in range(this_rank + 1, target_rank + 1):
                    if blocked is True:
                        blocked_spaces.append(board_map_index_to_alpha[j] + str(i))
                    elif (board[j][i] != 0) and (board[j][i].color == this_color):
                        blocked = True  # position is blocked by a friendly piece
                        blocked_spaces.append(board_map_index_to_alpha[j] + str(i))
                    elif (board[j][i] != 0) and (board[j][i].color != this_color):
                        blocked = True  # positions behind are blocked, but target can be captured
                    j -= 1

        return blocked_spaces


class Knight(Piece):
    def get_moves(self, position, board):
        file, rank = list(position.strip().lower())
        rank = int(rank)
        file = board_map_alpha_to_index[file]
        i, j = rank, file
        available_moves = []

        try:
            temp = board[i + 1][j - 2]
            available_moves.append([i + 1, j - 2])
        except:
            pass
        try:
            temp = board[i + 2][j - 1]
            available_moves.append([i + 2, j - 1])
        except:
            pass
        try:
            temp = board[i + 2][j + 1]
            available_moves.append([i + 2, j + 1])
        except:
            pass
        try:
            temp = board[i + 1][j + 2]
            available_moves.append([i + 1, j + 2])
        except:
            pass
        try:
            temp = board[i - 1][j + 2]
            available_moves.append([i - 1, j + 2])
        except:
            pass
        try:
            temp = board[i - 2][j + 1]
            available_moves.append([i - 2, j + 1])
        except:
            pass
        try:
            temp = board[i - 2][j - 1]
            available_moves.append([i - 2, j - 1])
        except:
            pass
        try:
            temp = board[i - 1][j - 2]
            available_moves.append([i - 1, j - 2])
        except:
            pass

        # filter negative values
        temp = [i for i in available_moves if i[0] >= 0 and i[1] >= 0]
        all_available_moves = ["".join([board_map_index_to_alpha[i[1]],
                                        str(i[0])]) for i in temp]
        all_available_moves.sort()

        return all_available_moves

    def no_jumping(self, from_square, to_square, color, board):
        blocked_spaces = []

        return blocked_spaces


class Pawn(Piece):
    def get_moves(self, position, board):
        # clamp x and y values to prevent them from going out of range
        clamp = lambda n, minn, maxn: max(min(maxn, n), minn)

        x, y = list(position.strip().lower())
        y = int(y)
        x = board_map_alpha_to_index[x]
        available_moves = []

        if y == 1 or y == 6:    # pawn is in its starting position (+2)
            if self.color == 'black':
                if board[x][y + 2] == 0:
                    temp = board[x][y + 2]
                    available_moves.append((x, y + 2))
            if self.color == 'white':
                if board[x][y - 2] == 0:
                    temp = board[x][y - 2]
                    available_moves.append((x, y - 2))

        if self.color == 'black':   # standard pawn move (+1)
            if board[x][y + 1] == 0:
                temp = board[x][y + 1]
                available_moves.append((x, y + 1))
        if self.color == 'white':
            if board[x][y - 1] == 0:
                temp = board[x][y - 1]
                available_moves.append((x, y - 1))

        # Diagonal captures
        if x == 0:    # pawn is on the left edge of the board
            if self.color == 'black':
                if (board[x + 1][y + 1] != 0) and (board[x + 1][y + 1].get_color() != self.color):
                    temp = board[x + 1][y + 1]
                    available_moves.append((x + 1, y + 1))
            elif self.color == 'white':
                if (board[x + 1][y - 1] != 0) and (board[x + 1][y - 1].get_color() != self.color):
                    temp = board[x + 1][y - 1]
                    available_moves.append((x + 1, y - 1))
        if x == 7:    # pawn is on the right edge of the board
            if self.color == 'black':
                if (board[x - 1][y + 1] != 0) and (board[x - 1][y + 1].get_color() != self.color):
                    temp = board[x - 1][y + 1]
                    available_moves.append((x - 1, y + 1))
            elif self.color == 'white':
                if (board[x - 1][y - 1] != 0) and (board[x - 1][y - 1].get_color() != self.color):
                    temp = board[x - 1][y - 1]
                    available_moves.append((x - 1, y - 1))
        else:
            if self.color == 'black':
                if (board[x + 1][y + 1] != 0) and (board[x + 1][y + 1].get_color() != self.color):
                    temp = board[x + 1][y + 1]
                    available_moves.append((x + 1, y + 1))
                elif (board[x - 1][y + 1] != 0) and (board[x - 1][y + 1].get_color() != self.color):
                    temp = board[x - 1][y + 1]
                    available_moves.append((x - 1, y + 1))
            else:
                if (board[x + 1][y - 1] != 0) and (board[x + 1][y - 1].get_color() != self.color):
                    temp = board[x + 1][y - 1]
                    available_moves.append((x + 1, y - 1))
                elif (board[x - 1][y - 1] != 0) and (board[x - 1][y - 1].get_color() != self.color):
                    temp = board[x - 1][y - 1]
                    available_moves.append((x - 1, y - 1))

        # filter negative values
        temp = [i for i in available_moves if i[0] >= 0 and i[1] >= 0]
        all_available_moves = ["".join([board_map_index_to_alpha[i[0]],
                                        str(i[1])]) for i in temp]
        all_available_moves.sort()
        return all_available_moves

    def no_jumping(self, from_square, to_square, color, board):
        blocked = False
        blocked_spaces = []
        this_file, this_rank = list(from_square.strip().lower())
        this_rank = int(this_rank)
        this_color = color  # color of current piece
        target_file, target_rank = list(to_square.strip().lower())
        target_rank = int(target_rank)

        if this_file == target_file:
            if target_rank > this_rank:  # DOWN ====================================================================
                for i in range(this_rank + 1, target_rank + 1):
                    if blocked is True:
                        blocked_spaces.append(this_file + str(i))
                    elif (board[board_map_alpha_to_index[this_file]][i] != 0) and \
                            (board[board_map_alpha_to_index[this_file]][i].color == this_color):
                        blocked = True  # position is blocked by a friendly piece
                        position = this_file + str(i)
                        blocked_spaces.append(position)
                    elif (board[board_map_alpha_to_index[this_file]][i] != 0) and \
                            (board[board_map_alpha_to_index[this_file]][i].color != this_color):
                        # positions behind are blocked, but target can be captured
                        blocked = True
            else:                       # UP =======================================================================
                for i in reversed(range(target_rank, this_rank)):
                    if blocked is True:
                        blocked_spaces.append(this_file + str(i))
                    elif (board[board_map_alpha_to_index[this_file]][i] != 0) and \
                            (board[board_map_alpha_to_index[this_file]][i].color == this_color):
                        blocked = True  # position is blocked by a friendly piece
                        position = this_file + str(i)
                        blocked_spaces.append(position)
                    elif (board[board_map_alpha_to_index[this_file]][i] != 0) and \
                            (board[board_map_alpha_to_index[this_file]][i].color != this_color):
                        blocked = True  # positions behind are blocked, but target can be captured

        return blocked_spaces
