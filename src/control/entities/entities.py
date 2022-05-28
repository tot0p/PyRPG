

from src.control.entities.att import attack

from random import choice



#Entities
class entities:
    '''
    simule n'importe qu'elle entities du jeu avec une possibilité d'attack et de vie
    '''

    def __init__(self,name,hp=100,att=[None,None,None,None]) -> None:
        self.name = name
        self.hp = hp
        self.hpMax = hp
        self._att = att
        self.resultOfLastAtt = None

    def GetAtt(self):
        '''permet de récupérer les attacks de l'entities sauf celle égale à None'''
        return [i for i in self._att if i!=None ]

    def GetAttName(self):
        '''recupere tous les attack name'''
        return [i.name for i in self._att if i!=None ]

    @property
    def att(self):
        '''génere le string à afficher pour l'interface utilisateur '''
        result = ""
        count = 1
        for x in self._att:
            result += str(count) + " : " + str(x) + " \n"
            count +=1
        return result

    @att.setter
    def att(self,v):
        '''
        est le setter de self.att qui prend comme expression type :
            votreEntities.att = (idDeLAttaque,LobjetAtt)
        '''
        assert isinstance(v,tuple) ; "la valeur n'est pas un tuple"
        assert len(v)==2 ; "il n'y a pas le nombre de valeur demandé dans la valeur"
        assert isinstance(v[0],int) ; "v[0] n'est pas un int"
        assert isinstance(v[1],attack); "v[1] n'est pas un obj attack"
        id = v[0]
        assert id <=len(self._att); "l'id est trop grand max 3"
        assert id >=0 ; "l'id est trop petit min 0"
        self._att[id]=v[1]


    def randomAtt(self):
        '''return un attack au hazard '''
        return choice(self._att)

    def attack(self,name:str,target,callback=lambda:print("")):
        '''permet de lancé  une attack'''
        for i in self._att:
            if i != None:
                if i.name == name:
                    self.resultOfLastAtt =  i.attack(self,target)
        callback()