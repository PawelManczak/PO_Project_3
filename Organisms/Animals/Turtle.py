from abc import ABC
from ctypes.wintypes import RGB
from random import randint

from Position import Position
from world import World
from Organisms.Animal import Animal


class Turtle(Animal, ABC):
    def __init__(self, w: World):
        super(Turtle, self).__init__("turtle", 2, 1, w, 'z', RGB(0,128,0))

    def get_organism(self):
        return Turtle(self.world)

    def action(self, pos: Position):
        rand = randint(0, 1)

        if rand == 0:
            super().action(pos)
        else:
            print("the turtle is resting")

    def collision(self, p: Position, a: Position):
        if self.world_map[a.x][a.y].get_strength() >= 5:
            super(Turtle, self).collision(p, a)
        else:
            print("the turtle deflected the attack!")
