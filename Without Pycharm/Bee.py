import pygame
from Utilities import sprite_sheet, load_image_v2
from Enemy_Configure import Bee_stay
from Enemy import Enemy

SIZE_CONST = 40
FPS = 30


class Bee(Enemy):
    def __init__(self, gr, pos, x_max=None, player=None, *args):
        super().__init__(gr, pos, Bee_stay, x_max, player)
        self.clock = pygame.time.Clock()

    def stay(self):
        if self.fps + 1 > 30:
            self.fps = 0
        self.image = Bee_stay[self.fps // 5]
        self.mask = pygame.mask.from_surface(self.image)
        self.fps += 1
        self.clock.tick(FPS)
