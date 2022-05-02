from kivy.uix.screenmanager import  Screen
from src.control.eventKey import EventKey


class  GameScreen(Screen,EventKey):
    def __init__(self, **kwargs) -> None:
        Screen.__init__(self,**kwargs)
        EventKey.__init__(self)
        self.Player = ""
        self.Map = ""
        self.textInput = self.ids.rootTextInput
        self.historyInput = self.ids.previousactions
        self.hist = self.ids.gametext
        self.rep = self.ids.textaction
        self.textInput.bind(on_text_validate=self.on_enter_textInput)

    def LaunchGame(self,Player,Map):
        self.Player = Player
        self.Map = Map

    def on_enter(self, *args):
        print(self.Player,self.Map)
        return super().on_enter(*args)

    def on_enter_textInput(self,instance):
        self.historyInput.text = self.historyInput.text + "\n" + instance.text
        instance.text = ""


    def key_action(self,keybord,keycode,_,keyName,textContent):
        if keycode == 27:
            self.manager.Switch("pause")


            