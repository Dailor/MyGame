from CharacterEvents import *
from Configure_Gameplay import *
from Utilities import load_image_v2, dont_check_tile
from Enemy import Enemy
from Configure_Map import BLOCK_SIZE
from Configure import SIZE
import pygame
import copy

SIZE_CONST = 35
INFELICITY = 25


class Player(pygame.sprite.Sprite):
    MAX_HP = 3

    def __init__(self, gr, pos, clock, x_max, bg, *args):
        super().__init__(gr)
        self.hp = Player.MAX_HP

        self.background_group = bg
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
        self.falling = True

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
        self.last_none_act = False
        self.attack = False
        self.air_attack = False
        self.stay_ = True

        self.for_attack = 0
        self.for_air_attack = 0
        self.for_stay = 0
        self.Jump_Count = 10
        self.right = 0
        self.left = 0

    def event_handler(self, event, dmg_get=False):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            event = MOVE_LEFT
        if key[pygame.K_RIGHT]:
            event = MOVE_RIGHT
        if key[pygame.K_UP] and self.jump_enable is False and self.falling is False:
            event = MOVE_UP
        if event is None and self.last_none_act:
            return
        else:
            self.last_none_act = False
        time = self.clock[0] / 1000
        rect_collide = copy.deepcopy(self.rect)
        rect_collide.w = 1

        if event == MOVE_LEFT:
            dx = SPEED_X * time
            collides = [(t.pos_x, t.pos_y, t.rect.w, t.rect.h, t) for t in
                        pygame.sprite.spritecollide(self, self.all_tiles, False) if
                        dont_check_tile(t) is False and rect_collide.colliderect(t.rect)]
            for x_t, y_t, w_t, h_t, t in collides:
                if not x_t < self.pos_x and isinstance(t, Enemy):
                    continue
                # if not (x_t <= self.pos_x - dx <= x_t + w_t) and not (y_t >= self.pos_y + self.rect.h - INFELICITY):
                if not (y_t >= self.pos_y + self.rect.h - INFELICITY):
                    return
            self.background_group.update(">")
            self.pos_x -= dx
            self.pos_rel_x -= dx
            self.is_right = False
            self.is_left = True
            self.stay_ = False
        elif event == MOVE_RIGHT:
            rect_collide.x += self.rect.w
            collides = [(t.pos_x, t.pos_y, t.rect.w, t.rect.h, t) for t in
                        pygame.sprite.spritecollide(self, self.all_tiles, False) if
                        dont_check_tile(t) is False is False and rect_collide.colliderect(t.rect)]
            dx = SPEED_X * time
            for x_t, y_t, w_t, h_t, t in collides:
                if not x_t > self.pos_x and isinstance(t, Enemy):
                    continue
                # if not (x_t <= self.pos_x + dx <= x_t + w_t) and not (y_t >= self.pos_y + self.rect.h - INFELICITY):
                if not (y_t >= self.pos_y + self.rect.h - INFELICITY):
                    return
            self.background_group.update("<")
            self.pos_x += dx
            self.pos_rel_x += dx
            self.is_right = True
            self.is_left = False
            self.stay_ = False
        if event is None:
            self.last_none_act = True
            self.is_left_before = self.is_left
            self.is_right = False
            self.is_left = False
            self.stay_ = True
        if event == MOVE_UP and (((
                                          self.jump_enable is False and self.falling) is False) or dmg_get):
            self.jump_enable = True
            self.falling = False

            self.vy = V0_JUMP
            if dmg_get:
                self.vy = 200
                self.pos_y += 20

        if event == ATTACK and self.attack is False:
            self.attack = True
            self.stay_ = False
        else:
            self.stay_ = True

    def render(self):
        self.mask = pygame.mask.from_surface(self.image)
        if self.right + 1 >= 30:
            self.right = 0
        if self.left + 1 >= 30:
            self.left = 0

        # if not self.is_left and not self.is_right:
        #     self.image = self.stay

        if self.is_left:
            self.is_right = False
            self.image = self.walkLeft[self.left // 5]
            self.left += 1
        elif self.is_right:
            self.is_left = False
            self.image = self.walkRight[self.right // 5]
            self.right += 1
        elif self.stay_:
            self.image = pygame.transform.flip(self.stay, self.is_left_before, False)

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

        # if self.for_stay + 1 >= 15:
        #     self.for_stay = 0
        #
        # if self.stay_:
        #     self.image = self.stay_images[self.for_stay // 5]
        #     self.for_stay += 1

        time = self.clock[0] / 1000
        if self.jump_enable is True:
            self.pos_y -= self.vy - GRAVITY * time ** 2 / 2
            self.vy -= GRAVITY * time
            if self.vy <= 0:
                self.jump_enable = False
            collides = [t for t in pygame.sprite.spritecollide(self, self.all_tiles, False) if dont_check_tile(t) is False]
            if len(collides) != 0:
                self.vy = 0
                self.jump_enable = False
                self.pos_y += 10
        elif self.jump_enable is False:
            check_collide = False
            rect_check = copy.deepcopy(self.rect)
            rect_check.w = 1

            rect_check.x = self.pos_x + self.rect.w // 2
            for t in self.all_tiles:
                if dont_check_tile(t): continue
                if rect_check.colliderect(t.rect):
                    check_collide = True
                    y_t, w_t = t.rect.y, t.rect.w
                    if self.pos_y <= y_t <= y_t + w_t <= self.pos_y + self.rect.h or y_t <= self.pos_y <= y_t + w_t <= self.pos_y + self.rect.h:
                        check_collide = False
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
