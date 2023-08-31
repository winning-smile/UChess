White = (255, 255, 255)
Black = (0, 0, 0)


def pawn_corner_check(x, y):
    corner_x_dict = {0: "U", 8: "D"}
    corner_y_dict = {7: "R", 0: "L"}

    if x in list(corner_x_dict.keys()):
        return corner_x_dict[x]

    if y in list(corner_y_dict.keys()):
        return corner_y_dict[y]


def pawn_logic(board, color, x, y):
    """Return pawn possible moves list"""
    possible_moves = []

    if color == White:
        pcc_flag = pawn_corner_check(x, y)

        if pcc_flag != "U":
            if board[x][y]:
                if not board[x-1][y]:
                    possible_moves.append([x - 1, y])
                    if not board[x-2][y] and not board[x][y].first_move:
                        possible_moves.append([x - 2, y])
                if pcc_flag != "L":
                    if board[x-1][y-1] and board[x - 1][y - 1].color == Black:
                        possible_moves.append([x - 1, y - 1])
                if pcc_flag != "R":
                    if board[x-1][y+1] and board[x - 1][y + 1].color == Black:
                        possible_moves.append([x - 1, y + 1])

    else:
        pcc_flag = pawn_corner_check(x, y)

        if pcc_flag != "D":
            if board[x][y]:
                if not board[x+1][y]:
                    possible_moves.append([x + 1, y])
                    if not board[x + 2][y] and not board[x][y].first_move:
                        possible_moves.append([x + 2, y])
                if pcc_flag != "L":
                    if board[x+1][y-1] and board[x + 1][y - 1].color == White:
                        possible_moves.append([x + 1, y - 1])
                if pcc_flag != "R":
                    if board[x+1][y+1] and board[x + 1][y + 1].color == White:
                        possible_moves.append([x + 1, y + 1])

    return possible_moves
