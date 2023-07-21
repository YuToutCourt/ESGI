from datetime import datetime

class Magazine:
    def __init__(self, titre:str, numero:int, date:str):
        self.titre = titre
        self.numero = numero
        self.date = date

    def __eq__(self, other):
        return self.numero == other.numero
    
    def __hash__(self):
        return hash(self.numero)