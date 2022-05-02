import random
import math
import src.control.jsonfile as json


class Quete:
    def __init__(self,path,debut:str) -> None:
        self.filename = path
        self.listquete = json.ReadJson(path)
        self.currentQuete = debut

    def generateMap(self,seed):
        return [(0,0,-1)]

class Map:
    def __init__(self,seed) -> None:
        self.width = 200
        self.height = 200
        self._seed = seed
        self.tiles = self.__generate_map()

    
    def __str__(self) -> str:
        return  "seed : " + str(self.seed)

    @property
    def seed(self):
        return self._seed

    @seed.setter
    def seed(self,val):
        self._seed = val
        self.tiles = self.__generate_map()

    def __generate_map(self):
        random.seed(self._seed)
        noise_map = [[0 for _ in range(self.width)] for _ in range(self.height)]
        new_value = 0
        top_of_range = 0
        bottom_of_range = 0
        for y in range(self.height):
            for x in range(self.width):
                if x == 0 and y == 0:
                    continue
                if y == 0:
                    new_value = noise_map[y][x - 1] + random.randint(-100, +100)
                elif x == 0:
                    new_value = noise_map[y - 1][x] + random.randint(-100, +100)
                else:
                    minimum = min(noise_map[y][x - 1], noise_map[y-1][x])
                    maximum = max(noise_map[y][x - 1], noise_map[y-1][x])
                    average_value = minimum + ((maximum-minimum)/2.0)
                    new_value = average_value + random.randint(-100, +100)
                noise_map[y][x] = new_value
                if new_value < bottom_of_range:
                    bottom_of_range = new_value
                elif new_value > top_of_range:
                    top_of_range = new_value
        difference = float(top_of_range - bottom_of_range)
        for y in range(self.height):
            for x in range(self.width):
                noise_map[y][x] = int(math.ceil((noise_map[y][x] - bottom_of_range)/100))
        return noise_map