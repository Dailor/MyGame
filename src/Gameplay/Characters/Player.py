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


class Player(Character):
    def __init__(self, groups, hp, dmg, stamina, regeneration=None, start_weapon=None):
        super().__init__(groups, hp, dmg, stamina, regeneration=None, start_weapon=None)
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = SIZE[1] // 2

    def append(self, event):
        self.events.append(event)

    def event_handler(self):
        while len(self.events):
            event = self.events.pop()
            if event == MOVE_LEFT:
                self.rect.x -= SPEED_X
            elif event == MOVE_RIGHT:
                self.rect.x += SPEED_X
