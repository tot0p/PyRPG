
from kivy.uix.screenmanager import  Screen
from src.control.eventKey import EventKey

class  HelpScreen(Screen):
        def __init__(self,**kwargs):
            Screen.__init__(self,**kwargs)
            EventKey.__init__(self)
            
        def key_action(self, keybord, keycode, _, keyName, textContent):
            if keycode == 27:
                self.manager.Switch("menu")