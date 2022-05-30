from abc import abstractmethod
from random import random

from Position import Position


class Organism:

    def __init__(self, species, strength, initiative, world, char):
        self.move = False
        self.species = species
        self.strength = strength
        self.initiative = initiative
        self.world: world = world
        self.world_map = world.get_map()
        self.age = 0
        self.char = char

    def get_move(self):
        return self.move

    def get_initiative(self):
        return self.initiative

    def get_strength(self):
        return self.strength

    def get_age(self):
        return self.age

    def get_species(self):
        return self.species

    def change_move(self):
        if self.move:
            self.move = False
        else:
            self.move = True

    def set_strength(self, strength):
        self.strength = strength

    def increment_age(self):
        self.age += 1

    def set_move(self, value):
        self.move = value

    @abstractmethod
    def action(self, p: Position):
        pass

    @abstractmethod
    def collision(self, a:Position, p:Position):
        if self.world_map[p.x][p.y].get_strength() < self.world_map[a.x][a.y].get_strength():
            self.world_map[p.x][p.y] = self.world_map[a.y][a.y]
            self.world_map[a.y][a.y] = None
        else:
            self.world_map[a.x][a.y] = None

    @abstractmethod
    def color(self):
        pass

    @abstractmethod
    def get_organism(self):
        pass

    def get_char(self):
        return self.char

    def collision(self, a: Position, p: Position):
        if self.world_map[p.x][p.y].get_strength() > self.world_map[a.x][a.y].get_strength():
            self.world_map[p.x][p.y] = self.world_map[a.y][a.y]
            self.world_map[a.y][a.y] = None
        else:
            self.world_map[a.y][a.y] = None

    def get_random_position_nearby(self, p):

        opcje = {}
        while opcje.size() < 8:

            los = random() % 8

            match los:
                case 0:
                    opcje.add(0)
                    if p.x > 0 and p.y > 0 and self.world_map[p.x - 1][p.y - 1] is None:
                        return Position(p.x - 1, p.y - 1)
                case 1:
                    opcje.add(1)
                    if p.y > 0 and self.world_map[p.x][p.y - 1] is None:
                        return Position(p.x, p.y - 1)
                case 2:
                    opcje.add(2)
                    if p.x < self.world.sizeX - 1 and p.y > 0 and self.world_map[p.x + 1][p.y - 1] is None:
                        return Position(p.x + 1, p.y - 1)
                case 3:
                    opcje.add(3)
                    if p.x > 0 and self.world_map[p.x - 1][p.y] is None:
                        return Position(p.x - 1, p.y)
                case 4:
                    opcje.add(4)
                    if p.x < self.world.sizeX - 1 and self.world_map[p.x + 1][p.y] is None:
                        return Position(p.x + 1, p.y)
                case 5:
                    opcje.add(5)
                    if p.x > 0 and p.y < self.world.sizeY - 1 and self.world_map[p.x - 1][p.y + 1] is None:
                        return Position(p.x - 1, p.y + 1)
                case 6:
                    opcje.add(6)
                    if p.y < self.world.sizeY - 1 and self.world_map[p.x][p.y + 1] is None:
                        return Position(p.x, p.y + 1)
                case 7:
                    opcje.add(7)
                    if p.x < self.world.sizeX - 1 and p.y < self.world.sizeY - 1:
                        if self.world_map[p.x + 1][p.y + 1] is None:
                            return Position(p.x + 1, p.y + 1)
        return p
