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
    def __init__(self,seed,nmax=20) -> None:
        self.width = 100
        self.height = 100
        self.quest = []
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
    
    def get_event(self,x,y):
        return str(self.tiles[y][x])

    def __generate_map(self):
        random.seed(self.seed)
        dic = {"1":10,"7":60,"8":5,"3":25}
        key = list(dic.keys())
        rangeRand = []
        for i in key:
            rangeRand += [i for _ in range(dic[i])]

        return [[rangeRand[random.randint(0,99)] for _ in range(self.width) ] for _ in range(self.height) ]
