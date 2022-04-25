from src.control.entities.entities import entities

class Player(entities):

    def __init__(self,name) -> None:
        super().__init__(name,100)
        self.xp = 0
        self.inv = {}
        
    def __str__(self):
        return "name : "+self.name+"\nhp : "+str(self.hp) + "\nxp : "+str(self.xp)