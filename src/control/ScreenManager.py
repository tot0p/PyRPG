from kivy.uix.screenmanager import ScreenManager,  NoTransition
from src.view.Menu import MenuScreen
from src.view.Settings import SettingsScreen
from src.view.NewGame import NewGameScreen
from src.view.Game import GameScreen




class Manager(ScreenManager):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.currentGame = GameScreen(name="game")
        self.add_widget(MenuScreen(name="menu"))
        self.add_widget(SettingsScreen(name="settings"))
        self.add_widget(NewGameScreen(name="newgame"))
        self.add_widget(self.currentGame)
        self.transition = NoTransition()

    def Switch(self,id):
        self.current = id


