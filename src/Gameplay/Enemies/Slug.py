import pygame
from Enemy_Configure import Slug_stay
from Enemy import Enemy

pygame.init()

SIZE_CONST = 40


class Slug(Enemy):
    def __init__(self, gr, pos, x_max=None, player=None, *args):
        super().__init__(gr, pos, Slug_stay, player, x_max)
        self.gr = gr

    def stay(self):
        if self.fps + 1 > 20:
            self.fps = 0
        self.image = Slug_stay[self.fps // 5]
        self.mask = pygame.mask.from_surface(self.image)
        self.fps += 1

    def drop_down(self):
        while True:
            collides = [t for t in pygame.sprite.spritecollide(self, self.gr, False) if t != self]
            if len(collides) == 0:
                self.rect.y += 1
                self.pos_y += 1
            else:
                break
