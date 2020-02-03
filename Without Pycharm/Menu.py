import pygame
import sys
from Utilities import text_writer, load_image, sprite_sheet
from Configure import *
from Rules import Rules
from Level_Choose import LevelChoose


class Menu:
    def __init__(self, screen, size):
        self.screen = screen
        self.SIZE = size
        self.events = list()
        self.background_group = pygame.sprite.Group()
        self.buttons_texts = MENU_TEXT
        self.buttons_sprites = pygame.sprite.Group()
        text_writer(size, self.buttons_texts, DELTA_MENU, COORDS_TEXT_MENU, FONT_SIZE_MENU, self.buttons_sprites, self.events, False)
        self.background = Background(self.background_group)
        self.clock = pygame.time.Clock()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.buttons_sprites.update(event.pos)

        while len(self.events):
            event = self.events.pop()
            if event == 0:
                self.level_choose_load()
            elif event == 1:
                self.rules_load()
            elif event == 2:
                self.terminate()

    def level_choose_load(self):
        level_choose = LevelChoose(self.screen, self.background, self.background_group)
        level_choose.rendering()

    def rules_load(self):
        rules = Rules(self.screen, self.background, self.background_group)
        rules.rendering()

    def terminate(self):
        pygame.quit()
        sys.exit()

    def render(self):
        self.event_handler()
        self.background_group.draw(self.screen)
        self.background.update()
        self.buttons_sprites.draw(self.screen)
        pygame.time.delay(MENU_M_SEC)
        return self


class Background(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.sheet = load_image(['Menu', 'background', 'background.png'], colorkey=None)
        self.frames = sprite_sheet(self.sheet, 5, 2)
        self.going_to = 0
        self.image = self.frames[self.going_to]
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self):
        self.going_to = (self.going_to + 1) % len(self.frames)
        self.image = self.frames[self.going_to]
