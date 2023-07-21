<!-- 
Author:  Yohann MALEY
Date:    21-07-2023
ESGI 3 -->

# Partie 1 : Questions à réponse courte (30 minutes)
## Question 1
###  Qu'est-ce qu'une structure de données ? Pourquoi est-ce important dans la programmation ?

Une structure de données est une manière d'organiser des données de façon à pouvoir les utiliser efficacement.
Il y a différentes structures de données, chacune ayant ses avantages et ses inconvénients. Il est donc super important de choisir la bonne structure de données pour le problème que l'on veut résoudre.

Liste des structures de données :
- Tableaux
- Listes chaînées
- Piles
- Files
- Arbres
- Graphes
- Tables de hachage

## Question 2
### Qu'est-ce qu'une boucle en programmation ? Expliquez la différence entre les boucles "for" et "while"

Une boucle est une structure de contrôle qui permet de répéter une ou plusieurs instructions un certain nombre de fois.

La boucle "for" est utilisée quand on sait à l'avance combien de fois on veut répéter les instructions. La boucle "while" est utilisée quand on ne sait pas à l'avance combien de fois on veut répéter les instructions.

## Question 3
### Qu'est-ce qu'une fonction en programmation ? Pourquoi les utilise-t-on ?

Une fonction est un bloc d'instructions qui peut être appelé plusieurs fois dans un programme. On utilise les fonctions pour éviter de répéter du code. Il est possible de passer des paramètres à une fonction pour que le résultat soit différent en fonction des paramètres.

## Question 4
### Qu'est-ce que la récursivité en programmation ? Pouvez-vous donner un exemple d'une fonction récursive ?

La récursivité est une technique de programmation qui consiste à appeler une fonction depuis elle-même. Il faut faire attention à ne pas créer une boucle infinie. Donc bien vérifier qu'il y a une condition d'arrêt.

Exemple de fonction récursive :
```py
def factorielle(n):
    return 1 if n == 0 else n * factorielle(n-1)
    # if n == 0:
    #     return 1
    # else:
    #     return n * factorielle(n-1)
```
Ouai j'aime bien faire des one-liners 🙂

## Question 5
### Qu'est-ce que l'héritage en programmation orientée objet ? Pouvez-vous donner un exemple ?

L'héritage en POO permet de créer une classe à partir d'une autre classe. La classe qui est héritée est appelée la classe superclasse. La classe qui hérite est appelée la classe sous-classe. Cela permet de réutiliser le code de la superclasse dans la sous-classe et de faire du polymorphisme.

Exemple :
```py
class Animal:
    def __init__(self, nom):
        self.nom = nom

    def parler(self):
        print("Je suis un animal")

class Chien(Animal):
    def __init__(self, nom):
        super().__init__(nom)

    def parler(self):
        print("Wouf !")

class Chat(Animal):
    def __init__(self, nom):
        super().__init__(nom)

    def parler(self):
        print("Miaou !")
```

