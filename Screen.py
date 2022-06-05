import sys
from ctypes.wintypes import RGB
from math import floor

import pygame

import world
from Organisms.Animals.Antelope import Antelope

from Organisms.Plants.PineBorscht import PineBorscht
from Organisms.Plants.Guarana import Guarana
from Organisms.Animals.Fox import Fox
from Organisms.Plants.Dandelion import Dandelion
from Organisms.Animals.Sheep import Sheep
from Organisms.Plants.Grass import Grass
from Organisms.Plants.Wolfberries import Wolfberries
from Organisms.Animals.Wolf import Wolf
from Organisms.Animals.Turtle import Turtle
from Organisms.Animals.CyberSheep import CyberSheep


def print_map(world: world.World, screen, SIZE_OF_TILE):
    for y in range(0, world.get_size_y()):
        for x in range(0, world.get_size_y()):
            if world.world_map[y][x] is not None:
                color = world.world_map[y][x].get_color()
                pygame.draw.rect(screen, color, pygame.Rect((y + 1) * SIZE_OF_TILE,
                                                            (x + 1) * SIZE_OF_TILE, SIZE_OF_TILE,
                                                            SIZE_OF_TILE))
            else:
                pygame.draw.rect(screen, (0, 0, 0),
                                 pygame.Rect((y + 1) * SIZE_OF_TILE, (x + 1) * SIZE_OF_TILE, SIZE_OF_TILE,
                                             SIZE_OF_TILE))


def show_game(world: world.World):
    pygame.init()
    screen = pygame.display.set_mode((1280, 720), 0, 32)

    screen.fill("black")
    print("show_game")
    SIZE_OF_TILE = 50
    print_map(world, screen, SIZE_OF_TILE)

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                x = floor((x - SIZE_OF_TILE) / SIZE_OF_TILE)
                y = floor((y - SIZE_OF_TILE) / SIZE_OF_TILE)
                print(x, " ", y)
                if x <= world.get_size_x() and y <= world.get_size_y():
                    world.world_map[x][y] = show_menu_list(world)
                    show_game(world)

            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    key = "DOWN"
                elif event.key == pygame.K_UP:
                    key = "UP"
                elif event.key == pygame.K_LEFT:
                    key = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    key = "RIGHT"
                elif event.key == pygame.K_SPACE:
                    key = "POWER"
                elif event.key == pygame.K_l:
                    world.load_from_file()
                    show_game(world)
                    continue
                elif event.key == pygame.K_s:
                    # save
                    world.save()
                    continue

                print_map(world, screen, SIZE_OF_TILE)
                pygame.display.flip()
                world.take_a_turn(key)
                world.print_world()


def show_menu_list(world: world.World):
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        screen = pygame.display.set_mode((1280, 720), 0, 32)
        screen.fill("white")
        SIZE_OF_TILE = 50
        # wolf
        wolf_rect = pygame.Rect(0, 0, SIZE_OF_TILE, SIZE_OF_TILE)
        pygame.draw.rect(screen, RGB(131, 139, 131), wolf_rect)
        # antelope
        antelope_rect = pygame.Rect(SIZE_OF_TILE, 0, SIZE_OF_TILE, SIZE_OF_TILE)
        pygame.draw.rect(screen, RGB(255, 0, 255), antelope_rect)
        # cybersheep
        cyber_rect = pygame.Rect(SIZE_OF_TILE * 2, 0, SIZE_OF_TILE, SIZE_OF_TILE)
        pygame.draw.rect(screen, RGB(209, 176, 217), cyber_rect)
        # fox
        fox_rect = pygame.Rect(SIZE_OF_TILE * 3, 0, SIZE_OF_TILE, SIZE_OF_TILE)
        pygame.draw.rect(screen, "orange", fox_rect)
        # Sheep
        sheep_rect = pygame.Rect(SIZE_OF_TILE * 4, 0, SIZE_OF_TILE, SIZE_OF_TILE)
        pygame.draw.rect(screen, "white", sheep_rect)
        # turtle
        turtle_rect = pygame.Rect(SIZE_OF_TILE * 5, 0, SIZE_OF_TILE, SIZE_OF_TILE)
        pygame.draw.rect(screen, RGB(0, 128, 0), turtle_rect)
        # dandelion
        dandelion_rect = pygame.Rect(SIZE_OF_TILE * 6, 0, SIZE_OF_TILE, SIZE_OF_TILE)
        pygame.draw.rect(screen, "yellow", dandelion_rect)
        # grass
        grass_rect = pygame.Rect(SIZE_OF_TILE * 7, 0, SIZE_OF_TILE, SIZE_OF_TILE)
        pygame.draw.rect(screen, RGB(0, 255, 64), grass_rect)
        # Guarana
        guarana_rect = pygame.Rect(SIZE_OF_TILE * 8, 0, SIZE_OF_TILE, SIZE_OF_TILE)
        pygame.draw.rect(screen, "#FC2B70", guarana_rect)
        # Pine borscht
        pine_rect = pygame.Rect(SIZE_OF_TILE * 9, 0, SIZE_OF_TILE, SIZE_OF_TILE)
        pygame.draw.rect(screen, RGB(142, 5, 212), pine_rect)
        # wolfberries
        wberr_rect = pygame.Rect(SIZE_OF_TILE * 10, 0, SIZE_OF_TILE, SIZE_OF_TILE)
        pygame.draw.rect(screen, RGB(252, 43, 112), wberr_rect)

        for event in pygame.event.get():
            pygame.display.update()
            # show_menu_list(world)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if wolf_rect.collidepoint(event.pos):
                    return Wolf(world)
                elif antelope_rect.collidepoint(event.pos):
                    return Antelope(world)
                elif fox_rect.collidepoint(event.pos):
                    return Fox(world)
                elif cyber_rect.collidepoint(event.pos):
                    return CyberSheep(world)
                elif sheep_rect.collidepoint(event.pos):
                    return Sheep(world)
                elif turtle_rect.collidepoint(event.pos):
                    return Turtle(world)
                elif dandelion_rect.collidepoint(event.pos):
                    return Dandelion(world)
                elif grass_rect.collidepoint(event.pos):
                    return Grass(world)
                elif guarana_rect.collidepoint(event.pos):
                    return Guarana(world)
                elif pine_rect.collidepoint(event.pos):
                    return PineBorscht(world)
                elif wberr_rect.collidepoint(event.pos):
                    return Wolfberries(world)

            if event.type == pygame.QUIT:
                sys.exit(0)
