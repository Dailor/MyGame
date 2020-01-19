import os
from Configure import SIZE

"""
Каждый level имеет BACKGROUND, TILES, 
"""


BG_SIZE = SIZE
BG_SPEED = 10, 0

MF_SIZE = SIZE
MF_SPEED = 20, 0

PATH_BACKGROUNDS = 'data\Gameplay\Backgrounds\\forest'
PATH_BG = os.path.join(PATH_BACKGROUNDS, 'background.png')
PATH_MF = os.path.join(PATH_BACKGROUNDS, "middleground.png")



