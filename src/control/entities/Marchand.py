from random import choice, randint
from src.view.Crypto import GetPrice

class Marchand:
    def __init__(self,player):
        self.type = choice(["btc","eth","sol","xmr"])
        self.player = player
        self.items = self.GenerateInv()
    
    def GenerateInv(self):
        result = []
        allName = self.player.GetAllInvNameAndPrice()
        while len(result) <4 :
            temp = choice(allName)
            n= randint(1,5)
            result.append((temp[0],GetPrice(self.type,temp[1]*n+randint(-10,10 )),n))
        return result

    def GetItemByName(self,name):
        for i in self.items:
            if i[0] == name:
                return i
        return None

    def DeleteItemByName(self,name):
        for i in self.items:
            if i[0] == name:
                self.items.remove(i)
                print(self.items)
                return

    def buy(self,name,callback):
        item = self.GetItemByName(name)
        if item != None:
            if self.player.wallet.get(self.type) >= item[1]:
                self.player.wallet.rm(self.type,item[1])
                self.player.AddObjByName(item[0],item[2])
                self.DeleteItemByName(name)
        callback()

    def sell(self,name,callback):
        price = self.player.DeleteItemByName(name)
        self.player.wallet.add(self.type,self.Price(price))
        callback()

    def Price(self,cost):
        return GetPrice(self.type,(cost * 0.80))