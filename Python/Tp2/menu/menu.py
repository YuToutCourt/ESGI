"""Auteur: Yohann Maley"""

import sys

from exo.all_exo import *

class Menu:
    def __init__(self, options: list):
        """
        Initializes the Menu class with a list of options to be displayed in the menu.
        Also gets the operating system type.
        """
        self.__os = sys.platform
        self.__options = options

    def __get_os(self):
        return self.__os

    def __get_options(self):
        return self.__options
    
    def __handle_menu_choice(self):
        """
        Handles menu choice, by calling the appropriate menu function based on the operating system.
        """
        if self.__get_os() == "win32":
            return self.__menu_windows()
        else :
            return self.__menu_linux()

    def show(self):
        """
        Display the menu by calling handle_menu_choice()
        """
        self.__handle_menu_choice()

    def __menu_windows(self):
        """
        Displays the menu for Windows systems using the consolemenu library.
        """
        try:
            from consolemenu import SelectionMenu
        except ImportError:
            print(">> Veuillez installer les dépendances avec la commande 'pip install -r requirements.txt' <<")
            sys.exit()

        menu = SelectionMenu(self.__get_options()[:len(self.__get_options()) - 1])
        while True:
            menu.show()
            selected_option = menu.selected_option

            self.__execute_function(selected_option)
            input("Appuyer sur une touche pour continuer...")

    def __menu_linux(self):
        """
        Displays the menu for Linux systems using the simple_term_menu library.
        """
        try:
            from simple_term_menu import TerminalMenu
        except ImportError:
            print(">> Veuillez installer les dépendances avec la commande 'pip install -r requirements.txt' <<")
            sys.exit()

        menu = TerminalMenu(self.__options)
        while True:
            choix = menu.show()
            self.__execute_function(choix)
    
    def __execute_function(self, choix:int):
        """
        Executes function based on the user's choice
        """
        options = {
            0: calcul_surface,
            1: jeu_allumettes,
            2: fichiers,
            3: livre,
            4: tkinter,
            5: sys.exit
        }

        if options.get(choix) is not None:
            options[choix]()