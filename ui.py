import pygame
from settings import font_arial, White, Black


def create_turn_display(turn_counter, screen):
    """ Drawing info about turn side and turn number"""
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


def draw_board_background(screen):
    """ Drawing chess cells """
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0:
                pygame.draw.rect(screen, White, (i * 80 + 320, j * 80 + 40, 80, 80))
            else:
                pygame.draw.rect(screen, "Brown", (i * 80 + 320, j * 80 + 40, 80, 80))


def draw_timer_display(color, times, timer_event):
    """ Drawing timer for black/white """
    if color == Black:
        times[3] -= 1
    else:
        times[1] -= 1

    if times[3] > 9:
        black_timer = font_arial.render("{}:{}".format(times[2], times[3]), True, (0, 0, 0))
    else:
        black_timer = font_arial.render("{}:0{}".format(times[2], times[3]), True, (0, 0, 0))

    if times[1] > 9:
        white_timer = font_arial.render("{}:{}".format(times[0], times[1]), True, (0, 0, 0))
    else:
        white_timer = font_arial.render("{}:0{}".format(times[0], times[1]), True, (0, 0, 0))

    white_timer_rect = white_timer.get_rect()
    white_timer_rect.center = (1100, 60)

    black_timer_rect = black_timer.get_rect()
    black_timer_rect.center = (1100, 660)

    if times[3] == 0:
        times[3] = 60
        times[2] -= 1
        pygame.time.set_timer(timer_event, 1000)

    if times[1] == 0:
        times[1] = 60
        times[0] -= 1
        pygame.time.set_timer(timer_event, 1000)

    return times,  white_timer,  white_timer_rect, black_timer, black_timer_rect
