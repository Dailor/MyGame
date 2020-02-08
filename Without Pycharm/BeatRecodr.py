import pygame
import sys
from Configure import SIZE
from Utilities import TextBox, EditText, text_writer


class BeatRec:
    MAX_LENGTH = 24
    DY = 26
    SCORE_TABLE = (260, 300)

    def __init__(self, screen, time, who_passed):
        who_passed = [f'{x}. {y}' for x,y in enumerate(who_passed[:5], start=1)]
        self.screen = screen
        self.name = ['']
        self.records_pl = text_writer(SIZE, who_passed, (0, BeatRec.DY), BeatRec.SCORE_TABLE, 27)

        hh = int(time // 3600)
        mm = int((time - hh * 3600) // 60)
        ss = int(time - hh * 3600 - mm * 60)
        self.welcome_text = f"You passed level for {hh}hh:{mm}mm:{ss}ss"

        self.welcome_text_gr = pygame.sprite.Group()
        self.tv_group = pygame.sprite.Group()

        pos = 200, 100
        pos2 = 110, 150
        pos3 = 290, 230
        color = 103, 222, 66
        color2 = 222, 21, 209

        TextBox(self.welcome_text_gr, pos, self.welcome_text, 30, color, False)
        self.tv = EditText(self.tv_group, pos2, self.name[0], 45, color2, True)
        TextBox(self.welcome_text_gr, pos3, "TOP PLAYERS", 39, color2, False)

    def rendering(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == 13:
                        return self.name[0]
                    elif 97 <= event.key <= 122 or 48 <= event.key <= 57:
                        if len(self.name[0]) <= BeatRec.MAX_LENGTH:
                            self.name[0] += chr(event.key)
                    elif event.key == pygame.K_BACKSPACE:
                        if len(self.name[0]):
                            self.name[0] = self.name[0][:-1]
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.records_pl, (0, 0))
            self.tv.update_text(self.name[0])
            self.welcome_text_gr.draw(self.screen)
            self.tv_group.draw(self.screen)
            pygame.display.flip()
