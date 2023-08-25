class Piece:
    def __init__(self, color, xy, figure=None):
        self.color = color          # Цвет клетки
        self.x = xy[0]              # Координата по y
        self.y = xy[1]              # Координата по x
        self.figure = figure        # id фигуры стоящей на клетке


class Figure:
    def __init__(self, color, value):
        self.first_move = False     # Флаг первого хода фигуры
        self.color = color          # Цвет фигуры
        self.val = value            # Значение фигуры
