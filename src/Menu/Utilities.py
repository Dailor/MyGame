import pygame
import os
from Configure import *
from TextBox import TextBox, ClickableTextBox


def sprite_sheet(sheet, columns, rows):
    frames = list()
    rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                       sheet.get_height() // rows)
    for j in range(rows):
        for i in range(columns):
            frame_location = (rect.w * i, rect.h * j)
            frame = sheet.subsurface(pygame.Rect(frame_location, rect.size))
            frame = pygame.transform.scale(frame, SIZE)
            frames.append(frame)
    return frames


def text_writer(size, all_text, delta, start_coords, font_size, buttons_group=None, event=None, draw_rect=None,
                number_event=None):
    x, y = start_coords
    dx, dy = delta

    if buttons_group is not None:
        button = True
        number_event = 0 if number_event is None else number_event
    else:
        button = False
    image = pygame.Surface(size)
    image.fill(FILL_COLOR_UTILITIES)

    lines_group = pygame.sprite.Group()

    for line in all_text:
        if button:
            ClickableTextBox(buttons_group, event, number_event, (x, y), line, font_size, draw_rect=draw_rect,
                             color=COLOR_TEXT)
            number_event += 1
        else:
            TextBox(lines_group, (x, y), line, font_size, draw_rect=False, color=COLOR_TEXT)
        x += dx
        y += dy

    lines_group.draw(image)
    image.set_colorkey(FILL_COLOR_UTILITIES)
    return image


def load_image(path, colorkey=None):
    path = os.path.join('data', *path)
    image = pygame.image.load(path)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def load_image_v2(path, size=None):
    image = load_image(path, None)
    image = pygame.transform.scale(image, size)
    print(size)
    return image
