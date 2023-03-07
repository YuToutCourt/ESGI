"""Auteur: Yohann Maley"""


def input_char():
    """
    Fonction pour choisir un caractère avec gestion d'erreur
    :return: str, Le caractère choisi
    """
    letter = input("Choisissez un caractère : ")
    while len(letter) > 1 or len(letter) == 0:
        print("Vous devez choisir un seul caractère !")
        letter = input("Choisissez un caractère : ")
    return letter

def input_float(txt, min_val, max_val):
    """
    Fonction pour choisir un nombre positif floatant avec une gestion d'erreur
    :param txt: int, Le texte à afficher
    :param min_val: int, La valeur minimale
    :param max_val: int, La valeur maximale

    :return: flaot, Le nombre choisi
    """
    while True:
        number = input(txt)
        if number.isdigit() == False:
            print("Vous devez choisir un nombre positif !")
            continue
        
        # Vérifiez si le nombre est dans la plage spécifiée
        if min_val <= number <= max_val:
            return float(number)
        elif number < min_val:
            print(f"Vous devez choisir un nombre supérieur à {min_val}")
        else:
            print(f"Vous devez choisir un nombre inférieur à {max_val}")

def input_int(txt, min_val, max_val):
    """
    Fonction pour choisir un nombre positif avec une gestion d'erreur
    :param txt: int, Le texte à afficher
    :param min_val: int, La valeur minimale
    :param max_val: int, La valeur maximale

    :return: int, Le nombre choisi
    """
    while True:
        number = input(txt)
        if number.isdigit() == False:
            print("Vous devez choisir un nombre positif !")
            continue
        
        # Vérifiez si le nombre est dans la plage spécifiée
        if min_val <= number <= max_val:
            return int(number)
        elif number < min_val:
            print(f"Vous devez choisir un nombre supérieur à {min_val}")
        else:
            print(f"Vous devez choisir un nombre inférieur à {max_val}")
