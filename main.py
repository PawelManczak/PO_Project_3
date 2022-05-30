# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Position import Position
from wolf import Wolf
from world import World

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    SIZE_X: int = 5
    SIZE_Y: int = 5

    world = World(SIZE_X, SIZE_Y)
    wolf = Wolf(world)
    wolf2 = Wolf(world)

    world.print_world()

    world.add_organism(Position(0, 0), wolf)
    world.add_organism(Position(1,0), wolf2)

    world.print_world()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
