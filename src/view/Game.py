from kivy.uix.screenmanager import  Screen
from src.control.jsonfile import ReadJson
from src.control.eventKey import EventKey


class  GameScreen(Screen,EventKey):
    def __init__(self, **kwargs) -> None:
        Screen.__init__(self,**kwargs)
        EventKey.__init__(self)
        self.Player = ""
        self.Map = ""
        self.textInput = self.ids.rootTextInput
        self.historyInput = self.ids.previousactions
        self.hist = self.ids.gametext
        self.eventPast = False
        self.rep = self.ids.textaction
        self.textInput.bind(on_text_validate=self.on_enter_textInput)

    def LaunchGame(self,Player,Map):
        self.Player = Player
        self.Map = Map

    def on_enter(self, *args):
        self.display_event("0")
        return super().on_enter(*args)

    def loadEvent(self,path,eventId):
        event = ReadJson(path)
        return event[eventId]

    def display_event(self,eventId):
        self.event = self.loadEvent("./src/data/event/eventBase.json",eventId)
        self.hist.text = self.event["hist"]
        self.rep.text = " ".join([x for x in self.event["rep"]])

    def on_enter_textInput(self,instance):
        self.historyInput.text = self.historyInput.text + "\n" + instance.text
        temp = self.historyInput.text.split("\n")
        if self.eventPast:
            if instance.text.lower() in ["top","bot","right","left"]:
                self.Player.move(instance.text)
                self.eventPast = False
                self.display_event(self.Map.get_event(self.Player.x,self.Player.y))
        else:
            if instance.text.lower() in self.event["rep"]:
                self.hist.text = self.event["histfin"] + "\n where you want to go"
                self.rep.text = " ".join(["top","bot","right","left"])
                self.eventPast = True
        if len(temp)>8:
            self.historyInput.text = temp[-1]
        instance.text = ""


    def key_action(self,keybord,keycode,_,keyName,textContent):
        if keycode == 27:
            self.manager.Switch("pause")


            