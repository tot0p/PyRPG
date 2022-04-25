# from src.control.SaveAndLoadGame import create_player
# from src.control.entities.att import attack

from src.control.map import Map

class Menu:

    def __init__(self) -> None:
        pass

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
        # p = create_player(input("Please enter your pseudo ?\n\t>> "))
        # print(p.att)
        # p.att =(0,attack("et non c une merde",6))
        # print(p.att)
        p = Map()
        print(p.tiles)