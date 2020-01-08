import os

#### Main
SIZE = 600, 300

#### Menu
MENU_TEXT = ["BEGIN GAME", "RULES"]  # MENU_TEXT = ["Начать игру", "Правила"]
MENU_M_SEC = 100
FONT_SIZE_MENU = 40
DY = 40
X_START = 10

#### TextBox
COLOR_FILL = 255, 255, 255
COLOR_TEXT = 182, 21, 222
FONT_SIZE = 40

#### RULES
with open('data/Menu/RULES_TEXT', encoding='utf-8') as f:
    RULES_TEXT = f.read().split('\n')
FONT_SIZE_RULES = 33
TEXT_COLOR_RULES = 182, 21, 222

#### UTILITIES
FILL_COLOR_UTILITIES = (0, 0, 0)
