"""Auteur: Yohann Maley"""

import sys

from exos.clavier import Clavier
from exos.ecran import Ecran
from exos.pc import Ordinateur
from utilitary.utilitary import *

# Define a list of public function of that module, available by import *
__all__ = ["exo1", "exo2", "exo3"]


def seuil(P: int, T: float) -> int:
    """
    Fonction qui calcule le nombre de mois nécessaires pour que le capital P atteigne 1000 euros

    :param P: int, Le capital initial
    :param T: float, Le taux d'intérêt

    :return: int, Le nombre de mois nécessaires
    """

    try:
        from tabulate import tabulate
    except ImportError:
        print(
            ">> Veuillez installer les dépendances avec la commande 'pip install -r requirements.txt' <<"
        )
        sys.exit()

    if P > 1000:
        return "P doit être inférieur à 1000"

    N = 0
    table = [["P", "N"]]
    while P < 1000:
        P *= T
        N += 1
        table.append([round(P, 2), N])
    print(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))
    return N


def exo1():
    """
    Fonction qui permet de lancer l'exercice 1
    """
    print("Exercice 1")
    print("Nmax : ", seuil(input_int("P: "), input_float("T: ")))


def suite(A: int, B: int, N: int):
    """
    Fonction qui calcule une suite

    :param A: int, Le premier terme
    :param B: int, Le deuxième terme
    :param N: int, Le nombre de termes

    :return: tuple[int, int], Le dernier terme et l'avant dernier terme
    """

    U0, U1 = A, B
    Un_1 = None

    for _ in range(2, N + 1):
        Un = (U0 + U1) / 2
        if Un_1 is not None:
            Un_1, Un_2 = Un, Un_1
            U0, U1 = Un_1, Un_2
        else:
            Un_1 = Un
            U0, U1 = U1, Un

    return Un, Un_1


def exo2():
    """
    Fonction qui permet de lancer l'exercice 2
    """
    print("Exercice 2")
    print(suite(input_int("A: "), input_int("B: "), input_int("N: ")))


def exo3():
    """
    Fonction qui permet de lancer l'exercice 3
    """

    clavier = Clavier("Clavier", "123", 100)
    ecran = Ecran("Ecran", "456", "104 x 58.5 cm")
    pc = Ordinateur("PC", "789", clavier, ecran)

    pc.save_config()
    pc.load_config()
