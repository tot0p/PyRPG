from kivy.uix.screenmanager import  Screen
from kivy.graphics import Line
from kivy.core.window import Window
from src.control.eventKey import EventKey
import yfinance as yf

    
class  CryptoScreen(Screen,EventKey):
    def __init__(self, **kwargs) -> None:
        Screen.__init__(self,**kwargs)
        EventKey.__init__(self)
        self.current = "BTC-EUR"
        self.msft = yf.Ticker(self.current)
        self.hist = self.msft.history(period="1d",interval="5m")
        self.prices = self.hist.Close
        self.ids.actprice.text = str(self.prices[len(self.prices)-1])+" €"


    def on_enter(self, *args):
        self.draw()
        Window.bind(on_resize=self.draw)
        return super().on_enter(*args)

    def on_leave(self, *args):
        Window.bind(on_resize = lambda x,y,z: 1+1)
        return super().on_leave(*args)

    def changeCrypto(self,name):
        self.current = name
        self.msft = yf.Ticker(name)
        self.hist = self.msft.history(period="1d",interval="5m")
        self.prices = self.hist.Close
        self.ids.actprice.text = str(self.prices[len(self.prices)-1])+" €"
        self.draw()

    def draw(self, *args):
        self.draw_button()
        self.width,self.height = (Window.size[0]/3)*2,(Window.size[1]/3)*2
        self.posx,self.posy = Window.size[0]/3,Window.size[1]/3
        self.ids.testcanvas.canvas.clear()
        self.pricesList = []
        for i in range(len(self.prices)):
            self.pricesList.append(self.posx + ((self.width - 0) / (len(self.prices) - 0)) * (i - 0))
            self.pricesList.append(self.posy + ((self.height - 0) / (max(self.prices) - min(self.prices))) * (self.prices[i] - min(self.prices)))
        with self.ids.testcanvas.canvas:
                Line(points=self.pricesList, width=2)
        return Screen.on_enter(self,*args)

    def draw_button(self):
        self.ids.btc.text = "BTC : " + str(self.manager.currentGame.Player.wallet.btc)
        self.ids.sol.text = "SOL : " + str(self.manager.currentGame.Player.wallet.sol)
        self.ids.eth.text = "ETH : " + str(self.manager.currentGame.Player.wallet.eth)
        self.ids.xmr.text = "XMR : " + str(self.manager.currentGame.Player.wallet.xmr)
        self.ids.balanceeur.text = "Balance : " + str(self.manager.currentGame.Player.wallet.eur)


    def buy(self):
        try:
            if self.eur >=float(self.ids.amount.text)*self.prices[len(self.prices)-1]:
                self.manager.currentGame.Player.wallet.eur -= float(self.ids.amount.text)*self.prices[len(self.prices)-1]
                self.manager.currentGame.Player.wallet.add(self.current.lower().split("-")[0],float(self.ids.amount.text))
            self.draw_button()
        except:
            print("oh non !")
    def sell(self):
        try:
            if self.manager.currentGame.Player.wallet.get(self.current.lower().split("-")[0],float(self.ids.amount.text)) >=float(self.ids.amount.text):
                self.manager.currentGame.Player.wallet.eur += float(self.ids.amount.text)*self.prices[len(self.prices)-1]
                self.manager.currentGame.Player.wallet.rm(self.current.lower().split("-")[0],float(self.ids.amount.text))
            self.draw_button()
        except:
            print("oh non !")
        


    def key_action(self,keybord,keycode,_,keyName,textContent):
        if keycode == 27:
            self.manager.Switch("game")