from Configure import *
from Background import ForrestBackgroundMain, ForrestBackgroundFront, Background
from CharacterEvents import *
from Player import Player
from Configure_Map import BLOCK_SIZE

from Map import generate_level
import sys
import pygame


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - HEIGHT // 2)


class GamePlayMain:
    def __init__(self, screen, level):
        self.screen = screen

        self.all_tiles = pygame.sprite.Group()
        self.player, x_max, y_max = generate_level(level, self.all_tiles)
        x_max *= BLOCK_SIZE[0]
        self.background_group = pygame.sprite.Group()
        self.background = ForrestBackgroundMain(self.screen, self.background_group, x_max)
        self.background_front = ForrestBackgroundFront(self.screen, self.background_group, x_max)

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
                    """
                    ПАУЗА                                        
                    """

    def keyboard_events(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            print(self.all_tiles)
            self.player.event_handler(MOVE_LEFT)
            self.background_group.update(">")
        elif key[pygame.K_RIGHT]:
            self.player.event_handler(MOVE_RIGHT)
            self.background_group.update("<")

    def event_handler(self):
        self.pygame_events()
        self.keyboard_events()
        self.camera_events()

    def camera_events(self):
        self.camera.update(self.player)
        for el in self.all_tiles:
            self.camera.apply(el)
        pass

    def drawing(self):
        self.screen.fill((255, 255, 255))
        self.background_group.draw(self.screen)
        self.all_tiles.draw(self.screen)
        pygame.display.flip()

    def rendering(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.camera = Camera()
        while self.running:
            self.event_handler()
            self.drawing()