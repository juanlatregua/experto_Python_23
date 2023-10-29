import random

from falling_letters.config import cfg_item

class Letter:

    def __init__(self, text, init_pos, end_pos, font):
        self.__position = init_pos
        self.__end_pos = end_pos
        self.__speed = random. uniform(cfg_item("letter","speed_range")[0],cfg_item("letter","speed_range")[1])

        self.__image = font.render(f"{text}", True, cfg_item("game","foreground_color"), None)

        self.__alive = True

    def update(self, delta_time):
        self.__position.y += self.__speed * delta_time

        if self.__position.y >= self.__end_pos.y:
            self.__alive = False

    def render(self, surface_dst):
        surface_dst.blit(self.__image, self.__position.xy)

    def is_alive(self):
        return self.__alive