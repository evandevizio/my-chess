import os
import pygame
from tkwindow import *
import ctypes
from piece import *


screen_width = 800
screen_height = 800

pos_x = screen_width / 2 - screen_width / 2
pos_y = screen_height - screen_height
os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (pos_x, pos_y)
os.environ['SDL_VIDEO_CENTERED'] = '0'

screen = pygame.display.set_mode((screen_width, screen_height))

window = tkwindow(screen.get_size()[0] * 1.7, screen.get_size()[1] / 6.7)
window.set_text("", 'white')

scrollbar = Scrollbar(window.lb, orient="vertical")
scrollbar.config(command=window.lb.yview)
scrollbar.pack(side="right", fill="y")

window.lb.config(yscrollcommand=scrollbar.set)

MessageBox = ctypes.windll.user32.MessageBoxExW

image_dict = {'X': pygame.image.load("images/wking.png"), 'x': pygame.image.load("images/bking.png"),
              'Q': pygame.image.load("images/wqueen.png"), 'q': pygame.image.load("images/bqueen.png"),
              'R': pygame.image.load("images/wrook.png"), 'r': pygame.image.load("images/brook.png"),
              'K': pygame.image.load("images/wknight.png"), 'k': pygame.image.load("images/bknight.png"),
              'B': pygame.image.load("images/wbishop.png"), 'b': pygame.image.load("images/bbishop.png"),
              'P': pygame.image.load("images/wpawn.png"), 'p': pygame.image.load("images/bpawn.png"),
              'h': pygame.image.load("images/highlight.png"), 'i': pygame.image.load("images/highlight2.png"),
              'j': pygame.image.load("images/highlight3.png")}


def initialize_board():
    # reset the chessboard
    board = [[0] * 8 for i in range(8)]

    # Create and place pieces on the board

    # White
    wking = King('X', 'white')
    wqueen = Queen('Q', 'white')
    wrook1 = Rook('R', 'white')
    wrook2 = Rook('R', 'white')
    wbishop1 = Bishop('B', 'white')
    wbishop2 = Bishop('B', 'white')
    wknight1 = Knight('K', 'white')
    wknight2 = Knight('K', 'white')
    wpawn1 = Pawn('P', 'white')
    wpawn2 = Pawn('P', 'white')
    wpawn3 = Pawn('P', 'white')
    wpawn4 = Pawn('P', 'white')
    wpawn5 = Pawn('P', 'white')
    wpawn6 = Pawn('P', 'white')
    wpawn7 = Pawn('P', 'white')
    wpawn8 = Pawn('P', 'white')

    # Black
    bking = King('x', 'black')
    bqueen = Queen('q', 'black')
    brook1 = Rook('r', 'black')
    brook2 = Rook('r', 'black')
    bbishop1 = Bishop('b', 'black')
    bbishop2 = Bishop('b', 'black')
    bknight1 = Knight('k', 'black')
    bknight2 = Knight('k', 'black')
    bpawn1 = Pawn('p', 'black')
    bpawn2 = Pawn('p', 'black')
    bpawn3 = Pawn('p', 'black')
    bpawn4 = Pawn('p', 'black')
    bpawn5 = Pawn('p', 'black')
    bpawn6 = Pawn('p', 'black')
    bpawn7 = Pawn('p', 'black')
    bpawn8 = Pawn('p', 'black')

    # test config for checkmate:
    board[2][0] = bking
    board[0][7] = wrook1
    board[7][7] = wrook2
    board[4][7] = wking

    board[0][7] = wrook1
    board[1][7] = wknight1
    board[2][7] = wbishop1
    board[3][7] = wqueen
    board[4][7] = wking
    board[5][7] = wbishop2
    board[6][7] = wknight2
    board[7][7] = wrook2
    board[0][6] = wpawn1
    board[1][6] = wpawn2
    board[2][6] = wpawn3
    board[3][6] = wpawn4
    board[4][6] = wpawn5
    board[5][6] = wpawn6
    board[6][6] = wpawn7
    board[7][6] = wpawn8

    board[0][0] = brook1
    board[1][0] = bknight1
    board[2][0] = bbishop1
    board[3][0] = bqueen
    board[4][0] = bking
    board[5][0] = bbishop2
    board[6][0] = bknight2
    board[7][0] = brook2
    board[0][1] = bpawn1
    board[1][1] = bpawn2
    board[2][1] = bpawn3
    board[3][1] = bpawn4
    board[4][1] = bpawn5
    board[5][1] = bpawn6
    board[6][1] = bpawn7
    board[7][1] = bpawn8

    return board


