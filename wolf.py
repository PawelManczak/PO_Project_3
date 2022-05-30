from abc import ABC

from world import World
from Animal import Animal


class Wolf(Animal, ABC):
    def __init__(self, w: World):
        super(Wolf, self).__init__("wilk", 9, 5, w, 'w')

    def get_organism(self):
        return Wolf(self.world)