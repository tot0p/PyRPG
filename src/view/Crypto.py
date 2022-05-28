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
        self.to = "game"
        self.hist = self.msft.history(period="1d",interval="5m")
        self.prices = self.hist.Close
        self.ids.actprice.text = "Current Price : " + str(self.prices[len(self.prices)-1])+" €"


    def on_enter(self, *args):
        """event de kivy quand on entre sur le screen"""
        self.draw()
        Window.bind(on_resize=self.draw)
        return super().on_enter(*args)

    def on_leave(self, *args):
        """event de kivy quand on quit sur le screen"""
        Window.bind(on_resize = lambda x,y,z: 1+1)
        return super().on_leave(*args)

    def changeCrypto(self,name):
        """permet de changer la current crypto"""
        self.current = name
        self.msft = yf.Ticker(name)
        self.hist = self.msft.history(period="1d",interval="5m")
        self.prices = self.hist.Close
        self.ids.actprice.text = str(self.prices[len(self.prices)-1])+" €"
        self.draw()

    def draw(self, *args):
        """dessine le graphique et les differents elements graphiques dynamique"""
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
        """dessine les button"""
        self.ids.btc.text = "BTC : " + str(self.manager.currentGame.Player.wallet.btc)
        self.ids.sol.text = "SOL : " + str(self.manager.currentGame.Player.wallet.sol)
        self.ids.eth.text = "ETH : " + str(self.manager.currentGame.Player.wallet.eth)
        self.ids.xmr.text = "XMR : " + str(self.manager.currentGame.Player.wallet.xmr)
        self.ids.balanceeur.text = "Balance : " + str(self.manager.currentGame.Player.wallet.eur) + " €"

    def maxBuy(self):
        """permet d'achete le max de la current crypto"""
        self.ids.amount.text = str(self.manager.currentGame.Player.wallet.eur/self.prices[len(self.prices)-1])
    def maxSell(self):
        """permet de vendre le max de la current crypto"""
        self.ids.amount.text = str(self.manager.currentGame.Player.wallet.get(self.current.lower().split("-")[0]))

    def buy(self):
        """permet de buy la current crypto"""
        try :
            if float(self.ids.amount.text)>0 and self.manager.currentGame.Player.wallet.eur >=float(self.ids.amount.text)*self.prices[len(self.prices)-1]:
                self.manager.currentGame.Player.wallet.eur -= float(self.ids.amount.text)*self.prices[len(self.prices)-1]
                self.manager.currentGame.Player.wallet.add(self.current.lower().split("-")[0],float(self.ids.amount.text))
            self.draw_button()
        except:
            print("non non non !")
        
    def sell(self):
        """permet de sell la current crypto"""
        try :
            if float(self.ids.amount.text)>0 and self.manager.currentGame.Player.wallet.get(self.current.lower().split("-")[0]) >=float(self.ids.amount.text):
                self.manager.currentGame.Player.wallet.eur += float(self.ids.amount.text)*self.prices[len(self.prices)-1]
                self.manager.currentGame.Player.wallet.rm(self.current.lower().split("-")[0],float(self.ids.amount.text))
            self.draw_button()
        except:
            print("non non non !")
        


    def key_action(self,keybord,keycode,_,keyName,textContent):
        if keycode == 27:
            self.manager.Switch(self.to)

def GetPrice(crypto,price=100):
    """permet de recuperer le nb de la crypto pour le price"""
    current = crypto.upper()+"-EUR"
    msft = yf.Ticker(current)
    hist = msft.history(period="1d",interval="5m")
    prices = hist.Close
    return price/prices[len(prices)-1]