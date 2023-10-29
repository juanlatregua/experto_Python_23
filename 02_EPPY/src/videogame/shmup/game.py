from importlib import resources

import pygame

from shmup.config import cfg_item
from shmup.config import Config
from shmup.fps_stats import FPSStats
from shmup.states.statemanager import StateManager
from shmup.assets.assetmanager import AssetManager
from shmup.assets.assetmanager import AssetType

class Game:

    def __init__(self):
        pygame.init()

        self.__screen = pygame.display.set_mode(cfg_item("game","screen_size"), 0, 32)
        pygame.display.set_caption(cfg_item("game","title"))

        self.__running = False
        self.__load_assets()

        self.__fps_stats = FPSStats()

        self.__state_manager = StateManager()

    def run(self):
        self.__running = True

        last_time = pygame.time.get_ticks()
        time_since_last_update = 0
        while self.__running:
            delta_time, last_time = self.__calc_delta_time(last_time)
            time_since_last_update += delta_time
            while time_since_last_update > cfg_item("timing","time_per_frame"):
                time_since_last_update -= cfg_item("timing","time_per_frame")
                self.__handle_input()
                self.__update(cfg_item("timing","time_per_frame"))

            self.__render()
        self.__release()

    def __handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.__running = False
                if event.key == pygame.K_F5:
                    Config.instance().debug = not Config.instance().debug

                self.__state_manager.handle_input(event)
            elif event.type == pygame.KEYUP:
                self.__state_manager.handle_input(event)

    def __update(self, delta_time):
        self.__state_manager.update(delta_time)
        self.__fps_stats.update(delta_time)

    def __render(self):
        self.__screen.fill(cfg_item("game","background_color"))

        self.__state_manager.render(self.__screen)
        if Config.instance().debug:
            self.__fps_stats.render(self.__screen)

        pygame.display.update()

    def __release(self):
        self.__state_manager.release()
        self.__unload_assets()
        pygame.quit()

    def __calc_delta_time(self, last_time):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - last_time
        return delta_time, current_time

    def __load_assets(self):
        AssetManager.instance().load('game', AssetType.Font, cfg_item("font", "name"), cfg_item("font", "file"), font_size = cfg_item("font", "size"))

    def __unload_assets(self):
        AssetManager.instance().clean('game')
