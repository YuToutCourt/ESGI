"""Auteur: Yohann Maley"""

from menu import Menu

if __name__ == "__main__":
    
    OPTIONS = ["Type predifinis", "Surface d'un trapèze", "Somme et factorielle d'un nombre", "Arbre de noël", 
            "math", "Res(X, N)", "Suite", "Tierce", "Quitter"]

    menu = Menu(OPTIONS)
    menu.show()