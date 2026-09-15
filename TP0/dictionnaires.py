"""Exercice 5 - Dicitionnaires"""

# Question 1

def quantite_piece(stock, modele, piece):
    """Retourne la quatité de pièce disponible pour le modèle et la pièce donnés"""
    return stock[modele][piece]

pieces_stock = {
"ModeleA": {"moteurs": 10, "capteurs": 25, "roues": 40},
"ModeleB": {"moteurs": 6, "capteurs": 15, "roues": 24},
}
assert quantite_piece(pieces_stock, "ModeleA", "moteurs") == 10

# Question 2

def consommer_piece(stock, modele, piece, quantite):
    """Retire une quantité donnée à une pièce d'un modèle donné"""
    stock[modele][piece] -= quantite

def ajouter_modele(stock, modele, moteurs, capteurs, roues):
    """Ajoute un modèle à un stocke déjà existant"""
    stock[modele] = {"moteurs" : moteurs, "capteurs" : capteurs, "roues" : roues}

def total_pieces(stock):
    """Retourne la somme des quantités de pièces dans le stock"""
    somme = {"moteurs":0, "capteurs":0, "roues":0}
    for modele in stock.values():
        for piece in modele.keys():
            somme[piece] += modele[piece]
    return somme


consommer_piece(pieces_stock, "ModeleA", "moteurs", 3)
assert pieces_stock["ModeleA"]["moteurs"] == 7
ajouter_modele(pieces_stock, "ModeleC",moteurs=4, capteurs=10, roues=16)
assert pieces_stock["ModeleC"] == {"moteurs": 4, "capteurs": 10, "roues": 16}
totaux = total_pieces(pieces_stock)
assert totaux == {"moteurs": 17, "capteurs": 50, "roues": 80}
