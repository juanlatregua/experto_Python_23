from enum import Enum
from importlib import resources

import pygame

from shmup.assets.spritesheet import SpriteSheet

class AssetType(Enum):
    Image = 0,
    SpriteSheet = 1,
    Font = 2,
    Sound = 3,
    Music = 4

class Asset:

    def __init__(self, asset_type, category):
        self.asset_type = asset_type
        self.category = category

    def load(self, asset_filename_path, data_filename_path = None, font_size = 0):
        if self.asset_type == AssetType.Image:
            self.payload = pygame.image.load(asset_filename_path).convert_alpha()
        elif self.asset_type == AssetType.SpriteSheet:
            with resources.path(data_filename_path[0], data_filename_path[1]) as data_path:
                self.payload = SpriteSheet(asset_filename_path, data_path)
        elif self.asset_type == AssetType.Font:
            self.payload = pygame.font.Font(asset_filename_path, font_size)
        elif self.asset_type == AssetType.Sound:
            self.payload = pygame.mixer.Sound(asset_filename_path)
        elif self.asset_type == AssetType.Music:
            self.payload = asset_filename_path