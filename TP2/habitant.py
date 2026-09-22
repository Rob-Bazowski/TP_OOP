"""Exercice 3 - De la fonction à la classe Habitant / Exercice 4 - Encapsulation"""

class Habitant:
    """Classe Habitant contenant le nom, l'âge, l'adresse et les animaux d'un habitant"""

    def __init__(self, nom, age, adresse, animaux = None):
        self.__nom = nom
        self.__age = age
        self.__adresse = adresse
        if animaux is not None:
            self.__animaux = animaux
        else:
            self.__animaux = {}

    def get_nom(self):
        return self.__nom

    def get_age(self):
        return self.__age

    def get_adresse(self):
        return self.__adresse
    
    def get_animaux(self):
        return self.__animaux

    def set_age(self, age):
        self.__age = age

    def set_adresse(self, adresse):
        self.__adresse = adresse

    def set_animaux(self, animaux):
        self.__animaux = animaux

    def affichage_adresse(self):
        """Affiche l'adresse d'un habitant"""
        print(f"{self.__nom} habite a Rue {self.__adresse}")

    def compte_animal(self, animal):
        """Compte le nombre le compte d'un certain animal qu'a un habitant"""
        if animal in self.__animaux.keys():
            return self.__animaux[animal]
        return 0

h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})
assert h1.get_nom() == "Aldric"
assert h1.compte_animal("vaches") == 3
assert h1.compte_animal("moutons") == 0
h1.affichage_adresse() # affiche "Aldric habite a Rue A"
