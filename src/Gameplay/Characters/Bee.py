import pygame
from Utilities import sprite_sheet, load_image_v2

SIZE_CONST = 5


class Bee(pygame.sprite.Sprite):
    def __init__(self, gr, pos, x_max=None, *args):
        super().__init__(gr)
        self.x_max = x_max
        self.pos_x, self.pos_y = pos
        self.bee = load_image_v2(['Gameplay/Enemies', 'bee.png'], (37, 39))
        self.frames = sprite_sheet(self.bee, 8, 1)
        self.fps = 0
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pos_x * SIZE_CONST, self.pos_y * SIZE_CONST
        self.pos_x, self.pos_y = self.rect.x, self.rect.y

    def stay(self):
        if self.fps + 1 > 40:
            self.fps = 0
        self.image = self.frames[self.fps // 5]
