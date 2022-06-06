import sys
from abc import ABC
from ctypes.wintypes import RGB

from Organisms.Plants.PineBorscht import PineBorscht
from Position import Position
from world import World
from Organisms.Animal import Animal


def the_shortest_distance(p1: Position, p2: Position):
    distance_to_return = 0
    while p1 != p2:
        if p1.x > p2.x:
            p1.x -= 1
        elif p1.x < p2.x:
            p1.x += 1

        if p1.y > p2.y:
            p1.y -= 1
        elif p1.y < p2.y:
            p1.y += 1

        distance_to_return += 1

    return distance_to_return


class CyberSheep(Animal, ABC):
    def __init__(self, w: World):
        super(CyberSheep, self).__init__("CyberSheep", 11, 4, w, 'Y', RGB(209, 176, 217))

    def get_organism(self):
        return CyberSheep(self.world)

    def _action(self, pos: Position):
        the_nearest_target = None
        distance = sys.maxsize

        for x in range(self.world.get_size_x()):
            for y in range(self.world.get_size_y()):
                if isinstance(self.world_map[x][y], PineBorscht) and the_shortest_distance(Position(x, y),
                                                                                           pos) < distance:
                    the_nearest_target = Position(x, y)
                    distance = the_shortest_distance(Position(x, y), pos)

        if the_nearest_target is None:
            super()._action(pos)
        else:
            # wybor najlepszego pola
            p1 = Position(pos.x, pos.y)

            if p1.x > the_nearest_target.x:
                p1.x -= 1
            elif p1.x < the_nearest_target.x:
                p1.x += 1

            if p1.y > the_nearest_target.y:
                p1.y -= 1
            elif p1.y < the_nearest_target.y:
                p1.y += 1

            print(p1.x, " ", p1.x)
            if self.world_map[p1.x][p1.y] is None or p1.__eq__(pos):  # zwykly ruch na poste
                print("basic")
                self._basic_move(pos, p1)
            elif self.world_map[p1.x][p1.y] is not None and self.world_map[p1.x][
                p1.y].get_species() == self.species:
                # rozmnazanie
                print("rozmnazanie " + self.world_map[p1.x][p1.y].get_species())
                p = super()._get_random_free_position_nearby(p1)
                if p != pos and super().get_age() > 0:
                    self.world_map[p.x][p.y] = self.get_organism()
            else:
                print("klepa: " + self.world_map[p1.x][p1.y].get_species() + " " + self.world_map[pos.x][
                    pos.y].get_species())

                # PINE_BORSCHT
                if isinstance(self.world_map[p1.x][p1.y], PineBorscht):
                    print("cybersheep ate pine borscht")
                    self.world_map[p1.x][p1.y] = self
                    self.world.delete_organism(pos)
                else:
                    self._attack(pos, p1)
