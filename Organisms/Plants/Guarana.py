from abc import ABC
from ctypes.wintypes import RGB

from Organisms.Plant import Plant
from Position import Position
from world import World


class Guarana(Plant, ABC):

    def __init__(self, w: World):
        super(Guarana, self).__init__("Guarana", 0, w, 't', RGB(252, 43, 112))

    def get_organism(self):
        return Guarana(self.world)

    def collision(self, p: Position, a: Position):
        print("strength before eating guarana ", self.world_map[a.x][a.y].get_strength())
        self.world_map[a.x][a.y].set_strength(self.world_map[a.x][a.y].get_strength() + 3)
        super().collision(p, a)
        print("strength after eating guarana ", self.world_map[p.x][p.y].get_strength())
