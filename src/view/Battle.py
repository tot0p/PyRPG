from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from src.control.eventKey import EventKey
from src.control.entities.enn import Ennemy

class BattleScreen(Screen,EventKey):
    def __init__(self,**kwargs) -> None:
        Screen.__init__(self,**kwargs)
        EventKey.__init__(self)


    def on_enter(self):
        self.Enn = Ennemy("luca")
        self.Player = self.manager.currentGame.Player
        self.ids.PlayerHp.text = "Hp : " + str(self.Player.hp)
        self.ids.PlayerStats.text = "def : " + str(self.Player.defence) + "\n att : \n" + self.Player.att
        self.BattleMenu("")

        return Screen.on_enter(self)
        
    def Attack(self,args):
        self.ids.BattleButtons.clear_widgets()
        self.ids.BattleButtons.add_widget(Button(text="attack 1",on_release=self.BattleMenu))
        self.ids.BattleButtons.add_widget(Button(text="attack 2",on_release=self.BattleMenu))
        self.ids.BattleButtons.add_widget(Button(text="attack 3",on_release=self.BattleMenu))
        self.ids.BattleButtons.add_widget(Button(text="attack 4",on_release=self.BattleMenu))
    
    def Items(self,args):
        self.ids.BattleButtons.clear_widgets()
        self.ids.BattleButtons.add_widget(Button(text="item 1",on_release=self.BattleMenu))
        self.ids.BattleButtons.add_widget(Button(text="item 2",on_release=self.BattleMenu))
        self.ids.BattleButtons.add_widget(Button(text="item 3",on_release=self.BattleMenu))
        self.ids.BattleButtons.add_widget(Button(text="item 4",on_release=self.BattleMenu))

    def BattleMenu(self,args):
        self.ids.BattleButtons.clear_widgets()
        self.ids.BattleButtons.add_widget(Button(text="attack",on_release=self.Attack))
        self.ids.BattleButtons.add_widget(Button(text="items",on_release=self.Items))

        