import pygame
import sys
from Configure_Map import *


class Background(pygame.sprite.Sprite):
    def __init__(self, screen, group, PATH, SIZE, SPEED, clock, colorkey=None, x_max=None):
        super().__init__(group)
        self.clock = clock
        self.screen = screen
        self.PATH_BG = PATH
        self.BG_SIZE = SIZE
        self.BG_SPEED = SPEED
        self.colorkey = colorkey

        self.main_bg_speed = BG_SPEED
        self.x_now = 0
        self.x_max = sys.maxsize if x_max is None else x_max

        self.image = pygame.Surface(self.BG_SIZE)
        self.rect = self.image.get_rect()

        self.load_background()
        self.image.blit(self.img, (0, 0))

    def load_background(self):
        self.img = pygame.image.load(self.PATH_BG)
        if self.colorkey is not None:
            self.image.set_colorkey(self.colorkey)

        self.img = pygame.transform.scale(self.img, self.BG_SIZE)

        self.left_img_x = 0
        self.right_img_x = self.BG_SIZE[0]

    def update(self, move, *args):
        t = self.clock[0] / 1000
        if move == '>':
            dx = -self.BG_SPEED[0]
            dx_ = -self.main_bg_speed[0]
        elif move == '<':
            dx = self.BG_SPEED[0]
            dx_ = self.main_bg_speed[0]

        dx *= t
        dx_ *= t

        if self.x_now + dx_ < 0 or self.x_now + dx_ + self.BG_SIZE[0] > self.x_max:
            return
        else:
            self.x_now += dx_

        self.left_img_x -= dx
        self.right_img_x -= dx
        if self.left_img_x > 0:
            self.right_img_x = self.left_img_x - self.BG_SIZE[0]
            self.left_img_x, self.right_img_x = self.right_img_x, self.left_img_x
        elif self.right_img_x < 0:
            self.left_img_x = self.right_img_x + self.BG_SIZE[0]
            self.left_img_x, self.right_img_x = self.right_img_x, self.left_img_x

        self.image.fill((0, 0, 0))
        self.image.blit(self.img, (int(self.left_img_x), 0))
        self.image.blit(self.img, (int(self.right_img_x), 0))


class ForrestBackgroundMain(Background):
    def __init__(self, screen, group, clock, x_max=None):
        super().__init__(screen, group, PATH_BG, BG_SIZE, BG_SPEED, clock, None, x_max)


class ForrestBackgroundFront(Background):
    def __init__(self, screen, group, clock, x_max=None):
        super().__init__(screen, group, PATH_MF, MF_SIZE, MF_SPEED, clock, (0, 0, 0), x_max)
