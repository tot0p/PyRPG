from src.control.jsonfile import ReadJson , json

class Event:
    def __init__(self,type="",hist="",rep="",histfin="",**args):
        self.type = type
        self.hist = hist
        self.rep = rep
        self.histfin = histfin
        self.currentId = ""

    def StrRep(self):
        return " ".join([x for x in self.rep])

    def __str__(self):
        return self.type +" " + self.hist + " " + self.StrRep() + " " + self.histfin


class EventGameManager:

    def __init__(self,path):
        self.all_events = {}
        events = ReadJson(path)
        for i in events :
            self.all_events[i]  = Event(**events[i])

    def loadEvent(self,id=""):
        if id =="":
            id = self.currentId
        else:
            self.currentId = id
        if id != "-1":
            return self.all_events[id] , False
        else:
            self.currentId = "3"
            return self.all_events["3"] , True

    def IsNormalType(self,id=""):
        if id =="":
            id = self.currentId
        else:
            self.currentId = id
        return self.all_events[id].type == ""


    

# if __name__ == "__main__":
#     eventMan = EventGameManager("../data/event/eventBase.json")
#     print(eventMan.loadEvent(1))