from abc import ABC, abstractmethod

import pygame

from shmup.config import cfg_item

class GameObject(pygame.sprite.Sprite, ABC):

    def __init__(self):
        super().__init__()
        self._position = pygame.math.Vector2(0.0, 0.0)
        self.rect = pygame.Rect(0,0,0,0)
        self.render_rect = pygame.Rect(0,0,0,0)

    @abstractmethod
    def handle_input(self, key, is_pressed):
        pass

    @abstractmethod
    def update(self, delta_time):
        pass

    @abstractmethod
    def render(self, surface_dst):
        pass

    @abstractmethod
    def release(self):
        pass

    def _center(self):
        self.rect.center = self._position.xy
        self.render_rect.center = self._position.xy

    def _render_debug(self, surface_dst):
        pygame.draw.rect(surface_dst, cfg_item("debug",
            "collider_color"), self.rect, 1)
        pygame.draw.rect(surface_dst, cfg_item("debug", "render_color"), self.render_rect, 1)