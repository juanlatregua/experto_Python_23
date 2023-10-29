from importlib import resources

import pygame

from shmup.entities.projectiles.projectile import Projectile
from shmup.config import cfg_item

class Projectile_Enemy(Projectile):

    def __init__(self, position):
        velocity = cfg_item("entities", "projectiles", "enemy", "velocity")
        self.name = cfg_item("entities", "projectiles", "enemy", "name")

        super().__init__(position, velocity)