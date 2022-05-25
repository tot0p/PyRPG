from src.control.entities.entities import entities

class Enemy(entities):

    def __init__(self,name,xpReward = 100) -> None:
        super().__init__(name,100)
        self.xpReward = xpReward

        
    def __str__(self):
        return "name : "+self.name