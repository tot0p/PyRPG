from kivy.uix.screenmanager import  Screen
from src.control.eventKey import EventKey


class  GameScreen(Screen,EventKey):
    def __init__(self, **kwargs) -> None:
        Screen.__init__(self,**kwargs)
        EventKey.__init__(self)
        self.Player = ""
        self.Map = ""

    def LaunchGame(self,Player,Map):
        self.Player = Player
        self.Map = Map

    def on_enter(self, *args):
        print(self.Player,self.Map)
        return super().on_enter(*args)

    def key_action(self,keybord,keycode,_,keyName,textContent):
        if keycode == 27:
            self.manager.Switch("pause")

            