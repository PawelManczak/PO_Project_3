from abc import ABC

from Organisms.Animal import Animal
from world import World


class Sheep(Animal, ABC):
    def __init__(self, w: World):
        super(Sheep, self).__init__("sheep", 4, 4, w, 'o', "white")

    def get_organism(self):
        return Sheep(self.world)