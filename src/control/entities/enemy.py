from src.control.entities.entities import entities
from src.control.jsonfile import ReadJson
from src.control.entities.att import attack

class Enemy(entities):

    def __init__(self,name,hp,att,xpReward = 100) -> None:
        super().__init__(name,hp,att)
        self.xpReward = xpReward
        self.isBoss = False

        
    def __str__(self):
        return "name : "+self.name


def LoadEnemy(id):
    temp = ReadJson("src/data/monster.json")[id]
    allAtt = []
    for i in temp["att"]:
        allAtt.append(attack(**i))
    return Enemy(temp["name"],temp["hp"],allAtt)