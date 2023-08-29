from settings import *
from start_game import *
import logics as lg
import itertools as it

# TODO Timer
# TODO Turn history
# TODO Engine analysis
# TODO liches manual analysis
# TODO killed figures
# TODO turn back
# TODO Win condition and screen
# TODO Menu -> [classic, rapid, blitz]
# TODO Check/Mate red glow
# TODO Mouse.drag figures moves
# TODO Multiplayer

def draw_board():
    """Отрисовка фона игрового поля"""
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0:
                pygame.draw.rect(screen, White, (i * 80 + 320, j * 80 + 40, 80, 80))
            else:
                pygame.draw.rect(screen, "Brown", (i * 80 + 320, j * 80 + 40, 80, 80))


def create_turn_display(turn_counter):
    if turn_counter % 2 != 0:
        turn_display = font_arial.render(f'Turn {turn_counter}', True, (0, 0, 0))
        color_display = font_arial.render("for WHITE", True, (255, 255, 255))
    else:
        turn_display = font_arial.render(f'Turn {turn_counter}', True, (0, 0, 0))
        color_display = font_arial.render("for BLACK", True, (0, 0, 0))

    turn_display_rect = turn_display.get_rect()
    color_display_rect = color_display.get_rect()
    turn_display_rect.center = (1100, 340)
    color_display_rect.center = (1100, 380)

    screen.blit(turn_display, turn_display_rect)
    screen.blit(color_display, color_display_rect)

def main_loop():
    running = True
    screen.fill("GREY")
    board = create_visual_board()
    l_board = lg.logic_board
    turn_counter = 1
    selected = False
    game_started = False

    draw_board()
    # Выбранная в текущий момент фигура
    selected_figure = None
    # Группируем спрайты возможных ходов
    available_moves_sprites = pygame.sprite.Group()
    # Группируем спрайты фигур для отрисовки
    figures = pygame.sprite.Group()
    for elem in board:
        figures.add(elem)

    # Таймер
    timer_event = pygame.USEREVENT + 1
    pygame.time.set_timer(timer_event, 1000)
    white_seconds = 15
    white_minutes = 120
    black_seconds = 15
    black_minutes = 120

    white_timer = font_arial.render("{}:0{}".format(white_minutes, white_seconds), True, (0, 0, 0))
    white_timer_rect = white_timer.get_rect()
    white_timer_rect.center = (1100, 660)

    black_timer = font_arial.render("{}:0{}".format(black_minutes, black_seconds), True, (0, 0, 0))
    black_timer_rect = black_timer.get_rect()
    black_timer_rect.center = (1100, 60)

    # Главный цикл игры
    while running:
        clock.tick(FPS)
        event_list = pygame.event.get()

        for event in event_list:
            if event.type == pygame.QUIT:
                running = False

            if game_started:
                if event.type == timer_event:
                    if turn_counter % 2 != 0:
                        black_seconds -= 1

                        if black_seconds > 9:
                            black_timer = font_arial.render("{}:{}".format(black_minutes, black_seconds), True, (0, 0, 0))
                        else:
                            black_timer = font_arial.render("{}:0{}".format(black_minutes, black_seconds), True, (0, 0, 0))

                        if white_seconds > 9:
                            white_timer = font_arial.render("{}:{}".format(white_minutes, white_seconds), True, (0, 0, 0))
                        else:
                            white_timer = font_arial.render("{}:0{}".format(white_minutes, white_seconds), True, (0, 0, 0))

                        white_timer_rect = white_timer.get_rect()
                        white_timer_rect.center = (1100, 60)

                        black_timer_rect = black_timer.get_rect()
                        black_timer_rect.center = (1100, 660)

                        if black_seconds == 0:
                            black_seconds = 60
                            black_minutes -= 1
                            pygame.time.set_timer(timer_event, 1000)
                    else:
                        white_seconds -= 1
                        if white_seconds > 9:
                            white_timer = font_arial.render("{}:{}".format(white_minutes, white_seconds), True, (0, 0, 0))
                        else:
                            white_timer = font_arial.render("{}:0{}".format(white_minutes, white_seconds), True, (0, 0, 0))

                        if black_seconds > 9:
                            black_timer = font_arial.render("{}:{}".format(black_minutes, black_seconds), True, (0, 0, 0))
                        else:
                            black_timer = font_arial.render("{}:0{}".format(black_minutes, black_seconds), True, (0, 0, 0))

                        white_timer_rect = white_timer.get_rect()
                        white_timer_rect.center = (1100, 60)

                        black_timer_rect = black_timer.get_rect()
                        black_timer_rect.center = (1100, 660)

                        if white_seconds == 0:
                            white_seconds = 60
                            white_minutes -= 1
                            pygame.time.set_timer(timer_event, 1000)

            # События по нажатию мыши
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Флаг для определения чей ход и отрисовки возможных ходов только у фигур одного цвета
                if turn_counter % 2 != 0:
                    turn_flag = White
                else:
                    turn_flag = Black

                # для отладки логической доски
                lg.print_lg_board(l_board)

                # TODO Починить то что нельзя убить верхние фигуры
                for figure, move in it.zip_longest(figures, available_moves_sprites):
                    if move:
                        if move.rect.collidepoint(event.pos):
                            l_board, move_flag = lg.move_logic_figure(selected_figure.x, selected_figure.y, move.x, move.y, l_board)
                            if move_flag == "kill":
                                for fig in figures:
                                    if fig.y == move.x and fig.x == move.y:
                                        fig.kill()

                            selected_figure.move_figure(move.x, move.y)

                            if selected_figure.val == "P":
                                if selected_figure.x == 7 and selected_figure.color == Black:
                                    selected_figure.to_queen()
                                    l_board[selected_figure.x][selected_figure.y].val = "Q"
                                elif selected_figure.x == 0 and selected_figure.color == White:
                                    selected_figure.to_queen()
                                    l_board[selected_figure.x][selected_figure.y].val = "Q"

                            game_started = True
                            pygame.mixer.music.play()
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

        screen.fill("GREY")
        draw_board()
        available_moves_sprites.draw(screen)
        figures.draw(screen)
        create_turn_display(turn_counter)
        screen.blit(black_timer, black_timer_rect)
        screen.blit(white_timer, white_timer_rect)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    main_loop()
