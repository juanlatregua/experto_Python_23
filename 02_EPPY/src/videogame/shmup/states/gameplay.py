import random

import pygame

from shmup.states.state import State
from shmup.entities.hero import Hero
from shmup.entities.rendergroup import RenderGroup
from shmup.entities.projectiles.projectile_factory import ProjectileType
from shmup.entities.projectiles.projectile_factory import ProjectileFactory
from shmup.assets.assetmanager import AssetManager
from shmup.assets.assetmanager import AssetType
from shmup.config import cfg_item
from shmup.entities.pool import Pool
from shmup.entities.enemy import Enemy
from shmup.entities.enemy import EnemyType

class GamePlay(State):

    def __init__(self):
        super().__init__()
        self.next_state = "Intro"

        self.__pool = Pool(5, Enemy)

        self.__players = RenderGroup()
        self.__allied_projectiles = RenderGroup()
        self.__enemy_projectiles = RenderGroup()
        self.__enemies = RenderGroup()

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                self.done = True
            self.__players.input(event.key, True)
        elif event.type == pygame.KEYUP:
            self.__players.input(event.key, False)

    def update(self, delta_time):
        if random.random() <= cfg_item("entities", "enemies", "spawn_prob"):
            self.__spawn_enemy()

        self.__players.update(delta_time)
        self.__allied_projectiles.update(delta_time)
        self.__enemy_projectiles.update(delta_time)
        self.__enemies.update(delta_time)

        self.__collide()

    def render(self, surface_dst):
        self.__players.draw(surface_dst)
        self.__allied_projectiles.draw(surface_dst)
        self.__enemy_projectiles.draw(surface_dst)
        self.__enemies.draw(surface_dst)

    def release(self):
        pass

    def enter(self):
        self.done = False

        self.__load_assets()
        self.__players.add(Hero(self.spawn_projectile))

    def exit(self):
        self.__players.empty()
        self.__allied_projectiles.empty()
        self.__enemy_projectiles.empty()
        self.__enemies.empty()
        self.__unload_assets()

    def spawn_projectile(self, proj_type, position):
        if proj_type == ProjectileType.Allied:
            self.__allied_projectiles.add(ProjectileFactory.create_projectile(proj_type, position))
        if proj_type == ProjectileType.Enemy:
            self.__enemy_projectiles.add(ProjectileFactory.create_projectile(proj_type, position))

    def __load_assets(self):
        AssetManager.instance().load('gameplay', AssetType.SpriteSheet, cfg_item('entities', 'name'), cfg_item('entities', 'image_file'),cfg_item('entities', 'data_file'))

    def __unload_assets(self):
        AssetManager.instance().clean('gameplay')

    def __spawn_enemy(self):
        enemy_type = EnemyType.Avenger if random.randint(0,1) == 0 else EnemyType.Raptor
        spawn_point = (random.randint(0, cfg_item("game", "screen_size")[0]),0.0)
        enemy = self.__pool.acquire()
        enemy.init(enemy_type, spawn_point, self.spawn_projectile, self.kill_enemy)
        self.__enemies.add(enemy)

    def kill_enemy(self, enemy):
        self.__enemies.remove(enemy)
        self.__pool.release(enemy)

    def __collide(self):
        for player in pygame.sprite.groupcollide(self.__players, self.__enemy_projectiles, True, True).keys():
            print("Game Over")

        for enemy in pygame.sprite.groupcollide(self.__enemies, self.__allied_projectiles, False, True).keys():
            self.kill_enemy(enemy)
            print("Enemy Killed")

        for player, enemies in pygame.sprite.groupcollide(self.__players, self.__enemies, True, False).items():
            for enemy in enemies:
                self.kill_enemy(enemy)
            print("Game Over")