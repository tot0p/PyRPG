from src.control.entities.entities import entities
from src.control.jsonfile import ReadJson
from src.control.entities.att import attack
from src.control.Items import  HealtPotions , DammagePotions , SkipCombat
from src.view.Crypto import GetPrice
from json import JSONEncoder


class Player(entities):
    '''représente le player'''

    def __init__(self,name,x=0,y=0) -> None:
        super().__init__(name,100,att=[attack(**ReadJson("src/data/attacks/attacks.json")[0]),None,None,None])
        self.x , self.y = 0,0
        self.xp = 0
        self.level = 1
        self.wallet =Wallet()
        self._inv = [
            HealtPotions("antivirus", "la base virale vps a été mise a jours\ngives 20hp", 1,20,50),
            HealtPotions("virus protection plan", "cleaning viruses away\ngives 50hp", 0,50,250),
            DammagePotions("usb killer","fries you oponent pc with hight voltage\ndeals 10hp",1,20,100),
            DammagePotions("bad overclocking", "set you opponent pc in flames\ndeals 50hp", 0,50,1000),
            SkipCombat("no connection", "skips a combat single use only and not usable on bosses", 1,2500),
            ]


    def levelUp(self,xpReward):
        ''' gere l'xp du player après un combat '''
        assert xpReward > 0 ; "xpReward can't < 0"
        self.xp += xpReward
        if self.xp >= self.level * 100:
            self.xp -= self.level * 100
            self.level +=1
            return True
        return False

    def AddObjByName(self,name,q=1):
        '''permet d'ajouter un item au joueur via son nom'''
        for i in self._inv:
            if i.name == name:
                i += q

    def DeleteItemByName(self,name):
        '''permet de delete un item au joueur via son nom'''
        for i in self._inv:
            if i.name == name:
                i -= 1
                return i.cost
            
    def GetObjByName(self,name):
        '''permet de recuperer un item au joueur via son nom'''
        try:
            return [i for i in self._inv if i.name == name][0]
        except:
            return None

    def GetAllInvNameAndPrice(self):
        '''permet de recuperer une liste d'un tuple du nom de l'object avec son prix'''
        return  [(i.name,i.cost) for i in self._inv]

    @property
    def inv(self):
        '''return un liste d'object avec seulement les utilisables'''
        return [i for i in self._inv if i.usable()]


    def move(self,s:str):
        '''permet de se déplacé sur la map'''
        s = s.lower()
        dict = {
                "up":lambda x,y : (x,y-1),
                "down": lambda x,y : (x,y+1),
                "right" : lambda x,y:(x+1,y),
                "left":lambda x,y:(x-1,y)
        }
        self.x , self.y = dict[s](self.x,self.y)

        
    def __str__(self):
        return "name : "+self.name+"\nhp : "+str(self.hp) + "\nxp : "+str(self.xp)



class Wallet:
    def __init__(self) -> None:
        self.eur = 100
        self.eth = GetPrice("eth")
        self.sol =  GetPrice("sol")
        self.btc =  GetPrice("btc")
        self.xmr =  GetPrice("xmr")

    def get(self,s):
        '''permet de get la valeur de l'attribut s'''
        return getattr(self,s)

    def rm(self,s,n):
        '''permet de supprimer n à l'attribut s'''
        if n>0:
            setattr(self,s,getattr(self,s)-n)

    def add(self,s,n):
        '''permet d'ajouter n à l'attribut s'''
        if n>0:
            setattr(self,s,getattr(self,s)+n)