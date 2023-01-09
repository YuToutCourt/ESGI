"""Auteur: Yohann Maley"""

import sys

from all_exo import *


OPTIONS = ["Type predifinis", "Surface d'un trapèze", "Somme et factorielle d'un nombre", "Arbre de noël", 
            "math", "Res(X, N)", "Suite", "Tierce", "Quitter"]

def menu_windows():
    try:
        from consolemenu import SelectionMenu
    except ImportError:
        print(">> Veuillez installer les dépendances avec la commande 'pip install -r requirements.txt' <<")
        sys.exit()

    menu = SelectionMenu(OPTIONS[:len(OPTIONS) - 1])
    while True:
        menu.show()
        selected_option = menu.selected_option

        execute_function(selected_option)
        input("Appuyer sur une touche pour continuer...")



def menu_linux():
    try:
        from simple_term_menu import TerminalMenu
    except ImportError:
        print(">> Veuillez installer les dépendances avec la commande 'pip install -r requirements.txt' <<")
        sys.exit()

    menu = TerminalMenu(OPTIONS)
    while True:
        choix = menu.show()
        execute_function(choix)



def execute_function(choix:int):
    options = {
        0: type_predifinis,
        1: surface_trapeze,
        2: somme_facotrielle,
        3: arbre_noel,
        4: math_,
        5: lambda: Res(int(input("Entrer la valeur de x : ")), int(input("Entrer la valeur de N : "))),
        6: lambda: (print(U(int(input("Entrer la valeur de n : ")))), print(V(int(input("Entrer la valeur de n : "))))),
        7: tierce,
        8: sys.exit
    }
    try:
        options[choix]()
    except KeyError:
        print("Choix invalide")