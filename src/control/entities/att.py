from random import randint
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