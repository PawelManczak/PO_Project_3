from abc import ABC
from ctypes.wintypes import RGB

from Organisms.Plant import Plant
from world import World


class Grass(Plant, ABC):

    def __init__(self, w: World):
        super(Grass, self).__init__("Grass", 0, w, 't',	RGB(0, 255, 64))

    def get_organism(self):
        return Grass(self.world)