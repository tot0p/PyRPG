from kivy.uix.screenmanager import  Screen
from kivy.uix.label import Label
from src.control.eventKey import EventKey


class WinScreen(Screen,EventKey):
    """ecran de victoire"""
    def __init__(self, **kwargs) -> None:
        Screen.__init__(self,**kwargs)
        EventKey.__init__(self)