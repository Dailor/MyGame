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

BLOCK_SIZE = 45, 45
BIG_BLOCK_SIZE = 100, 100

TILES_PATH = "Gameplay/Tiles/"

GRASS_BLOCK = "grass_block.png"
BIG_STONE = "big_stone.png"
SMALL_STONE = "small_stone.png"
HOUSE = "house.png"
DIRTY_BLOCK = 'block.png'
PLATFORM = 'small-platform.png'
BUSH = 'bush.png'
TREE = 'tree.png'
ROCK = 'rock.png'
DOOR = 'door.png'
CRANK_DOWN = 'crank-down.png'
CRANK_UP = 'crank-up.png'
FACE_BLOCK = 'face-block.png'
SHROOMS = 'shrooms.png'
SIGN = 'sign.png'
SKULLS = 'skulls.png'
SPIKES = 'spikes.png'
SPIKES_SKULL = 'spike-skull.png'
SPIKES_TOP = 'spikes-top.png'
