from Utilities import load_image_v2
import pygame

pygame.init()
pygame.display.set_mode()
#### Character
REGENERATION = 20
STAMINA_RECOVERY = 20

### Player

MAX_JUMP_H = None
SPEED_X = 100
SPEED_Y = 0
STAR_SIZE = 25, 25
V0 = 100
V0_JUMP = 15
GRAVITY = 200
PLAYER_SIZE = 60, 60

ANIM_walkRight = [['Gameplay/Character/run', 'adventurer-run-00.png'],
                  ['Gameplay/Character/run', 'adventurer-run-01.png'],
                  ['Gameplay/Character/run', 'adventurer-run-02.png'],
                  ['Gameplay/Character/run', 'adventurer-run-03.png'],
                  ['Gameplay/Character/run', 'adventurer-run-04.png'],
                  ['Gameplay/Character/run', 'adventurer-run-05.png']]

ANIM_walkLeft = [['Gameplay/Character/run', 'left-00.png'],
                 ['Gameplay/Character/run', 'left-01.png'],
                 ['Gameplay/Character/run', 'left-02.png'],
                 ['Gameplay/Character/run', 'left-03.png'],
                 ['Gameplay/Character/run', 'left-04.png'],
                 ['Gameplay/Character/run', 'left-05.png']]

ANIM_attackLeft = [['Gameplay/Character/default attack', 'left-00.png'],
                   ['Gameplay/Character/default attack', 'left-01.png'],
                   ['Gameplay/Character/default attack', 'left-02.png'],
                   ['Gameplay/Character/default attack', 'left-03.png'],
                   ['Gameplay/Character/default attack', 'left-04.png'],
                   ['Gameplay/Character/default attack', 'left-05.png']]

ANIM_attackRight = [['Gameplay/Character/default attack', 'adventurer-attack2-00.png'],
                    ['Gameplay/Character/default attack', 'adventurer-attack2-01.png'],
                    ['Gameplay/Character/default attack', 'adventurer-attack2-02.png'],
                    ['Gameplay/Character/default attack', 'adventurer-attack2-03.png'],
                    ['Gameplay/Character/default attack', 'adventurer-attack2-04.png'],
                    ['Gameplay/Character/default attack', 'adventurer-attack2-05.png']]

ANIM_airLeft = [['Gameplay/Character/air attack', 'left-00.png'],
                ['Gameplay/Character/air attack', 'left-01.png'],
                ['Gameplay/Character/air attack', 'left-02.png'],
                ['Gameplay/Character/air attack', 'left-03.png']]

ANIM_airRight = [['Gameplay/Character/air attack', 'adventurer-air-attack1-00.png'],
                 ['Gameplay/Character/air attack', 'adventurer-air-attack1-01.png'],
                 ['Gameplay/Character/air attack', 'adventurer-air-attack1-02.png'],
                 ['Gameplay/Character/air attack', 'adventurer-air-attack1-03.png']]

ANIM_stay_images = [['Gameplay/Character/idle', 'adventurer-idle-00.png'],
                    ['Gameplay/Character/idle', 'adventurer-idle-01.png'],
                    ['Gameplay/Character/idle', 'adventurer-idle-02.png']]

STAR = [load_image_v2(['Gameplay/Special/star', 'star-1.png'], STAR_SIZE),
        load_image_v2(['Gameplay/Special/star', 'star-2.png'], STAR_SIZE),
        load_image_v2(['Gameplay/Special/star', 'star-3.png'], STAR_SIZE),
        load_image_v2(['Gameplay/Special/star', 'star-4.png'], STAR_SIZE),
        load_image_v2(['Gameplay/Special/star', 'star-5.png'], STAR_SIZE),
        load_image_v2(['Gameplay/Special/star', 'star-6.png'], STAR_SIZE)]
