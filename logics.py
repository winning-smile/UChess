import pygame
from settings import Black, White
import numpy as np
#
class Logic_Figure:
    def __init__(self, color, value, xy):
        self.first_move = False     # Флаг первого хода фигуры
        self.color = color          # Цвет фигуры
        self.val = value            # Значение фигуры
        self.x = xy[0]              # Координата по х
        self.y = xy[1]              # Координата по y

def logic(val, color, x, y):
    """возвращает массив доступных ходов"""
    return logic_dict[val](logic_board, color, x, y)

def pawn_logic(board, color, x, y):
    possible_moves = []

    if color == White:
        if not board[x-1][y]:
            possible_moves.append([x - 1, y])
        if board[x-1][y-1] and board[x - 1][y - 1].color == Black:
            possible_moves.append([x - 1, y - 1])
        if board[x-1][y-1] and board[x - 1][y + 1].color == Black:
            possible_moves.append([x - 1, y + 1])

    else:
        if not board[x+1][y]:
            possible_moves.append([x + 1, y])
        if board[x+1][y-1] and board[x + 1][y - 1].color == White:
            possible_moves.append([x + 1, y - 1])
        if board[x+1][y-1] and board[x + 1][y + 1].color == White:
            possible_moves.append([x + 1, y + 1])

    return possible_moves


def create_logic_board():
    lb = np.zeros((8, 8), dtype=object)

    # Создаём логическую доску
    lb[0][0] = Logic_Figure(Black, "R", [0, 0])
    lb[0][1] = Logic_Figure(Black, "K", [0, 1])
    lb[0][2] = Logic_Figure(Black, "B", [0, 2])
    lb[0][3] = Logic_Figure(Black, "Q", [0, 3])
    lb[0][4] = Logic_Figure(Black, "S", [0, 4])
    lb[0][5] = Logic_Figure(Black, "B", [0, 5])
    lb[0][6] = Logic_Figure(Black, "K", [0, 6])
    lb[0][7] = Logic_Figure(Black, "R", [0, 7])

    for i in range(8):
        lb[1][i] = Logic_Figure(Black, "P", [1, i])

    for i in range(8):
        lb[6][i] = Logic_Figure(White, "P", [6, i])

    lb[7][0] = Logic_Figure(White, "R", [7, 0])
    lb[7][1] = Logic_Figure(White, "K", [7, 1])
    lb[7][2] = Logic_Figure(White, "B", [7, 2])
    lb[7][3] = Logic_Figure(White, "Q", [7, 3])
    lb[7][4] = Logic_Figure(White, "S", [7, 4])
    lb[7][5] = Logic_Figure(White, "B", [7, 5])
    lb[7][6] = Logic_Figure(White, "K", [7, 6])
    lb[7][7] = Logic_Figure(White, "R", [7, 7])

    return lb


def create_available_moves_sprites(moves, available_moves_sprites):
    for sprite in available_moves_sprites:
        sprite.kill()
        del sprite

    available_moves_sprites.empty()

    for move in moves:
        sprite = pygame.sprite.Sprite()
        sprite.image = pygame.image.load("img/possible_move.png").convert_alpha()
        sprite.x = move[1]
        sprite.y = move[0]
        sprite.rect = sprite.image.get_rect(center=(360 + sprite.x * 80, 80 + sprite.y * 80))
        available_moves_sprites.add(sprite)


logic_board = create_logic_board()
logic_dict = {"P": pawn_logic}
