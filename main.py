import kivy
kivy.require('1.8.0')

from kivy.config import Config
from kivy.app import App
# from kivy.core.window import Window

from src.control.ScreenManager import Manager


class PyRPGApp(App):
    kv_directory = "src/data"

    def build(self):
        sm = Manager()
        return sm

# menu = Menu()

if __name__ == "__main__":
    # Window.maximize()
    # Window.fullscreen = "auto"
    Config.set('kivy', 'exit_on_escape', '0')
    PyRPGApp().run()