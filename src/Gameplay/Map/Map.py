from Configure_Map import *
from Configure import *
from Configure_Map import *
import Tiles
from Player import Player


def load_level(filename):
    filename = "data/Gameplay/Levels/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip('\n').replace(" ", '.') for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def generate_level(level, gr, clock):
    level = load_level(level)
    new_player, x, y = None, None, None
    print('\n'.join(level))
    for y in range(len(level)):
        for x in range(len(level[y])):
            pos = x, y
            if level[y][x] == 'g':
                Tiles.GrassBlock(gr, pos)
            elif level[y][x] == '@':
                pos_player = x, y
                # вернем игрока, а также размер поля в клетках
    x_max = x * BLOCK_SIZE[0]
    y_max = y * BLOCK_SIZE[1]
    new_player = Player(gr, pos_player, clock, x_max)
    return new_player, x_max, y_max
