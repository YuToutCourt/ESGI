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

    S = 0
    L = a
    while L < b:
        S = S + L * L * p
        L = L + p

    S = 0
    L = a
    while L-p >= a:
        S = p*()
    # TODO : demander au prof j'ai pas compris


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
            print(f"{'|'*nb_allumettes} L'ordinateur enlève {nb_remove} allumettes")
        else:
            nb_remove = int(input("Combien d'allumettes prenez-vous ? "))
            if nb_remove > 3 or nb_remove < 1:
                print("Vous devez prendre entre 1 et 3 allumettes")
            
            print(f"{'|'*nb_allumettes} {pseudo} enlève {nb_remove} allumettes")

        nb_allumettes = nb_allumettes - nb_remove
        turn += 1

        
