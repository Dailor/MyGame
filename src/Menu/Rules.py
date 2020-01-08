import pygame
from Utilities import text_writer
from TextBox import TextBox, ClickableTextBox
import sys
from Configure import *


class Rules:
    def __init__(self, screen, bg, bg_group):
        self.screen = screen
        self.text = self.game_rules()
        self.background = bg
        self.background_group = bg_group

    def terminate(self):
        pygame.quit()
        sys.exit()

    def game_rules(self):
        return text_writer(SIZE, RULES_TEXT, DELTA_RULES, COORDS_TEXT_RULES, FONT_SIZE_RULES)

    def rendering(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                    running = False
            self.background_group.draw(self.screen)
            self.background.update()
            self.screen.blit(self.text, (0, 0))
            pygame.time.delay(MENU_M_SEC)
            pygame.display.flip()
