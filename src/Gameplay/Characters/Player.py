from Character import Character
from CharacterEvents import *
from Configure_Gameplay import *
from Utilities import load_image
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

        self.stay = load_image(['Gameplay/Character/idle1', 'adventurer-idle-00.png'])
        self.image = self.stay
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = self.pos_x * SIZE_CONST, self.pos_y * SIZE_CONST
        self.pos_x, self.pos_y = self.rect.x, self.rect.y
        


        self.jump_enable = False
        
        self.fps = 0
        self.walkRight = [load_image(['Gameplay/Character/run', 'adventurer-run-00.png']),
                          load_image(['Gameplay/Character/run', 'adventurer-run-01.png']),
                          load_image(['Gameplay/Character/run', 'adventurer-run-02.png']),
                          load_image(['Gameplay/Character/run', 'adventurer-run-03.png']),
                          load_image(['Gameplay/Character/run', 'adventurer-run-04.png']),
                          load_image(['Gameplay/Character/run', 'adventurer-run-05.png'])]

        self.walkLeft = [load_image(['Gameplay/Character/run', 'left-00.png']),
                         load_image(['Gameplay/Character/run', 'left-01.png']),
                         load_image(['Gameplay/Character/run', 'left-02.png']),
                         load_image(['Gameplay/Character/run', 'left-03.png']),
                         load_image(['Gameplay/Character/run', 'left-04.png']),
                         load_image(['Gameplay/Character/run', 'left-05.png'])]

        self.attackLeft = [load_image(['Gameplay/Character/default attack', 'left-00.png']),
                           load_image(['Gameplay/Character/default attack', 'left-01.png']),
                           load_image(['Gameplay/Character/default attack', 'left-02.png']),
                           load_image(['Gameplay/Character/default attack', 'left-03.png']),
                           load_image(['Gameplay/Character/default attack', 'left-04.png']),
                           load_image(['Gameplay/Character/default attack', 'left-05.png'])]

        self.attackRight = [load_image(['Gameplay/Character/default attack', 'adventurer-attack2-00.png']),
                            load_image(['Gameplay/Character/default attack', 'adventurer-attack2-01.png']),
                            load_image(['Gameplay/Character/default attack', 'adventurer-attack2-02.png']),
                            load_image(['Gameplay/Character/default attack', 'adventurer-attack2-03.png']),
                            load_image(['Gameplay/Character/default attack', 'adventurer-attack2-04.png']),
                            load_image(['Gameplay/Character/default attack', 'adventurer-attack2-05.png'])]

        self.airLeft = [load_image(['Gameplay/Character/air attack', 'left-00.png']),
                        load_image(['Gameplay/Character/air attack', 'left-01.png']),
                        load_image(['Gameplay/Character/air attack', 'left-02.png']),
                        load_image(['Gameplay/Character/air attack', 'left-03.png'])]

        self.airRight = [load_image(['Gameplay/Character/air attack', 'adventurer-air-attack1-00.png']),
                         load_image(['Gameplay/Character/air attack', 'adventurer-air-attack1-01.png']),
                         load_image(['Gameplay/Character/air attack', 'adventurer-air-attack1-02.png']),
                         load_image(['Gameplay/Character/air attack', 'adventurer-air-attack1-03.png'])]

        self.stay_images = [load_image(['Gameplay/Character/idle1', 'adventurer-idle-00.png']),
                            load_image(['Gameplay/Character/idle1', 'adventurer-idle-01.png']),
                            load_image(['Gameplay/Character/idle1', 'adventurer-idle-02.png'])]

        self.is_right = False
        self.is_left = False
        self.attack = False
        self.air_attack = False
        self.stay_ = True
        self.for_attack = 0
        self.for_air_attack = 0
        self.for_stay = 0

    def event_handler(self, event):
        time = self.clock[0] / 1000
        print(time)
        if event == MOVE_LEFT:
            self.pos_x -= SPEED_X * time
        elif event == MOVE_RIGHT:
            self.pos_x += SPEED_X * time
        self.rect.x = self.pos_x
        #print(self.pos_x)
        elif event == MOVE_UP and self.jump_enable is False:
            self.jump_enable = True
            self.previous_y = self.rect.y
            self.time_j = 0
            self.clock.tick()
        elif event == ATTACK:
            self.attack = True
            self.stay_ = False
        elif event == DODGE_ATTACK:
            self.air_attack = True
            self.stay_ = False

        self.render()
        # print(self.is_right, self.is_left)

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
        # print(self.for_stay)
