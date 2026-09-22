"""Exercice 3 - De la fonction à la classe Habitant / Exercice 4 - Encapsulation 
/ Exercice 6 - Surcharge du constructeur / Exercice 7 - Héritage : Adulte et Enfant"""

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
        if self.__age > 62:
            return 0
        else:
            62 - self.__age

@dispatch(Habitant, str)
def set_info(habitant, nom):
    habitant.set_nom(nom)

@dispatch(Habitant, str, int)
def set_info(habitant, nom, age):
    habitant.set_nom(nom)
    habitant.set_age(age)

try:
    h1 = Habitant("Jean", 12, "Boulevard McDonald", {})
except TypeError:
    pass