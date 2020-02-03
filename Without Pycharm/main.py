
import pygame
from Menu import Menu
from Configure import *


class MainGame:
    def __init__(self, size):
        self.SIZE = size
        self.now_going = None
        self.screen = pygame.display.set_mode(self.SIZE)
        self.screen.fill(pygame.Color('white'))
        self.run = Menu(self.screen, self.SIZE)

    def render(self):
        while True:
            pygame.mixer.music.load('data/Gameplay/sound/enchanted_forest.mp3')
            pygame.mixer.music.play()
            self.run = self.run.render()
            if self.run is False:
                break
            pygame.display.flip()

    def start(self):
        self.render()


if __name__ == '__main__':
    pygame.init()
    game = MainGame(SIZE)
    game.start()
