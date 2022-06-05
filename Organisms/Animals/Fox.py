from abc import ABC
from ctypes.wintypes import RGB

from Organisms.Animal import Animal
from Position import Position
from world import World


class Fox(Animal, ABC):
    def __init__(self, w: World):
        super(Fox, self).__init__("fox", 3, 7, w, 'l', "orange")

    def get_organism(self):
        return Fox(self.world)

    def attack(self, old: Position, pos: Position):
        if self.world_map[old.x][old.y].get_strength() < self.world_map[pos.x][pos.y].get_strength():
            print("The fox resigned from attacking the stronger opponent")
        else:
            self.world_map[pos.x][pos.y].collision(old, pos);
