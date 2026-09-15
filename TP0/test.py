"""Exercice 7 - Tests unitaires"""

# Question 1

import unittest
from tuples import releves, recalibrer
from ensembles import robots_exploration, robots_transport
from ensembles import robots_double_mission, ajouter_robot_mission

class TestJournalDeBord(unittest.TestCase):
    """Tests pour les fonctions sur les relevés (tuples)."""

    def test_recalibrer_capteur_existant(self):
        """Test de la fonction recalibrer"""
        resultat = recalibrer(releves, "laser_avant", 2.40)
        self.assertEqual(resultat[0], ("laser_avant", 2.40, "m"))

    def test_recalibrer_capteur_absent(self):
        """Cas limite : le capteur demande n’existe pas."""
        resultat = recalibrer(releves, "telescope", 1000)
        self.assertEqual(resultat, releves)

class TestFlotteRobots(unittest.TestCase):
    """Test pour les fonctions sur la flotte de robots (ensembles)."""

    def test_robots_double_mission(self):
        """Test de la fonction robots_double_mission"""
        resultat = robots_double_mission(robots_transport, robots_exploration)
        self.assertEqual(resultat, {"R5", "R7"})

    def test_ajouter_robot_mission(self):
        """Cas limite : ajout d'un robot déjà existant"""
        resultat = ajouter_robot_mission(robots_exploration, "R7")
        self.assertEqual(resultat, {"R2", "R5", "R7"})

if __name__ == "__main__":
    unittest.main(verbosity=2)
