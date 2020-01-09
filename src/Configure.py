import os

#### Main
SIZE = 800, 600
WIDTH, HEIGHT = SIZE
SQUARE = WIDTH * HEIGHT

#### Menu
MENU_TEXT = ["BEGIN GAME", "RULES", "ВЫХОД"]  # MENU_TEXT = ["Начать игру", "Правила"]
MENU_M_SEC = 100
FONT_SIZE_MENU = 50
DELTA_MENU = (0, 70)
COORDS_TEXT_MENU = (80, 107)

#### RULES
with open('data/Menu/RULES_TEXT', encoding='utf-8') as f:
    RULES_TEXT = f.read().split('\n')
FONT_SIZE_RULES = 40
TEXT_COLOR_RULES = 182, 21, 222
DELTA_RULES = (0, 80)
COORDS_TEXT_RULES = (30, 54)

#### LEVEL_CHOOSE
LEVEL_ARROW_FONT_SIZE = 40
LEVEL_Y_ARROWS = 545
LEVEL_ARROW_COORDS = ((50, LEVEL_Y_ARROWS), (670, LEVEL_Y_ARROWS))

LEVEL_FONT_SIZE = 40

LEVEL_CHOOSE_COUNT = 10
LEVEL_CHOOSE_ROWS = 3
LEVEL_CHOOSE_COLS = 4

LEVEL_X_ROWS = 55
LEVEL_Y_ROWS = 87
LEVEL_DELTA = (200, 0)
LEVEL_COORDS_ROWS = (
    (LEVEL_X_ROWS, LEVEL_Y_ROWS + 50), (LEVEL_X_ROWS, LEVEL_Y_ROWS + 230), (LEVEL_X_ROWS, LEVEL_Y_ROWS + 420))

LEVEL_CHOOSE_LEVELS = list()
level_count = 0
clause = True
while True:
    if clause is False:
        break
    rows = list()
    for row in range(LEVEL_CHOOSE_ROWS):
        if clause is False:
            break
        text_list = list()
        for text in range(LEVEL_CHOOSE_COLS):
            text_list.append(f'LEVEL {level_count}')
            level_count += 1
            if level_count == LEVEL_CHOOSE_COUNT:
                clause = False
                break
        rows.append(tuple(text_list))
    LEVEL_CHOOSE_LEVELS.append(tuple(rows))
LEVEL_CHOOSE_LEVELS = tuple(LEVEL_CHOOSE_LEVELS)

#### UTILITIES
FILL_COLOR_UTILITIES = (0, 0, 0)

#### TextBox
COLOR_FILL = 255, 255, 255
COLOR_TEXT = 182, 21, 222
FONT_SIZE = 107
