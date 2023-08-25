import pygame
from settings import Black, White

img_dict = {(Black, "P") : "img/bP.png", (Black, "R") : "img/bR.png", (Black, "K") : "img/bN.png",
            (Black, "B") : "img/bB.png", (Black, "Q") : "img/bQ.png", (Black, "S") : "img/bK.png",
            (White, "P") : "img/wP.png", (White, "R") : "img/wR.png", (White, "K") : "img/wN.png",
            (White, "B") : "img/wB.png", (White, "Q") : "img/wQ.png", (White, "S") : "img/wK.png"}
class Figure(pygame.sprite.Sprite):
    def __init__(self, color, value, xy):
        pygame.sprite.Sprite.__init__(self)
        self.first_move = False     # Флаг первого хода фигуры
        self.color = color          # Цвет фигуры
        self.val = value            # Значение фигуры
        self.x = xy[0]              # Координата по х
        self.y = xy[1]              # Координата по y

        # Изображение фигуры и его положение
        self.image = pygame.image.load(img_dict[(self.color, self.val)]).convert_alpha()
        self.rect = self.image.get_rect(center=(360 + self.x*80, 80 + self.y*80))