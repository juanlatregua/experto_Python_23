from enum import Enum
import random

import pygame

from shmup.entities.gameobject import GameObject
from shmup.entities.pool import ReusableObject
from shmup.config import cfg_item
from shmup.config import Config
from shmup.assets.assetmanager import AssetManager
from shmup.entities.projectiles.projectile_factory import ProjectileType

class EnemyType(Enum):
    Raptor = 0,
    Avenger = 1

class Enemy(GameObject, ReusableObject):

    def __init__(self):
        super().__init__()

    def init(self, enemy_type, spawn_point, spawn_projectile_callback, kill_callback):
        self.__spawn_projectile_callback = spawn_projectile_callback
        self.__kill_callback = kill_callback
        self.__type = enemy_type

        if self.__type == EnemyType.Avenger:
            self.__enemy_name = cfg_item("entities", "enemies", "avenger", "name")
            self.__speed = cfg_item("entities", "enemies", "avenger", "speed")
            self.__fire_rate = cfg_item("entities", "enemies", "avenger", "fire_rate")

        if self.__type == EnemyType.Raptor:
            self.__enemy_name = cfg_item("entities", "enemies", "raptor", "name")
            self.__speed = cfg_item("entities", "enemies", "raptor", "speed")
            self.__fire_rate = cfg_item("entities", "enemies", "raptor", "fire_rate")

        _, rect = AssetManager.instance().get(self.__enemy_name, cfg_item("entities","name"))

        self._position = pygame.math.Vector2(spawn_point[0], spawn_point[1])

        self.rect = rect.copy()
        self.render_rect = self.rect.copy()
        self.rect.inflate_ip(self.rect.width * cfg_item("entities","enemies", "percent_collider")[0],self.rect.height * cfg_item("entities","enemies", "percent_collider")[1])

        self._center()

    def handle_input(self, key, is_pressed):
        pass

    def update(self, delta_time):
        if random.random() <= self.__fire_rate:
            self.__spawn_projectile_callback(ProjectileType.Enemy, self.render_rect.midbottom)

        velocity = pygame.math.Vector2(0.0, self.__speed)
        distance = velocity * delta_time
        self._position += distance
        self._center()

        if self._position.y >= cfg_item("game", "screen_size")[1]:
            self.__kill_callback(self)

    def render(self, surface_dst):
        image, rect = AssetManager.instance().get(self.__enemy_name, cfg_item("entities","name"))
        img = pygame.Surface(rect.size, pygame.SRCALPHA, 32)
        img.blit(image, (0,0), rect)
        img = pygame.transform.rotate(img, -180)
        surface_dst.blit(img, self.render_rect)

        if Config.instance().debug:
            self._render_debug(surface_dst)

    def release(self):
        pass

    def reset(self):
        self.__enemy_name = ""
        self.rect = pygame.Rect(0,0,0,0)