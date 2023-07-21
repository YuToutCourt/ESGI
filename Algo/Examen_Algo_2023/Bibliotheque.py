from Livre import Livre
from Magazine import Magazine

class Bibliotheque:
    def __init__(self, nom, liste_livres:list[Livre], liste_magazine:list[Magazine]):
        self.nom = nom
        self.liste_livres = liste_livres
        self.liste_magazine = liste_magazine

    def ajouter_livre(self, livre:Livre):
        self.liste_livres.append(livre)

    def ajouter_magazine(self, magazine:Magazine):
        self.liste_magazine.append(magazine)

    def livre_disponible(self):
        return self.liste_livres
    
    def magazine_disponible(self):
        return self.liste_magazine
    
    def emprunter_livre(self, livre:Livre):
        self.liste_livres.remove(livre)

    def emprunter_magazine(self, magazine:Magazine):
        self.liste_magazine.remove(magazine)

    def chercher_livre(self, titre=None, auteur=None):
        for livre in self.liste_livres:
            if titre == livre.titre or auteur == livre.auteur:
                return livre
        return None
    
    def chercher_magazine(self, titre=None, numero=None):
        for magazine in self.liste_magazine:
            if titre == magazine.titre or numero == magazine.numero:
                return magazine
        return None