import pygame
import sys
from Utilities  import TextBox, EditText


class BeatRec:
    MAX_LENGTH = 24

    def __init__(self, screen, data=None):
        self.screen = screen
        self.name = ['']
        if data is None:
            self.welcome_text = 'You was first who have passed level, type you name and press Enter'
        else:
            self.welcome_text = f"Wow,  you beat Last record {data[0]} of {data[1]}"
        self.welcome_text_gr = pygame.sprite.Group()
        self.tv_group = pygame.sprite.Group()
        pos = 165, 100
        pos2 = 210, 150
        color = 103, 222, 66
        color2 = 222, 21, 209
        TextBox(self.welcome_text_gr, pos, self.welcome_text, 30, color, False)
        self.tv = EditText(self.tv_group, pos2, self.name[0], 45, color2, True)

    def update_edit(self):
        pass

    def rendering(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    print(event.key)
                    if event.key == 13:
                        return self.name[0]
                    elif 97 <= event.key <= 122 or 48 <= event.key <= 57:
                        if len(self.name[0]) <= BeatRec.MAX_LENGTH:
                            self.name[0] += chr(event.key)
                    elif event.key == pygame.K_BACKSPACE:
                        if len(self.name[0]):
                            self.name[0] = self.name[0][:-1]
                    else:
                        print(self.name[0])
            self.screen.fill((0, 0, 0))
            self.tv.update_text(self.name[0])
            self.welcome_text_gr.draw(self.screen)
            self.tv_group.draw(self.screen)
            pygame.display.flip()


pygame.init()

size = 1000, 800
screen = pygame.display.set_mode(size)

ex = BeatRec(screen)
ex.rendering()
