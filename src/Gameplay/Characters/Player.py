from Character import Character
from CharacterEvents import *
from Configure_Gameplay import *
from Configure import SIZE
import pygame


def easy_difficult():
    return


def middle_difficult():
    return


def hard_difficult():
    return


# class Player(Character):
#     def __init__(self, groups, hp, dmg, stamina, regeneration=None, start_weapon=None):
#         super().__init__(groups, hp, dmg, stamina, regeneration=None, start_weapon=None)
#         self.image = pygame.Surface((20, 20))
#         self.image.fill((255, 0, 0))
#         self.rect = self.image.get_rect()
#         self.rect.x = 20
#         self.rect.y = SIZE[1] // 2

SIZE_CONST = 50


class Player(pygame.sprite.Sprite):
    def __init__(self, gr, pos, *args):
        super().__init__(gr)
        pos_x, pos_y = pos

        self.image = pygame.Surface((30, 30))
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = pos_x * SIZE_CONST, pos_y * SIZE_CONST
        self.image.fill((255, 20, 0))

        self.jump_enable = False
        self.clock = pygame.time.Clock()

    def event_handler(self, event):
        if event == MOVE_LEFT:
            self.rect.x -= SPEED_X
        elif event == MOVE_RIGHT:
            self.rect.x += SPEED_X
        elif event == MOVE_UP and self.jump_enable is False:
            self.jump_enable = True
            self.time_j = 0
            self.clock.tick()

        if self.jump_enable:
            self.jump()


    def jump(self):
        time = self.time_j + self.clock.tick() / 1000
        dy = V0 - GRAVITY * time ** 2 / 2
        if dy < 0:
            dy = 0
            self.jump_enable = False
        self.rect.y += dy

