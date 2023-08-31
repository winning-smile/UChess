White = (255, 255, 255)
Black = (0, 0, 0)


def bishop_logic(board, color, x, y):
    """Return bishop possible moves list"""
    possible_moves = []
    bishop_moves_ur = []
    bishop_moves_lr = []
    bishop_moves_ul = []
    bishop_moves_ll = []
    bishop_moves_all = [bishop_moves_ur, bishop_moves_lr, bishop_moves_ul, bishop_moves_ll]

    for i, j, k in zip(range(x, 0, -1), range(y, 7, 1), range(1, 8, 1)):
        bishop_moves_ur.append([x - k, y + k])

    for i, j, k in zip(range(x, 7, 1), range(y, 7, 1), range(1, 8, 1)):
        bishop_moves_lr.append([x + k, y + k])

    for i, j, k in zip(range(x, 7, 1), range(y, 0, -1), range(1, 8, 1)):
        bishop_moves_ll.append([x + k, y - k])

    for i, j, k in zip(range(x, 0, -1), range(y, 0, -1), range(1, 8, 1)):
        bishop_moves_ul.append([x - k, y - k])

    if color == White:
        for bishop_moves in bishop_moves_all:
            for move in bishop_moves:
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
        for bishop_moves in bishop_moves_all:
            for move in bishop_moves:
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

