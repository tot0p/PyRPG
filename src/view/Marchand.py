from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button

from src.control.eventKey import EventKey
from src.control.entities.Marchand import Marchand


class MarchandScreen(Screen,EventKey):
    def __init__(self,**kwargs) -> None:
        Screen.__init__(self,**kwargs)
        EventKey.__init__(self)
        self.inTrade = False
    
    def on_enter(self):
        if not self.inTrade:
            self.marchand = Marchand(self.manager.currentGame.Player)
            self.inTrade = True
        self.drawItems()

    def drawItems(self):
        self.ids.BuyGrid.clear_widgets()
        self.ids.SellGrid.clear_widgets()
        self.MarchandInv = self.marchand.items
        self.PlayerInv = self.manager.currentGame.Player.inv
        for i in self.MarchandInv:
            self.ids.BuyGrid.add_widget(Button(text=i[0]+"\nQuantity : "+str(i[2])+"\nPrice : "+str(i[1])+" "+self.marchand.type,on_release= lambda x : self.marchand.buy(x.text.split("\n")[0],self.drawItems)))
        for i in self.PlayerInv:
            self.ids.SellGrid.add_widget(Button(text=i.name+"\nQuantity : "+str(i.durability)+"\nPrice : "+str(self.marchand.Price(i.cost))+" "+self.marchand.type,on_release= lambda x : self.marchand.sell(x.text.split("\n")[0],self.drawItems)))

    def exit(self):
        self.inTrade = False
        self.manager.Switch("game")

    def on_leave(self):
        self.ids.BuyGrid.clear_widgets()
        self.ids.SellGrid.clear_widgets()
        
    def key_action(self, keybord, keycode, _, keyName, textContent):
        if keycode == 27:
            pass