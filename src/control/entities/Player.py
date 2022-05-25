from src.control.entities.entities import entities
from src.control.jsonfile import ReadJson
from src.control.entities.att import attack
from src.control.Items import  HealtPotions , DammagePotions , SkipCombat



class Player(entities):

    def __init__(self,name,x=0,y=0) -> None:
        super().__init__(name,100,att=[attack(**ReadJson("src/data/attacks/attacks.json")[0]),None,None,None])
        self.x , self.y = 0,0
        self.xp = 0
        self.level = 1
        self.wallet =Wallet()
        self._inv = [
            HealtPotions("Antivirus", "la base virale vps a été mise a jours\ngives 20hp", 1),
            DammagePotions("usb killer","fries you oponent pc with hight voltage\ndeals 10hp",1),
            SkipCombat("no connection", "skips a combat single use only and not usable on bosses", 0),
            ]

    def levelUp(self,xpReward):
        assert xpReward > 0 ; "xpReward can't < 0"
        self.xp += xpReward
        if self.xp >= self.level * 100:
            self.xp -= self.level * 100
            self.level +=1
            return True
        return False

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