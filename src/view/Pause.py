from kivy.uix.screenmanager import  Screen
from src.control.eventKey import EventKey
    
class  PauseScreen(Screen,EventKey):
    def __init__(self, **kwargs) -> None:
        Screen.__init__(self,**kwargs)
        EventKey.__init__(self)

    def key_action(self,keybord,keycode,_,keyName,textContent):
        if keycode == 27:
            self.manager.Switch("game")