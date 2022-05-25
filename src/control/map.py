import random
import math
import src.control.jsonfile as json


class Quete:
    def __init__(self,path) -> None:
        self.id = 0
        self.listquete = json.ReadJson(path)

    def GetBoss(self):
        return self.listquete[self.id]["enn"]

    @property
    def name(self):
        return self.listquete[self.id]["name"]

    def generate(self):
        return (1,1)
        # return (random.randint(0, 20),random.randint(0, 20))

    def Next(self):
        self.id += 1
        return self.id < len(self.listquete)

class Map:
    def __init__(self,seed,nmax=20) -> None:
        self.width = 20
        self.height = 20
        self.quest = [Quete("src/data/boss.json")]
        self._seed = seed
        self.tiles = self.__generate_map()
        g = self.quest[0].generate()
        print(g)
        self.tiles[g[0]][g[1]] = -1

    
    def NextQuest(self,id=0):
        t = self.quest[id].Next()
        if t:
            g = self.quest[0].generate()
            self.tiles[g[0]][g[1]] = -1
            return False
        else:
            self.quest.pop(id)
            return True

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
        if self.Only0():
            self.__generate_map()
        s = str(self.tiles[y][x])
        self.tiles[y][x] = 0
        return s
    
    def Only0(self):
        for i in self.tiles:
            for y in self.tiles:
                if y != 0 :
                    return False
        return True

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
