import os

from random import randint

def calcul_surface():
    """
    Fonction qui calcule la surface sous la courbe
    de la fonction y = x * x avec des rectangles avec x ∈ [a,b] et un pas p*
    """
    a = int(input("Entrer a : "))
    b = int(input("Entrer b : "))
    p = float(input("Entrer p : "))

    U0 = a*a*p
    S = U0
    n = 1
    while a + p*n < b:
        U0 = (a + p * n) * (a + p * n) * p
        S = U0 + S
        n = n + 1

    print(f"Calcul de l'intégrale de la fonction y = x * x avec {a} <= x < {b} et p = {p}")
    print(f"La surface est de {S}")

def jeu_allumettes():
    """
    Fonction qui simule le jeu des allumettes
    """
    pseudo = input("Entrer votre nom : ")
    nb_allumettes = int(input("Entrer le nombre d'allumettes de départ : "))
    turn = 0
    while nb_allumettes > 0:
        print("Il reste", nb_allumettes, "allumettes")
        if turn % 2 == 0:
            nb_remove = randint(1, 3)
            print(f"{'📍'*nb_allumettes} L'ordinateur enlève {nb_remove} allumettes")
        else:
            nb_remove = int(input("Combien d'allumettes prenez-vous ? "))
            if nb_remove > 3 or nb_remove < 1:
                print("Vous devez prendre entre 1 et 3 allumettes")
            
            print(f"{'📍'*nb_allumettes} {pseudo} enlève {nb_remove} allumettes")

        nb_allumettes = nb_allumettes - nb_remove
        turn += 1
    # TODO : To finish

def fichiers():
    nombres = list(map(int, input("Entrer une liste de nombres séparés par des espaces : ").split()))

    def create(file_name: str, data:list[int], binary=False):
        """
        Creates a file with the given name, and writes the data into it.
        :param file_name: str
        :param data: list[int]
        :param binary: bool
        """
        mode = "wb" if binary else "w"
        with open(file_name, mode) as f:
            for d in data:
                if binary:
                    f.write(d.to_bytes(4, byteorder="big"))
                else:
                    f.write(str(d) + "\n")

    def read(file_name:str, binary=False):
        """
        Reads the given file, and prints the content of the file.
        :param file_name: str
        :param binary: bool
        """
        mode = "rb" if binary else "r"
        with open(file_name, mode) as f:
            while True:
                if binary:
                    d = f.read(4)
                    if not d: break
                    print(int.from_bytes(d, byteorder="big"))
                else:
                    d = f.readline()
                    if not d: break
                    print(int(d))

    create("BDD.bin", nombres, binary=True)
    read("BDD.bin", binary=True)
    create("BDD.txt", nombres, binary=False)
    read("BDD.txt", binary=False)


