from classes import Figure
from settings import Black, White

# Start board dictionary
sbd = { (0, 0) : Figure(Black, "R", [0, 0]), (0, 7) : Figure(Black, "R", [7, 0]),
        (0, 1) : Figure(Black, "K", [1, 0]), (0, 6) : Figure(Black, "K", [6, 0]),
        (0, 2) : Figure(Black, "B", [2, 0]), (0, 5) : Figure(Black, "B", [5, 0]),
        (0, 3) : Figure(Black, "Q", [3, 0]), (0, 4) : Figure(Black, "S", [4, 0]),

        (7, 0) : Figure(White, "R", [0, 7]), (7, 7) : Figure(White, "R", [7, 7]),
        (7, 1) : Figure(White, "K", [1, 7]), (7, 6) : Figure(White, "K", [6, 7]),
        (7, 2) : Figure(White, "B", [2, 7]), (7, 5) : Figure(White, "B", [5, 7]),
        (7, 3) : Figure(White, "Q", [3, 7]), (7, 4) : Figure(White, "S", [4, 7]),

        (1, 0) : Figure(Black, "P", [0, 1]), (1, 1) : Figure(Black, "P", [1, 1]),
        (1, 2) : Figure(Black, "P", [2, 1]), (1, 3) : Figure(Black, "P", [3, 1]),
        (1, 4) : Figure(Black, "P", [4, 1]), (1, 5) : Figure(Black, "P", [5, 1]),
        (1, 6) : Figure(Black, "P", [6, 1]), (1, 7) : Figure(Black, "P", [7, 1]),

        (6, 0) : Figure(White, "P", [0, 6]), (6, 1) : Figure(White, "P", [1, 6]),
        (6, 2) : Figure(White, "P", [2, 6]), (6, 3) : Figure(White, "P", [3, 6]),
        (6, 4) : Figure(White, "P", [4, 6]), (6, 5) : Figure(White, "P", [5, 6]),
        (6, 6) : Figure(White, "P", [6, 6]), (6, 7) : Figure(White, "P", [7, 6])}

def start():
    """Creating start game board"""
    board = []

    # Заполняем доску фигурами
    for i in range(8):
        for j in range(8):
            if (i, j) in sbd.keys():
                board.append(sbd[(i, j)])

    return board