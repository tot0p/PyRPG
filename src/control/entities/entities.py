

from src.control.entities.att import attack


## Error
class ErrorAttEntities(Exception):
    def __init__(self,maxi,obj, *args: object) -> None:
        super().__init__(*args)
        self.max = maxi
        self.obj = obj


#Entities
class entities:

    def __init__(self,name,hp=100,defence=10,att=[attack("Luca"),None,None,None]) -> None:
        self.name = name
        self.hp = hp
        self.defence = defence
        self._att = att
        self.status = []

    @property
    def att(self):
        result = ""
        count = 1
        for x in self._att:
            result += str(count) + " : " + str(x) + " \n"
            count +=1
        return result

    @att.setter
    def att(self,v):
        assert isinstance(v,tuple) ; "la valeur n'est pas un tuple"
        assert len(v)==2 ; "il n'y a pas le nombre de valeur demandé dans la valeur"
        assert isinstance(v[0],int) ; "v[0] n'est pas un int"
        assert isinstance(v[1],attack); "v[1] n'est pas un obj attack"
        id = v[0]
        if id > len(self._att):
            raise ErrorAttEntities(len(self._att,self))
        self._att[id]=v[1]


    def attack(self,name:str,target):
        for i in self._att:
            if i.name == name:
                i.attack(self,target)