from kivy.uix.screenmanager import  Screen
from src.control.jsonfile import ReadJson,WriteJson
from src.control.eventKey import EventKey
from src.control.eventGameManager import EventGameManager,EventGameManagerEncoder
from src.control.entities.Player import PlayerEncoder
from src.control.map import MapEncoder
import json
from json import JSONEncoder



pathEventsFile = "./src/data/event/eventBase.json"

class  GameScreen(Screen,EventKey):
    def __init__(self, **kwargs) -> None:
        Screen.__init__(self,**kwargs)
        EventKey.__init__(self)
        self.Player = ""
        self.Map = ""
        self.event = None
        self.MonsterFight = 0
        self.eventGameManager = EventGameManager(pathEventsFile)
        self.textInput = self.ids.rootTextInput
        self.historyInput = self.ids.previousactions
        self.hist = self.ids.gametext
        self.eventPast = False
        self.rep = self.ids.textaction
        self.textInput.bind(on_text_validate=self.on_enter_textInput)
        self.posDep = []

    def LaunchGame(self,Player,Map):
        self.Player = Player
        self.Map = Map
        self.SaveGame()
    
    def SaveGame(self):
        PlayerData = json.dumps(self.Player,cls=PlayerEncoder)
        MapData = json.dumps(self.Map,cls=MapEncoder)
        EventGameManagerData = json.dumps(self.eventGameManager,cls=EventGameManagerEncoder)
        GameData = {
            "Player":PlayerData,
            "Map":MapData,
            "eventGameManager":EventGameManagerData,
            "event":self.event,
            "eventPast":self.eventPast,
            "MonsterFight":self.MonsterFight,
        }
        WriteJson("src/data/save.json",GameData)

        
        

    def on_enter(self, *args):
        if self.event == None:
            self.display_event(self.Map.get_event(self.Player.x,self.Player.y))
        return super().on_enter(*args)


    def display_event(self,eventId):
        self.event, self.special = self.eventGameManager.loadEvent(eventId)
        self.hist.text = self.event.hist
        self.rep.text = self.event.StrRep()

    def on_enter_textInput(self,instance):
        self.historyInput.text = self.historyInput.text + "\n" + instance.text
        temp = self.historyInput.text.split("\n")
        if self.eventPast:
            if instance.text.lower() in self.posDep:
                self.Player.move(instance.text)
                self.eventPast = False
                self.display_event(self.Map.get_event(self.Player.x,self.Player.y))
        else:
            if instance.text.lower() in self.event.rep:
                if self.eventGameManager.IsNormalType():
                    self.hist.text = self.event.histfin + "\n where you want to go"
                    self.generatePosDep()
                    self.rep.text = ",\n".join(self.posDep)
                    self.eventPast = True
                else:
                    self.hist.text = self.event.histfin + "\n where you want to go"
                    self.generatePosDep()
                    self.rep.text = ",\n".join(self.posDep)
                    self.eventPast = True
                    self.manager.Switch(self.event.type)
        if len(temp)>8:
            self.historyInput.text = temp[-1]
        instance.text = ""

    def generatePosDep(self):
        self.posDep = []
        if self.Player.y > 0:
            self.posDep.append("up")
        if self.Player.y < 20:
            self.posDep.append("down")
        if self.Player.x > 0:
            self.posDep.append("left")
        if self.Player.x < 20:
            self.posDep.append("right")


    def key_action(self,keybord,keycode,_,keyName,textContent):
        if keycode == 27:
            self.manager.Switch("pause")