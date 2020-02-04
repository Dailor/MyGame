import pygame

pygame.init()
RUNNING = pygame.mixer.music.load('data/Gameplay/sound/running.mp3')
JUMP = pygame.mixer.music.load('data/Gameplay/sound/jump.mp3')
HURT = pygame.mixer.music.load('data/Gameplay/sound/hurt.mp3')
ENEMY_DEATH = pygame.mixer.music.load('data/Gameplay/sound/enemy-death.mp3')
CHEST = pygame.mixer.music.load('data/Gameplay/sound/chest.mp3')


#  data/Gameplay/sound/enchanted_forest

def background_music():
    pygame.mixer.music.load('data/Gameplay/sound/enchanted_forest.mp3')
    pygame.mixer.music.play()


def jump_music():
    # print('Ok')
    pygame.mixer.music.load('data/Gameplay/sound/jump.mp3')
    pygame.mixer.music.play()


def hurt_music():
    pygame.mixer.music.load('data/Gameplay/sound/hurt.mp3')
    pygame.mixer.music.play()
