from all_exo import *

def menu():
    while True:
        print("1. Type predifinis\n2. Surface d'un trapèze\n3. Somme et factorielle d'un nombre\n4. Arbre de noël\n5. math")
        print("6. Res(X, N)\n7. Suite\n8. Tierce\n9. Quitter")
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
            case 6:
                x = int(input("Entrer la valeur de x : "))
                N = int(input("Entrer la valeur de N : "))
                print(Res(x, N))
            case 7:
                value = int(input("Entrer la valeur de n : "))
                print(U(value))
                print(V(value))
            case 8:
                tierce()
            case 9:
                break
            case _:
                print("Choix invalide")
                