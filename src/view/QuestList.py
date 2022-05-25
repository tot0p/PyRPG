    
from kivy.uix.screenmanager import  Screen
from kivy.uix.label import Label
from src.control.eventKey import EventKey

    
class QuestListScreen(Screen,EventKey):
    def __init__(self, **kwargs) -> None:
        Screen.__init__(self,**kwargs)
        EventKey.__init__(self)

    def on_enter(self, *args):
        for i in self.manager.currentGame.Map.quest:
            self.ids.QuestList.add_widget(Label(text=str(i)))
        return super().on_enter(*args)

    def key_action(self, keybord, keycode, _, keyName, textContent):
        if keycode == 27:
            self.manager.Switch("game")
    
    
    
