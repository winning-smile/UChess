from settings import *
from start_game import create_visual_board
import logics as lg
from logics import logic_board


def draw_board():
    """Отрисовка полей игровой доски"""
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0:
                pygame.draw.rect(screen, White, (i * 80 + 320, j * 80 + 40, 80, 80))
            else:
                pygame.draw.rect(screen, "Brown", (i * 80 + 320, j * 80 + 40, 80, 80))


def main_loop():
    running = True
    screen.fill("GREY")
    board = create_visual_board()
    l_board = lg.logic_board
    turn_counter = 1
    turn_flag = None

    draw_board()

    #
    selected_figure = None
    # Группируем спрайты возможных ходов
    available_moves_sprites = pygame.sprite.Group()
    # Группируем спрайты фигур для отрисовки
    figures = pygame.sprite.Group()
    for elem in board:
        figures.add(elem)

    # Главный цикл игры
    while running:
        clock.tick(FPS)
        event_list = pygame.event.get()

        for event in event_list:
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if turn_counter % 2 != 0:
                    turn_flag = White
                else:
                    turn_flag = Black

                lg.print_lg_board(l_board)

                for move in available_moves_sprites:
                    if move.rect.collidepoint(event.pos):
                        l_board = lg.move_logic_figure(selected_figure.x, selected_figure.y, move.x, move.y, l_board)
                        selected_figure.move_figure(move.x, move.y)
                        turn_counter += 1

                for figure in figures:
                    if figure.rect.collidepoint(event.pos) and figure.color == turn_flag:
                        selected_figure = figure
                        lg.create_available_moves_sprites(lg.logic(figure.val, figure.color, figure.x, figure.y), available_moves_sprites)

                    elif figure.rect.collidepoint(event.pos) and figure.color != turn_flag:
                        available_moves_sprites.empty()

        draw_board()
        figures.draw(screen)
        available_moves_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    main_loop()
