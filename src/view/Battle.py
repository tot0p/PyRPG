from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from src.control.eventKey import EventKey
from src.control.entities.enemy import Enemy , LoadEnemy
from src.control.entities.att import GetAllAtt , attack
from random import choice

class BattleScreen(Screen,EventKey):
    def __init__(self,**kwargs) -> None:
        Screen.__init__(self,**kwargs)
        EventKey.__init__(self)
        self.bossBattel = False


    def createEnemy(self):
        temp = self.manager.currentGame.MonsterFight
        if self.manager.currentGame.special:
            t = self.manager.currentGame.Map.quest[0].GetBoss()
            att = []
            for i in t["att"]:
                att.append(attack(**i))
            self.Enemy = Enemy(t["name"], t["hp"], att)
            self.bossBattel = True
            self.Enemy.isBoss=True
        else:
            if temp < 3:
                self.Enemy = LoadEnemy(temp)
            else:
                r = GetAllAtt()
                att = [choice(r),choice(r),choice(r),choice(r)]
                for i in att:
                    i.damage += self.manager.currentGame.MonsterFight
                self.Enemy = Enemy("Strong Hackerman", 150, att)
            self.manager.currentGame.MonsterFight +=1

    def on_enter(self):
        self.createEnemy()
        self.Player = self.manager.currentGame.Player
        self.ids.PlayerName.text = self.Player.name
        self.ids.EnemyName.text = self.Enemy.name
        self.BattleMenu("")

        return Screen.on_enter(self)

    def on_leave(self):
        self.Player.resultOfLastAtt = None
        self.Enemy.resultOfLastAtt = None
        self.ids.ActionDisplayPlayer.text = "Player Action :"
        self.ids.ActionDisplayEnemy.text = "Enemy Action :"
        if self.bossBattel:
            t = self.manager.currentGame.Map.NextQuest()
            self.bossBattel = False
            if t :
                self.manager.Switch("win")
        return Screen.on_leave(self)
        
    def Attack(self,args):
        self.ids.BattleButtons.clear_widgets()
        for i in self.Player.GetAtt():
            self.ids.BattleButtons.add_widget(Button(text=i.name,on_release=lambda x : self.Player.attack(x.text,self.Enemy,lambda : self.Enemy.attack(self.Enemy.randomAtt().name, self.Player,lambda : self.BattleMenu("")))))
    
    def Items(self,args):
        self.ids.BattleButtons.clear_widgets()
        if len(self.Player.inv)<=0:
            self.ids.BattleButtons.add_widget(Button(text="You have no items in your inventory",on_release=lambda x: self.BattleMenu("")))
        else:
            for i in self.Player.inv:
                self.ids.BattleButtons.add_widget(Button(text=i.name+"\nUse Left : "+i.GetNumberUse(),on_release=lambda x : self.Player.GetObjByName(x.text.split("\n")[0]).use(self.Player,self.Enemy,lambda : self.Enemy.attack(self.Enemy.randomAtt().name, self.Player,lambda : self.displayItemMessage(self.Player.GetObjByName(x.text.split("\n")[0]))))))
        
    def displayItemMessage(self,item):
        self.Player.resultOfLastAtt = item.messageAction 
        self.BattleMenu("")

    def BattleMenu(self,args):
        if self.Player.hp <=0:
            self.manager.Switch("gameover")
            return
        elif self.Enemy.hp <=0:
            if self.Player.levelUp(self.Enemy.xpReward):
                self.manager.SwitchAtt()
            else:
                self.manager.Switch("box")
            return
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

    def key_action(self, keybord, keycode, _, keyName, textContent):
        if keycode == 27:
            self.BattleMenu("")