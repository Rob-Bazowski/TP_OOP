import unittest
from habitant import Adulte, Enfant

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
        """Test animal, cas usuel"""
        compte = habitant_test.compte_animal("Vaches")
        self.assertEqual(compte, 10000)

    def test_compte_animal_limite(self):
        """Test animal, cas limite"""
        compte = habitant_test.compte_animal("Licornes")
        self.assertEqual(compte, 0)

if __name__ == "__main__":
    unittest.main(verbosity = 2)
                 

    