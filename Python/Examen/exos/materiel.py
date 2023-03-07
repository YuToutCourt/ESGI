"""Auteur: Yohann Maley"""


class Materiel:
    def __init__(self, type_materiel: str, num_serie: str):
        self.__type_materiel = type_materiel
        self.__num_serie = num_serie

    def get_type_materiel(self):
        return self.__type_materiel

    def get_num_serie(self):
        return self.__num_serie

    def set_type_materiel(self, type_materiel):
        self.__type_materiel = type_materiel

    def set_num_serie(self, num_serie):
        self.__num_serie = num_serie

    def __str__(self) -> str:
        return f"""
Type de matériel: {self.get_type_materiel()}
Numéro de série: {self.get_num_serie()}
        """
