from Organisms.Animals.Antelope import Antelope
from Organisms.Animals.CyberSheep import CyberSheep
from Organisms.Animals.Fox import Fox
from Organisms.Animals.Human import Human
from Organisms.Animals.Sheep import Sheep
from Organisms.Animals.Turtle import Turtle
from Organisms.Plants.Dandelion import Dandelion
from Organisms.Plants.Grass import Grass
from Organisms.Plants.Guarana import Guarana
from Organisms.Plants.PineBorscht import PineBorscht
from Organisms.Plants.Wolfberries import Wolfberries
from Position import Position
from Organisms.Animals.Wolf import Wolf
from Screen import show_game
from world import World

if __name__ == '__main__':
    SIZE_X: int = 20
    SIZE_Y: int = 8

    world = World(SIZE_Y, SIZE_X)

    # default set

    wolf = Wolf(world)
    wolf2 = Wolf(world)
    sheep = Sheep(world)
    turtle = Turtle(world)
    fox = Fox(world)
    antelope = Antelope(world)
    human = Human(world)
    dandelion = Dandelion(world)
    grass = Grass(world)
    guarana = Guarana(world)
    wolfberries = Wolfberries(world)
    pine_borscht = PineBorscht(world)
    cybersheep = CyberSheep(world)

    world.add_organism(Position(0, 0), wolf)
    world.add_organism(Position(1, 1), sheep)
    world.add_organism(Position(2, 2), turtle)
    world.add_organism(Position(3, 2), fox)
    world.add_organism(Position(3, 3), antelope)
    world.add_organism(Position(6, 6), human)
    # world.add_organism(Position(7, 7), dandelion)
    # world.add_organism(Position(7, 6), grass)
    # world.add_organism(Position(5, 6), guarana)
    # world.add_organism(Position(2, 7), wolfberries)
    world.add_organism(Position(0, 7), pine_borscht)
    world.add_organism(Position(7, 7), cybersheep)

    show_game(world)
