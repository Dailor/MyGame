import pygame
from Configure_Gameplay import STAR
from Characters import CharacterEvents
from Enemy import Enemy

pygame.init()
SIZE_CONST = 50


class Star(Enemy):
    def __init__(self, gr, pos, list, x_max=None, player=None, *args):
        super().__init__(gr, pos, STAR, player, x_max)

    def stay(self):
        if self.fps + 1 > 30:
            self.fps = 0
        self.image = STAR[self.fps // 5]
        self.fps += 1

    def damage_check(self, player):
        if pygame.sprite.collide_mask(self, player):
            if player.hp <= 2:
                player.hp += 1
            self.kill()
