import unittest
from habitant import Adulte
from village import Village

# Question 1

habitant_test = Adulte("Jean-Édouard", 56, "Rue du Faubourg Saint-Honoré", {"Vaches" : 10000, "Renards" : 1, "Cochons" : 2})

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
        self.assertEqual(village_test_composition.get_habitants()[0].get_nom(), "Victor")
        self.assertEqual(village_test_composition.get_habitants()[0].get_age(), 21)
        self.assertEqual(village_test_composition.get_habitants()[0].get_adresse(), "Rue Victor Hugo")
        self.assertEqual(village_test_composition.get_habitants()[0].get_animaux(), {})

    def test_ajout_agregation(self):
        """Test ajouter_habitant_composition, cas usuel"""
        village_test_agregation.ajouter_habitant_agregation(adulte2)
        self.assertEqual(village_test_agregation.get_habitants()[0].get_nom(), "Napoléon")
        self.assertEqual(village_test_agregation.get_habitants()[0].get_age(), 34)
        self.assertEqual(village_test_agregation.get_habitants()[0].get_adresse(), "Rue de la Gare")
        self.assertEqual(village_test_agregation.get_habitants()[0].get_animaux(), {"Cochons" : 1, "Cheveaux" : 15})
        
    def test_ajouter_limite(self):
        village_test_limite1.ajouter_habitant_agregation(adulte1)
        village_test_limite2.ajouter_habitant_composition("Bob", 21, "Parvis de Notre-Dame", {})
        self.assertEqual(village_test_limite1.get_habitants()[0].get_nom(), village_test_limite2.get_habitants()[0].get_nom())
        self.assertEqual(village_test_limite1.get_habitants()[0].get_age(), village_test_limite2.get_habitants()[0].get_age())
        self.assertEqual(village_test_limite1.get_habitants()[0].get_adresse(), village_test_limite2.get_habitants()[0].get_adresse())
        self.assertEqual(village_test_limite1.get_habitants()[0].get_animaux(), village_test_limite2.get_habitants()[0].get_animaux())

if __name__ == "__main__":
    unittest.main(verbosity = 2)
