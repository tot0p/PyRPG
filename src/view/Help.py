
from kivy.uix.screenmanager import  Screen
from src.control.eventKey import EventKey
import webbrowser

class  HelpScreen(Screen):
    """screen de help"""
    def __init__(self,**kwargs):
        Screen.__init__(self,**kwargs)
        EventKey.__init__(self)
            
    def OpenIssuePage(self):
        """permet d'open la page pour report des bugs"""
        webbrowser.open("https://github.com/tot0p/RPG/issues")

    def key_action(self, keybord, keycode, _, keyName, textContent):
        if keycode == 27:
            self.manager.Switch("menu")