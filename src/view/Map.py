from kivy.uix.screenmanager import Screen
from src.control.eventKey import EventKey
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout


class MapScreen(Screen, EventKey):
    def __init__(self, **kwargs) -> None:
        self.mapIco = {"0": "⬛", "1": "👤", "2": "🎁", "3": "💥"}

        Screen.__init__(self, **kwargs)
        EventKey.__init__(self)

    def on_enter(self, *args):
        player_x = self.manager.currentGame.Player.x
        player_y = self.manager.currentGame.Player.y
        for y in range(player_y - 2, player_y + 3):
            for x in range(player_x - 2, player_x + 3):
                if x < 0 or y < 0:
                    self.ids.map.add_widget(Label(text=" ", font_size=30))
                elif x == player_x and y == player_y:
                    self.ids.map.add_widget(
                        Label(
                            text="🤖",
                            font_size=30,
                            font_name="./src/font/NotoEmoji-VariableFont_wght.ttf",
                        )
                    )
                else:
                    self.ids.map.add_widget(
                        Label(
                            text=self.mapIco[
                                str(self.manager.currentGame.Map.tiles[y][x])
                            ],
                            font_size=30,
                            font_name="./src/font/NotoEmoji-VariableFont_wght.ttf",
                        )
                    )
        return super().on_enter(*args)

    def on_leave(self, *args):
        self.ids.map.clear_widgets()

    def key_action(self, keybord, keycode, _, keyName, textContent):
        if keycode == 27:
            self.manager.Switch("game")
