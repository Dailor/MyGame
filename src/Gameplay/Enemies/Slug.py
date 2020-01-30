import pygame
from Enemy_Configure import Slug_stay
from Enemy import Enemy

pygame.init()

SIZE_CONST = 40


class Slug(Enemy):
    def __init__(self, gr, pos, x_max=None, player=None, *args):
        super().__init__(gr, pos, Slug_stay, player, x_max)

    def stay(self):
        if self.fps + 1 > 20:
            self.fps = 0
        self.image = Slug_stay[self.fps // 5]
        self.mask = pygame.mask.from_surface(self.image)
        self.fps += 1
