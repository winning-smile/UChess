from settings import *

img_dict = {(Black, "P"): "img/bP.png", (Black, "R"): "img/bR.png", (Black, "K"): "img/bN.png",
            (Black, "B"): "img/bB.png", (Black, "Q"): "img/bQ.png", (Black, "S"): "img/bK.png",
            (White, "P"): "img/wP.png", (White, "R"): "img/wR.png", (White, "K"): "img/wN.png",
            (White, "B"): "img/wB.png", (White, "Q"): "img/wQ.png", (White, "S"): "img/wK.png"}


class Figure(pygame.sprite.Sprite):
    """Game figure class"""
    def __init__(self, color, value, xy):
        super().__init__()
        self.first_move = False     # First turn flag
        self.color = color          # Figure color
        self.val = value            # Figure value
        self.x = xy[0]              # Figure x coord
        self.y = xy[1]              # Figure y coord

        # Figure image and rect
        self.image = pygame.image.load(img_dict[(self.color, self.val)]).convert_alpha()
        self.rect = self.image.get_rect(center=(360 + self.y*80, 80 + self.x*80))

    def flow_figure(self, x, y):
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(self.y, self.x))

    def move_figure(self, x, y):
        """Moves figure on x,y coords"""
        print("yes")
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(360 + self.y * 80, 80 + self.x * 80))

    def to_queen(self):
        self.val = "Q"
        self.image = pygame.image.load(img_dict[(self.color, self.val)]).convert_alpha()
        self.rect = self.image.get_rect(center=(360 + self.y * 80, 80 + self.x * 80))