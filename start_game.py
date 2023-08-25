import numpy as np
from classes import Piece, Figure
from settings import Black, White

# Start board dictionary
sbd = { (0, 0) : Figure("Black", "R"), (0, 7) : Figure("Black", "R"),
        (0, 1) : Figure("Black", "K"), (0, 6) : Figure("Black", "K"),
        (0, 2) : Figure("Black", "B"), (0, 5) : Figure("Black", "B"),
        (0, 3) : Figure("Black", "Q"), (0, 4) : Figure("Black", "S"),
        (7, 0) : Figure("White", "R"), (7, 7) : Figure("White", "R"),
        (7, 1) : Figure("White", "K"), (7, 6) : Figure("White", "K"),
        (7, 2) : Figure("White", "B"), (7, 5) : Figure("White", "B"),
        (7, 3) : Figure("White", "Q"), (7, 4) : Figure("White", "S"),
        (1, 0) : Figure("Black", "P"), (1, 1) : Figure("Black", "P"),
        (1, 2) : Figure("Black", "P"), (1, 3) : Figure("Black", "P"),
        (1, 4) : Figure("Black", "P"), (1, 5) : Figure("Black", "P"),
        (1, 6) : Figure("Black", "P"), (1, 7) : Figure("Black", "P"),
        (6, 0) : Figure("White", "P"), (6, 1) : Figure("White", "P"),
        (6, 2) : Figure("White", "P"), (6, 3) : Figure("White", "P"),
        (6, 4) : Figure("White", "P"), (6, 5) : Figure("White", "P"),
        (6, 6) : Figure("White", "P"), (6, 7) : Figure("White", "P")}

def start():
    """Creating start game board"""
    board = []

    # Заполняем доску клетками
    for i in range(8):
        for j in range(8):
            board.append(Piece(Black, [j, i], sbd.get((i, j)))) if (i+j) % 2 != 0 else board.append(Piece(White, [j, i], sbd.get((i, j))))

    # Заполняем доску фигурами

    return board