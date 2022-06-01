# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

import pygame

from Organisms.Animals.Antelope import Antelope
from Organisms.Animals.Fox import Fox
from Organisms.Animals.Human import Human
from Organisms.Animals.Sheep import Sheep
from Organisms.Animals.Turtle import Turtle
from Position import Position
from Organisms.Animals.Wolf import Wolf
from world import World

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    SIZE_X: int = 8
    SIZE_Y: int = 8

    world = World(SIZE_X, SIZE_Y)

    wolf = Wolf(world)
    wolf2 = Wolf(world)
    sheep = Sheep(world)
    turtle = Turtle(world)
    fox = Fox(world)
    antelope = Antelope(world)
    human = Human(world)

    world.print_world()

    world.add_organism(Position(0, 0), wolf)
    world.add_organism(Position(1, 0), wolf2)
    world.add_organism(Position(1, 1), sheep)
    world.add_organism(Position(2, 2), turtle)
    world.add_organism(Position(3, 2), fox)
    world.add_organism(Position(3, 3), antelope)
    world.add_organism(Position(6, 6), human)

    world.print_world()

    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    key = ""
    SIZE_OF_TILE = 50
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    key = "DOWN"
                elif event.key == pygame.K_UP:
                    key = "UP"
                elif event.key == pygame.K_LEFT:
                    key = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    key = "RIGHT"

                for y in range(0, world.sizeY):
                    for x in range(0, world.sizeX):
                        if world.world_map[y][x] is not None:
                            color = world.world_map[y][x].get_color()
                            pygame.draw.rect(screen, color, pygame.Rect((y+1)*SIZE_OF_TILE,
                                                                        (x+1)*SIZE_OF_TILE, SIZE_OF_TILE, SIZE_OF_TILE))
                        else:
                            pygame.draw.rect(screen, (0,0,0),
                                             pygame.Rect((y + 1) * SIZE_OF_TILE, (x + 1) * SIZE_OF_TILE, SIZE_OF_TILE,
                                                         SIZE_OF_TILE))

                pygame.display.flip()
                world.take_a_turn(key)
                world.print_world()
