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

# Question 2

    def affichage_adresse(self):
        """Affiche l'adresse d'un habitant"""
        print(f"{self.nom} habite a Rue {self.adresse}")

    def compte_animal(self, animal):
        """Compte le nombre le compte d'un certain animal qu'a un habitant"""
        if animal in self.animaux.keys():
            return self.animaux[animal]
        return 0

h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})
assert h1.nom == "Aldric"
assert h1.compte_animal("vaches") == 3
assert h1.compte_animal("moutons") == 0
h1.affichage_adresse() # affiche "Aldric habite a Rue A"
