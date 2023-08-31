from figure_classes.rook import rook_logic
from figure_classes.bishop import bishop_logic

def queen_logic(board, color, x, y):
    """Return queen possible moves list"""
    possible_moves = []
    possible_moves.extend(bishop_logic(board, color, x, y))
    possible_moves.extend(rook_logic(board, color, x, y))

    return possible_moves
