"""Exercice 9 - Tests unitaires"""

import unittest
from habitant import Adulte, Enfant
from village import Village

# Question 1

dicitonnaire_test = {"Vaches" : 10000, "Renards" : 1, "Cochons" : 2}
habitant_test = Adulte("Jean-Édouard", 56, "Rue du Faubourg Saint-Honoré", dicitonnaire_test)

class TestHabitant(unittest.TestCase):
    """Tests pour la classe Habitant et l'encapsulation"""

    def test_age_settler_valide(self):
        """Test du settler, cas usuel"""
        habitant_test.age = 55
        self.assertEqual(habitant_test.age, 55)

    def test_age_settler_invalide(self):
        """Test du settler, cas limite"""
        try:
            habitant_test.age = -17
            assert False, "Une ValueError aurait dû être levée"
        except ValueError:
            pass

    def test_compte_animal_usuel(self):
        """Test compte_animal, cas usuel"""
        compte = habitant_test.compte_animal("Vaches")
        self.assertEqual(compte, 10000)

    def test_compte_animal_limite(self):
        """Test compte_animal, cas limite"""
        compte = habitant_test.compte_animal("Licornes")
        self.assertEqual(compte, 0)

# Question 2
adulte1 = Adulte("Bob", 21, "Parvis de Notre-Dame", {})
adulte2 = Adulte("Napoléon", 34, "Rue de la Gare", {"Cochons" : 1, "Cheveaux" : 15})
village_test_composition = Village("Y")
village_test_agregation = Village("Saint-Remy-en-Bouzemont-Saint-Genest-et-Isson")
village_test_limite1 = Village("La Chapelle-Palluau")
village_test_limite2 = Village("Paris")

class TestVillage(unittest.TestCase):
    """Tests pour la classe Village"""

    def test_ajout_composition(self):
        """Test ajouter_habitant_composition, cas usuel"""
        village_test_composition.ajouter_habitant_composition("Victor", 21, "Rue Victor Hugo", {})
        nom = village_test_composition.get_habitants()[0].get_nom()
        self.assertEqual(nom, "Victor")
        age = village_test_composition.get_habitants()[0].get_age()
        self.assertEqual(age, 21)
        adresse = village_test_composition.get_habitants()[0].get_adresse()
        self.assertEqual(adresse, "Rue Victor Hugo")
        animaux = village_test_composition.get_habitants()[0].get_animaux()
        self.assertEqual(animaux, {})

    def test_ajout_agregation(self):
        """Test ajouter_habitant_composition, cas usuel"""
        village_test_agregation.ajouter_habitant_agregation(adulte2)
        nom = village_test_agregation.get_habitants()[0].get_nom()
        self.assertEqual(nom, "Napoléon")
        age = village_test_agregation.get_habitants()[0].get_age()
        self.assertEqual(age, 34)
        adresse = village_test_agregation.get_habitants()[0].get_adresse()
        self.assertEqual(adresse, "Rue de la Gare")
        animaux = village_test_agregation.get_habitants()[0].get_animaux()
        self.assertEqual(animaux, {"Cochons" : 1, "Cheveaux" : 15})

    def test_ajouter_limite(self):
        """Test ajouter_habitant_composition et ajouter_habitant_agregation, cas limite"""
        village_test_limite1.ajouter_habitant_agregation(adulte1)
        village_test_limite2.ajouter_habitant_composition("Bob", 21, "Parvis de Notre-Dame", {})
        nom1 = village_test_limite1.get_habitants()[0].get_nom()
        nom2 = village_test_limite2.get_habitants()[0].get_nom()
        self.assertEqual(nom1, nom2)
        age1 = village_test_limite1.get_habitants()[0].get_age()
        age2 = village_test_limite2.get_habitants()[0].get_age()
        self.assertEqual(age1, age2)
        adresse1 = village_test_limite1.get_habitants()[0].get_adresse()
        adresse2 = village_test_limite2.get_habitants()[0].get_adresse()
        self.assertEqual(adresse1, adresse2)
        animaux1 = village_test_limite1.get_habitants()[0].get_animaux()
        animaux2 = village_test_limite2.get_habitants()[0].get_animaux()
        self.assertEqual(animaux1, animaux2)

# Question 3

enfant_test = Enfant("Baptiste", 12, "Roubaix", {"Chiens" : 0})

class TestHeritage(unittest.TestCase):
    """Test pour les classes Enfant et Adulte"""

    def test_creation_enfant(self):
        """Test de la création d'un enfant, limite"""
        try:
            Enfant("Sébastien", 20, "Rue A")
            assert False, "Une ValueError aurait dû être levée"
        except ValueError:
            pass

    def test_retraite_usuel(self):
        """Test de calcul_anne_avant_retraite"""
        resultat = adulte1.calcul_annee_avant_retraite()
        self.assertEqual(resultat, 41)

    def test_retraite_limite(self):
        """Test de calcul_anne_avant_retraite"""
        resultat = adulte2.calcul_annee_avant_retraite()
        self.assertEqual(resultat, "Un enfant ne peut pas calculer sa retraite")



if __name__ == "__main__":
    unittest.main(verbosity = 2)
