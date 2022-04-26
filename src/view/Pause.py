    
from kivy.uix.screenmanager import  Screen
from kivy.graphics import Line    
from src.control.eventKey import EventKey
    
class  PauseScreen(Screen,EventKey):
    def __init__(self, **kwargs) -> None:
        Screen.__init__(self,**kwargs)
        EventKey.__init__(self)
        with self.canvas:
            Line(points=[100,250,200,180,300,187,400,200,500,97,600,90,700,50], width=1)
    
    
    
