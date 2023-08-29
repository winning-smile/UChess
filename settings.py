import pygame

# Screen settings
WIDTH = 1280
HEIGHT = 720
FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("UChess")

# Color presets
White = (255, 255, 255)
Black = (0, 0, 0)
Grey = (150, 150, 150)

# Sound
pygame.mixer.init()
pygame.mixer.music.load("move_sound.mp3")

# Text
pygame.font.init()
font_arial = pygame.font.SysFont('arial.ttf', 50)
