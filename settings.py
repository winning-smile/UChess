import pygame

WIDTH = 1280
HEIGHT = 720
FPS = 30

White = (255, 255, 255)
Black = (0, 0, 0)
Grey = (150, 150, 150)

sysfont = pygame.font.get_default_font()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("UChess")