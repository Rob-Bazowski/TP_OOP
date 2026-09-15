"""Exercice 6 - Qualité de code"""

def cout_deplacement_propre(type_de_sol, x1, y1, x2, y2):
    """Nouvelle fonction propre calculant la distance entre (x1, y1) et (x2, y2) 
    sur différents type de sols pour un robot"""
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if type_de_sol == "R":
        cout = distance * 1.0
    elif type_de_sol == "H":
        cout = distance * 1.5
    elif type_de_sol == "s":
        cout = distance * 2.0
    else:
        cout = distance * 3.0
    print(f"cout:{cout}")
    return cout
