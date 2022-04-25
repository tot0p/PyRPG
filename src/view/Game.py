from kivy.uix.screenmanager import  Screen

class  GameScreen(Screen):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.Player = ""
        self.Map = ""

    def LaunchGame(self,Player,Map):
        self.Player = Player
        self.Map = Map

    def on_enter(self, *args):
        print(self.Player,self.Map)
        return super().on_enter(*args)