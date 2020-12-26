import time
from board import *
from player import *


pygame.init()

pygame.display.set_caption("MyChess", "None")

green = (0, 200, 0)
bright_green = (0, 255, 0)
red = (200, 0, 0)
bright_red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
very_light_grey = (200, 200, 200)
dark_grey = (32, 32, 32)
very_dark_grey = (16, 16, 16)


def text_objects(text, font):
    text_surface = font.render(text, True, (0, 0, 0))
    return text_surface, text_surface.get_rect()


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    small_text = pygame.font.SysFont('consolas', 20)
    text_surf, text_rect = text_objects(msg, small_text)
    text_rect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(text_surf, text_rect)


def turn_process(player1, player2, board):

    done = False

    while not done and player1.checkmate is False and player2.checkmate is False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                quit_game()

        distribute_pieces(player1, player2, board)

        if player1.turn is True:
            player1.start_turn()
            window.set_text("============================", 'white')
            window.set_text("It is " + player1.color + "\'s turn.", 'white')
            window.set_text("============================", 'white')
            # User square selection:
            current_pos, new_pos = square_selection_process(board, player1)
            # move the pieces:
            move(current_pos, new_pos, board)
            highlight_square(current_pos, 'j')
            highlight_square(new_pos, 'i')
            look_for_check(player1, player2, board)
            player1.end_turn()
            player2.turn = True
        else:
            player2.start_turn()
            window.set_text("============================", 'white')
            window.set_text("It is " + player2.color + "\'s turn.", 'white')
            window.set_text("============================", 'white')
            # User square selection:
            current_pos, new_pos = square_selection_process(board, player2)
            # move the pieces:
            move(current_pos, new_pos, board)
            highlight_square(current_pos, 'j')
            highlight_square(new_pos, 'i')
            look_for_check(player1, player2, board)
            player2.end_turn()
            player1.turn = True

    # Game over
    window.set_text("Returning to main menu in 30 seconds ...", 'yellow')
    for i in range(30, 0, -1):
        time.sleep(1)
        if i <= 5:
            window.set_text(str(i), 'yellow')

    window.clear_text()


def quit_game():
    pygame.display.quit()
    pygame.quit()
    sys.exit()


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        screen.fill((25, 25, 25))
        large_text = pygame.font.SysFont('consolas', 110)
        large_text_white = large_text.render("MyChess", 1, (255, 255, 255))
        small_text = pygame.font.SysFont('consolas', 22)
        version_text_white = small_text.render("v0.7-alpha", 1, (255, 255, 255))
        name_text_white = small_text.render("by Evan DeVizio", 1, (255, 255, 255))
        screen.blit(large_text_white, (190, 245))
        screen.blit(version_text_white, (660, 750))
        screen.blit(name_text_white, (30, 750))

        button("START", 150, 550, 100, 50, green, bright_green, game_loop)
        button("QUIT", 550, 550, 100, 50, red, bright_red, quit_game)

        pygame.display.update()


def game_loop():
    board = initialize_board()    # create board
    update_images(board)

    pygame.display.flip()

    p1 = Player('white', True)    # create players
    p2 = Player('black', False)

    turn_process(p1, p2, board)


game_intro()
