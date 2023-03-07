"""Auteur: Yohann Maley"""

from menu.menu import Menu

def main():
    options = ("", "Quitter")
    menu = Menu(options)
    menu.show()


if __name__ == "__main__":
    main()