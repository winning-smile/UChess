import pygame

# Screen settings
WIDTH = 1280
HEIGHT = 720
FPS = 60
CELLSIZE = 80
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

# Timers
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1000)
times = [120, 1, 120, 1]

white_timer = font_arial.render("{}:0{}".format(times[0], times[1]), True, (0, 0, 0))
white_timer_rect = white_timer.get_rect()
white_timer_rect.center = (1100, 660)

black_timer = font_arial.render("{}:0{}".format(times[2], times[3]), True, (0, 0, 0))
black_timer_rect = black_timer.get_rect()
black_timer_rect.center = (1100, 60)

# Variables
game = True
selected = False
game_started = False
castling_dict = ["wsc", "wlc", "bsc", "blc"]
turn_counter = 1
selected_figure = None
available_moves_sprites = pygame.sprite.Group()
move_square = pygame.sprite.GroupSingle()
drop_pos = None
info = None

