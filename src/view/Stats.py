from kivy.uix.screenmanager import  Screen
from kivy.uix.label import Label
from src.control.eventKey import EventKey

    
class StatsScreen(Screen,EventKey):
    """affiche les stats"""
    def __init__(self, **kwargs) -> None:
        Screen.__init__(self,**kwargs)
        EventKey.__init__(self)

    def on_enter(self, *args):
        """event de kivy quand on entre sur le screen"""
        self.ids.Stats.add_widget(Label(text="Name : " + self.manager.currentGame.Player.name))
        self.ids.Stats.add_widget(Label(text=str(self.manager.currentGame.Player.hp)+'\\'+str(self.manager.currentGame.Player.hpMax)+' hp'))
        self.ids.Stats.add_widget(Label(text=str(self.manager.currentGame.Player.xp)+" xp"))
        self.ids.Stats.add_widget(Label(text="level " + str(self.manager.currentGame.Player.level)))
        self.ids.Stats.add_widget(Label(text=""))
        self.ids.Stats.add_widget(Label(text="attacks :"))
        self.ids.Stats.add_widget(Label(text=self.manager.currentGame.Player.att))
        return super().on_enter(*args)

    def on_leave(self):
        """event de kivy quand on quit sur le screen"""
        self.ids.Stats.clear_widgets()

    def key_action(self, keybord, keycode, _, keyName, textContent):
        if keycode == 27:
            self.manager.Switch("game")
    
    
    
