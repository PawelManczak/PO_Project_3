

from Organisms.Organism import Organism
from Position import Position


class World:
    # window
    key = None

    def __init__(self, sizeX, sizeY):
        self.turn = 0
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.world_map = [[None for x in range(0, sizeX)] for y in range(0, sizeY)]
        print("konstruktor swiata")

    def print_world(self):
        for y in range(0, self.sizeY):
            for x in range(0, self.sizeX):
                if self.world_map[x][y] is not None:
                    print(self.world_map[x][y].get_char(), end='')
                else:
                    print(' ', end='')
            print("")

        print("----------------")

    def add_organism(self, p: Position, organism: Organism):
        self.world_map[p.x][p.y] = organism

    def delete_organism(self, p: Position):
        self.world_map[p.x][p.y] = None

    def get_map(self):
        return self.world_map

    def take_a_turn(self, key):
        self.key = key
        maxInicjatywa = 7
        maxWiek = self.turn
        for i in range(maxInicjatywa, 0, -1):
            for j in range(maxWiek, 0, -1):
                for y in range(0, self.sizeY):
                    for x in range(0, self.sizeX):
                        if self.world_map[x][y] is not None and self.world_map[x][y].get_age() == j and \
                                self.world_map[x][y].get_initiative() == i and self.world_map[x][y].get_move():
                            # if (self.world_map[x][y] instanceof Czlowiek)
                            # System.out.println("czlowiek here");
                            self.world_map[x][y].change_move()
                            self.world_map[x][y].action(Position(x, y))

        for y in range(0, self.sizeY):
            for x in range(0, self.sizeX):
                if self.world_map[x][y] is not None:
                    self.world_map[x][y].change_move()
                    self.world_map[x][y].increment_age()
        self.turn += 1
