from abc import ABC

from Organisms.Organism import Organism
from Position import Position


class Animal(Organism, ABC):

    def __init__(self, species, strength, initiative, world, char, color):
        super().__init__(species, strength, initiative, world, char, color)

    def _basic_move(self, old: Position, pos: Position):
        self.world.delete_organism(old)
        self.world.add_organism(pos, self)

    def _attack(self, old: Position, pos: Position):
        self.world_map[pos.x][pos.y]._collision(pos, old)

    def _action(self, pos: Position):
        old = Position(pos.x, pos.y)
        #print(pos.x, " : ", pos.y)
        pos = super(Animal, self)._get_random_position_nearby(pos)
        #print(pos.x, " : ", pos.y)
        if self.world_map[pos.x][pos.y] is None or old.__eq__(pos):  # zwykly ruch na poste
            self._basic_move(old, pos)
        elif self.world_map[pos.x][pos.y] is not None and self.world_map[pos.x][pos.y].get_species() == self.species:
            # rozmnazanie
            print("rozmnazanie " + self.world_map[pos.x][pos.y].get_species())
            p = super()._get_random_free_position_nearby(pos)
            if p != pos and super().get_age() > 0:
                self.world_map[p.x][p.y] = self.get_organism()
        else:
            print("klepa: " + self.world_map[pos.x][pos.y].get_species() + " " + self.world_map[old.x][
                old.y].get_species())
            self._attack(old, pos)
