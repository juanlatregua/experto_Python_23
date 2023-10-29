from importlib import resources
from os import path

import pygame

from shmup.assets.asset import Asset
from shmup.assets.asset import AssetType

class AssetManager:

    __instance = None

    @staticmethod
    def instance():
        if AssetManager.__instance is None:
            AssetManager()
        return AssetManager.__instance

    def __init__(self):
        if AssetManager.__instance is None:
            AssetManager.__instance = self

            self.__assets = {}

        else:
            raise Exception("AssetManager is a Singleton, Only One Instance Allowed")

    def load(self, category, asset_type, asset_name, asset_filename_path, data_filename_path = None, font_size=0):
        with resources.path(asset_filename_path[0], asset_filename_path[1]) as asset_path:
            if path.isfile(asset_path) and asset_name not in self.__assets:
                asset = Asset(asset_type, category)
                asset.load(asset_path, data_filename_path, font_size)
                self.__assets[asset_name] = asset

    def get(self, asset_name, sheet_name = None):
        if sheet_name:
            if sheet_name in self.__assets:
                return self.__assets[sheet_name].payload.get_image(asset_name)
            return pygame.Surface((0,0)), pygame.Rect(0,0,0,0)
        else:
            if asset_name in self.__assets:
                if self.__assets[asset_name].asset_type == AssetType.Image:
                    return self.__assets[asset_name].payload, self.__assets[asset_name].get_rect()
                else:
                    return self.__assets[asset_name].payload
            else:
                return None

    def clean(self, category = None):
        if category:
            for k in list(self.__assets.keys()):
                if self.__assets[k].category == category:
                    del self.__assets[k]
        else:
            self.__assets = {}