def update_images(board):
    # iterate through board and place pieces
    draw_board()
    for i in range(8):
        for j in range(8):
            if board[i][j] != 0:
                image_key = (board[i][j]).key
                screen.blit(image_dict[image_key], ((i*100) + 8, (j*100) + 8))
    pygame.display.flip()


def draw_board():
    # chessboard visual
    for x in range(0, screen_width, screen_width // 4):
        for y in range(0, screen_height, screen_height // 4):
            pygame.draw.rect(screen, (150, 150, 150), (x, y, screen_width // 8, screen_height // 8))

    for x in range(screen_width // 8, screen_width, screen_width // 4):
        for y in range(0, screen_height, screen_height // 4):
            pygame.draw.rect(screen, (60, 60, 60), (x, y, screen_width // 8, screen_height // 8))

    for x in range(0, screen_width, screen_width // 4):
        for y in range(screen_height // 8, screen_height, screen_height // 4):
            pygame.draw.rect(screen, (60, 60, 60), (x, y, screen_width // 8, screen_height // 8))

    for x in range(screen_width // 8, screen_width, screen_width // 4):
        for y in range(screen_height // 8, screen_height, screen_height // 4):
            pygame.draw.rect(screen, (150, 150, 150), (x, y, screen_width // 8, screen_height // 8))


def print_board(board):
    # display board in console
    for i in range(8):
        for j in range(8):
            if board[i][j] != 0:
                print(board[i][j].get_key(), end=" ")
            else:
                print(board[i][j], end=" ")
        print('\n')


def get_click_position():
    # gets the chess position of a square that the user clicks on
    pos = pygame.mouse.get_pos()
    click_position = ((board_map_index_to_alpha[pos[0] // 100])
                      + str(pos[1] // 100))  # cell size = 100

    return click_position


def get_display_coords(position):
    # translate a given chess position to the screen coordinates
    file, rank = list(position.strip().lower())
    rank = int(rank)
    file = board_map_alpha_to_index[file]
    display_x = (rank*100) + 8  # "+8px" looks more centered
    display_y = (file*100) + 8

    return display_x, display_y


def highlight_square(position, colorkey):
    y, x = get_display_coords(position)

    # highlight determined by colorkey. yellow: move selection, green: new move, blue: previous move
    screen.blit(image_dict[colorkey], (x - 8, y - 8))  # -8 for visual offset
    pygame.display.flip()


def square_selection_process(board, player):
    # this is where square choices are prepared/error-checked
    # before being sent to the moving function

    current_player = player
    this_piece = None
    temp_from_square = None
    temp_to_square = None
    temp_current_player_positions = []
    blocked_spaces = current_player.blocked_spaces
    reselect = False  # flag for re-selection

    # create list of player's occupied spaces:
    for i in current_player.get_pieces_on_board():
        temp_current_player_positions.append(board_map_index_to_alpha[i[0]] + str(i[1]))

    done1 = False
    done2 = False

    while (temp_from_square is None and temp_to_square is None) or reselect is True:
        while not done1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    temp_from_square = get_click_position()
                    this_piece = board[board_map_alpha_to_index[temp_from_square[0]]][int(temp_from_square[1])]
                    # check if the user selected a blank square as their first selection:
                    if temp_from_square not in temp_current_player_positions:
                        window.set_text('You can\'t select that space.', 'yellow')
                        done1 = False
                    else:
                        highlight_square(temp_from_square, 'h')
                        done1 = True
        while not done2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    temp_to_square = get_click_position()
                    reselect = False

                    #  allow user to select a different piece if they choose a piece of their color:
                    if board[board_map_alpha_to_index[temp_to_square[0]]][int(temp_to_square[1])] != 0 and \
                            board[board_map_alpha_to_index[temp_to_square[0]]][int(temp_to_square[1])].color \
                            == this_piece.color:
                        reselect = True
                        done1 = True
                        temp_from_square = temp_to_square
                        temp_to_square = None
                        update_images(board)
                        highlight_square(temp_from_square, 'h')

                    # determine which spaces are blocked if a player chooses a bishop, rook, queen,
                    # or a pawn that has not moved yet:
                    if reselect is False and ((piece_key_to_name[this_piece.key] == "Rook" or "Bishop" or "Queen")
                                              or (piece_key_to_name[this_piece.key] == "Pawn")
                                              and this_piece.has_moved is False):
                        blocked_spaces = this_piece.no_jumping(temp_from_square, temp_to_square,
                                                               this_piece.color, board)

                    #  destination is not in list of possible moves, is occupied, or is blocked:
                    #if temp_to_square not in temp_current_player_positions:
                        #reselect = False

                    if ((temp_to_square not in this_piece.get_moves(temp_from_square, board) and
                         reselect is False) or temp_to_square in blocked_spaces):
                        window.set_text('You can\'t move to that space.', 'yellow')
                        done2 = False
                    else:
                        done2 = True

                    if reselect is True:
                        done2 = False

    update_images(board)

    return temp_from_square, temp_to_square


def distribute_pieces(p1, p2, board):
    # give players their pieces based on color:
    white_pieces = []
    black_pieces = []
    for i in range(8):
        for j in range(8):
            if board[i][j] != 0:  # if space is not empty
                if board[i][j].color == 'black':
                    black_pieces.append((i, j))
                else:
                    white_pieces.append((i, j))

    if p1.color == 'white':
        p1.pieces_on_board = white_pieces
        p2.pieces_on_board = black_pieces
    else:
        p1.pieces_on_board = black_pieces
        p2.pieces_on_board = white_pieces

    return white_pieces, black_pieces


def look_for_check(p1, p2, board):

    white_pieces, black_pieces = distribute_pieces(p1, p2, board)

    p1.blocked_spaces = []
    p2.blocked_spaces = []
    black_king_pos = None
    white_king_pos = None
    white_moves = []
    black_moves = []

    p1.in_check = False
    p2.in_check = False

    # get lists of all possible locations each player can move to
    # and get both king's locations
    # ===========================================================

    if p1.color == 'black':
        for i in black_pieces:
            black_moves.append((board[i[0]][i[1]]).get_moves(board_map_index_to_alpha[i[0]] + str(i[1]), board))
            # find the king's location:
            if (board[i[0]][i[1]]).key == "x" and (board[i[0]][i[1]]).color == "black":
                black_king_pos = board_map_index_to_alpha[i[0]] + str(i[1])
        for j in white_pieces:
            white_moves.append((board[j[0]][j[1]]).get_moves(board_map_index_to_alpha[j[0]] + str(j[1]), board))
            if (board[j[0]][j[1]]).key == "X" and (board[j[0]][j[1]]).color == "white":
                white_king_pos = board_map_index_to_alpha[j[0]] + str(j[1])

        p1_moves = black_moves
        p1_king_pos = black_king_pos
        p2_moves = white_moves
        p2_king_pos = white_king_pos

    else:
        for j in white_pieces:
            white_moves.append((board[j[0]][j[1]]).get_moves(board_map_index_to_alpha[j[0]] + str(j[1]), board))
            if (board[j[0]][j[1]]).key == "X" and (board[j[0]][j[1]]).color == "white":
                white_king_pos = board_map_index_to_alpha[j[0]] + str(j[1])
        for i in black_pieces:
            black_moves.append((board[i[0]][i[1]]).get_moves(board_map_index_to_alpha[i[0]] + str(i[1]), board))
            if (board[i[0]][i[1]]).key == "x" and (board[i[0]][i[1]]).color == "black":
                black_king_pos = board_map_index_to_alpha[i[0]] + str(i[1])

        p1_moves = white_moves
        p1_king_pos = white_king_pos
        p2_moves = black_moves
        p2_king_pos = black_king_pos

    # make 2D list of moves into a single list
    p1_moves_flat = [item for sublist in p1_moves for item in sublist]
    p2_moves_flat = [item for sublist in p2_moves for item in sublist]

    # remove a position from movelist if that space is blocked
    for m in list(set(p1_moves_flat)):
        if board[board_map_alpha_to_index[m[0]]][int(m[1])] != 0:
            m_piece = (board[board_map_alpha_to_index[m[0]]][int(m[1])])
            if (piece_key_to_name[m_piece.get_key()] == 'Rook' or piece_key_to_name[m_piece.get_key()] == 'Bishop'
                or piece_key_to_name[m_piece.get_key()] == 'Queen') and (p2_king_pos in m_piece.get_moves(m, board))\
                    and (m_piece.color == p1.color):
                p1.blocked_spaces = m_piece.no_jumping(m, p2_king_pos, m_piece.color, board)

    for n in p1.blocked_spaces:
        if n in p1_moves_flat:
            p1_moves_flat.remove(n)

    if p1_king_pos in p2_moves_flat:
        (board[board_map_alpha_to_index[p1_king_pos[0]]][int(p1_king_pos[1])]).is_in_check = True
        p1.in_check = True
        window.set_text("Player 1 is in check.", 'salmon')

    if p2_king_pos in p1_moves_flat:
        (board[board_map_alpha_to_index[p2_king_pos[0]]][int(p2_king_pos[1])]).is_in_check = True
        p2.in_check = True
        window.set_text("Player 2 is in check.", 'salmon')

    p1_king_moves = board[board_map_alpha_to_index[p1_king_pos[0]]][int(p1_king_pos[1])].get_moves(p1_king_pos, board)
    p2_king_moves = board[board_map_alpha_to_index[p2_king_pos[0]]][int(p2_king_pos[1])].get_moves(p2_king_pos, board)

    # checkmate:
    if p1.in_check:
        if all(elem in p2_moves_flat for elem in p1_king_moves):
            p1.checkmate = True
            if p1.color == 'white':
                window.set_text("=================================", 'light green')
                window.set_text("Checkmate. Player 2 (black) wins.", 'light green')
                window.set_text("=================================", 'light green')
            else:
                window.set_text("=================================", 'light green')
                window.set_text("Checkmate. Player 2 (white) wins.", 'light green')
                window.set_text("=================================", 'light green')

    if p2.in_check:
        if all(elem in p1_moves_flat for elem in p2_king_moves):
            p2.checkmate = True
            if p2.color == 'black':
                window.set_text("=================================", 'light green')
                window.set_text("Checkmate. Player 1 (white) wins.", 'light green')
                window.set_text("=================================", 'light green')
            else:
                window.set_text("=================================", 'light green')
                window.set_text("Checkmate. Player 1 (black) wins.", 'light green')
                window.set_text("=================================", 'light green')


def move(from_square, to_square, board):
    player_file, player_rank = list(from_square.strip().lower())
    player_rank = int(player_rank)
    player_file = board_map_alpha_to_index[player_file]
    player_piece = board[player_file][player_rank]
    player_moves = player_piece.get_moves(from_square, board)

    dest_file, dest_rank = list(to_square.strip().lower())
    dest_rank = int(dest_rank)
    dest_file = board_map_alpha_to_index[dest_file]
    dest_piece = board[dest_file][dest_rank]

    if dest_piece != 0:
        window.set_text(player_piece.color.capitalize() + ' ' + (piece_key_to_name[player_piece.key]) + ' takes '
                        + dest_piece.color.capitalize() + ' ' + (piece_key_to_name[dest_piece.key]), 'light blue')

    if to_square not in player_moves:
        window.set_text('That is not a valid move.', 'yellow')
    else:
        # replace destination space with player_piece
        # and set from_square to 0 (empty)
        board[dest_file][dest_rank] = player_piece
        board[player_file][player_rank] = 0

    update_images(board)
