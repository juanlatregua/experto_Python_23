import urllib.request
import os

import pygame

from marquee.config import cfg_item

class BitmapFont:

    def __init__(self):
        urllib.request.urlretrieve(cfg_item("font","url"), os.path.join(*cfg_item("font","file")))
        self.__image = pygame.image.load(os.path.join(*cfg_item("font","file"))).convert_alpha()

        self.__create_letter_dict()

    def __create_letter_dict(self):
        letter_size = cfg_item("font", "letter_size")
        self.__font = dict()

        for i in range(cfg_item("font","total_letters")):
            left = letter_size[0] * (i % cfg_item("font", "letters_per_line"))

            top = letter_size[1] * int(i / cfg_item("font", "letters_per_line"))

            self.__font[self.__translate(i)] = pygame.Rect(left, top, letter_size[0], letter_size[1])

    def render(self, surface_dst, letter, pos):
         surface_dst.blit(self.__image, pos, self.__font[letter.upper()])

    def __translate(self, number):
            if number >= 0 and number <= 25:
                character = chr(number + 65)
            elif number >= 26 and number <= 34:
                character = chr(number + 23)
            else:
                rest = ['0', '-', '.', ':', '?', '!', '(', ')', ' ', '+']
                character = rest[number - 35]

            return character