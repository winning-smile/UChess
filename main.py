import pygame
from settings import *
from start_game import start
from pygame.locals import *
import pygame.font

def main_loop():
    running = True
    board = start()

    f1 = pygame.font.Font(None, 36)

    while running:
        for event in pygame.event.get():
            screen.fill("GREY")

            for piece in board:
                pygame.draw.rect(screen, piece.color, (piece.x * 80 + 320, piece.y * 80 + 40, 80, 80))
                if piece.figure:
                    text1 = f1.render(piece.figure.val, True, Grey)
                    screen.blit(text1, (piece.x * 80 + 320, piece.y * 80 + 40))

            pygame.display.flip()
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    main_loop()
