from abc import ABC
from ctypes.wintypes import RGB


from Organisms.Plant import Plant
from Position import Position
from world import World


class PineBorscht(Plant, ABC):

    def __init__(self, w: World):
        super(PineBorscht, self).__init__("Pine Borscht", 10, w, 'S', RGB(142, 5, 212))

    def get_organism(self):
        return PineBorscht(self.world)

    def collision(self, p: Position, a: Position):
        print(self.world_map[a.x][a.y].get_species(), " ate Pine Borscht and die")
        self.world.delete_organism(p)
        self.world.delete_organism(a)

    def action(self, p: Position):
        from Organisms.Animals.CyberSheep import CyberSheep
        if p.x > 0 and p.y > 0 \
                and not isinstance(self.world_map[p.x - 1][p.y - 1], CyberSheep):
            self.world_map[p.x - 1][p.y - 1] = None
        if p.y > 0 \
                and not isinstance(self.world_map[p.x][p.y - 1], CyberSheep):
            self.world_map[p.x][p.y - 1] = None
        if p.x < self.world.get_size_x() - 1 \
                and p.y > 0 and not isinstance(self.world_map[p.x + 1][p.y - 1], CyberSheep):
            self.world_map[p.x + 1][p.y - 1] = None
        if p.x > 0 \
                and not isinstance(self.world_map[p.x - 1][p.y], CyberSheep):
            self.world_map[p.x - 1][p.y] = None
        if p.x < self.world.get_size_x() - 1 \
                and not isinstance(self.world_map[p.x + 1][p.y], CyberSheep):
            self.world_map[p.x + 1][p.y] = None
        if p.x > 0 and p.y < self.world.get_size_y() - 1 \
                and not isinstance(self.world_map[p.x - 1][p.y + 1], CyberSheep):
            self.world_map[p.x - 1][p.y + 1] = None
        if p.y < self.world.get_size_y() - 1 \
                and not isinstance(self.world_map[p.x][p.y + 1], CyberSheep):
            self.world_map[p.x][p.y + 1] = None
        if p.x < self.world.get_size_x() - 1 and p.y < self.world.get_size_y() - 1 \
                and not isinstance(self.world_map[p.x + 1][p.y + 1], CyberSheep):
            self.world_map[p.x + 1][p.y + 1] = None
