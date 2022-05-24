from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from src.control.eventKey import EventKey
from src.control.entities.enemy import Enemy

class BattleScreen(Screen,EventKey):
    def __init__(self,**kwargs) -> None:
        Screen.__init__(self,**kwargs)
        EventKey.__init__(self)


    def on_enter(self):
        self.Enemy = Enemy("luca")
        self.Player = self.manager.currentGame.Player
        self.BattleMenu("")

        return Screen.on_enter(self)
        
    def Attack(self,args):
        self.ids.BattleButtons.clear_widgets()
        for i in self.Player.GetAtt():
            self.ids.BattleButtons.add_widget(Button(text=i,on_release=lambda x : self.Player.attack(i,self.Enemy,lambda : self.Enemy.attack(self.Enemy.randomAtt().name, self.Player,lambda : self.BattleMenu("")))))
    
    def Items(self,args):
        self.ids.BattleButtons.clear_widgets()
        if len(self.Player.inv)<=0:
            self.ids.BattleButtons.add_widget(Button(text="You have no items in your inventory",on_release=lambda x: self.BattleMenu("")))
        else:
            for i in self.Player.inv:
                self.ids.BattleButtons.add_widget(Button(text=i.name+"\nUse Left : "+i.GetNumberUse(),on_release=lambda x :i.use(self.Player,self.Enemy,lambda : self.Enemy.attack(self.Enemy.randomAtt().name, self.Player,lambda : self.displayItemMessage(i)))))
        
    def displayItemMessage(self,item):
        self.Player.resultOfLastAtt = item.messageAction 
        self.BattleMenu("")

    def BattleMenu(self,args):
        if self.Enemy.hp <=0:
            self.manager.Switch("game")
        if self.Player.hp <=0:
            self.manager.Switch("gameover")
        if self.Player.resultOfLastAtt != None:
            self.ids.ActionDisplayPlayer.text = "Player Action :"+"\n"+self.Player.resultOfLastAtt
        if self.Enemy.resultOfLastAtt != None :
            self.ids.ActionDisplayEnemy.text = "Enemy Action :"+"\n"+self.Enemy.resultOfLastAtt
        self.ids.PlayerHp.text = "Hp : " + str(self.Player.hp)
        self.ids.PlayerStats.text = "\n att : \n" + self.Player.att
        self.ids.EnemyHp.text = "Hp : " + str(self.Enemy.hp)
        self.ids.EnemyStats.text = "\n att : \n" + self.Enemy.att
        self.ids.BattleButtons.clear_widgets()
        self.ids.BattleButtons.add_widget(Button(text="attack",on_release=self.Attack))
        self.ids.BattleButtons.add_widget(Button(text="items",on_release=self.Items))

        