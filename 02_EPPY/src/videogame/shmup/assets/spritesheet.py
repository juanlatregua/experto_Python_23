from os import path
import json

import pygame

class SpriteSheet:

    def __init__(self, image_filename, data_filename):
        if path.isfile(image_filename) and path.isfile(data_filename):
            with open(data_filename) as f:
                self.__dict = json.load(f)

            self.__image = pygame.image.load(image_filename).convert_alpha()
        else:
            self.__dict = {}
            self.__image = pygame.Surface((0,0))

    def get_image(self, name):
        if name in self.__dict:
            return self.__image, pygame.Rect(self.__dict[name])

        return pygame.Surface((0,0)), pygame.Rect(0,0,0,0)