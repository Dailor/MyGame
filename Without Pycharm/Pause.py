import pygame
from Configure import *
from Utilities import text_writer, load_image, sprite_sheet
import sys

pygame.init()


class Pause:
    def __init__(self, screen):
        self.screen = screen
        self.buttons_texts = PAUSE_TEXT
        self.events = []
        self.buttons_sprites = pygame.sprite.Group()
        self.size = SIZE
        text_writer(self.size, self.buttons_texts, DELTA_PAUSE, COORDS_TEXT_PAUSE, FONT_SIZE_PAUSE,
                    self.buttons_sprites,
                    self.events, False)
        self.clock = pygame.time.Clock()
        self.render()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.buttons_sprites.update(event.pos)

        while len(self.events):
            event = self.events.pop()
            if event == 0:
                self.continue_game()
            elif event == 1:
                self.terminate()

    def terminate(self):
        pygame.quit()
        sys.exit()

    def continue_game(self):
        pass

    def render(self):
        self.event_handler()
        self.buttons_sprites.draw(self.screen)
        pygame.time.delay(MENU_M_SEC)
        return self
