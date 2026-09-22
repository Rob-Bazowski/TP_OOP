"""Exercice 3 - De la fonction à la classe Habitant / Exercice 4 - Encapsulation 
/ Exercice 6 - Surcharge du constructeur / Exercice 7 - Héritage : Adulte et Enfant
/ Exercice 8 - Polymorphisme"""

from multipledispatch import dispatch
from abc import ABC, abstractmethod

class Habitant (ABC):
    """Classe Habitant contenant le nom, l'âge, l'adresse et les animaux d'un habitant"""

    def __init__(self, nom, age, adresse, animaux = None):
        self.__nom = nom
        self.__age = age
        self.__adresse = adresse
        if animaux is not None:
            self.__animaux = animaux
        else:
            self.__animaux = {}

    @property
    def age(self):
        return self.__age 

    @age.setter
    def age(self, age):
        if age < 0 or 130 < age:
            raise ValueError("L'âge doit être compris entre 0 et 130")
        self.__age = age

    def get_nom(self):
        return self.__nom

    def get_age(self):
        return self.__age

    def get_adresse(self):
        return self.__adresse

    def set_nom(self, nom):
        self.__nom = nom

    def set_age(self, age):
        self.__age = age

    def set_adresse(self, adresse):
        self.__adresse = adresse

    def set_animaux(self, animaux):
        self.__animaux = animaux

    def affichage_adresse(self):
        """Affiche l'adresse d'un habitant"""
        print(f"{self.__nom} habite a {self.__adresse}")

    def compte_animal(self, animal):
        """Compte le nombre le compte d'un certain animal qu'a un habitant"""
        if animal in self.__animaux.keys():
            return self.__animaux[animal]
        return 0

    @abstractmethod
    def calcul_annee_avant_retraite(self):
        pass

    def __str__(self):
        return f"{self.__nom}, {self.__age}, habite a {self.__adresse} possède {self.__animaux}"

class Adulte(Habitant):
    """Classe habitant adulte"""

    def __init__(self, nom, age, adresse, animaux = None):
        if age >= 18:
            super().__init__(nom, age, adresse, animaux)
        else:
            raise ValueError("Un adulte ne peut pas avoir moins de 18 ans.")

    def calcul_annee_avant_retraite(self):
        """Calcule le nombre d'année avant la retraite si l'habitant n'est pas déjà à la retraite"""
        if self.age >= 62:
            return "Déjà à la retraite"
        else:
            return 62 - self.age

class Enfant(Habitant):
    """Classe habitant enfant"""

    def __init__(self, nom, age, adresse, animaux = None):
        if age < 18:
            super().__init__(nom, age, adresse, animaux)
        else:
            raise ValueError("Un enfant ne peut pas avoir plus de 18 ans.")

    def calcul_annee_avant_retraite(self):
        """Ne calcule pas le nombre d'année avant la retraite"""
        return "Un enfant ne peut pas calculer sa retraite"

@dispatch(Habitant, str)
def set_info(habitant, nom):
    habitant.set_nom(nom)

@dispatch(Habitant, str, int)
def set_info(habitant, nom, age):
    habitant.set_nom(nom)
    habitant.set_age(age)

def affichage(h: Habitant):
    print(h)

try:
    h1 = Habitant("Jean", 12, "Boulevard McDonald", {})
except TypeError:
    pass

adulte = Adulte("Marie", 35, "Rue A")
enfant = Enfant("Lucas", 12, "Rue B")
assert isinstance(adulte, Habitant)
assert adulte.calcul_annee_avant_retraite() == 27
assert "enfant" in enfant.calcul_annee_avant_retraite()
try:
    Enfant("Oups", 25, "Rue C")
    assert False, "une ValueError aurait du etre levee"
except ValueError:
    pass

print("Fonction print :")
print(adulte)
print("Fonction affichage :")
affichage(adulte)
affichage(enfant)