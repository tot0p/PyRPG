# from src.control.SaveAndLoadGame import create_player
# from src.control.entities.att import attack
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button


import re

class MenuButton(Button):
    def __init__(self, func,**kwargs):
        super().__init__(**kwargs)
        self.func = func
    
    def on_release(self):
        self.func()
        return super().on_release()

class MenuScreen(Screen):
    def __init__(self,**kwargs) -> None:
        super().__init__(**kwargs)
        self.options = {"Load Game":lambda  : print("Load Game"),"New Game":lambda : self.manager.Switch("newgame"),"Options":lambda :print("Options"),"Quit":lambda : exit(0)}
        t = []
        for key in self.options:
            t.append(key)
            button = MenuButton(self.options[key],text=str(len(t))+". "+key)
            self.ids.gridMenu.add_widget(button)

class Menu:

    def __init__(self) -> None:
        self.options = {"Load Game":lambda : print("Load Game"),"New Game":lambda :print("New Game"),"Options":lambda :print("Options"),"Quit":lambda : exit(0)}

    def aff(self):
        print(r'''
        _______           _______  _______  _______ 
        (  ____ )|\     /|(  ____ )(  ____ )(  ____ \
        | (    )|( \   / )| (    )|| (    )|| (    \/
        | (____)| \ (_) / | (____)|| (____)|| |      
        |  _____)  \   /  |     __)|  _____)| | ____ 
        | (         ) (   | (\ (   | (      | | \_  )
        | )         | |   | ) \ \__| )      | (___) |
        |/          \_/   |/   \__/|/       (_______)
        ''')


        #main menu
        print(r'''
        Main menu :
        ''')


        run = True
        while run:
            choice = input("\t>>")
            if choice in t:
                run = False
            elif re.search(r"^[1-"+str(len(t))+r"]*$",choice) !=None:
                choice = t[int(choice)-1]
                run = False

        return self.options[choice]
        


