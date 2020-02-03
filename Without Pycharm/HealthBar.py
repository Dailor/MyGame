import pygame


class HealthBar(pygame.sprite.Sprite):
    MAX_HEALTH = 3

    def __init__(self, gr, pos, black):
        super().__init__(gr)

        self.black = black
        self.image = pygame.Surface((150, 30))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        self.black_border()
        self.red_inner(HealthBar.MAX_HEALTH)

    def black_border(self):
        pygame.draw.rect(self.image, pygame.Color("Black"), (0, 0, self.rect.w, self.rect.h), self.black)

    def red_inner(self, n):
        self.image.fill((255, 255, 255))
        self.black_border()
        pygame.draw.rect(self.image, pygame.Color("Red"),
                         (
                             self.black - 1, self.black - 1, (self.rect.w - self.black - 1) / HealthBar.MAX_HEALTH * n,
                             self.rect.h - self.black - 1))

# TEST
# pygame.init()
# disp = pygame.display.set_mode((300, 300))
# gr = pygame.sprite.Group()
# hp = HealthBar(gr, (0, 0), 4)
# disp.fill((255, 255, 255))
# gr.draw(disp)
# hp.red_inner(2)
# gr.draw(disp)
# pygame.display.flip()
#
# while pygame.event.wait().type != pygame.QUIT:
#     pass
