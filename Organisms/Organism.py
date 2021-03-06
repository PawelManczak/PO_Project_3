from abc import abstractmethod
from random import randint

from Position import Position


class Organism:

    def __init__(self, species, strength, initiative, world, char, color):
        self.move = False
        self.species = species
        self.strength = strength
        self.initiative = initiative
        self.world: world = world
        self.world_map = world.get_map()
        self.age = 0
        self.char = char
        self.color = color

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

    def set_age(self, age):
        self.age = age

    @abstractmethod
    def _action(self, p: Position):
        pass

    def _collision(self, a: Position, p: Position):
        if self.world_map[p.x][p.y].get_strength() < self.world_map[a.x][a.y].get_strength():
            self.world_map[p.x][p.y] = self.world_map[a.x][a.y]
            self.world_map[a.x][a.y] = None
        else:
            self.world_map[a.x][a.y] = None

    def get_color(self):
        return self.color

    @abstractmethod
    def get_organism(self):
        pass

    def get_char(self):
        return self.char

    def _get_random_position_nearby(self, p):
        options = set()

        while len(options) < 8:
            randOpt = randint(0, 7)
            # print(randOpt)
            match randOpt:
                case 0:
                    options.add(0)
                    if p.x > 0 and p.y > 0:
                        return Position(p.x - 1, p.y - 1)
                case 1:
                    options.add(1)
                    if p.y > 0:
                        return Position(p.x, p.y - 1)
                case 2:
                    options.add(2)
                    if p.x < self.world.get_size_x() - 1 and p.y > 0:
                        return Position(p.x + 1, p.y - 1)
                case 3:
                    options.add(3)
                    if p.x > 0:
                        return Position(p.x - 1, p.y)
                case 4:
                    options.add(4)
                    if p.x < self.world.get_size_x() - 1:
                        return Position(p.x + 1, p.y)
                case 5:
                    options.add(5)
                    if p.x > 0 and p.y < self.world.get_size_y() - 1:
                        return Position(p.x - 1, p.y + 1)
                case 6:
                    options.add(6)
                    if p.y < self.world.get_size_y() - 1:
                        return Position(p.x, p.y + 1)
                case 7:
                    options.add(7)
                    if p.x < self.world.get_size_x() - 1 and p.y < self.world.get_size_y() - 1:
                        return Position(p.x + 1, p.y + 1)
        return p

    def _get_random_free_position_nearby(self, p):

        options = set()

        while len(options) < 8:
            randOpt = randint(0, 7)
            # print(randOpt)
            match randOpt:
                case 0:
                    options.add(0)
                    if p.x > 0 and p.y > 0 and self.world_map[p.x - 1][p.y - 1] is None:
                        return Position(p.x - 1, p.y - 1)
                case 1:
                    options.add(1)
                    if p.y > 0 and self.world_map[p.x][p.y - 1] is None:
                        return Position(p.x, p.y - 1)
                case 2:
                    options.add(2)
                    if p.x < self.world.get_size_x() - 1 and p.y > 0 and self.world_map[p.x + 1][p.y - 1] is None:
                        return Position(p.x + 1, p.y - 1)
                case 3:
                    options.add(3)
                    if p.x > 0 and self.world_map[p.x - 1][p.y] is None:
                        return Position(p.x - 1, p.y)
                case 4:
                    options.add(4)
                    if p.x < self.world.get_size_x() - 1 and self.world_map[p.x + 1][p.y] is None:
                        return Position(p.x + 1, p.y)
                case 5:
                    options.add(5)
                    if p.x > 0 and p.y < self.world.get_size_y() - 1 and self.world_map[p.x - 1][p.y + 1] is None:
                        return Position(p.x - 1, p.y + 1)
                case 6:
                    options.add(6)
                    if p.y < self.world.get_size_y() - 1 and self.world_map[p.x][p.y + 1] is None:
                        return Position(p.x, p.y + 1)
                case 7:
                    options.add(7)
                    if p.x < self.world.get_size_x() - 1 and p.y < self.world.get_size_y() - 1:
                        if self.world_map[p.x + 1][p.y + 1] is None:
                            return Position(p.x + 1, p.y + 1)
        return p
