
class attack:
    def __init__(self,name,damage=10,effects=[]) -> None:
        self.name = name
        self.damage = damage
        self.effects = effects

    def __str__(self) -> str:
        return self.name

    def attack(self,attacker,reciver) -> None:
        reciver.hp -= self.damage
        for effect in self.effects:
            effect.cast_effect(attacker,reciver)