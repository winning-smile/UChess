from settings import *
from start_game import create_visual_board
import logics as lg


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
                for move in available_moves_sprites:
                    if move.rect.collidepoint(event.pos):
                        selected_figure.move_figure(move.x, move.y)
                        # TODO CHANGE LOGIC_BOARD ON MOVE

                for figure in figures:
                    if figure.rect.collidepoint(event.pos):
                        selected_figure = figure
                        lg.create_available_moves_sprites(lg.logic(figure.val, figure.color, figure.x, figure.y), available_moves_sprites)

        draw_board()
        figures.draw(screen)
        available_moves_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    main_loop()
