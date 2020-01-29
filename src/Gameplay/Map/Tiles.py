import pygame

from Configure_Map import *
from Utilities import load_image


class Tile(pygame.sprite.Sprite):
    def __init__(self, groups, size, pos, path):
        x, y = pos
        if (isinstance(groups, tuple) or isinstance(groups, list)) is False:
            groups = (groups,)
        super().__init__(*groups)
        self.image = load_image([TILES_PATH, path])
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x * BLOCK_SIZE[0], y * BLOCK_SIZE[0]
        self.pos_x, self.pos_y = self.rect.x, self.rect.y


class GrassBlock(Tile):
    def __init__(self, groups, pos):
        super().__init__(groups, BLOCK_SIZE, pos, GRASS_BLOCK)


class SmallStoneBlock(Tile):
    def __init__(self, groups, pos):
        super().__init__(groups, BLOCK_SIZE, pos, SMALL_STONE)


class Dirty(Tile):
    def __init__(self, groups, pos):
        super().__init__(groups, BLOCK_SIZE, pos, DIRTY_BLOCK)


class Platform(Tile):
    def __init__(self, groups, pos):
        super().__init__(groups, BLOCK_SIZE, pos, PLATFORM)


