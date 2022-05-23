

class Items:
    def __init__(self,name,desc,effect,durability,cost=0) -> None:
        self.nbuse = 0
        self.durability = durability
        self.effect = effect
        self.cost = cost
        self.destroy = False
        self.name = name
        self.desc = desc

    def use(self,launcher,target):
        self.nbuse +=1
        self.effect(launcher,target)
        if self.nbuse > self.durability and self.durability != -1:
            self.destroy = True

def Healt(launcher,target):
    if launcher.hpMax - launcher.hp > 10 :
        launcher.hp += 10
    else:
        launcher.hp = launcher.hpMax