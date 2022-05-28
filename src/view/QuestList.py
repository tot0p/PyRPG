    
from kivy.uix.screenmanager import  Screen
from kivy.uix.label import Label
from src.control.eventKey import EventKey

    
class QuestListScreen(Screen,EventKey):
    """affche la list des quetes"""
    def __init__(self, **kwargs) -> None:
        Screen.__init__(self,**kwargs)
        EventKey.__init__(self)

    def on_enter(self, *args):
        """event de kivy quand on entre sur le screen"""
        for i in self.manager.currentGame.Map.quest:
            self.ids.QuestList.add_widget(Label(text="-"+ i.name+"\nPosition : "+"x "+str(i.x)+" "+"y "+str(i.y)+"\nPlayer position : "+"x "+str(self.manager.currentGame.Player.x)+" "+"y "+str(self.manager.currentGame.Player.y)))
        return super().on_enter(*args)

    def on_leave(self):
        """event de kivy quand on quit sur le screen"""
        self.ids.QuestList.clear_widgets()
        self.ids.QuestList.add_widget(Label(text="Quest List"))

    def key_action(self, keybord, keycode, _, keyName, textContent):
        if keycode == 27:
            self.manager.Switch("game")
    
    
    
