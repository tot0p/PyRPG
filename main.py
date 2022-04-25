import kivy
kivy.require('1.8.0')

from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,  NoTransition , Screen


from src.view.Menu import MenuScreen
from src.view.Settings import SettingsScreen

class PyRPGApp(App):
    kv_directory = "src/data"

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(SettingsScreen(name="settings"))
        sm.transition = NoTransition()
        return sm

# menu = Menu()

if __name__ == "__main__":
    PyRPGApp().run()