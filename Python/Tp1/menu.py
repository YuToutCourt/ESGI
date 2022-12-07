from all_exo import *

def menu():
    print("1. Type predifinis\n2. Surface d'un trapèze\n3. Somme et factorielle d'un nombre\n4. Arbre de noël\n5. math\n6. Quitter")
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
            