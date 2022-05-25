from re import S
from kivy.uix.screenmanager import Screen
from src.control.map import Map
from src.control.entities.Player import Player
import random
import sys
from src.control.eventKey import EventKey


class NewGameScreen(Screen, EventKey):
    def __init__(self, **kw):
        Screen.__init__(self, **kw)
        EventKey.__init__(self)
        self.ids.buttonCreateGame.on_release = self.__createGame
        self.ids.seedNewGame.text = str(random.randrange(sys.maxsize))
        self.filename = "src/data/save"

    def on_enter(self, *args):
        self.ids.nameNewGame.text = ""
        self.ids.seedNewGame.text = str(random.randrange(sys.maxsize))
        self.ids.nameerror.txt = ""
        return super().on_enter(*args)

    def __createGame(self):
        if self.ids.nameNewGame.text == "":
            self.ids.nameerror.text = "you cant have an empty name"
        else:
            self.manager.currentGame.LaunchGame(
                Player(self.ids.nameNewGame.text), Map(self.ids.seedNewGame.text)
            )
            self.manager.Switch("game")

    def key_action(self, keybord, keycode, _, keyName, textContent):
        if keycode == 27:
            self.manager.Switch("menu")
        if keycode == 13:
            self.__createGame()