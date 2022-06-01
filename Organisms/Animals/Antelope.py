from abc import ABC
from ctypes.wintypes import RGB

from random import randint
from typing import OrderedDict

from Organisms.Animal import Animal
from Position import Position
from world import World


class Antelope(Animal, ABC):
    def __init__(self, w: World):
        super(Antelope, self).__init__("antelope", 4, 4, w, 'a', RGB(255,0,255))

    def get_organism(self):
        return Antelope(self.world)

    def collision(self, p: Position, a: Position):
        rand = randint(0, 1)
        if rand == 0:
            super().collision(p,a)
        else:
            free_pos = super().get_random_free_position_nearby(p)
            self.world_map[free_pos.x][free_pos.y] = self
            self.world_map[p.x][p.y] = self.world_map[a.x][a.y]
            self.world_map[a.x][a.y] = None
            print("anteleope has escaped")

    def basic_move(self, old: Position, pos: Position):
        self.world.delete_organism(old)
        self.world.add_organism(pos, self)
        super(Antelope, self).action(pos)