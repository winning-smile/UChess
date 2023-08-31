import pygame
from settings import Black, White, CELLSIZE
import numpy as np
from figure_classes.fclass import Figure
from figure_classes.queen import queen_logic
from figure_classes.king import king_logic
from figure_classes.rook import rook_logic
from figure_classes.bishop import bishop_logic
from figure_classes.knight import knight_logic
from figure_classes.pawn import pawn_logic

# TODO Check\mate
# TODO taking on the pass


def get_figure_under_mouse(x, y, board, turn_flag):
    if 960 > x > 320 and 680 > y > 40:
        tmp = board[(y-40) // CELLSIZE][(x-320) // CELLSIZE]
        if tmp and tmp.color == turn_flag:
            return tmp


def get_norm_coords(x, y):
    if 960 > x > 320 and 680 > y > 40:
        return (y-40) // CELLSIZE, (x-320) // CELLSIZE


def dragndrop(x, y, selected_figure):
    if selected_figure:
        selected_figure.flow_figure(y, x)

    return (y-40)//CELLSIZE, (x-320) // CELLSIZE


def logic(val, color, x, y, board):
    """Return list of available moves for selected figure"""
    return logic_dict[val](board, color, x, y)


def find_king_coords(board, color):
    for figure in board.ravel():
        if figure and figure.val == "S" and figure.color == color:
            return [figure.x, figure.y]


def check_mate(board, old_x, old_y, new_y, new_x):
    l_board_copy = board.copy()
    opposite_figures = []
    king_coords = find_king_coords(l_board_copy, l_board_copy[old_x][old_y].color)

    for figure in l_board_copy.ravel():
        if figure and figure.color != l_board_copy[old_x][old_y].color:
            opposite_figures.append(figure)

    l_board_copy, flag = move_logic_figure(old_x, old_y, new_y, new_x, l_board_copy)

    for figure in opposite_figures:
        possible_moves = logic(figure.val, figure.color, figure.x, figure.y, l_board_copy)
        for move in possible_moves:
            if move == king_coords:
                return True

    return False


def move_logic_figure(old_x, old_y, new_y, new_x, board):
    """Move figure on logic board"""

    flag = "move"
    print("MOVE COORDS", new_x, new_y)
    if board[new_x][new_y]:

        print("KILL COORDS", new_x, new_y)
        flag = "kill"

    if board[old_x][old_y].val == "S" and not board[old_x][old_y].first_move:
        if board[old_x][old_y].color == White:
            if board[new_x][new_y+1] and board[new_x][new_y+1].val == "R" and (not board[new_x][new_y+1].first_move) and board[new_x][new_y+1].color == board[old_x][old_y].color:
                flag = "wsc"

                tmp = board[old_x][old_y]
                board[old_x][old_y] = 0
                board[new_x][new_y] = tmp
                tmp = board[new_x][new_y+1]
                board[new_x][new_y + 1] = 0
                board[new_x][new_y - 1] = tmp

                board[new_x][new_y].first_move = True
                board[new_x][new_y - 1].first_move = True
                return board, flag

            elif board[new_x][new_y-2] and board[new_x][new_y-2].val == "R" and (not board[new_x][new_y-2].first_move) and board[new_x][new_y-2].color == board[old_x][old_y].color:
                flag = "wlc"

                tmp = board[old_x][old_y]
                board[old_x][old_y] = 0
                board[new_x][new_y] = tmp
                tmp = board[new_x][new_y - 2]
                board[new_x][new_y - 2] = 0
                board[new_x][new_y + 1] = tmp

                board[new_x][new_y].first_move = True
                board[new_x][new_y + 1].first_move = True
                return board, flag

        else:
            if board[new_x][new_y+1] and board[new_x][new_y+1].val == "R" and (not board[new_x][new_y+1].first_move) and board[new_x][new_y+1].color == board[old_x][old_y].color:
                flag = "bsc"

                tmp = board[old_x][old_y]
                board[old_x][old_y] = 0
                board[new_x][new_y] = tmp
                tmp = board[new_x][new_y+1]
                board[new_x][new_y + 1] = 0
                board[new_x][new_y - 1] = tmp

                board[new_x][new_y].first_move = True
                board[new_x][new_y - 1].first_move = True
                return board, flag

            elif board[new_x][new_y-2] and board[new_x][new_y-2].val == "R" and (not board[new_x][new_y-2].first_move) and board[new_x][new_y-2].color == board[old_x][old_y].color:
                flag = "blc"

                tmp = board[old_x][old_y]
                board[old_x][old_y] = 0
                board[new_x][new_y] = tmp
                tmp = board[new_x][new_y - 2]
                board[new_x][new_y - 2] = 0
                board[new_x][new_y + 1] = tmp

                board[new_x][new_y].first_move = True
                board[new_x][new_y + 1].first_move = True
                return board, flag

    board[old_x][old_y].first_move = True
    tmp = board[old_x][old_y]
    board[old_x][old_y] = 0
    board[new_x][new_y] = tmp

    return board, flag


def print_lg_board(board):
    """Logic board output"""
    for i in range(len(board)):
        print("")
        for j in range(len(board)):
            if board[i][j]:
                print(board[i][j].val, end=" ")
            else:
                print(board[i][j], end=" ")

    print("")


def create_logic_board():
    """Create logic board"""
    lb = np.zeros((8, 8), dtype=object)

    lb[0][0] = Figure(Black, "R", [0, 0])
    lb[0][1] = Figure(Black, "K", [0, 1])
    lb[0][2] = Figure(Black, "B", [0, 2])
    lb[0][3] = Figure(Black, "Q", [0, 3])
    lb[0][4] = Figure(Black, "S", [0, 4])
    lb[0][5] = Figure(Black, "B", [0, 5])
    lb[0][6] = Figure(Black, "K", [0, 6])
    lb[0][7] = Figure(Black, "R", [0, 7])

    for i in range(8):
        lb[1][i] = Figure(Black, "P", [1, i])

    for i in range(8):
        lb[6][i] = Figure(White, "P", [6, i])

    lb[7][0] = Figure(White, "R", [7, 0])
    lb[7][1] = Figure(White, "K", [7, 1])
    lb[7][2] = Figure(White, "B", [7, 2])
    lb[7][3] = Figure(White, "Q", [7, 3])
    lb[7][4] = Figure(White, "S", [7, 4])
    lb[7][5] = Figure(White, "B", [7, 5])
    lb[7][6] = Figure(White, "K", [7, 6])
    lb[7][7] = Figure(White, "R", [7, 7])

    return lb


def create_available_moves_sprites(moves, available_moves_sprites):
    """ Create available moves sprites from available moves list"""
    for sprite in available_moves_sprites:
        sprite.kill()
        del sprite

    available_moves_sprites.empty()

    available_moves = []
    for move in moves:
        available_moves.append(move)
        sprite = pygame.sprite.Sprite()
        sprite.image = pygame.image.load("img/possible_move.png").convert_alpha()
        sprite.x = move[1]
        sprite.y = move[0]
        sprite.rect = sprite.image.get_rect(center=(360 + sprite.x * 80, 80 + sprite.y * 80))
        available_moves_sprites.add(sprite)

    return available_moves_sprites, available_moves


logic_board = create_logic_board()
logic_dict = {"P": pawn_logic, "R": rook_logic, "K": knight_logic, "B": bishop_logic, "Q": queen_logic, "S": king_logic}
