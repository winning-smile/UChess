White = (255, 255, 255)
Black = (0, 0, 0)


def knight_corner_check(knight_moves):
    moves = []
    for move in knight_moves:
        if move[0] in [0, 1, 2, 3, 4, 5, 6, 7] and move[1] in [0, 1, 2, 3, 4, 5, 6, 7]:
            moves.append(move)

    return moves


def knight_logic(board, color, x, y):
    """Return knight possible moves list"""
    knight_moves = [[x-2, y+1], [x-1, y+2], [x+1, y+2], [x+2, y+1], [x+2, y-1], [x+1, y-2], [x-1, y-2], [x-2, y-1]]
    possible_moves = []
    knight_moves = knight_corner_check(knight_moves)

    if color == White:
        for move in knight_moves:
            x = move[0]
            y = move[1]
            if not board[x][y] or board[x][y].color == Black:
                possible_moves.append(move)
    else:
        for move in knight_moves:
            x = move[0]
            y = move[1]
            if not board[x][y] or board[x][y].color == White:
                possible_moves.append(move)

    return possible_moves
