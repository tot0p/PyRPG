

class Items:
    '''
    class géneral representant tout les items
    '''
    def __init__(self,name,effect,desc,durability,messageAction,cost=0) -> None:
        self.nbuse = 0
        self.durability = durability
        self.cost = cost
        self.name = name
        self.desc = desc
        self.effect = effect
        self.messageAction = messageAction

    def __iadd__(self,o):
        if type(o) == int and self.durability >= 0:
            self.durability += o
        return self

    def __isub__(self,o):
        if type(o) == int and self.durability >= 0:
            self.durability -= o
        return self

    def use(self,launcher,target,callback=print):
        """permet d'utiliser un item """
        if self.nbuse < self.durability or self.durability == -1:
            self.nbuse +=1
            self.effect(launcher,target)
        callback()
    
    def usable(self):
        """verifie si un items et utilisable"""
        return self.nbuse < self.durability or self.durability == -1

    def GetNumberUse(self):
        """permet de get le nombre d'utilisation restante"""
        return "unbreakable" if self.durability == -1 else str(self.durability - self.nbuse)


class HealtPotions(Items):
    """represente un potion de soin"""
    def __init__(self, name, desc, durability , hpGiven = 20,cost=0):
        self.hpGiven = hpGiven
        super().__init__(name, self.Healt, desc, durability,"use potion of healt",cost)


    def Healt(self,launcher,target):
        """represente l'effet de soin"""
        if launcher.hpMax - launcher.hp > self.hpGiven :
            launcher.hp += self.hpGiven
        else:
            launcher.hp = launcher.hpMax

class DammagePotions(Items):
    """represente potion de degats"""
    def __init__(self, name,desc, durability,dammage=10,cost=0):
        self.dammage = dammage
        super().__init__(name, self.Dammage, desc, durability,"use potion of Dammage",cost)

    def Dammage(self,launcher,target):
        """represent l'effet de degats"""
        target.hp -= self.dammage



class SkipCombat(Items):
    def __init__(self, name,desc, durability,cost=0):
        super().__init__(name, self.Skip, desc, durability,"skipped combat",cost)

    def Skip(self,launcher,target):
        """
        represente l'effet de skip
        """
        if not target.isBoss:
            self.messageAction = "skipped combat"
            target.hp=0
        else :
            self.messageAction = "this item is not effective against a boss"
            self.durability += 1

