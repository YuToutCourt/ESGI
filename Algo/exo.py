"""
Author:  Yohann MALEY
Date:    06-03-2022
ESGI 3
"""

def exo_1(chaine: str):
    """Retourne la chaine inversée"""
    return chaine[::-1]

def exo_2(chaine: str):
    """Retourne True si la chaine est trié dans l'ordre alphabétique, False sinon"""
    return sorted(list(chaine)) == list(chaine)

def exo_3(chaine: str):
    """Retourne le nombre de mots"""
    return len(chaine.split(" "))

def exo_4(chaine :str):
    """Retourne le nombre de majuscules et de minuscules"""
    return len([c for c in chaine if c.isupper()]), len([c for c in chaine if c.islower()])

def exo_5(chaine:str):
    """Retourne la chaine sans les caractères spéciaux"""
    return "".join(c for c in chaine if c.isalnum() or c == ' ')
    
def exo_6(chaine: str, n: int):
    """Retourne la chaine avec chaque caractère répété n fois"""
    return "".join(c*n for c in chaine)

def exo_7(nombre: int):
    """Retourne la somme des nombres impairs jusqu'à nombre"""
    if nombre % 2 == 0 : return "Le nombre doit être impair"
    return sum(i for i in range(1, nombre+1, 2))
    
def exo_8(nombre :int):
    """Retourne tout les nombres pairs jusqu'à nombre"""
    return [i for i in range(1, nombre+1) if i % 2 == 0]

def exo_9(chaine :str):
    """Retourne True si la chaine est un palindrome, False sinon"""
    return chaine == chaine[::-1]

def exo_10(chaine1: str, chaine2: str):
    """La distance de Hamming"""
    if len(chaine1) != len(chaine2): return "Les chaines doivent être de même taille"
    return sum(1 for i in range(len(chaine1)) if chaine1[i] != chaine2[i])
    

if __name__ == "__main__":
    print(exo_1("Hello World"))
    print(exo_2("abc"))
    print(exo_3("Hello World"))
    print(exo_4("Hello World"))
    print(exo_5("Hello World"))
    print(exo_6("Hello World", 2))
    print(exo_7(9))
    print(exo_8(10))
    print(exo_9("KAYAK"))
    print(exo_10("Hello Wzrld", "Hallo World"))