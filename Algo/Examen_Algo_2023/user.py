from Bibliotheque import Bibliotheque
from Livre import Livre
from Magazine import Magazine

class User:
    def __init__(self, nom:str, prenom:str, livre_emprunter:list[Livre], magazine_emprunter:list[Magazine]):
        self.nom = nom
        self.prenom = prenom
        self.livre_emprunter = livre_emprunter
        self.magazine_emprunter = magazine_emprunter

    def retour_livre(self, livre:Livre, bibliotheque:Bibliotheque):
        for livre_emprunter in self.livre_emprunter:
            if livre_emprunter == livre:
                self.livre_emprunter.remove(livre)
                bibliotheque.ajouter_livre(livre)
                break
        

    def retour_magazine(self, magazine:Magazine, bibliotheque:Bibliotheque):
        for magazine_emprunter in self.magazine_emprunter:
            if magazine_emprunter == magazine:
                self.magazine_emprunter.remove(magazine)
                bibliotheque.ajouter_magazine(magazine)
                break

    def emprunter_livre(self, livre:Livre, bibliotheque:Bibliotheque):
        self.livre_emprunter.append(livre)
        bibliotheque.emprunter_livre(livre)

    def emprunter_magazine(self, magazine:Magazine, bibliotheque:Bibliotheque):
        self.magazine_emprunter.append(magazine)
        bibliotheque.emprunter_magazine(magazine)

    def affiche_livre_emprunter(self):
        for livre in self.livre_emprunter:
            print(livre.titre, livre.auteur, livre.isbn)

    def affiche_magazine_emprunter(self):
        for magazine in self.magazine_emprunter:
            print(magazine.titre, magazine.numero, magazine.date)