import json
import os

def WriteJson(path: str, cont: dict):
    """
    permet d'ecrire dans un fichier sous le format json
    """
    with open(path, 'w') as f:
        json.dump(cont, f)


def ReadJson1Prof(path: str):
    """
    permet de lire dans un fichier sous le format json à un de profondeur
    """
    with open(path) as f:
        data = json.load(f)
    return data

def ReadJson(path: str):
    """
    permet de lire dans un fichier sous le format json
    """
    with open(path) as f:
        data = json.loads(f.read())
    return data

def ExistFile(path:str) -> bool:
    """
    permet de vérifier si un fichier existe
    """
    if os.path.isfile(path) == True:
        if os.path.getsize(path) > 0:
            return True
        else:
            return False
    else:
        file = open(path, 'a')
        file.close()
        return False