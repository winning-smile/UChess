from classes import Figure
from settings import Black, White

# Start board dictionary
sbd = { (0, 0): Figure(Black, "R", [0, 0]), (0, 7): Figure(Black, "R", [0, 7]),
        (0, 1): Figure(Black, "K", [0, 1]), (0, 6): Figure(Black, "K", [0, 6]),
        (0, 2): Figure(Black, "B", [0, 2]), (0, 5): Figure(Black, "B", [0, 5]),
        (0, 3): Figure(Black, "Q", [0, 3]), (0, 4): Figure(Black, "S", [0, 4]),

        (7, 0): Figure(White, "R", [7, 0]), (7, 7): Figure(White, "R", [7, 7]),
        (7, 1): Figure(White, "K", [7, 1]), (7, 6): Figure(White, "K", [7, 6]),
        (7, 2): Figure(White, "B", [7, 2]), (7, 5): Figure(White, "B", [7, 5]),
        (7, 3): Figure(White, "Q", [7, 3]), (7, 4): Figure(White, "S", [7, 4]),

        (1, 0): Figure(Black, "P", [1, 0]), (1, 1): Figure(Black, "P", [1, 1]),
        (1, 2): Figure(Black, "P", [1, 2]), (1, 3): Figure(Black, "P", [1, 3]),
        (1, 4): Figure(Black, "P", [1, 4]), (1, 5): Figure(Black, "P", [1, 5]),
        (1, 6): Figure(Black, "P", [1, 6]), (1, 7): Figure(Black, "P", [1, 7])
    ,
        (6, 0): Figure(White, "P", [6, 0]), (6, 1): Figure(White, "P", [6, 1]),
        (6, 2): Figure(White, "P", [6, 2]), (6, 3): Figure(White, "P", [6, 3]),
        (6, 4): Figure(White, "P", [6, 4]), (6, 5): Figure(White, "P", [6, 5]),
        (6, 6): Figure(White, "P", [6, 6]), (6, 7): Figure(White, "P", [6, 7])}


def create_visual_board():
    """Creating start game board"""
    board = []
    # Заполняем доску фигурами
    for i in range(8):
        for j in range(8):
            if (i, j) in sbd.keys():
                board.append(sbd[(i, j)])

    return board
