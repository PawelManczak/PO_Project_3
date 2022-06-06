from Organisms.Organism import Organism
from Position import Position


class World:
    def __init__(self, size_x, size_y):
        self.max_initiative = 0
        self.turn = 0
        self.size_x = size_x
        self.size_y = size_y
        self.world_map = [[None for _ in range(0, size_y)] for _ in range(0, size_x)]

    def print_world(self):
        for y in range(0, self.size_y):
            for x in range(0, self.size_x):
                if self.world_map[x][y] is not None:
                    print(self.world_map[x][y].get_char(), end='')
                else:
                    print(' ', end='')
            print("")

        print("----------------")

    def add_organism(self, p: Position, organism: Organism):
        self.world_map[p.x][p.y] = organism
        self.max_initiative = max(self.max_initiative, organism.get_initiative())

    def delete_organism(self, p: Position):
        self.world_map[p.x][p.y] = None

    def get_map(self):
        return self.world_map

    def take_a_turn(self, key):
        self.key = key
        max_initiative = self.max_initiative
        
        for i in range(max_initiative, -1, -1):
            for j in range(self.turn, 0, -1):
                for y in range(0, self.size_y):
                    for x in range(0, self.size_x):
                        if self.world_map[x][y] is not None and self.world_map[x][y].get_age() == j and \
                                self.world_map[x][y].get_initiative() == i and self.world_map[x][y].get_move():
                            self.world_map[x][y].change_move()
                            self.world_map[x][y]._action(Position(x, y))

        for y in range(0, self.size_y):
            for x in range(0, self.size_x):
                if self.world_map[x][y] is not None:
                    self.world_map[x][y].change_move()
                    self.world_map[x][y].increment_age()
        self.turn += 1

    def get_size_x(self):
        return self.size_x

    def get_size_y(self):
        return self.size_y

    def get_key(self):
        return self.key

    def save(self):
        from Organisms.Animals.Human import Human
        file = open('save.txt', 'w')
        file.write(str(self.size_x) + "\n")
        file.write(str(self.size_y) + "\n")

        for y in range(0, self.size_y):
            for x in range(0, self.size_x):
                if isinstance(self.world_map[x][y], Human):
                    human: Human = self.world_map[x][y]
                    file.write(human.get_species() + "\n")
                    file.write(str(human.get_power_time()) + "\n")
                    file.write(str(human.get_strength()) + "\n")
                    file.write(str(human.get_age()) + "\n")
                elif self.world_map[x][y] is None:
                    file.write("None \n")
                else:
                    file.write(self.world_map[x][y].get_species() + "\n")
                    file.write(str(self.world_map[x][y].get_strength()) + "\n")
                    file.write(str(self.world_map[x][y].get_age()) + "\n")
        file.close()
        print("saved!")

    def load_from_file(self):
        from Organisms.Animals.Human import Human
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

        file = open("save.txt", "r")

        self.size_x = int(file.readline())
        self.size_y = int(file.readline())
        self.world_map = [[None for x in range(0, self.size_x)] for y in range(0, self.size_y)]
        for y in range(0, self.size_y):
            for x in range(0, self.size_x):
                species = file.readline().strip()
                p = Position(x, y)
                

                if species == "None":
                    self.world_map[x][y] = None
                elif species == "human":
                    human = Human(self)
                    human.set_power_time(int(file.readline()))
                    human.set_strength(int(file.readline()))
                    human.set_age(int(file.readline()))
                    self.add_organism(p, human)
                else:
                    match species:

                        case "antelope":
                            self.add_organism(p, Antelope(self))
                        case "Pine Borscht":
                            self.add_organism(p, PineBorscht(self))
                        case "Guarana":
                            self.add_organism(p, Guarana(self))
                        case "fox":
                            self.add_organism(p, Fox(self))
                        case "Dandelion":
                            self.add_organism(p, Dandelion(self))
                        case "sheep":
                            self.add_organism(p, Sheep(self))
                        case "Grass":
                            self.add_organism(p, Grass(self))
                        case "Wolfberries":
                            self.add_organism(p, Wolfberries(self))
                        case "wolf":
                            self.add_organism(p, Wolf(self))
                        case "turtle":
                            self.add_organism(p, Turtle(self))
                        case "CyberSheep":
                            self.add_organism(p, CyberSheep(self))

                print(species)
        print("loaded")
        file.close()
