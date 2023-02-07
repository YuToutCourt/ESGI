from exo.livre import Livre

class Roman(Livre):
    def __init__(self, nom: str, auteur: str, maison_edition: str, code_barre: str, type_roman:str, description:str):
        super().__init__(nom, auteur, maison_edition, code_barre)
        self.__type_roman = type_roman
        self.__description = description
    
    def get_type_roman(self):
        return self.__type_roman

    def get_description(self):
        return self.__description

    def set_type_roman(self, type_roman:str):
        self.__type_roman = type_roman

    def set_description(self, description:str):
        self.__description = description


    def modifier_livre(self, nom: str, auteur: str, maison_edition: str, code_barre: str, type_roman:str, description:str):
        super().modifier_livre(nom, auteur, maison_edition, code_barre)
        self.set_type_roman(type_roman)
        self.set_description(description)

    def __str__(self) -> str:
        return super().__str__() + f"\nType de roman : {self.get_type_roman()}\nDescription : {self.get_description()}"

    def afficher_livre(self):
        print(self)