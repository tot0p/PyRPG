import random
import math
import src.control.jsonfile as json
from json import JSONEncoder


class Quete:
    """
    represente une quete
    """
    def __init__(self,path) -> None:
        self.id = 0
        self.listquete = json.ReadJson(path)
        self.x = 0
        self.y = 0

    def GetBoss(self):
        """permet de récuperer le boss"""
        return self.listquete[self.id]["enn"]

    @property
    def name(self):
        """recupere le nom de la current quete"""
        return self.listquete[self.id]["name"]

    def generate(self):
        """genere le spawn de la quete"""
        # return (1,1)
        self.x =random.randint(0, 9)
        self.y = random.randint(0, 9)
        return (self.y,self.x)

    def Next(self):
        """passe à l'etape suivante de la quete"""
        self.id += 1
        return self.id < len(self.listquete)

class Map:
    """
    représente la map
    """
    def __init__(self,seed,nmax=20) -> None:
        self.width = 10
        self.height = 10
        self.quest = [Quete("src/data/boss.json")]
        self._seed = seed
        self.tiles = self.__generate_map()
        g = self.quest[0].generate()
        self.tiles[g[0]][g[1]] = -1
    
    def NextQuest(self,id=0):
        """
        pass à l'etape suivante de la quete id
        """
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
        """permet de set la seed et de regenerer la map"""
        self._seed = val
        self.tiles = self.__generate_map()
    
    def get_event(self,x,y):
        """recuperer l'event à x y"""
        if self.Only0():
            self.__generate_map()
        s = str(self.tiles[y][x])
        return s
    
    def Only0(self):
        """vérifie si la map n'a plus d'event"""
        for i in self.tiles:
            for y in self.tiles:
                if y != 0 :
                    return False
        return True

    def __generate_map(self):
        """genere la map"""
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

