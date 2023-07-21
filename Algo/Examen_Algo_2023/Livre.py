class Livre:
    def __init__(self, titre:str, auteur:str, isbn:str):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn

    def __eq__(self, other):
        return self.isbn == other.isbn
    
    def __hash__(self):
        return hash(self.isbn)
