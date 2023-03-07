"""Auteur: Yohann Maley"""

from exos.materiel import Materiel


class Ecran(Materiel):
    def __init__(self, type_materiel: str, num_serie: str, taille: str):
        super().__init__(type_materiel, num_serie)
        self.__taille = taille

    def get_taille(self):
        return self.__taille

    def set_taille(self, taille):
        self.__taille = taille

    def __str__(self) -> str:
        return super().__str__() + f"Taille: {self.get_taille()}"
