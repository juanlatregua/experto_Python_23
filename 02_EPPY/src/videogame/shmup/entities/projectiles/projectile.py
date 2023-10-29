import pygame

from shmup.entities.gameobject import GameObject
from shmup.config import cfg_item
from shmup.config import Config
from shmup.assets.assetmanager import AssetManager

class Projectile(GameObject):

    def __init__(self, position, velocity):
        super().__init__()

        self._position = pygame.math.Vector2(position)
        self.__velocity = pygame.math.Vector2(velocity)

        _, rect = AssetManager.instance().get(self.name, cfg_item("entities","name"))

        self.rect = rect.copy()
        self.render_rect = self.rect.copy()

        self._center()

    def handle_input(self, key, is_pressed):
        pass

    def update(self, delta_time):
        self._position += self.__velocity * delta_time
        self._center()

        if self._position.y > cfg_item("game", "screen_size")[1] or self._position.y < 0:
            self.kill()

    def render(self, surface_dst):
        image, rect = AssetManager.instance().get(self.name, cfg_item("entities","name"))
        surface_dst.blit(image, self.render_rect, rect)

        if Config.instance().debug:
            self._render_debug(surface_dst)

    def release(self):
        pass