from Character import Character
from CharacterEvents import *
from Configure_Gameplay import *
from Utilities import load_image_v2
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

    def __init__(self, gr, pos, clock, x_max, *args):
        super().__init__(gr)
        self.x_max = x_max
        self.clock = clock
        self.pos_x, self.pos_y = pos

        self.stay = load_image_v2(['Gameplay/Character/idle', 'adventurer-idle-00.png'], PLAYER_SIZE)
        self.image = self.stay
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = self.pos_x * SIZE_CONST, self.pos_y * SIZE_CONST
        self.pos_x, self.pos_y = self.rect.x, self.rect.y
        self.pos_rel_x, self.pos_rel_x = self.pos_x, self.pos_y

        self.jump_enable = False

        self.fps = 0
        self.walkRight = [load_image_v2(path, PLAYER_SIZE) for path in ANIM_walkRight]

        self.walkLeft = [load_image_v2(path, PLAYER_SIZE) for path in ANIM_walkLeft]

        self.attackLeft = [load_image_v2(path, PLAYER_SIZE) for path in ANIM_attackLeft]

        self.attackRight = [load_image_v2(path, PLAYER_SIZE) for path in ANIM_attackRight]

        self.airLeft = [load_image_v2(path, PLAYER_SIZE) for path in ANIM_airLeft]

        self.airRight = [load_image_v2(path, PLAYER_SIZE) for path in ANIM_airRight]

        self.stay_images = [load_image_v2(path, PLAYER_SIZE) for path in ANIM_stay_images]

        self.is_right = False
        self.is_left = False
        self.attack = False
        self.air_attack = False
        self.stay_ = True
        self.for_attack = 0
        self.for_air_attack = 0
        self.for_stay = 0
        self.Jump_Count = 10

    def event_handler(self, event):
        time = self.clock[0] / 1000
        if event == MOVE_LEFT:
            dx = SPEED_X * time
            self.pos_x -= dx
            self.pos_rel_x -= dx
            self.is_right = False
            self.is_left = True
            self.stay_ = False
        elif event == MOVE_RIGHT:
            dx = SPEED_X * time
            self.pos_x += dx
            self.pos_rel_x += dx
            self.is_right = True
            self.is_left = False
            self.stay_ = False
        elif event == MOVE_UP and self.jump_enable is False:
            self.jump_enable = True
        elif event == ATTACK and self.jump_enable is True:
            self.air_attack = True
            self.stay_ = False
        elif event == ATTACK and self.attack is False:
            self.attack = True
            self.stay_ = False
        else:
            self.stay_ = True
        self.rect.x = self.pos_x
        self.render()

    def render(self):
        if self.fps + 1 >= 30:
            self.fps = 0

        if not self.is_left and not self.is_right:
            self.image = self.stay

        if self.is_left:
            self.image = self.walkLeft[self.fps // 5]
            self.fps += 1
        elif self.is_right:
            self.image = self.walkRight[self.fps // 5]
            self.fps += 1
        else:
            self.image = self.stay

        if self.attack:
            if self.for_attack + 1 >= 30:
                self.for_attack = 0
            if self.is_left:
                self.image = self.attackLeft[self.for_attack // 5]
                self.for_attack += 1
            elif self.is_right:
                self.image = self.attackRight[self.for_attack // 5]
                self.for_attack += 1
            self.attack = False

        if self.air_attack:
            if self.for_air_attack + 1 >= 20:
                self.for_air_attack = 0
            if self.is_left:
                self.image = self.airLeft[self.for_air_attack // 5]
                self.for_air_attack += 1
            elif self.is_right:
                self.image = self.airRight[self.for_air_attack // 5]
                self.for_air_attack += 1
            self.air_attack = False

        if self.for_stay + 1 >= 15:
            self.for_stay = 0

        if self.stay_:
            self.image = self.stay_images[self.for_stay // 5]
            self.for_stay += 1

        if self.jump_enable is True:
            if self.Jump_Count >= -10:
                if self.Jump_Count < 0:
                    self.pos_y += (self.Jump_Count ** 2) / 2
                else:
                    self.pos_y -= (self.Jump_Count ** 2) / 2
                self.Jump_Count -= 1
            else:
                self.jump_enable = False
                self.Jump_Count = 10
