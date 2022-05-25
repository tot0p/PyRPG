    
from kivy.uix.screenmanager import  Screen
from kivy.graphics import Line    
from src.control.eventKey import EventKey
from src.control.CarrouselBox import CarrouselBox
from kivy.uix.image import AsyncImage
from kivy.clock import Clock
from random import choice
from src.view.Crypto import GetPrice
    
class BoxScreen(Screen,EventKey):
    def __init__(self, **kwargs) -> None:
        self.i = 0
        self.isOpening = False
        self.Att = False
        Screen.__init__(self,**kwargs)
        EventKey.__init__(self)
        currentPath = "src/data/img/"
        self.EventsList = [
            EventsLootBox("btc",currentPath + "btc.png","btc","crypto"),
            EventsLootBox("eth",currentPath +"eth.png","eth","crypto"),
            EventsLootBox("sol",currentPath +"sol.png","sol","crypto"),
            EventsLootBox("xmr",currentPath +"xmr.png","xmr","crypto"),
            EventsLootBox("usb killer", currentPath +"usb-killer.png","fries you oponent pc with hight voltage\ndeals 10hp","obj"),
            EventsLootBox("antivirus", currentPath +"heal.png", "la base virale vps a été mise a jours\ngives 20hp","obj"),
            EventsLootBox("gatorade", currentPath + "gatorade.png", "add hp to your player","boost"),
            EventsLootBox("usb stick",currentPath + "usb-attach.png","make you learn one random attack","att"),
            EventsLootBox("no connection", currentPath + "no-internet.jpg", "skips a combat single use only and not usable on bosses","obj"),
            EventsLootBox("rtx3090", currentPath + "rtx3090.png", "augment your hashing power double your damage for the next turn","boost")
            ]
        

    def on_enter(self):
        self.ids.CarouselGrid.clear_widgets()
        self.carousel = CarrouselBox(loop=True,anim_type="linear",anim_move_duration=0.1)
        for i in self.EventsList:
            image = AsyncImage(source=i.img, allow_stretch=True) 
            self.carousel.add_widget(image)
        self.ids.CarouselGrid.add_widget(self.carousel)
        
    def on_leave(self):
        self.isOpening = False
        self.i = 0
        self.Att = False
        self.ids.LootboxBtn.text = 'Open Lootbox'
        self.ids.LootboxBtn.on_release = self.open_box

    def displayLoot(self,loot):
        self.ids.LootboxBtn.text = "you won : \n" + str(loot)
        if self.Att:
            self.ids.LootboxBtn.on_release= lambda : self.manager.SwitchAtt(False)
        else:
            self.ids.LootboxBtn.on_release= lambda : self.manager.Switch("game")

    def open_box(self):
        if not self.isOpening:
            self.ids.LootboxBtn.text = "Oppening ..."
            self.isOpening = True
            self.event = Clock.schedule_interval( self.playAnymeLoot, 0.2)

    def playAnymeLoot(self,inter):
        if self.i > 20 :
            # ev = choice(self.EventsList)
            ev = self.EventsList[6]
            self.carousel.load_slide(self.carousel.slides[self.EventsList.index(ev)])
            self.event.cancel()
            ev.active(self.manager.currentGame.Player,self)
            self.displayLoot(ev.Name)
        else:
            self.carousel.load_next()
            self.i+=1
        
    
    # def key_action(self, keybord, keycode, _, keyName, textContent):
    #     if keycode == 27:
    #         self.carousel.load_next(mode='next')
    
    

class EventsLootBox:

    def __init__(self,Name,img,desc,typ):
        self.Name = Name
        self.img = img
        self.desc = desc
        self.type = typ

    def active(self, player,lootbox):
        if self.type == "crypto":
            wallet =  player.wallet
            wallet.add(self.Name,GetPrice(self.Name))
        elif self.type == "att":
            lootbox.Att = True
        elif self.type == "obj":
            player.AddObjByName(self.Name)
        elif self.type == "boost":
            if self.Name == "rtx3090":
                for i in player.GetAtt():
                    i.damage += player.level *3
            elif self.Name == "gatorade":
                player.hp += 10 * player.level
                player.hpMax += 10 * player.level
            
    
