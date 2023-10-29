from importlib import resources
import random

import pygame

from falling_letters.config import cfg_item
from falling_letters.entities.letter import Letter

class Manager:

    def __init__(self):
        self.__letters = []

        with resources.path(cfg_item("font", "file")[0], cfg_item("font", "file")[1]) as font_image_file:
            self.__font = pygame.font.Font(font_image_file, cfg_item("font", "size"))

    def handle_input(self, event):
        self.__spawn_letter(event.unicode)

    def update(self, delta_time):
        for letter in self.__letters:
            if letter.is_alive():
                letter.update(delta_time)
            else:
                self.__letters.remove(letter)

    def render(self, surface_dst):
        for letter in self.__letters:
            letter.render(surface_dst)

    def release(self):
        pass

    def __spawn_letter(self, text):
        x_pos = random.randrange(0, cfg_item("game","screen_size")[0])
        init_pos = pygame.math.Vector2(x_pos, 0)
        end_pos = pygame.math.Vector2(x_pos, cfg_item("game","screen_size")[1])

        self.__letters.append(Letter(text, init_pos, end_pos, self.__font))

        print(len(self.__letters))