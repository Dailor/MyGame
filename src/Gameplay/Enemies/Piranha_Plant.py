import pygame
from Enemy import Enemy
from Enemy_Configure import Piranha_Plant


class PiranhaPlant(Enemy):
    def __init__(self, gr, pos, x_max=None, *args):
        super().__init__(gr, pos, Piranha_Plant, x_max)

    def stay(self):
        if self.fps + 1 > 20:
            self.fps = 0
        self.image = Piranha_Plant[self.fps // 5]
        self.fps += 1