from abc import ABC

from Organism import Organism
from Position import Position


class Animal(Organism, ABC):

    def __init__(self, species, strength, initiative, world, char):
        super().__init__(species, strength, initiative, world, char)

    def basic_move(self, old: Position, pos: Position):
        self.world.delete_organism(old)
        self.world.add_organism(pos, self)

    def attack(self, old:Position, pos:Position):
        self.world_map[pos.x][pos.y].collsion(pos, old)

    def action(self, pos: Position):
        old = Position(pos.x, pos.y)
        pos = super(Animal, self).get_random_position_nearby(pos)

        if self.world_map[pos.x][pos.y] is None or old.__eq__(pos): # zwykly ruch na poste
            self.basic_move(old, pos)
        elif self.world_map[pos.x][pos.y] is not None and self.world_map[pos.x][pos.y].getSpieces().equals(self.species):
            #rozmnazanie
            print("rozmnazanie " + self.world_map[pos.x][pos.y].getSpieces())
            p = super().get_random_position_nearby(pos)
            if p != pos and super().get_age()>0:
                self.world_map[p.x][p.y] = self.get_organism()
        else:
            print("klepa: " + self.world_map[pos.x][pos.y].getSpieces() + " " + self.world_map[old.x][old.y].getSpieces())
            self.attack(old, pos)

