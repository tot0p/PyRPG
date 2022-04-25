from src.control.entities.entities import entities

class Ennemy(entities):

    def __init__(self,name,loot=[0,[]]) -> None:
        super().__init__(name,100)
        self.loot = loot

        
    def __str__(self):
        return "name : "+self.name