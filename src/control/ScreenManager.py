import imp
from kivy.uix.screenmanager import ScreenManager,  NoTransition
from src.view.Menu import MenuScreen
from src.view.Settings import SettingsScreen
from src.view.NewGame import NewGameScreen
from src.view.Game import GameScreen
from src.view.Pause import PauseScreen
from src.view.Box import BoxScreen
from src.view.Crypto import CryptoScreen
from src.view.Map import   MapScreen
from src.view.QuestList import QuestListScreen
from src.view.Battle import BattleScreen





class Manager(ScreenManager):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.currentGame = GameScreen(name="game")
        self.add_widget(MenuScreen(name="menu"))
        # self.add_widget(SettingsScreen(name="settings"))
        self.add_widget(NewGameScreen(name="newgame"))
        self.add_widget(PauseScreen(name="pause"))
        self.add_widget(CryptoScreen(name="wallet"))
        self.add_widget(MapScreen(name="map"))
        self.add_widget(QuestListScreen(name="quest"))
        self.add_widget(self.currentGame)

        #eventGame
        self.add_widget(BoxScreen(name="box"))
        self.add_widget(BattleScreen(name="bataille"))
        

        self.transition = NoTransition()

    def Switch(self,id):
        self.current = id







