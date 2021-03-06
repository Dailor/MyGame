import pygame
from Configure import *


class TextBox(pygame.sprite.Sprite):
    def __init__(self, group, coords, text, font_size, color=None, draw_rect=True):
        super().__init__(group)
        self.gr = group

        if color is None:
            self.color = COLOR_TEXT
        else:
            self.color = tuple(color)

        self.draw_rect_bool = draw_rect

        self.coords = coords
        self.font_size = font_size

        self.font = pygame.font.Font(None, font_size)
        self.text = self.font.render(text, 0, self.color)

        self.SIZE = self.text.get_width() * 1.25, self.text.get_height() * 1.30
        self.SIZE = tuple(map(int, self.SIZE))

        self.image_init()


        if self.draw_rect_bool:
            self.draw_rect()
        self.draw_text()
        self.image.set_colorkey(COLOR_FILL)

    def image_init(self):
        self.image = pygame.Surface(self.SIZE)
        self.image.fill(COLOR_FILL)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.coords)

    def draw_rect(self):
        pygame.draw.rect(self.image, self.color, (0, 0, *self.SIZE), 1)

    def draw_text(self):
        if self.draw_rect_bool is True:
            text_coords = self.SIZE[0] * 0.25 / 2, self.SIZE[1] * 0.3 / 2
        else:
            text_coords = 0, 0
        text_coords = tuple(map(int, text_coords))
        self.image.blit(self.text, text_coords)


class EditText(TextBox):
    SIZE = 500,40
    def __init__(self, group, coords, text, font_size, color=None, draw_rect=True):
        super(EditText, self).__init__(group, coords, text, font_size, color=None, draw_rect=True)

    def image_init(self):
        self.image = pygame.Surface(EditText.SIZE)
        self.image.fill(COLOR_FILL)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.coords)


    def update_text(self, text):
        self.gr.remove()
        self.__init__(self.gr, self.coords, text, self.font_size, self.color, self.draw_rect_bool)

    def draw_rect(self):
        pygame.draw.rect(self.image, self.color, (0, 0, *EditText.SIZE), 1)

    def draw_text(self):
        if self.draw_rect_bool is True:
            text_coords = EditText.SIZE[0] * 0.25 / 2, EditText.SIZE[1] * 0.3 / 2
        else:
            text_coords = 0, 0
        text_coords = tuple(map(int, text_coords))
        self.image.blit(self.text, text_coords)

class ClickableTextBox(TextBox):
    def __init__(self, group, event_taker, number_event, coords, text, font_size, color=None, draw_rect=True):
        super().__init__(group, coords, text, font_size, color, draw_rect)
        self.event_taker = event_taker
        self.number_event = number_event

    def update(self, coords, *params):
        if self.rect.collidepoint(coords):
            self.event_taker.append(self.number_event)
