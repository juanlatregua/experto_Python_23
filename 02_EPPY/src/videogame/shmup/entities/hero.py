from importlib import resources

import pygame

from shmup.config import cfg_item
from shmup.config import Config
from shmup.entities.gameobject import GameObject
from shmup.entities.projectiles.projectile_factory import ProjectileType
from shmup.assets.assetmanager import AssetManager

class Hero(GameObject):

    def __init__(self, spawn_projectile_callback):
        super().__init__()

        self.__spawn_projectile_callback = spawn_projectile_callback

        _, rect = AssetManager.instance().get(cfg_item("entities", "hero", "name"), cfg_item("entities","name"))

        self._position = pygame.math.Vector2(cfg_item("game","screen_size")[0]/2, cfg_item("game","screen_size")[1]/2)

        self.rect = rect.copy()
        self.render_rect = self.rect.copy()
        self.rect.inflate_ip(self.rect.width * cfg_item("entities","hero", "percent_collider")[0],self.rect.height * cfg_item("entities","hero", "percent_collider")[1])

        self._center()

        self.__is_moving_left = False
        self.__is_moving_right = False
        self.__is_moving_up = False
        self.__is_moving_down = False

        self.__cool_down = 0.0

    def handle_input(self, key, is_pressed):
        if key == pygame.K_LEFT:
            self.__is_moving_left = is_pressed
        if key == pygame.K_RIGHT:
            self.__is_moving_right = is_pressed
        if key == pygame.K_UP:
            self.__is_moving_up = is_pressed
        if key == pygame.K_DOWN:
            self.__is_moving_down = is_pressed
        if key ==  pygame.K_SPACE:
            if self.__cool_down <= 0.0:
                self.__fire()

    def update(self, delta_time):
        velocity = pygame.math.Vector2(0.0, 0.0)

        if self.__is_moving_left:
            velocity.x -= cfg_item("entities","hero", "speed")
        if self.__is_moving_right:
            velocity.x += cfg_item("entities","hero", "speed")
        if self.__is_moving_up:
            velocity.y -= cfg_item("entities","hero", "speed")
        if self.__is_moving_down:
            velocity.y += cfg_item("entities","hero", "speed")

        distance = velocity * delta_time
        self._position += distance
        self._center()

        if self.__cool_down >= 0.0:
            self.__cool_down -= delta_time

    def render(self, surface_dst):
        hero_name = cfg_item("entities","hero","name")
        if self.__is_moving_left:
            hero_name = cfg_item("entities","hero","name_left")
        if self.__is_moving_right:
            hero_name = cfg_item("entities","hero","name_right")
        if self.__is_moving_left and self.__is_moving_right:
            hero_name = cfg_item("entities","hero","name")

        image, rect = AssetManager.instance().get(hero_name, cfg_item("entities","name"))
        surface_dst.blit(image, self.render_rect, rect)

        if Config.instance().debug:
            self._render_debug(surface_dst)

    def release(self):
        pass

    def __fire(self):
        self.__cool_down = cfg_item("entities", "hero", "cool_down_time")
        self.__spawn_projectile_callback(ProjectileType.Allied, self.render_rect.midtop)