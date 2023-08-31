White = (255, 255, 255)
Black = (0, 0, 0)


def rook_logic(board, color, x, y):
    """Return rook possible moves list"""
    possible_moves = []
    rook_moves_u = []
    rook_moves_d = []
    rook_moves_l = []
    rook_moves_r = []
    rook_moves_all = [rook_moves_u, rook_moves_d, rook_moves_l, rook_moves_r]

    for i, j in zip(range(x, 7, 1), range(1, 8, 1)):
        rook_moves_u.append([x + j, y])

    for i, j in zip(range(x, 0, -1), range(1, 8, 1)):
        rook_moves_d.append([x - j, y])

    for i, j in zip(range(y, 7, 1), range(1, 8, 1)):
        rook_moves_l.append([x, y + j])

    for i, j in zip(range(y, 0, -1), range(1, 8, 1)):
        rook_moves_r.append([x, y - j])

    if color == White:
        for rook_moves in rook_moves_all:
            for move in rook_moves:
                x = move[0]
                y = move[1]
                if not board[x][y]:
                    possible_moves.append(move)
                elif board[x][y].color == Black:
                    possible_moves.append(move)
                    break
                elif board[x][y].color == White:
                    break
    else:
        for rook_moves in rook_moves_all:
            for move in rook_moves:
                x = move[0]
                y = move[1]
                if not board[x][y]:
                    possible_moves.append(move)
                elif board[x][y].color == White:
                    possible_moves.append(move)
                    break
                elif board[x][y].color == Black:
                    break

    return possible_moves
