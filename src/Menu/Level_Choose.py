import pygame
import sys
from Utilities import text_writer
from TextBox import ClickableTextBox
from Configure import *
from GamePlayMain import GamePlayMain
from BeatRecodr import BeatRec
import json


class LevelChoose:
    def __init__(self, screen, background, background_group):
        self.screen = screen

        try:
            with open(SAVE_PATH, 'r') as f:
                self.save = json.load(f)
        except Exception as e:
            self.save = dict()
            save = self.save
            for i in range(level_count):
                save[i] = dict()
                save[i]['last_time_start'] = None
                save[i]['last_pos'] = None
                save[i]['record'] = None
                save[i]['opened'] = False if i != 0 else True
                save[i]['recName'] = ''
            with open(SAVE_PATH, 'w') as f:
                json.dump(save, f)

        self.background = background
        self.background_group = background_group
        self.events = list()
        self.pages_loader()
        self.arrow_loader()
        self.page_now = 0
        self.level_choose_f.close()

    def save_passed(self, n, time):
        previous_time = self.save[n - 1]['record']
        previous_name = self.save[n - 1]['recName']

        if time < previous_time:
            br = BeatRec(self.screen, (previous_time, previous_name))
            name = br.rendering()

        elif previous_time is None:
            br = BeatRec(self.screen)
            name = br.rendering()

        try:
            self.save[n]['opened'] = True
            with open(SAVE_PATH, 'w') as f:
                json.dump(self.save, f)
        except:
            end = pygame.image.load("data/end_game.png")
            self.screen.blit(end, (0, 0))
            pygame.display.flip()
            while pygame.event.wait().type != pygame.KEYDOWN:
                pass
            pygame.quit()
            sys.exit()

    def pages_loader(self):
        self.all_pages = list()
        coords = LEVEL_COORDS_ROWS
        number_event = 0
        for page in LEVEL_CHOOSE_LEVELS:
            pages = pygame.sprite.Group()
            for row, coord in zip(page, coords):
                text_writer(SIZE, row, LEVEL_DELTA, coord, LEVEL_FONT_SIZE, pages, self.events, False,
                            number_event, lvls_data=self.lvls_data[number_event: number_event + LEVEL_CHOOSE_COLS])
                number_event += LEVEL_CHOOSE_COLS
            self.all_pages.append(pages)

    def arrow_loader(self):
        self.arrows_group = pygame.sprite.Group()
        arrows = ["<==", "==>"]
        n = -2

        for arr, coord in zip(arrows, LEVEL_ARROW_COORDS):
            ClickableTextBox(self.arrows_group, self.events, n, coord, arr, LEVEL_ARROW_FONT_SIZE)
            n += 1

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.all_pages[self.page_now].update(event.pos)
                self.arrows_group.update(event.pos)

        while len(self.events):
            event = self.events.pop()
            if event == -2:
                if self.page_now == 0:
                    self.running = False
                    return False
                else:
                    self.page_now -= 1
            elif event == -1:
                if self.page_now == (len(LEVEL_CHOOSE_LEVELS) - 1):
                    continue
                else:
                    self.page_now += 1
            else:
                if self.lvls_data[event] == '0':
                    continue
                level = GamePlayMain(self.screen, f"Level{event}")
                pass_level = level.rendering()
                if pass_level:
                    print(True)
                    self.save_passed(event + 1)
                    self.__init__(self.screen, self.background, self.background_group)
                    pygame.display.flip()

    def rendering(self):
        self.running = True
        while self.running:
            self.event_handler()
            self.background_group.draw(self.screen)
            self.background.update()
            self.all_pages[self.page_now].draw(self.screen)
            self.arrows_group.draw(self.screen)
            pygame.time.delay(MENU_M_SEC)
            pygame.display.flip()

    def terminate(self):
        pygame.quit()
        sys.exit()
