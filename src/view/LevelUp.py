    
from kivy.uix.screenmanager import  Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from src.control.eventKey import EventKey
from src.control.entities.att import Get4RandomAtt

    
class LevelUpScreen(Screen,EventKey):
    def __init__(self, **kwargs) -> None:
        Screen.__init__(self,**kwargs)
        EventKey.__init__(self)
        self.openBox = True
        self.randomAttackList = []

    def on_enter(self, *args):
        """event de kivy quand on entre sur le screen"""
        self.ids.LevelUpGrid.add_widget(Label(text="choose wich attack you want to learn"))
        self.randomAttackList = Get4RandomAtt(self.manager.currentGame.Player)
        for i in self.randomAttackList:
            self.ids.LevelUpGrid.add_widget(Button(text=i.name+"\nDamage : "+str(i.damage)+"\nSucces Chance : "+str(i.reusite)+" %",on_release= self.selectAttack))
        
    def __GetAttByName(self,name):
        """permet de recuperer l'att par nom"""
        try :
            return [i for i in self.randomAttackList if i.name == name][0]
        except:
            return None

    def selectAttack(self,button):
        """permet d'afficher le selecteur d'attaque"""
        self.ids.LevelUpGrid.clear_widgets()
        allAttPlayer = self.manager.currentGame.Player.GetAtt()
        if len(allAttPlayer) == 4:
            self.ids.LevelUpGrid.add_widget(Label(text="choose wich attack to replace"))
            for id,i in enumerate (allAttPlayer):
                self.ids.LevelUpGrid.add_widget(Button(text=str(id+1) +" - "+i.name+"\nDamage : "+str(i.damage)+"\nSucces Chance : "+str(i.reusite)+" %",on_release=lambda x :self.replaceAttack(int(x.text.split(" - ")[0])-1, self.__GetAttByName(button.text.split("\n")[0]), self.attackChoice)))
        else:
            self.replaceAttack(len(allAttPlayer),self.__GetAttByName(button.text.split("\n")[0]), self.attackChoice)
    
    def replaceAttack(self, id,attack,callback):
        """permet de replacer une attaque si le joueur en à déjà 4"""
        self.manager.currentGame.Player.att = (id,attack)
        callback()
        
    def on_leave(self):
        """event de kivy quand on quit sur le screen"""
        self.ids.LevelUpGrid.clear_widgets()
    
    def attackChoice(self):
        """permet d'afficher le selecteur d'attaque"""
        self.ids.LevelUpGrid.clear_widgets()
        if self.openBox:
            self.ids.LevelUpGrid.add_widget(Button(text="go to open your lootbox",on_release=lambda x : self.manager.Switch("box")))
        else:
            self.manager.Switch("game")
    
    
