import pygame

from Configure_Map import *
from Utilities import load_image

BLOCK_SIZE = 50, 50

class Tile(pygame.sprite.Sprite):
    def __init__(self, groups, size, pos, path):
        x, y = pos
        if (isinstance(groups, tuple) or isinstance(groups, list)) is False:
            groups = (groups,)
        super().__init__(*groups)
        self.image = load_image([TILES_PATH, path])
        self.image = pygame.transform.scale(self.image, size)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x * BLOCK_SIZE[0], y * BLOCK_SIZE[0]
        self.pos_x, self.pos_y = self.rect.x, self.rect.y
        self.rel_pos_x, self.rel_pos_y = self.rect.x, self.rect.y


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


class House(Tile):
    def __init__(self, groups, pos):
        super().__init__(groups, BLOCK_SIZE, pos, HOUSE)


class Bush(Tile):
    def __init__(self, groups, pos):
        super().__init__(groups, BLOCK_SIZE, pos, BUSH)


class Tree(Tile):
    def __init__(self, groups, pos):
        super().__init__(groups, BLOCK_SIZE, pos, TREE)


class Rock(Tile):
    def __init__(self, groups, pos):
        super().__init__(groups, BLOCK_SIZE, pos, ROCK)


class Door(Tile):
    def __init__(self, groups, pos):
        super().__init__(groups, BLOCK_SIZE, pos, DOOR)


class CrankDown(Tile):
    def __init__(self, groups, pos):
        super().__init__(groups, BLOCK_SIZE, pos, CRANK_DOWN)


class CrankUp(Tile):
    def __init__(self, groups, pos):
        super().__init__(groups, BLOCK_SIZE, pos, CRANK_UP)


class FaceBlock(Tile):
    def __init__(self, groups, pos):
        super().__init__(groups, BLOCK_SIZE, pos, FACE_BLOCK)


class Shrooms(Tile):
    def __init__(self, groups, pos):
        super().__init__(groups, BLOCK_SIZE, pos, SHROOMS)


class Sign(Tile):
    def __init__(self, groups, pos):
        super().__init__(groups, BLOCK_SIZE, pos, SIGN)


class Skulls(Tile):
    def __init__(self, groups, pos):
        super().__init__(groups, BLOCK_SIZE, pos, SKULLS)


class Spikes(Tile):
    def __init__(self, groups, pos):
        super().__init__(groups, BLOCK_SIZE, pos, SPIKES)


class SpikesSkull(Tile):
    def __init__(self, groups, pos):
        super().__init__(groups, BLOCK_SIZE, pos, SPIKES_SKULL)


class SpikesTop(Tile):
    def __init__(self, groups, pos):
        super().__init__(groups, BLOCK_SIZE, pos, SPIKES_TOP)
