White = (255, 255, 255)
Black = (0, 0, 0)


def king_corner_check(king_moves):
    moves = []
    for move in king_moves:
        if move[0] in [0, 1, 2, 3, 4, 5, 6, 7] and move[1] in [0, 1, 2, 3, 4, 5, 6, 7]:
            moves.append(move)

    return moves


def king_castling_check(x, k_y, r_y, board):
    if k_y > r_y:
        for i in range(k_y-1, r_y, -1):
            if board[x][i]:
                return False
    else:
        for i in range(k_y+1, r_y, 1):
            if board[x][i]:
                return False

    return True


def king_logic(board, color, x, y):
    """Return king possible moves list"""
    possible_moves = []
    king_moves = [[x-1, y], [x-1, y+1], [x, y+1], [x+1, y+1], [x+1, y], [x+1, y-1], [x, y-1], [x-1, y-1]]
    king_moves = king_corner_check(king_moves)

    if color == White:
        for move in king_moves:
            x_new = move[0]
            y_new = move[1]
            if not board[x_new][y_new] or board[x_new][y_new].color == Black:
                possible_moves.append(move)
        if board[x][y]:
            if not board[x][y].first_move:
                if board[7][0] and not board[7][0].first_move:
                    if king_castling_check(7, 4, 0, board):
                        possible_moves.append([7, 2])
                if board[7][7] and not board[7][7].first_move:
                    if king_castling_check(7, 4, 7, board):
                        possible_moves.append([7, 6])
    else:
        for move in king_moves:
            x_new = move[0]
            y_new = move[1]
            if not board[x_new][y_new] or board[x_new][y_new].color == White:
                possible_moves.append(move)

        if board[x][y]:
            if not board[x][y].first_move:
                if board[0][0] and not board[0][0].first_move:
                    if king_castling_check(0, 4, 0, board):
                        possible_moves.append([0, 2])
                if board[0][7] and not board[0][7].first_move:
                    if king_castling_check(0, 4, 7, board):
                        possible_moves.append([0, 6])

    return possible_moves
