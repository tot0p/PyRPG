from kivy.uix.screenmanager import  Screen
from kivy.graphics import Line  
from src.control.eventKey import EventKey
from kivy.core.window import Window,WindowBase
import yfinance as yf
    
class  PauseScreen(Screen,EventKey):
    def __init__(self, **kwargs) -> None:
        Screen.__init__(self,**kwargs)
        EventKey.__init__(self)
        msft = yf.Ticker("ETH-EUR")
        hist = msft.history(period="1d",interval="5m")
        self.prices = hist.Close
        self.pricesList = []

    
    def on_enter(self, *args):
        width,height = Window.size
        Window.bind(on_resize=self.resize)
        for i in range(len(self.prices)):
            self.pricesList.append(0 + ((width - 0) / (len(self.prices) - 0)) * (i - 0))
            self.pricesList.append(0 + ((height - 0) / (max(self.prices) - min(self.prices))) * (self.prices[i] - min(self.prices)))

        with self.canvas:
            Line(points=self.pricesList, width=2)
    
    def on_leave(self, *args):
        Window.bind(on_resize=WindowBase.on_resize)
    
    def resize(self,parent,width,height):
        self.canvas.clear()
        self.pricesList = []
        for i in range(len(self.prices)):
            self.pricesList.append(0 + ((width - 0) / (len(self.prices) - 0)) * (i - 0))
            self.pricesList.append(0 + ((height - 0) / (max(self.prices) - min(self.prices))) * (self.prices[i] - min(self.prices)))

        with self.canvas:
            Line(points=self.pricesList, width=1)

    
