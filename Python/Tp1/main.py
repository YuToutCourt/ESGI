import platform

from menu import menu_windows, menu_linux

if __name__ == "__main__":
    
    # On vérifie le système d'exploitation pour afficher le menu correspondant
    if platform.system() == 'Windows':
        menu_windows()
    else:
        menu_linux()