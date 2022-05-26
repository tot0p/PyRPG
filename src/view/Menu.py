# from src.control.SaveAndLoadGame import create_player
# from src.control.entities.att import attack
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button

from src.control.eventKey import EventKey


class MenuButton(Button):
    def __init__(self, func, **kwargs):
        super().__init__(**kwargs)
        self.func = func

    def on_release(self):
        self.func()
        return super().on_release()


class MenuScreen(Screen, EventKey):
    def __init__(self, **kwargs) -> None:
        Screen.__init__(self, **kwargs)
        EventKey.__init__(self)
        self.options = {
            "Load Game": lambda: self.manager.currentGame.LoadGame(),
            "New Game": lambda: self.manager.Switch("newgame"),
            "Help": lambda: self.manager.Switch("help"),
            "Quit": lambda: exit(0),
        }
        t = []
        for key in self.options:
            t.append(key)
            button = MenuButton(self.options[key], text=str(len(t)) + ". " + key)
            self.ids.gridMenu.add_widget(button)

    def on_enter(self):
        self.manager.Reset()
