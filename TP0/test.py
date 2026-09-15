"""Exercice 7 - Tests unitaires"""

# Question 1

import unittest
from tuples import releves, recalibrer
from ensembles import robots_exploration, robots_transport
from ensembles import robots_double_mission, ajouter_robot_mission
from dictionnaires import pieces_stock, consommer_piece, total_pieces

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

# Question 2

class TestFlotteRobots(unittest.TestCase):
    """Test pour les fonctions sur la flotte de robots (ensembles)."""

    def test_robots_double_mission(self):
        """Test de la fonction robots_double_mission"""
        resultat = robots_double_mission(robots_transport, robots_exploration)
        self.assertEqual(resultat, {"R5", "R7"})

    def test_ajouter_robot_mission_usuel(self):
        """Test de la fonction ajouter_robot_mission"""
        resultat = ajouter_robot_mission(robots_exploration, "R8")
        self.assertEqual(resultat, {"R2", "R5", "R7", "R8"})

    def test_ajouter_robot_mission_limite(self):
        """Cas limite : ajout d'un robot déjà existant"""
        resultat = ajouter_robot_mission(robots_exploration, "R7")
        self.assertEqual(resultat, {"R2", "R5", "R7"})

class TestInventaire(unittest.TestCase):
    """Test pour les fonctions d'inventaire (dictionnaires)."""

    def test_consommer_piece(self):
        """Test de la fonction consommer_piece"""
        consommer_piece(pieces_stock, "ModeleA", "moteurs", 3)
        self.assertEqual(pieces_stock["ModeleA"]["moteurs"], 4)

    def test_total_pieces_usuel(self):
        """Test de la fonction total_piece"""
        resultat = total_pieces(pieces_stock)
        self.assertEqual(resultat, {"moteurs": 14, "capteurs": 50, "roues": 80})

    def test_total_pieces_limite(self):
        """Cas limite : Le stock ne contient pas de modèles"""
        resultat = total_pieces({})
        self.assertEqual(resultat, {"moteurs": 0, "capteurs": 0, "roues": 0})

if __name__ == "__main__":
    unittest.main(verbosity=2)
