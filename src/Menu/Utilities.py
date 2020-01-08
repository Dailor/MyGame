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


def text_writer(size, all_text, delta, start_coords, font_size=None, *button):
    x, y = start_coords
    dx, dy = delta

    if len(button):
        buttons_group, event, draw_rect, *number_event = button
        number_event = number_event[0] if len(number_event) else 0
    image = pygame.Surface(size)
    image.fill(FILL_COLOR_UTILITIES)

    font_size = FONT_SIZE if font_size is None else font_size
    lines_group = pygame.sprite.Group()

    for line in all_text:
        if len(button):
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
