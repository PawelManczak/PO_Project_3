from abc import ABC
from ctypes.wintypes import RGB

from Organisms.Plant import Plant
from Position import Position
from world import World


class Wolfberries(Plant, ABC):

    def __init__(self, w: World):
        super(Wolfberries, self).__init__("Wolfberries", 99, w, 'W', RGB(252, 43, 112))

    def get_organism(self):
        return Wolfberries(self.world)

    def collision(self, p: Position, a: Position):
        print(self.world_map[a.x][a.y].get_species(), "ate wolfberries and die")
        self.world.delete_organism(p)
        self.world.delete_organism(a)
