from random import randint , choice
from src.control.jsonfile import ReadJson
class attack:
    def __init__(self,name,damage=10,reusite = 100,missMessage="miss",succesMessage="succes",effects=[]) -> None:
        self.name = name
        self.damage = damage
        self.reusite = reusite
        self.effects = effects
        self.missMessage = missMessage
        self.succesMessage = succesMessage

    def __str__(self) -> str:
        return self.name 

    def attack(self,attacker,reciver) -> str:
        k = randint(0, 100)
        if k <= self.reusite:
            reciver.hp -= self.damage
            for effect in self.effects:
                effect.cast_effect(attacker,reciver)
            return self.succesMessage
        else:
            return self.missMessage


def GetAllAtt():
    return [attack(**i) for i in ReadJson("src/data/attacks/attacks.json")]


def Get4RandomAtt(player):
    result = []
    all_attack = GetAllAtt()
    temp = GetAllAtt()[0]
    player_att = player.GetAttName()
    while len(result) < 4 :
        temp = choice(all_attack)
        if temp.name not in player_att and temp not in result:
            result.append(temp)
    return result