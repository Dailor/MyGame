from Configure import *
from Background import ForrestBackgroundMain, ForrestBackgroundFront, Background
from CharacterEvents import *
from HealthBar import HealthBar
import Tiles
from Map import generate_level, slugs, bees, piranhas, stars
import sys
import pygame
import json
from Sounds import *
from Pause import Pause
from Enemy import Enemy
from GameOver import GameOver
import time

class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self, bg):
        self.bg = bg
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.pos_x += self.dx
        obj.pos_y += self.dy

        obj.rect.x = obj.pos_x
        obj.rect.y = obj.pos_y

    # позиционировать камеру на объекте target
    def update(self, target):
        x, y = target.pos_x, target.pos_y

        self.dx = -(x + target.rect.w / 2 - WIDTH / 2)
        self.dy = -(y + target.rect.h / 2 - HEIGHT / 2)


class GamePlayMain:
    def __init__(self, screen, level, number_level, save):
        self.save = save
        saved_time = self.save[str(number_level)]['last_time_start']
        self.game_start_time = time.time() if saved_time is None else saved_time
        self.number_level = number_level
        self.screen = screen
        self.level_pre = level
        self.hb_gr = pygame.sprite.Group()
        self.hb = HealthBar(self.hb_gr, (20, 20), 4)
        self.clock_t = pygame.time.Clock()
        self.clock = [0]
        self.all_tiles = pygame.sprite.Group()
        self.background_group = pygame.sprite.Group()
        self.player, x_max, y_max = generate_level(level, self.all_tiles, self.clock, self.background_group, pos_pl=self.save[str(number_level)]['last_pos'])
        self.spites_start()
        self.background = ForrestBackgroundMain(self.screen, self.background_group, self.clock, x_max)
        self.background_front = ForrestBackgroundFront(self.screen, self.background_group, self.clock, x_max)
        self.ifpause = False

    def spites_start(self):
        for t in self.all_tiles:
            try:
                t.drop_down()
            except Exception as e:
                continue

    def terminate(self):
        self.save_data()
        sys.exit()
        pygame.quit()

    def save_data(self):
        t, pos_pl  =self.game_start_time, (self.player.pos_rel_x, self.player.pos_rel_y)
        self.save[str(self.number_level)]['last_pos'] = pos_pl
        self.save[str(self.number_level)]['last_time_start'] = t
        with open(SAVE_PATH, 'w') as f:
            json.dump(self.save, f)


    def pygame_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.terminate()
            if event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_ESCAPE:
                    pass

    def keyboard_events(self):
        key = pygame.key.get_pressed()
        for i in slugs:
            i.stay()
        for j in bees:
            j.stay()
        for z in piranhas:
            z.stay()
        for u in stars:
            u.stay()
        if key[pygame.K_ESCAPE]:
            print(pygame.sprite.spritecollide(self.player, self.all_tiles, False))
        if key[pygame.K_LEFT]:
            self.player.event_handler(MOVE_LEFT)
        elif key[pygame.K_RIGHT]:
            self.player.event_handler(MOVE_RIGHT)
        elif key[pygame.K_UP]:
            jump_music()
            self.player.event_handler(MOVE_UP)
            self.clock_t.tick(40)
            background_music()
        elif key[pygame.K_f]:
            hurt_music()
            self.player.event_handler(ATTACK)
            self.clock_t.tick(40)
            background_music()
        else:
            self.player.event_handler(None)

    def event_handler(self):
        self.pygame_events()
        self.keyboard_events()
        self.player.render()
        [t.damage_check(self.player) for t in self.all_tiles if isinstance(t, Enemy)]
        self.hb.red_inner(self.player.hp)
        if self.player.hp == 0:
            self.running = False
        self.camera_events()

    def camera_events(self):
        self.camera.update(self.player)
        for el in self.all_tiles:
            self.camera.apply(el)

    def drawing(self):
        self.screen.fill((255, 255, 255))
        self.background_group.draw(self.screen)
        self.all_tiles.draw(self.screen)
        self.hb_gr.draw(self.screen)
        pygame.display.flip()

    def rendering(self):
        self.running = True
        self.passed_level = False
        self.camera = Camera(self.background_front)
        while self.running:
            self.clock[0] = self.clock_t.tick()
            self.event_handler()
            if any(isinstance(t, Tiles.House) for t in pygame.sprite.spritecollide(self.player, self.all_tiles, False)):
                self.running = False
                self.passed_level = True

                self.save[str(self.number_level)]['last_pos'] = None
                self.save[str(self.number_level)]['last_time_start'] = None
                with open(SAVE_PATH, 'w') as f:
                    json.dump(self.save, f)

                break
            if self.player.game_over:
                self.running = False
                break
            self.drawing()
        if self.passed_level:
            return True, time.time() - self.game_start_time
        else:
            game_over = GameOver(self.screen)
            result = game_over.rendering()
            if result is False:
                return False, None
            else:
                again = GamePlayMain(self.screen, self.level_pre)
                return again.rendering()

    def pause(self):
        Pause(self.screen)
