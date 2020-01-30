from Character import Character
from CharacterEvents import *
from Configure_Gameplay import *
from Utilities import load_image_v2
from Configure_Map import BLOCK_SIZE
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

SIZE_CONST = 37


class Player(pygame.sprite.Sprite):
    def __init__(self, gr, pos, clock, x_max, *args):
        super().__init__(gr)
        self.all_tiles = gr
        self.x_max = x_max
        self.clock = clock
        self.pos_x, self.pos_y = pos
        self.vy = 0

        self.stay = load_image_v2(['Gameplay/Character/idle', 'adventurer-idle-00.png'], PLAYER_SIZE)
        self.image = self.stay
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pos_x * SIZE_CONST, self.pos_y * SIZE_CONST
        self.pos_x, self.pos_y = self.rect.x, self.rect.y
        self.pos_rel_x, self.pos_rel_x = self.pos_x, self.pos_y

        self.jump_enable = False
        self.falling = False

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
        self.bubble()

    def bubble(self):
        while True:
            clause = True
            for tile in self.all_tiles:
                if isinstance(tile, Player):
                    continue
                if pygame.sprite.collide_mask(self, tile):
                    self.rect.y += 2
                    clause = False
                    break
            if clause:
                break

    def event_handler(self, event):
        time = self.clock[0] / 1000
        collides = [(t.rect.x, t.rect.y, t.rect.w, t.rect.h) for t in
                    pygame.sprite.spritecollide(self, self.all_tiles, False) if isinstance(t, Player) is False]
        if event == MOVE_LEFT:
            # for x_t, y_t, w_t, h_t in collides:
            #     if x_t <= self.rect.x - 1 <= x_t + w_t and y_t - h_t > self.rect.y - self.rect.h:
            #         return
            dx = SPEED_X * time
            self.pos_x -= dx
            self.pos_rel_x -= dx
            self.is_right = False
            self.is_left = True
            self.stay_ = False
        elif event == MOVE_RIGHT:
            # for x_t, y_t, w_t, h_t in collides:
            #     if x_t <= self.rect.x + self.rect.w + 1 <= x_t + w_t and y_t - h_t > self.rect.y - self.rect.h:
            #         return
            dx = SPEED_X * time
            self.pos_x += dx
            self.pos_rel_x += dx
            self.is_right = True
            self.is_left = False
            self.stay_ = False
        if event == MOVE_UP and self.jump_enable is False:
            self.jump_enable = True
            self.vy = V0_JUMP
        if event == ATTACK and self.jump_enable is True and self.attack is False:
            self.air_attack = True
            self.stay_ = False
        if event == ATTACK and self.attack is False:
            self.attack = True
            self.stay_ = False
        else:
            self.stay_ = True

    def render(self):
        self.mask = pygame.mask.from_surface(self.image)
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

        time = self.clock[0] / 1000
        if self.jump_enable is True:
            self.pos_y -= self.vy - GRAVITY * time ** 2 / 2
            self.vy -= GRAVITY * time
            if self.vy <= 0:
                self.jump_enable = False
        elif self.jump_enable is False:
            check_collide = False
            for tile in self.all_tiles:
                if isinstance(tile, Player):
                    continue
                if (pygame.sprite.collide_mask(self, tile) and self.rect.y - self.rect.h >= tile.rect.y) is False:
                    check_collide = True
                    break
            if check_collide is False:
                self.falling = True
                self.vy += GRAVITY * time
                self.pos_y += self.vy * time + GRAVITY * time ** 2 / 2
            else:
                self.falling = False
                self.vy = 0

        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
