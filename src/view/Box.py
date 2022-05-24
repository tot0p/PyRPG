    
from kivy.uix.screenmanager import  Screen
from kivy.graphics import Line    
from src.control.eventKey import EventKey
from src.control.CarrouselBox import CarrouselBox
from kivy.uix.image import AsyncImage
from kivy.clock import Clock
from random import choice
from time import sleep
    
class BoxScreen(Screen,EventKey):
    def __init__(self, **kwargs) -> None:
        self.i = 0
        self.isOpening = False
        Screen.__init__(self,**kwargs)
        EventKey.__init__(self)
        self.EventsList = [EventsLootBox("btc","src/data/img/btc.png"),EventsLootBox("eth","src/data/img/eth.png"),EventsLootBox("sol","src/data/img/sol.png"),EventsLootBox("xmr","src/data/img/xmr.png")]
        

    def on_enter(self):
        self.ids.CarouselGrid.clear_widgets()
        self.carousel = CarrouselBox(loop=True,anim_type="linear",anim_move_duration=0.1)
        for i in self.EventsList:
            image = AsyncImage(source=i.img, allow_stretch=True) 
            self.carousel.add_widget(image)
        self.ids.CarouselGrid.add_widget(self.carousel)
        
    def displayLoot(self,loot):
        self.ids.LootboxBtn.text = "you won : \n" + str(loot)
        self.ids.LootboxBtn.on_release= lambda : self.manager.Switch("game")

    def open_box(self):
        if not self.isOpening:
            self.ids.LootboxBtn.text = "Oppening ..."
            self.isOpening = True
            self.event = Clock.schedule_interval( self.playAnymeLoot, 0.2)

    def playAnymeLoot(self,inter):
        if self.i > 20 :
            ev = choice(self.EventsList)
            self.carousel.load_slide(self.carousel.slides[self.EventsList.index(ev)])
            self.event.cancel()
            ev.active(self.manager.currentGame.Player)
            sleep(1)
            self.displayLoot(ev.Name)
        else:
            self.carousel.load_next()
            self.i+=1
        
    
    # def key_action(self, keybord, keycode, _, keyName, textContent):
    #     if keycode == 27:
    #         self.carousel.load_next(mode='next')
    
    

class EventsLootBox:

    def __init__(self,Name,img,effect=print):
        self.Name = Name
        self.img = img
        self._effect = effect

    def active(self, player):
        self._effect(player)
    
