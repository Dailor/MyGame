from Configure import *
from Background import ForrestBackgroundMain, ForrestBackgroundFront, Background
from CharacterEvents import *
from Player import Player
from Configure_Map import BLOCK_SIZE
from Bee import Bee
import Tiles
from Map import generate_level, slugs, bees, piranhas
import sys
import pygame
from Sounds import *
from Pause import Pause


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
    def __init__(self, screen, level):
        self.screen = screen
        self.clock_t = pygame.time.Clock()
        self.clock = [0]
        self.all_tiles = pygame.sprite.Group()
        self.player, x_max, y_max = generate_level(level, self.all_tiles, self.clock)
        self.background_group = pygame.sprite.Group()
        self.background = ForrestBackgroundMain(self.screen, self.background_group, self.clock, x_max)
        self.background_front = ForrestBackgroundFront(self.screen, self.background_group, self.clock, x_max)
        self.ifpause = False

    def terminate(self):
        sys.exit()
        pygame.quit()

    def pygame_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.terminate()
            if event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_ESCAPE:
                    # print('ok')
                    self.ifpause = True
                    self.pause()

    def keyboard_events(self):
        key = pygame.key.get_pressed()
        # self.bee.stay()
        # self.slug.stay()
        for i in slugs:
            i.stay()
        for j in bees:
            j.stay()
        for z in piranhas:
            z.stay()
        if key[pygame.K_ESCAPE]:
            print(pygame.sprite.spritecollide(self.player, self.all_tiles, False))
        if key[pygame.K_LEFT]:
            self.player.event_handler(MOVE_LEFT)
            self.background_group.update(">")
        elif key[pygame.K_RIGHT]:
            self.player.event_handler(MOVE_RIGHT)
            self.background_group.update("<")
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

    def event_handler(self):
        self.pygame_events()
        self.keyboard_events()
        self.player.render()
        self.camera_events()

    def camera_events(self):
        self.camera.update(self.player)
        for el in self.all_tiles:
            self.camera.apply(el)

    def drawing(self):
        self.screen.fill((255, 255, 255))
        self.background_group.draw(self.screen)
        self.all_tiles.draw(self.screen)
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
                #self.passed_level = True
                break
            self.drawing()
        if self.passed_level:
            """
            Тут победа
            """
            pass
        else:
            return

    def pause(self):
        Pause(self.screen)
