from src.control.entities.entities import entities

class Player(entities):

    def __init__(self,name) -> None:
        super().__init__(name,100)
        self.xp = 0
        self.wallet =Wallet()
        self.inv = {}
        
    def __str__(self):
        return "name : "+self.name+"\nhp : "+str(self.hp) + "\nxp : "+str(self.xp)



class Wallet:
    def __init__(self) -> None:
        self.eur = 100
        self.eth = 10
        self.sol = 2
        self.btc = 1
        self.xmr = 0

    def rm(self,s,n):
        setattr(self,s,getattr(self,s)-n)

    def add(self,s,n):
        setattr(self,s,getattr(self,s)+n)