"""Exercice 5 - Compositio et agrégation : la classe Village"""

class Village:
    """Classe Village contenant le nom du village et la liste de ses habitants"""

    def __init__(self, nom):
        self.nom = nom
        self.habitants = []