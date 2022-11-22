from all_exo import *

def menu():
    choix = int(input("Choisissez une option : "))
    match choix:
        case 1:
            type_predifinis()
        case 2:
            surface_trapeze()
        case 3:
            somme_facotrielle()
        case 4:
            arbre_noel()
        case 5:
            math_()
        case _:
            print("Choix invalide")
            