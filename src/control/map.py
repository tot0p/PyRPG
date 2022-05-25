import random
import math
import src.control.jsonfile as json


class Quete:
    def __init__(self,path,debut:str) -> None:
        self.filename = path
        self.listquete = json.ReadJson(path)
        self.currentQuete = debut

    def generateMap(self,seed):
        return [(0,0,0)]

class Map:
    def __init__(self,seed,nmax=20) -> None:
        self.width = 20
        self.height = 20
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
        s = str(self.tiles[y][x])
        self.tiles[y][x] = 0
        return s

    def __generate_map(self):
        random.seed(self.seed)
        genPath = "src/data/event/gen.json"
        dic = json.ReadJson(genPath)
        key = list(dic.keys())
        rangeRand = []
        maxCheck = 0
        for i in key:
            maxCheck += dic[i]
            rangeRand += [i for _ in range(dic[i])]
            if maxCheck > 100:
                raise OverflowError("generation probability sum in \""+genPath+"\" cant be higher than 100")


        return [[rangeRand[random.randint(0,99)] for _ in range(self.width) ] for _ in range(self.height) ]
