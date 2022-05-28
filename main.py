import kivy
kivy.require('1.8.0')

from kivy.config import Config
from kivy.app import App
from kivy.core.window import Window

from src.control.ScreenManager import Manager
from src.control.eventKey import EventKeyManager


__author__  = "Thomas Lemaitre , Luca Morgado"
__status__  = "release"
__version__ = "1.0"
__date__    = "26 may 2022"

class PyRPGApp(App):
    kv_directory = "src/data" # endroit ou le fichier d'interface est (src/data/pyrpg.kv)

    def build(self):
        sm = Manager()
        self.ekm = EventKeyManager(sm)
        Window.bind(on_key_down= self.ekm.key_action)
        # sm.Switch("box")
        return sm

# menu = Menu()

if __name__ == "__main__":
    Window.maximize()
    # Window.fullscreen = "auto"
    Config.set('kivy', 'exit_on_escape', '0')
    Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
    PyRPGApp().run()