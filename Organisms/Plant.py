from abc import ABC
from random import randint

from Organisms.Organism import Organism
from Position import Position


class Plant(Organism, ABC):

    def __init__(self, species, strength, world, char, color):
        super(Plant, self).__init__(species, strength, 0, world, char, color)

    def _action(self, p: Position):
        rand = randint(0, 2)
        if rand == 0 and self.get_age() > 0:

            new_p = self._get_random_free_position_nearby(p)
            if p != new_p:
                self.world_map[new_p.x][new_p.y] = self.get_organism()

    def _collision(self, p: Position, a: Position):
        print(self.world_map[a.x][a.y].get_species() + "ate " + self.world_map[p.x][p.y].get_species())
        self.world_map[p.x][p.y] = self.world_map[a.x][a.y]
        self.world_map[a.x][a.y] = None
