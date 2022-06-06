from abc import ABC

from Organisms.Plant import Plant
from Position import Position
from world import World


class Dandelion(Plant, ABC):

    def __init__(self, w: World):
        super(Dandelion, self).__init__("Dandelion", 0, w, 'm', "yellow")

    def _action(self, p: Position):
        for x in range(3):
            super()._action(p)

    def get_organism(self):
        return Dandelion(self.world)
