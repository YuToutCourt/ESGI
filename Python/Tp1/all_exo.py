"""Auteur: Yohann Maley"""

import matplotlib.pyplot as plt

from math import factorial, log, sin, cos


# Define a list of public function of that module, available by import *
__all__ = ["type_predifinis", "surface_trapeze", "somme_facotrielle", "arbre_noel", "math_", "Res", "U", "V", "tierce"]

def type_predifinis():
    """
    Script permettant de rentrer 1 caractères et un entier
    Afficher la variables sous forme d'entiers et de caractères
    """

    while True:
        # Saisie des variables
        caractere = input("Entrer un caractère : ")

        if not caractere.isalpha() or len(caractere) > 1:
            print("Erreur, vous n'avez pas entré un caractère")
            continue
        
        entier = input("Entrer un entier : ")
        if not entier.isdigit():
            print("Erreur, vous n'avez pas entré un entier")
            continue 

        entier = int(entier)

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
    a = input("Entrer la longueur du côté a : ")
    b = input("Entrer la longueur du côté b : ")
    h = input("Entrer la hauteur h : ")

    if not all([a.isdigit(), b.isdigit(), h.isdigit()]):
        print("Erreur, vous n'avez pas entré un entier")
        return

    a, b, h = int(a), int(b), int(h)

    # Calcul de la surface
    surface = (a + b) * h * 0.5

    # Affichage de la surface
    print(f"La surface du trapèze est de {surface} m")

    points = [[0, 0], [a/3, h], [(a+2)/3, h], [a, 0], [(a+2)/3, 0], [(a+2)/3, h], [(a+2)/3, 0], [a/3, 0], [a/3, h], [a/3, 0], [0, 0]]

    plt.plot(*zip(*points))
    plt.show()

def somme_facotrielle():
    """
    Script permettant de calculer la somme et la factorielle d'un nombre
    """

    while True:

        number = input("Entrer un entier positif : ")

        if not number.isdigit():
            print("Erreur, vous n'avez pas entré un entier")
            continue

        number = int(number)

        somme, factorielle = 0, factorial(number)
        number_used_in_str = []

        # Un autre moyen de faire la somme et la factorielle mais on utilise sum() et listcomprehension ce qui nous 
        # fait boucler 2 fois sur la liste des nombres, ce qui n'est pas très optimisé :)
        
        # somme = sum(range(1, number + 1))
        # factorielle = math.factorial(number)
        # numbers_used_in_str = [str(i) for i in range(1, number + 1)]
        
        # Calcul de la somme et de la factorielle
        for i in range(1, number + 1):
            somme += i
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
    hauteur = input("Hauteur de l'arbre : ")

    if not hauteur.isdigit():
        print("Erreur, vous n'avez pas entré un entier")
        return

    hauteur = int(hauteur)

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
    entier = input("Entrer un entier : ")

    if not entier.isdigit():
        print("Erreur, vous n'avez pas entré un entier")
        return

    print(f"log({entier}) = {log(entier)}")
    print(f"sin({entier}) = {sin(entier)}")
    print(f"cos({entier}) = {cos(entier)}")


def f1(x: float, n: int) -> float:
    """
    Calcul de la fonction f1(x,n) = x^n / n!
    :param x: float
    :param n: int

    :return: float
    """
    return x ** n / factorial(n)

def Res(x: float, N: int) -> float:
    """
    Calcul de la somme de f1(x,n) pour n allant de 1 à N
    :param x: float
    :param N: int

    :return: float
    """
    # formule mathématique pour la somme de la suite géométrique de raison x et de premier terme 1/0!
    return (1 - x**(N+1)) / (1 - x)
    # return sum(f1(x, n) for n in range(1, N+1)) Solution pas optimisée

def U(n: int) -> float:
    """
    Calcul de la suite U
    :param n: int

    :return: float
    """
    somme = 1
    fact = 1
    for i in range(1, n+1):
        fact *= i
        somme += 1/fact
    return somme

def V(n: int) -> float:
    """
    Calcul de la suite V
    :param n: int

    :return: float
    """
    return sum(1/factorial(i) for i in range(1,n+1))+1/(n*factorial(n))


def tierce():
    """
    Calcul de la probabilité de gagner au tiercé, quarté, quinté...
    """
    # Demande du nombre de chevaux partants et de chevaux joués à l'utilisateur
    n = input("Nombre de chevaux partants : ")
    p = input("Nombre de chevaux joués : ")

    if not all([n.isdigit(), p.isdigit()]):
        print("Erreur, vous n'avez pas entré un entier")
        return

    n, p = int(n), int(p)

    n, np = factorial(n), factorial(n-p)

    X =  n // np
    Y =  n // (factorial(p) *  np)
    
    # Affichage des chances de gagner
    print(f"Une chance sur {int(X)} de gagner dans l'ordre")
    print(f"Une chance sur {int(Y)} de gagner dans le désordre")