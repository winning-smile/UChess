from settings import *
from start_game import start


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
    board = start()

    draw_board()

    # Группируем справйты фигур для отрисовки
    figures = pygame.sprite.Group()
    for elem in board:
        figures.add(elem)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        figures.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    main_loop()
