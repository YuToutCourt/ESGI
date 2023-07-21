"""
Author:  Yohann MALEY
Date:    21-07-2023
ESGI 3
"""
from Livre import Livre
from Magazine import Magazine
from Bibliotheque import Bibliotheque
from user import User

if __name__ == '__main__':
    
    # Création de la liste de livre
    liste_livres = []
    liste_livres.append(Livre("L'art de la guerre", "Sun Tzu", "978-2253139815"))
    liste_livres.append(Livre("Le Seigneur des anneaux", "J. R. R. Tolkien", "978-2266282390"))
    liste_livres.append(Livre("Le Trône de fer", "George R. R. Martin", "978-2290002582"))
    liste_livres.append(Livre("Le Nom du vent", "Patrick Rothfuss", "978-2290013311"))

    # Création de la liste de magazine
    liste_magazine = []
    liste_magazine.append(Magazine("Le Point", 2424, "21/07/2023"))
    liste_magazine.append(Magazine("Le Point", 2425, "28/07/2023"))
    liste_magazine.append(Magazine("Le Point", 2426, "04/08/2023"))
    liste_magazine.append(Magazine("Le Point", 2427, "11/08/2023"))

    # Création de la bibliothèque
    bibliotheque = Bibliotheque("Bibliothèque de Paris", liste_livres, liste_magazine)

    # Création de la liste d'utilisateur
    liste_utilisateur = []
    liste_utilisateur.append(User("MALEY", "Yohann", [], []))
    liste_utilisateur.append(User("DUPONT", "Jean", [], []))
    liste_utilisateur.append(User("DURAND", "Pierre", [], []))

    # Affichage des livres disponibles
    print("Livres disponibles:")
    for livre in bibliotheque.livre_disponible():
        print(livre.titre, livre.auteur, livre.isbn)

    # Affichage des magazines disponibles
    print("Magazines disponibles:")
    for magazine in bibliotheque.magazine_disponible():
        print(magazine.titre, magazine.numero, magazine.date)

    print("L'utilisateur 1 emprunte un livre et un magazine")    
    # L'utilisateur 1 emprunte un livre
    liste_utilisateur[0].emprunter_livre(bibliotheque.chercher_livre(titre="Le Trône de fer"), bibliotheque)
    # L'utilisateur 1 emprunte un magazine
    liste_utilisateur[0].emprunter_magazine(bibliotheque.chercher_magazine(titre="Le Point"), bibliotheque)


    # Affichage des livres et magazines empruntés par l'utilisateur 1
    print("Livres empruntés par l'utilisateur 1:")
    liste_utilisateur[0].affiche_livre_emprunter()
    print("Magazines empruntés par l'utilisateur 1:")
    liste_utilisateur[0].affiche_magazine_emprunter()


    # Affichage des livres disponibles
    print("Livres disponibles:")
    for livre in bibliotheque.livre_disponible():
        print(livre.titre, livre.auteur, livre.isbn)

    # Affichage des magazines disponibles
    print("Magazines disponibles:")
    for magazine in bibliotheque.magazine_disponible():
        print(magazine.titre, magazine.numero, magazine.date)

    print("L'utilisateur 1 retourne un livre et un magazine")
    # L'utilisateur 1 retourne un livre
    liste_utilisateur[0].retour_livre(liste_utilisateur[0].livre_emprunter[0], bibliotheque)
    # L'utilisateur 1 retourne un magazine
    liste_utilisateur[0].retour_magazine(liste_utilisateur[0].magazine_emprunter[0], bibliotheque)  

    # Affichage des livres disponibles
    print("Livres disponibles:")
    for livre in bibliotheque.livre_disponible():
        print(livre.titre, livre.auteur, livre.isbn)

    # Affichage des magazines disponibles
    print("Magazines disponibles:")
    for magazine in bibliotheque.magazine_disponible():
        print(magazine.titre, magazine.numero, magazine.date)