from turtle import onrelease
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import  Screen
from kivy.uix.button import Button
from kivy.graphics import Line
from kivy.uix.label import Label
from kivy.core.window import Window
from src.control.eventKey import EventKey

class InventoryScreen(Screen,EventKey):
    def __init__(self,**kwargs) -> None:
        Screen.__init__(self,**kwargs)
        EventKey.__init__(self)

    def on_enter(self):
        self.ids.Inventory.clear_widgets()
        for i in self.manager.currentGame.Player.inv:
            ObjGrid = GridLayout(cols = 1)
            ObjGrid.add_widget(Label(text="Name : "+i.name+"\nDescription : "+i.desc+"\nUses Left : "+i.GetNumberUse()+"\nCost : "+str(i.cost)+" €"))
            ObjGrid.add_widget(Label(text=""))
            if i.name == "antivirus" or i.name == "virus protection plan" :
                ObjGrid.add_widget(Button(text=i.name+"\nPlayer health : "+str(self.manager.currentGame.Player.hp)+"\nUse item",on_release=lambda x: self.manager.currentGame.Player.GetObjByName(x.text.split("\n")[0]).use(self.manager.currentGame.Player,self.manager.currentGame.Player,lambda:self.on_enter())))
            else:
                ObjGrid.add_widget(Label(text=""))
            self.ids.Inventory.add_widget(ObjGrid)
            
    def on_leave(self):
        self.ids.Inventory.clear_widgets()

    def key_action(self,keybord,keycode,_,keyName,textContent):
        if keycode == 27:
            self.manager.Switch("game")