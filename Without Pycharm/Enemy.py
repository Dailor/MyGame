import pygame
import CharacterEvents

SIZE_CONST = 50


class Enemy(pygame.sprite.Sprite):
    def __init__(self, gr, pos, list, x_max=None, player=None, *args):
        super().__init__(gr)
        self.player_alone = player
        self.x_max = x_max
        self.pos_x, self.pos_y = pos
        self.bee = list[0]
        self.fps = 0
        self.image = self.bee
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pos_x * SIZE_CONST, self.pos_y * SIZE_CONST
        self.pos_x, self.pos_y = self.rect.x, self.rect.y
        self.mask = pygame.mask.from_surface(self.image)

    def damage_check(self, player):
        if pygame.sprite.collide_mask(self, player):
            # self.player.take_dmg()
            player.event_handler(CharacterEvents.MOVE_UP, True)
            player.hp -= 1
