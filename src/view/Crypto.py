    
from kivy.uix.screenmanager import  Screen
from kivy.graphics import Line    
    
class  CryptoScreen(Screen):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=[100,250,200,180,300,187,400,200,500,97,600,90,700,50], width=1)
    
    
    
