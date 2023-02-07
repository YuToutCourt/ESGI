from menu.menu import Menu

def main():
    options = ["Calcul surface", "Jeu des allumettes", "Fichiers", "Livre", "Tkinter", "Quitter"]
    menu = Menu(options)
    menu.show()


if __name__ == "__main__":
    main()