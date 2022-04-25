# from src.control.SaveAndLoadGame import create_player
# from src.control.entities.att import attack
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.core.window import Window


import re

class MenuButton(Button):
    def __init__(self, func,**kwargs):
        super().__init__(**kwargs)
        self.func = func
    
    def on_release(self):
        self.func()
        return super().on_release()

class MenuScreen(Screen):
    def __init__(self,**kwargs) -> None:
        super().__init__(**kwargs)
        Window.bind(on_key_down=self.key_action)
        self.options = {"Load Game":lambda  : print("Load Game"),"New Game":lambda : self.manager.Switch("newgame"),"Options":lambda :print("Options"),"Quit":lambda : exit(0)}
        t = []
        for key in self.options:
            t.append(key)
            button = MenuButton(self.options[key],text=str(len(t))+". "+key)
            self.ids.gridMenu.add_widget(button)

    def key_action(self,keybord,keycode,_,string,textContent):
        if keycode == 27:
            exit(0)