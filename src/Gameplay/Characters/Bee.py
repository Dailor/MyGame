import pygame
from Utilities import sprite_sheet, load_image_v2
from Enemy_Configure import Bee_stay
from Enemy import Enemy

SIZE_CONST = 40


class Bee(Enemy):
    def __init__(self, gr, pos, x_max=None, *args):
        super().__init__(gr, pos, Bee_stay, x_max)

    def stay(self):
        if self.fps + 1 > 30:
            self.fps = 0
        self.image = Bee_stay[self.fps // 5]
        self.fps += 1
