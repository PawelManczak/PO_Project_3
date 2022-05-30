# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

from Organisms.Animals.Fox import Fox
from Organisms.Animals.Sheep import Sheep
from Organisms.Animals.Turtle import Turtle
from Position import Position
from Organisms.Animals.Wolf import Wolf
from world import World

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    SIZE_X: int = 4
    SIZE_Y: int = 4

    world = World(SIZE_X, SIZE_Y)

    wolf = Wolf(world)
    wolf2 = Wolf(world)
    sheep = Sheep(world)
    turtle = Turtle(world)
    fox = Fox(world)

    world.print_world()

    world.add_organism(Position(0, 0), wolf)
    world.add_organism(Position(1, 0), wolf2)
    world.add_organism(Position(1, 1), sheep)
    world.add_organism(Position(2,2), turtle)
    world.add_organism(Position(3, 2), fox)

    world.print_world()

    for line in sys.stdin:
        world.take_a_turn(line)
        world.print_world()
