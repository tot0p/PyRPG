import json
import os

def WriteJson(path: str, cont: dict):
    with open(path, 'w') as f:
        json.dump(cont, f)


def ReadJson(path: str) -> dict:
    with open(path) as f:
        data = json.load(f)
    return data

def ExistFile(path:str) -> bool:
    if os.path.isfile(path) == True:
        if os.path.getsize(path) > 0:
            return True
        else:
            return False
    else:
        file = open(path, 'a')
        file.close()
        return False