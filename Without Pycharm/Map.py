from Configure_Map import *
from Configure import *
from Configure_Map import *
import Tiles
from Player import Player
from Bee import Bee
from Slug import Slug
from Piranha_Plant import PiranhaPlant
from Star import Star

slugs = []
bees = []
piranhas = []
stars = []


def load_level(filename):
    filename = "data/Gameplay/Levels/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip('\n').replace(" ", '.') for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def generate_level(level, gr, clock, bg):
    level = load_level(level)
    new_player, x, y = None, None, None
    pos_bee = None
    pos_player = None
    pos_slug = None
    player_list = list()
    player_list.append(0)
    for y in range(len(level)):
        for x in range(len(level[y])):
            pos = x, y
            if level[y][x] == 'g':
                Tiles.GrassBlock(gr, pos)
            elif level[y][x] == '@':
                pos_player = x, y
                # вернем игрока, а также размер поля в клетках
            elif level[y][x] == 'o':
                pos_bee = x, y
                bee = Bee(gr, pos_bee, None, player_list)
                bees.append(bee)
            elif level[y][x] == 's':
                Tiles.SmallStoneBlock(gr, pos)
            elif level[y][x] == 'd':
                Tiles.Dirty(gr, pos)
            elif level[y][x] == 'u':
                pos_slug = x, y
                slug = Slug(gr, pos_slug, None, player_list)
                slugs.append(slug)
            elif level[y][x] == 'p':
                Tiles.Platform(gr, pos)
            elif level[y][x] == 'e':
                pos_piranha = x, y
                piranha = PiranhaPlant(gr, pos_piranha, None, player_list)
                piranhas.append(piranha)
            elif level[y][x] == 'b':
                Tiles.Sign(gr, pos)
            elif level[y][x] == 't':
                Tiles.Tree(gr, pos)
            elif level[y][x] == 'k':
                Tiles.Bush(gr, pos)
            elif level[y][x] == 'r':
                Tiles.Rock(gr, pos)
            elif level[y][x] == 'c':
                Tiles.Door(gr, pos)
            elif level[y][x] == 'h':
                Tiles.House(gr, pos)
            elif level[y][x] == 'f':
                Tiles.FaceBlock(gr, pos)
            elif level[y][x] == 'm':
                Tiles.Shrooms(gr, pos)
            elif level[y][x] == 'w':
                Tiles.Skulls(gr, pos)
            elif level[y][x] == 'z':
                Tiles.SpikesSkull(gr, pos)
            elif level[y][x] == '#':
                star = Star(gr, pos, None, player_list)
                stars.append(star)
    x_max = x * BLOCK_SIZE[0]
    y_max = y * BLOCK_SIZE[1]
    new_player = Player(gr, pos_player, clock, x_max, bg)
    player_list[0] = new_player
    # slug = Slug(gr, pos_slug)
    return new_player, x_max, y_max
