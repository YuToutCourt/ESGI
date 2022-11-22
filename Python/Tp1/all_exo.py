import math

def type_predifinis():
    """
    Script permettant de rentrer 1 caractères et un entier
    Afficher la variables sous forme d'entiers et de caractères
    """

    while True:
        # Saisie des variables
        caractere = input("Entrer un caractère : ")
        entier = int(input("Entrer un entier : "))

        # Affichage des variables
        print(f'{caractere} vaut {ord(caractere)}')
        print(f'{entier} vaut {chr(entier)}')

        if input("Voulez-vous continuer ? (o/n) : ") == 'n':
            break


def surface_trapeze():
    """
    Script permettant de calculer la surface d'un trapèze
    """
    
    # Saisie des variables
    a = int(input("Entrer la longueur du côté a : "))
    b = int(input("Entrer la longueur du côté b : "))
    h = int(input("Entrer la hauteur h : "))

    # Calcul de la surface
    surface = (a + b) * h * 0.5

    # Affichage de la surface
    print(f"La surface du trapèze est de {surface} m")


def somme_facotrielle():
    """
    Script permettant de calculer la somme et la factorielle d'un nombre
    """

    while True:

        number = int(input("Entrer un entier positif : "))

        somme, factorielle = 0, 1
        number_used_in_str = []

        # Calcul de la somme et de la factorielle
        for i in range(1, number + 1):
            somme += i
            factorielle *= i
            number_used_in_str.append(str(i))

        # Affichage de la somme
        print(" + ".join(number_used_in_str), "=", somme)
        print(somme, "=", " + ".join(number_used_in_str))

        # Affichage de la factorielle
        print(" * ".join(number_used_in_str), "=", factorielle)
        print(factorielle, "=", " * ".join(number_used_in_str))

        if input("Voulez-vous continuer ? (o/n) : ") == 'n':
            break

def arbre_noel():
    """
    Script permettant de dessiner un arbre de noël
    """

    # Saisie de la hauteur de l'arbre
    hauteur = int(input("Hauteur de l'arbre : "))

    # Dessin de l'arbre entouré de =
    for i in range(hauteur):
        print(f"{'=' * (hauteur - i)}{'*' * (2 * i + 1)}{'=' * (hauteur - i)}")

    # Dessin de la base de l'arbre
    print("="*hauteur + "*" + "="*hauteur)
    print("="*(hauteur-1) + "***" + "="*(hauteur-1))



def math_():
    """
    Script permettant de saisir un entier au clavier et d'afficher :
        • logarithme népérien de l’entier
        • sinus de l’entier
        • cosinus de l’entier
    """
    entier = int(input("Entrer un entier : "))

    print(f"log({entier}) = {math.log(entier)}")
    print(f"sin({entier}) = {math.sin(entier)}")
    print(f"cos({entier}) = {math.cos(entier)}")


def res(x:int, n:int):
    """
    J'ai pas compris faut faire quoi
    """