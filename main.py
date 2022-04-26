import kivy
kivy.require('1.8.0')

from kivy.config import Config
from kivy.app import App
from kivy.core.window import Window

from src.control.ScreenManager import Manager
from src.control.eventKey import EventKeyManager


class PyRPGApp(App):
    kv_directory = "src/data"

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
    PyRPGApp().run()