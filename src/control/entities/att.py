from random import randint , choice
from src.control.jsonfile import ReadJson
class attack:
    '''
    réprésente une attack d'une entities
    '''
    def __init__(self,name,damage=10,reusite = 100,missMessage="miss",succesMessage="succes") -> None:
        self.name = name
        self.damage = damage
        self.reusite = reusite
        self.missMessage = missMessage
        self.succesMessage = succesMessage

    def __str__(self) -> str:
        return self.name + " damage: " + str(self.damage)

    def attack(self,attacker,reciver) -> str:
        '''simule l'application de l'attaque '''
        k = randint(0, 100)
        if k <= self.reusite:
            reciver.hp -= self.damage
            return self.succesMessage
        else:
            return self.missMessage


def GetAllAtt():
    '''donne toute les attacks sous forme d'une liste d'attack depuis le json'''
    return [attack(**i) for i in ReadJson("src/data/attacks/attacks.json")]


def Get4RandomAtt(player):
    '''
    générer une list de 4 attaque différente de celle que le player possède déjà
    '''
    result = []
    all_attack = GetAllAtt()
    temp = GetAllAtt()[0]
    player_att = player.GetAttName()
    while len(result) < 4 :
        temp = choice(all_attack)
        if temp.name not in player_att and temp not in result:
            result.append(temp)
    return result