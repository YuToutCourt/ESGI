from random import randint

from exo.livre import Livre
from exo.roman import Roman
from exo.tkinter_exo import App

__all__ = ["calcul_surface", "jeu_allumettes", "fichiers", "livre", "tkinter"]

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
    nb_allumettes = input("Entrer le nombre d'allumettes de départ : ")

    if not nb_allumettes.isdigit():
        print("Le nombre d'allumettes doit être un entier")
        return

    nb_allumettes = int(nb_allumettes)
    
    turn = randint(0, 1) # choisir aléatoirement le joueur de départ (0 = ordinateur, 1 = joueur)
    while nb_allumettes > 0:
        print(f"Il reste {'📍'*nb_allumettes} allumettes\n")

        if turn == 0: # tour de l'ordi
            nb_remove = randint(1, 3)
            print(f"{'📍'*nb_allumettes} L'ordinateur enlève {nb_remove} allumettes")
            turn = 1

        else:
            while True:
                nb_remove = input("Combien d'allumettes prenez-vous ? ")

                if not nb_remove.isdigit():
                    print("Vous devez prendre un nombre d'allumettes")
                    continue
                
                nb_remove = int(nb_remove)
                
                if nb_remove > 3 or nb_remove < 1:
                    print("Vous devez prendre entre 1 et 3 allumettes")
                    continue

                else : break
            
            print(f"{'📍'*nb_allumettes} {pseudo} enlève {nb_remove} allumettes")
            turn = 0
        nb_allumettes -= nb_remove
    
    if turn == 1:
        print(f"{pseudo} a gagné !\nL'ordinateur a perdu !")
    else:
        print(f"L'ordinateur a gagné !\n{pseudo} a perdu !")

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
                if binary: f.write(d.to_bytes(4, byteorder="big"))
                else: f.write(str(d) + "\n")

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

def livre():

    livre1 = Livre("One Piece", "Eiichiro Oda", "Shueisha", "978-2-7560-4075-2")

    livre1.afficher_livre()
    livre1.modifier_livre("My Hero Academia", "Kohei Horikoshi", "Shueisha", "978-2-7560-4075-2")
    livre1.afficher_livre()


    roman1 = Roman("One Piece", "Eiichiro Oda", "Shueisha", "978-2-7560-4075-2", "Shonen", "Un pirate qui veut devenir le roi des pirates")

    roman1.afficher_livre()
    roman1.modifier_livre("Bocchi the Rock", "Aki Hamaji", "Doki", "978-3-7580-7075-2", "Seinen", "Gotou Hitori est une lycéenne qui a commencé à apprendre à jouer de la guitare parce qu'elle rêve de faire partie d'un groupe, mais elle est tellement timide qu'elle ne s'est pas fait un seul ami. Cependant, son rêve pourrait devenir réalité après avoir rencontré Ijichi Nijika, une fille qui joue de la batterie et cherche un nouveau guitariste pour son groupe.")
    roman1.afficher_livre()

def tkinter():

    app = App()
    app.mainloop()