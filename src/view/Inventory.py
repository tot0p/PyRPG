from kivy.uix.screenmanager import  Screen
from kivy.graphics import Line
from kivy.uix.label import Label
from kivy.core.window import Window
from src.control.eventKey import EventKey

class InventoryScreen(Screen,EventKey):
    def __init__(self,**kwargs) -> None:
        Screen.__init__(self,**kwargs)
        EventKey.__init__(self)

    def on_enter(self):
        for i in self.manager.currentGame.Player.inv:
            self.ids.Inventory.add_widget(Label(text="Name : "+i.name+"\nDescription : "+i.desc+"\nUses Left : "+i.GetNumberUse()+"\nCost : "+str(i.cost)+" €"))
            
    def on_leave(self):
        self.ids.Inventory.clear_widgets()

    def key_action(self,keybord,keycode,_,keyName,textContent):
        if keycode == 27:
            self.manager.Switch("game")