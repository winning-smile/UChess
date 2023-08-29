import pygame
from settings import Black, White
import numpy as np

# TODO castling
# TODO Check\mate
# TODO taking on the pass
class Logic_Figure:
    def __init__(self, color, value, xy):
        self.first_move = False     # Флаг первого хода фигуры
        self.color = color          # Цвет фигуры
        self.val = value            # Значение фигуры
        self.x = xy[0]              # Координата по х
        self.y = xy[1]              # Координата по y

def logic(val, color, x, y):
    """возвращает массив доступных ходов"""
    return logic_dict[val](logic_board, color, x, y)

def move_logic_figure(old_x, old_y, new_y, new_x, board):
    """Перемещает фигуру на логической доске"""
    flag = "move"
    if board[new_x][new_y]:
        flag = "kill"
    tmp = board[old_x][old_y]
    board[old_x][old_y] = 0
    board[new_x][new_y] = tmp
    return board, flag

def print_lg_board(board):
    """Вывод логической доски для отладки"""
    for i in range(len(board)):
        print("")
        for j in range(len(board)):
            if board[i][j]:
                print(board[i][j].val, end=" ")
            else:
                print(board[i][j], end=" ")

    print("")

def pawn_corner_check(x, y):
    corner_x_dict = {0: "U", 8: "D"}
    corner_y_dict = {7: "R", 0: "L"}

    if x in list(corner_x_dict.keys()):
        return corner_x_dict[x]

    if y in list(corner_y_dict.keys()):
        return corner_y_dict[y]

def pawn_logic(board, color, x, y):
    """Создание массива возможных ходов пешки"""
    possible_moves = []

    if color == White:
        pcc_flag = pawn_corner_check(x, y)

        if pcc_flag != "U":
            if not board[x-1][y]:
                possible_moves.append([x - 1, y])
            if pcc_flag != "L":
                if board[x-1][y-1] and board[x - 1][y - 1].color == Black:
                    possible_moves.append([x - 1, y - 1])
            if pcc_flag != "R":
                if board[x-1][y+1] and board[x - 1][y + 1].color == Black:
                    possible_moves.append([x - 1, y + 1])

    else:
        pcc_flag = pawn_corner_check(x, y)

        if pcc_flag != "D":
            if not board[x+1][y]:
                possible_moves.append([x + 1, y])
            if pcc_flag != "L":
                if board[x+1][y-1] and board[x + 1][y - 1].color == White:
                    possible_moves.append([x + 1, y - 1])
            if pcc_flag != "R":
                if board[x+1][y+1] and board[x + 1][y + 1].color == White:
                    possible_moves.append([x + 1, y + 1])

    return possible_moves

def rook_logic(board, color, x, y):
    """Создание массива возможных ходов ладьи"""
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

    return possible_moves


def knight_corner_check(knight_moves):
    moves = []
    for move in knight_moves:
        if move[0] in [0, 1, 2, 3, 4, 5, 6, 7] and move[1] in [0, 1, 2, 3, 4, 5, 6, 7]:
            moves.append(move)

    return moves


def knight_logic(board, color, x, y):
    """Создание массива возможных ходов коня"""
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

def bishop_logic(board, color, x, y):
    """Создание массива возможных ходов слона"""
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

def queen_logic(board, color, x, y):
    possible_moves = []
    possible_moves.extend(bishop_logic(board, color, x, y))
    possible_moves.extend(rook_logic(board, color, x, y))

    return possible_moves

def king_corner_check(king_moves):
    moves = []
    for move in king_moves:
        if move[0] in [0, 1, 2, 3, 4, 5, 6, 7] and move[1] in [0, 1, 2, 3, 4, 5, 6, 7]:
            moves.append(move)

    return moves

def king_logic(board, color, x, y):
    """Создание массива возможных ходов короля"""
    possible_moves = []
    king_moves = [[x-1, y], [x-1, y+1], [x, y+1], [x+1, y+1], [x+1, y], [x+1, y-1], [x, y-1], [x-1, y-1]]
    king_moves = king_corner_check(king_moves)

    if color == White:
        for move in king_moves:
            x = move[0]
            y = move[1]
            if not board[x][y] or board[x][y].color == Black:
                possible_moves.append(move)
    else:
        for move in king_moves:
            x = move[0]
            y = move[1]
            if not board[x][y] or board[x][y].color == White:
                possible_moves.append(move)

    return possible_moves
def create_logic_board():
    """Создание логической доски для вычисления возможных ходов фигур"""
    lb = np.zeros((8, 8), dtype=object)

    # Создаём логическую доску
    lb[0][0] = Logic_Figure(Black, "R", [0, 0])
    lb[0][1] = Logic_Figure(Black, "K", [0, 1])
    lb[0][2] = Logic_Figure(Black, "B", [0, 2])
    lb[0][3] = Logic_Figure(Black, "Q", [0, 3])
    lb[0][4] = Logic_Figure(Black, "S", [0, 4])
    lb[0][5] = Logic_Figure(Black, "B", [0, 5])
    lb[0][6] = Logic_Figure(Black, "K", [0, 6])
    lb[0][7] = Logic_Figure(Black, "R", [0, 7])

    for i in range(8):
        lb[1][i] = Logic_Figure(Black, "P", [1, i])

    for i in range(8):
        lb[6][i] = Logic_Figure(White, "P", [6, i])

    lb[7][0] = Logic_Figure(White, "R", [7, 0])
    lb[7][1] = Logic_Figure(White, "K", [7, 1])
    lb[7][2] = Logic_Figure(White, "B", [7, 2])
    lb[7][3] = Logic_Figure(White, "Q", [7, 3])
    lb[7][4] = Logic_Figure(White, "S", [7, 4])
    lb[7][5] = Logic_Figure(White, "B", [7, 5])
    lb[7][6] = Logic_Figure(White, "K", [7, 6])
    lb[7][7] = Logic_Figure(White, "R", [7, 7])

    return lb


def create_available_moves_sprites(moves, available_moves_sprites):
    """По массиву возможных ходов добавляем спрайт хода для будущей отрисовки"""
    for sprite in available_moves_sprites:
        sprite.kill()
        del sprite

    available_moves_sprites.empty()

    for move in moves:
        sprite = pygame.sprite.Sprite()
        sprite.image = pygame.image.load("img/possible_move.png").convert_alpha()
        sprite.x = move[1]
        sprite.y = move[0]
        sprite.rect = sprite.image.get_rect(center=(360 + sprite.x * 80, 80 + sprite.y * 80))
        available_moves_sprites.add(sprite)

    return available_moves_sprites


logic_board = create_logic_board()
logic_dict = {"P": pawn_logic, "R": rook_logic, "K": knight_logic, "B": bishop_logic, "Q": queen_logic, "S": king_logic}
