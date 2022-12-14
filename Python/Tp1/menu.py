"""Auteur: Yohann Maley"""

import sys

from all_exo import *

class Menu:
    def __init__(self, options: list):
        """
        Initializes the Menu class with a list of options to be displayed in the menu.
        Also gets the operating system type.
        """
        self.os = sys.platform
        self.options = options
    
    def handle_menu_choice(self):
        """
        Handles menu choice, by calling the appropriate menu function based on the operating system.
        """
        if self.os == "win32":
            return self.menu_windows()
        else :
            return self.menu_linux()

    def show(self):
        """
        Display the menu by calling handle_menu_choice()
        """
        self.handle_menu_choice()

    def menu_windows(self):
        """
        Displays the menu for Windows systems using the consolemenu library.
        """
        try:
            from consolemenu import SelectionMenu
        except ImportError:
            print(">> Veuillez installer les dépendances avec la commande 'pip install -r requirements.txt' <<")
            sys.exit()

        menu = SelectionMenu(self.options[:len(self.options) - 1])
        while True:
            menu.show()
            selected_option = menu.selected_option

            self.execute_function(selected_option)
            input("Appuyer sur une touche pour continuer...")

    def menu_linux(self):
        """
        Displays the menu for Linux systems using the simple_term_menu library.
        """
        try:
            from simple_term_menu import TerminalMenu
        except ImportError:
            print(">> Veuillez installer les dépendances avec la commande 'pip install -r requirements.txt' <<")
            sys.exit()

        menu = TerminalMenu(self.options)
        while True:
            choix = menu.show()
            self.execute_function(choix)
    
    def execute_function(self, choix:int):
        """
        Executes function based on the user's choice
        """
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

        if options.get(choix) is not None:
            options[choix]()
