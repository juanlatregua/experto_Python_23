from importlib import resources

import pygame

from shmup.entities.projectiles.projectile import Projectile
from shmup.config import cfg_item

class Projectile_Allied(Projectile):

    def __init__(self, position):
        velocity = cfg_item("entities", "projectiles", "allied", "velocity")
        self.name = cfg_item("entities", "projectiles", "allied", "name")

        super().__init__(position, velocity)
