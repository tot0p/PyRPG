from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from src.control.eventKey import EventKey
from src.control.entities.enemy import Enemy

class GameOverScreen(Screen,EventKey):
    """screen de game over"""
    def __init__(self,**kwargs) -> None:
        Screen.__init__(self,**kwargs)
        EventKey.__init__(self)
