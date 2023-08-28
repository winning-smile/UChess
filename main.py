from settings import *
from start_game import create_visual_board
import logics as lg
import itertools as it


def draw_board():
    """Отрисовка фона игрового поля"""
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
    selected = False

    draw_board()

    # Выбранная в текущий момент фигура
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

            # События по нажатию мыши
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Флаг для определения чей ход и отрисовки возможных ходов только у фигур одного цвета
                if turn_counter % 2 != 0:
                    turn_flag = White
                else:
                    turn_flag = Black

                # для отладки логической доски
                lg.print_lg_board(l_board)

                for figure, move in it.zip_longest(figures, available_moves_sprites):
                    if move:
                        if move.rect.collidepoint(event.pos):
                            l_board, move_flag = lg.move_logic_figure(selected_figure.x, selected_figure.y, move.x, move.y, l_board)
                            if move_flag == "kill":
                                for fig in figures:
                                    if fig.y == move.x and fig.x == move.y:
                                        fig.kill()

                            selected_figure.move_figure(move.x, move.y)
                            turn_counter += 1
                            available_moves_sprites.empty()
                            break

                    if figure:
                        if figure.rect.collidepoint(event.pos):
                            if figure.color == turn_flag:
                                selected_figure = figure
                                print(figure.x, figure.y)
                                available_moves_sprites = lg.create_available_moves_sprites(lg.logic(figure.val, figure.color, figure.x, figure.y), available_moves_sprites)
                                break
                            else:
                                available_moves_sprites.empty()
                                break

        draw_board()
        available_moves_sprites.draw(screen)
        figures.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    main_loop()
