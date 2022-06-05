from abc import ABC
from ctypes.wintypes import RGB

from Organisms.Animal import Animal
from Position import Position
from world import World


class Human(Animal, ABC):
    def __init__(self, w: World):
        super(Human, self).__init__("human", 5, 4, w, 'c', RGB(250,255,0))
        self.power_time = 0

    def get_organism(self):
        return None

    def get_power_time(self):
        return self.power_time

    def set_power_time(self, time):
        self.power_time = time

    def action(self, position: Position):
        old = Position(position.x, position.y)
        print("strength: ", super().get_strength())

        if self.world.get_key() == "UP" and position.y > 0:
            position.y -= 1
        elif self.world.get_key() == "DOWN" and position.y < self.world.get_size_y() - 1:
            position.y += 1
        elif self.world.get_key() == "LEFT" and position.x > 0:
            position.x -= 1
        elif self.world.get_key() == "RIGHT" and position.x < self.world.get_size_x() - 1:
            position.x += 1
        elif self.world.get_key() == "POWER":
            if self.power_time == 0:
                self.power_time = 10
                self.set_strength(self.get_strength() + 10)
            else:
                print("wait ", self.power_time, " rounds")

        if old == position:
            return
        if self.world_map[position.x][position.y] is not None:
            self.attack(old, position)
        else:
            self.world.delete_organism(old)
            self.world.add_organism(position, self)

        if self.power_time > 0:
            self.power_time -= 1
            self.set_strength(self.get_strength() - 1)
