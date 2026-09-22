"""Exercice 5 - Compositio et agrégation : la classe Village"""

# Question 1

from habitant import Habitant

class Village:
    """Classe Village contenant le nom du village et la liste de ses habitants"""

    def __init__(self, nom):
        self.nom = nom
        self.habitants = []

    def get_habitants(self):
        return self.habitants

# Question 2

    def ajouter_habitant_composition(self, nom, age, adresse, animaux = None):
        """Ajout d'un habitant au village"""
        self.habitants.append(Habitant(nom, age, adresse, animaux))

    def ajouter_habitant_agregation(self, habitant):
        """Ajout d'un habitant au village"""
        self.habitants.append(habitant)

    def afficher_habitants(self):
        texte = "["
        for i,habitant in enumerate(self.habitants):
            if i != len(self.habitants)-1:
                texte += f"{habitant.get_nom()}, "
            else:
                texte += f"{habitant.get_nom()}]"
        print(texte)

pytown = Village("PyTown")
pytown.ajouter_habitant_composition("Aldric", 25, "Rue A", {"vaches": 3})
elise = Habitant("Elise", 28, "Rue B", {"poules": 10})
pytown.ajouter_habitant_agregation(elise)
autre_village = Village("VillageVoisin")
autre_village.ajouter_habitant_agregation(elise) # meme habitant dans 2 villages
assert len(pytown.get_habitants()) == 2
assert elise in autre_village.get_habitants()
pytown.afficher_habitants()

# Question 3
# Dans ajouter_habitant_composition, on crée un nouvel objet habitant dans la méthode -> Compostion
# Dans ajouter_habitant_agregation, on ajoute un objet habitant déjà existant dans la méthode -> Agrégation
