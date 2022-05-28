from random import choice, randint
from src.view.Crypto import GetPrice

class Marchand:
    '''
    represente une boutique dans le jeu

        il a un type qui est représenté par la devise qu'il utilise
    '''
    def __init__(self,player):
        self.type = choice(["btc","eth","sol","xmr"])
        self.player = player
        self.items = self.GenerateInv()
    
    def GenerateInv(self):
        '''genere l'offre de la boutique'''
        result = []
        allName = self.player.GetAllInvNameAndPrice()
        while len(result) <4 :
            temp = choice(allName)
            n= randint(1,5)
            result.append((temp[0],GetPrice(self.type,temp[1]*n+randint(-10,10 )),n))
        return result

    def GetItemByName(self,name):
        '''recupere un items par son nom'''
        for i in self.items:
            if i[0] == name:
                return i
        return None

    def DeleteItemByName(self,name):
        '''delete un items par son nom'''
        for i in self.items:
            if i[0] == name:
                self.items.remove(i)
                return

    def buy(self,name,callback):
        '''gere l'achat du player d'un article'''
        item = self.GetItemByName(name)
        if item != None:
            if self.player.wallet.get(self.type) >= item[1]:
                self.player.wallet.rm(self.type,item[1])
                self.player.AddObjByName(item[0],item[2])
                self.DeleteItemByName(name)
        callback()

    def sell(self,name,callback):
        '''gere la vente d'un object du player'''
        price = self.player.DeleteItemByName(name)
        self.player.wallet.add(self.type,self.Price(price))
        callback()

    def Price(self,cost):
        '''permet de transformer le cout d'un items en euro à la devise du marchand'''
        return GetPrice(self.type,(cost * 0.80))