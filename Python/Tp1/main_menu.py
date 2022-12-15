
import sys
import importlib

from all_exo import *

__all__ = ["menu_windows", "menu_linux"]

OPTIONS = ["Type predifinis", "Surface d'un trapèze", "Somme et factorielle d'un nombre", "Arbre de noël", "math", "Res(X, N)", "Suite", "Tierce", "Quitter"]


def menu_windows():
    try:
        from consolemenu import SelectionMenu
    except ImportError:
        importlib.import_module('pip').main(['install', 'console-menu'])

    while True:
        menu = SelectionMenu(OPTIONS[:len(OPTIONS) - 1])

        menu.show()
        selected_option = menu.selected_option


        execute_function(selected_option)
        _ = input("Appuyer sur une touche pour continuer...")



def menu_linux():
    try:
        from simple_term_menu import TerminalMenu
    except ImportError:
        importlib.import_module('pip').main(['install', 'simple_term_menu'])

    menu = TerminalMenu(OPTIONS)
    while True:
        choix = menu.show()
        execute_function(choix)



def execute_function(choix:int):
    match choix:
        case 0:
            type_predifinis()
        case 1:
            surface_trapeze()
        case 2:
            somme_facotrielle()
        case 3:
            arbre_noel()
        case 4:
            math_()
        case 5:
            x = int(input("Entrer la valeur de x : "))
            N = int(input("Entrer la valeur de N : "))
            print(Res(x, N))
        case 6:
            value = int(input("Entrer la valeur de n : "))
            print(U(value))
            print(V(value))
        case 7:
            tierce()
        case 8:
            sys.exit()
        case _:
            print("Choix invalide")