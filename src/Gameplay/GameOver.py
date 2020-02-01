import pygame
import sys
from Configure import SIZE


class GameOver:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load("data/game_over.jpg"), SIZE)
        self.pos_y = -self.image.get_rect().h
        self.speed = 100

    def rendering(self):
        clock = pygame.time.Clock()
        while self.pos_y < 0:
            self.screen.blit(self.image, (0, int(self.pos_y)))
            self.pos_y += clock.tick() / 1000 * self.speed
            pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    key = pygame.key.get_pressed()
                    if key[pygame.K_ESCAPE]:
                        return False
                    elif key[pygame.K_r]:
                        return True
