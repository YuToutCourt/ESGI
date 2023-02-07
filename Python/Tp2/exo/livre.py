class Livre:
    def __init__(self, nom:str, auteur:str, maison_edition:str, code_barre:str):
        self.__nom = nom
        self.__auteur = auteur
        self.__maison_edition = maison_edition
        self.__code_barre = code_barre

    def get_nom(self):
        return self.__nom

    def get_auteur(self):
        return self.__auteur

    def get_maison_edition(self):
        return self.__maison_edition

    def get_code_barre(self):
        return self.__code_barre

    def set_nom(self, nom:str):
        self.__nom = nom
    
    def set_auteur(self, auteur:str):
        self.__auteur = auteur

    def set_maison_edition(self, maison_edition:str):
        self.__maison_edition = maison_edition

    def set_code_barre(self, code_barre:str):
        self.__code_barre = code_barre

    
    def modifier_livre(self, nom:str, auteur:str, maison_edition:str, code_barre:str):
        self.set_nom(nom)
        self.set_auteur(auteur)
        self.set_maison_edition(maison_edition)
        self.set_code_barre(code_barre)

    def __str__(self) -> str:
        return f"Nom : {self.get_nom()}\nAuteur : {self.get_auteur()}\nMaison d'édition : {self.get_maison_edition()}\nCode barre : {self.get_code_barre()}"
    
    def afficher_livre(self):
        print(self)   