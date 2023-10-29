from importlib import resources

import pygame

from shmup.states.state import State
from shmup.config import cfg_item
from shmup.assets.assetmanager import AssetManager

class Intro(State):

    def __init__(self):
        super().__init__()
        self.next_state = "GamePlay"

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            self.done = True

    def update(self, delta_time):
        pass

    def render(self, surface_dst):
        surface_dst.blit(self.__image, (cfg_item("intro", "pos_label")[0], cfg_item("intro", "pos_label")[1]))
        surface_dst.blit(self.__image_key, (cfg_item("intro", "pos_key")[0], cfg_item("intro", "pos_key")[1]))

    def release(self):
        pass

    def enter(self):
        self.done = False

        font = AssetManager.instance().get(cfg_item("font", "name"))

        self.__image = font.render(f"Welcome to my Super Mega Game", True, cfg_item("game", "foreground_color"), None)
        self.__image_key = font.render(f"Press any Key to Play", True, cfg_item("game", "foreground_color"), None)

    def exit(self):
        pass