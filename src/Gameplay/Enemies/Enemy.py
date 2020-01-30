import pygame

SIZE_CONST = 40


class Enemy(pygame.sprite.Sprite):
    def __init__(self, gr, pos, list, x_max=None, *args):
        super().__init__(gr)
        self.x_max = x_max
        self.pos_x, self.pos_y = pos
        self.bee = list[0]
        self.fps = 0
        self.image = self.bee
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pos_x * SIZE_CONST, self.pos_y * SIZE_CONST
        self.pos_x, self.pos_y = self.rect.x, self.rect.y
