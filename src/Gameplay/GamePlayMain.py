from Configure import *
from Background import ForrestBackgroundMain, ForrestBackgroundFront, Background
from CharacterEvents import *
from Player import Player
import sys
import pygame


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        if isinstance(obj, Background):
            obj.update('>' if self.dx > 0 else '<')
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - HEIGHT // 2)


class GamePlayMain:
    def __init__(self, screen):
        self.screen = screen

        self.background_group = pygame.sprite.Group()
        self.background = ForrestBackgroundMain(self.screen, self.background_group)
        self.background_front = ForrestBackgroundFront(self.screen, self.background_group)

        self.player_gruop = pygame.sprite.Group()
        self.player = Player(self.player_gruop, 100, 50, 50)

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
            self.player.append(MOVE_LEFT)
            self.background_group.update(">")
        elif key[pygame.K_RIGHT]:
            self.player.append(MOVE_RIGHT)
            self.background_group.update("<")

    def event_handler(self):
        self.pygame_events()
        self.keyboard_events()

    def drawing(self):
        self.screen.fill((255, 255, 255))
        self.background_group.draw(self.screen)
        pygame.display.flip()

    def rendering(self):
        self.running = True
        # camera = Camera()
        while self.running:
            self.event_handler()
            self.drawing()
            # camera.update(self.player)
            # for el in self.background_group:
            #     camera.apply(el)
