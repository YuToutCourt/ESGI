"""Auteur: Yohann Maley"""

from exos.materiel import Materiel
from exos.clavier import Clavier
from exos.ecran import Ecran


class Ordinateur(Materiel):
    def __init__(
        self, type_materiel: str, num_serie: str, clavier: Clavier, ecran: Ecran
    ):
        super().__init__(type_materiel, num_serie)
        self.__clavier = clavier
        self.__ecran = ecran

    def get_clavier(self):
        return self.__clavier

    def get_ecran(self):
        return self.__ecran

    def set_clavier(self, clavier: Clavier):
        self.__clavier = clavier

    def set_ecran(self, ecran: Ecran):
        self.__ecran = ecran

    def save_config(self):
        """
        Sauvegarde la configuration de l'ordinateur dans un fichier
        """
        content = "\n".join(
            [
                self.get_type_materiel(),
                self.get_num_serie(),
                self.get_clavier().__str__(),
                self.get_ecran().__str__(),
            ]
        )

        with open("config.txt", "w", encoding="utf-8") as f:
            f.write(content)

    def load_config(self):
        """
        Lit le fichier de configuration et charge les données
        """
        with open("config.txt", "r") as f:
            data = f.read()
            print(data)
