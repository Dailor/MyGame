import os
from Configure import SIZE
from Configure_Gameplay import SPEED_X, SPEED_Y

"""
Каждый level имеет BACKGROUND, TILES, 
"""

BG_SIZE = SIZE
BG_SPEED = SPEED_X / 2, 0

MF_SIZE = SIZE
MF_SPEED = SPEED_X, 0

PATH_BACKGROUNDS = 'data\Gameplay\Backgrounds\\forest'
PATH_BG = os.path.join(PATH_BACKGROUNDS, 'background.png')
PATH_MF = os.path.join(PATH_BACKGROUNDS, "middleground.png")
