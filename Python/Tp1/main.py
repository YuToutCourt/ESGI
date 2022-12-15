import platform

from main_menu import *


if __name__ == "__main__":
    
    if platform.system() == 'Windows':
        menu_windows()
    else:
        menu_linux()