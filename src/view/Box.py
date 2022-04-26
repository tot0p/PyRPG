    
from kivy.uix.screenmanager import  Screen
from kivy.graphics import Line    
from src.control.eventKey import EventKey
from src.control.CarrouselBox import CarrouselBox
from kivy.uix.image import AsyncImage
    
class BoxScreen(Screen,EventKey):
    def __init__(self, **kwargs) -> None:
        Screen.__init__(self,**kwargs)
        EventKey.__init__(self)
        self.carousel = CarrouselBox(loop=True,anim_type="in_elastic")
        for i in range(10):
            src = "https://cdn.discordapp.com/attachments/899663943256121405/965541933512548392/PXL_20220417_140835813.PORTRAIT2.jpg"
            image = AsyncImage(source=src, allow_stretch=True) 
            self.carousel.add_widget(image)
        self.ids.CarouselGrid.add_widget(self.carousel)

    def key_action(self, keybord, keycode, _, keyName, textContent):
        if keycode == 27:
            self.carousel.load_next(mode='next')
    
    
    
