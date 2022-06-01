from abc import ABC
from ctypes.wintypes import RGB

from Organisms.Plant import Plant
from Position import Position
from world import World


class Dandelion(Plant, ABC):
    # mlecz

    def __init__(self, w: World):
        super(Dandelion, self).__init__("Dandelion", 0, w, 'm', RGB(0, 1000, 200))

    def action(self, p: Position):
        for x in range(3):
            super().action(p)

    def get_organism(self):
        return Dandelion(self.world)
