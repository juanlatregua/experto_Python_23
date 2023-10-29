import pygame

from marquee.config import cfg_item
from marquee.bitmapfont import BitmapFont

class Scroll:

    def __init__(self):
        self.__text = list(cfg_item("scroll", "text"))
        self.__pos = pygame.math.Vector2(cfg_item("game", "screen_size")[0], cfg_item("game", "screen_size")[1]/ 2)
        self.__font = BitmapFont()
        self.__current_letter_index = 0

    def update(self, delta_time):
        self.__pos.x -= cfg_item("scroll", "speed") * delta_time
        if self.__pos.x <= -cfg_item("font", "letter_size")[0]:
            self.__pos.x = 0
            self.__current_letter_index += 1

    def render(self, surface_dst):
        letters_in_screen = int(cfg_item("game", "screen_size")[0] / cfg_item("font", "letter_size")[0]) + 1
        for i in range(letters_in_screen):
            index = (self.__current_letter_index + i) % len(self.__text)
            self.__font.render(surface_dst, self.__text[index], (self.__pos.x + (i * cfg_item("font", "letter_size")[0]), self.__pos.y))