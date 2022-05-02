

class Items:
    def __init__(self,damage,durability,cost=0) -> None:
        self.nbuse = 0
        self.durability = durability
        self.damage = damage
        self.cost = cost
        self.destroy = False

    def use(self):
        self.nbuse +=1
        if self.nbuse > self.durability and self.durability != -1:
            self.destroy = True