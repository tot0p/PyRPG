import imp
from kivy.uix.screenmanager import ScreenManager,  NoTransition
from src.view.Menu import MenuScreen
from src.view.Help import HelpScreen
from src.view.NewGame import NewGameScreen
from src.view.Game import GameScreen
from src.view.Pause import PauseScreen
from src.view.Box import BoxScreen
from src.view.Crypto import CryptoScreen
from src.view.Map import   MapScreen
from src.view.QuestList import QuestListScreen
from src.view.Battle import BattleScreen
from src.view.GameOver import GameOverScreen
from src.view.Inventory import InventoryScreen
from src.view.Stats import StatsScreen
from src.view.LevelUp import LevelUpScreen
from src.view.Marchand import MarchandScreen
from src.view.Win import WinScreen





class Manager(ScreenManager):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.currentGame = GameScreen(name="game")
        self.add_widget(HelpScreen(name="help"))
        self.add_widget(NewGameScreen(name="newgame"))
        self.currentWallet = CryptoScreen(name="wallet")
        self.add_widget(self.currentWallet)
        self.add_widget(MapScreen(name="map"))
        self.add_widget(QuestListScreen(name="quest"))
        self.add_widget(InventoryScreen(name="inventory"))
        self.add_widget(StatsScreen(name="stats"))
        self.add_widget(WinScreen(name="win"))
        self.add_widget(self.currentGame)

        #eventGame
        self.currentLevelUp = LevelUpScreen(name="levelup")
        self.add_widget(self.currentLevelUp)
        self.add_widget(MarchandScreen(name="marchand"))
        self.add_widget(BoxScreen(name="box"))
        self.add_widget(BattleScreen(name="bataille"))

        #!!!!!!!!!!  surtout le laisser à la fin des add_widget VRAIMENT IMPORTANT POUR LE RESET  !!!!!!!!!!
        self.add_widget(MenuScreen(name="menu"))
        self.add_widget(PauseScreen(name="pause"))
        self.add_widget(GameOverScreen(name="gameover")) 

        

        self.transition = NoTransition()
        self.Switch("menu")

    def Switch(self,id):
        self.current = id
    
    def SwitchAtt(self,lootbox = True):
        self.Switch("levelup")
        self.currentLevelUp.openBox = lootbox

    def SwitchWallet(self,to="game"):
        self.Switch("wallet")
        self.currentWallet.to=to

    def Reset(self):
        self.screens = self.screens[-3:]
        self.currentGame = GameScreen(name="game")
        self.add_widget(HelpScreen(name="help"))
        self.add_widget(NewGameScreen(name="newgame"))
        self.currentWallet = CryptoScreen(name="wallet")
        self.add_widget(self.currentWallet)
        self.add_widget(MapScreen(name="map"))
        self.add_widget(QuestListScreen(name="quest"))
        self.add_widget(InventoryScreen(name="inventory"))
        self.add_widget(StatsScreen(name="stats"))
        self.add_widget(WinScreen(name="win"))
        self.add_widget(self.currentGame)

        #eventGame
        self.currentLevelUp = LevelUpScreen(name="levelup")
        self.add_widget(self.currentLevelUp)
        self.add_widget(MarchandScreen(name="marchand"))
        self.add_widget(BoxScreen(name="box"))
        self.add_widget(BattleScreen(name="bataille"))

        #!!! pour que ça marche en tout temps !!!
        self.screens =  self.screens [3:] + self.screens[0:3]
        self.Switch("menu")






