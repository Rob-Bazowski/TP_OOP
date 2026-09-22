"""Exercice 3 - De la fonction à la classe Habitant"""

# Question 1

class Habitant:
    """Classe Habitant contenant le nom, l'âge, l'adresse et les animaux d'un habitant"""

    def __init__(self, nom, age, adresse, animaux = None):
        self.nom = nom
        self.age = age
        self.adresse = adresse
        if animaux is not None:
            self.animaux = animaux
        else:
            self.animaux = {}
