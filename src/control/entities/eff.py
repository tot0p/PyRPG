
class effect:
    def __init__(self,name,effecter,is_reciving=False) -> None:
        self.name = name
        self.effecter = effecter
        self.is_reciving = is_reciving
    
    def cast_effect(self,attacker,reciver):
        if self.is_reciving:
            self.effecter(attacker)
        else:
            self.effecter(reciver)