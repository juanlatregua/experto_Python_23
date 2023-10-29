from enum import Enum

from shmup.entities.projectiles.projectile_allied import Projectile_Allied
from shmup.entities.projectiles.projectile_enemy import Projectile_Enemy

class ProjectileType(Enum):
    Allied = 0
    Enemy = 1

class ProjectileFactory:

    @staticmethod
    def create_projectile(proj_type, position):
        if proj_type == ProjectileType.Allied:
            return Projectile_Allied(position)
        elif proj_type == ProjectileType.Enemy:
            return Projectile_Enemy(position)
