"""Auteur: Yohann Maley"""

from exos.materiel import Materiel


class Clavier(Materiel):
    def __init__(self, type_materiel: str, num_serie: str, nombre_touche: int):
        super().__init__(type_materiel, num_serie)
        self.__nombre_touche = nombre_touche

    def get_nombre_touche(self):
        return self.__nombre_touche

    def set_nombre_touche(self, nombre_touche):
        self.__nombre_touche = nombre_touche

    def __str__(self) -> str:
        return super().__str__() + f"Nombre de touche: {self.get_nombre_touche()}"
