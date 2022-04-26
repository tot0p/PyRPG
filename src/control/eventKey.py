

class EventKeyNotDefiened(Exception):
    def __init__(self,name):
        super().__init__(f"le Screen {name} n'hérite pas de EventKey")


class EventKey:
    def key_action(self,keybord,keycode,_,keyName,textContent):
        if keycode == 27:
            exit(0)

class EventKeyManager:
    def __init__(self,sm) -> None:
        self.sm = sm
        for i in self.sm.screens:
            if not (hasattr(i, 'key_action') and callable(getattr(i, 'key_action'))):
                raise EventKeyNotDefiened(i.name)
        

    def key_action(self,keybord,keycode,_,keyName,textContent):
        self.sm.current_screen.key_action(keybord,keycode,_,keyName,textContent)
        