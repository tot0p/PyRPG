from src.control.entities.entities import entities
from src.control.jsonfile import ReadJson
from src.control.entities.att import attack
from src.control.Items import  HealtPotions , DammagePotions



class Player(entities):

    def __init__(self,name,x=0,y=0) -> None:
        super().__init__(name,100,att=[attack(**ReadJson("src/data/attacks/attacks.json")[0]),None,None,None])
        self.x , self.y = 0,0
        self.xp = 0
        self.wallet =Wallet()
        self._inv = [HealtPotions("Healt potion", "ta mère", 1),DammagePotions("DammagePot","ton père",1)]

    @property
    def inv(self):
        return [i for i in self._inv if i.usable()]


    def move(self,s:str):
        s = s.lower()
        dict = {
                "top":lambda x,y : (x,y-1),
                "bot": lambda x,y : (x,y+1),
                "right" : lambda x,y:(x+1,y),
                "left":lambda x,y:(x-1,y)
        }
        self.x , self.y = dict[s](self.x,self.y)
        
    def __str__(self):
        return "name : "+self.name+"\nhp : "+str(self.hp) + "\nxp : "+str(self.xp)



class Wallet:
    def __init__(self) -> None:
        self.eur = 100
        self.eth = 10
        self.sol = 2
        self.btc = 1
        self.xmr = 0

    def get(self,s):
        return getattr(self,s)

    def rm(self,s,n):
        setattr(self,s,getattr(self,s)-n)

    def add(self,s,n):
        setattr(self,s,getattr(self,s)+n)