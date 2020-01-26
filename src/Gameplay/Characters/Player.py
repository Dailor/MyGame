from Character import Character
from CharacterEvents import *
from Configure_Gameplay import *
from Configure import SIZE
import pygame
import threading


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


class PlayerEvents(threading.Thread):
    def __init__(self):
        super().__init__()
        self.running = True

    def run(self):
        while self.running:
            break


class Player(pygame.sprite.Sprite):
    def __init__(self, gr, pos, clock, *args):
        super().__init__(gr)
        self.clock = clock
        self.pos_x, self.pos_y = pos

        self.image = pygame.Surface((30, 30))
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = self.pos_x * SIZE_CONST, self.pos_y * SIZE_CONST
        self.pos_x, self.pos_y = self.rect.x, self.rect.y
        self.image.fill((255, 20, 0))


        self.jump_enable = False

    def event_handler(self, event):
        time = self.clock[0] / 1000
        print(time)
        if event == MOVE_LEFT:
            self.pos_x -= SPEED_X * time
        elif event == MOVE_RIGHT:
            self.pos_x += SPEED_X * time
        self.rect.x = self.pos_x
        #print(self.pos_x)