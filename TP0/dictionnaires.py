# Question 1

def quantite_piece(stock, modele, piece):
    return stock[modele][piece];

pieces_stock = {
"ModeleA": {"moteurs": 10, "capteurs": 25, "roues": 40},
"ModeleB": {"moteurs": 6, "capteurs": 15, "roues": 24},
}
assert quantite_piece(pieces_stock, "ModeleA", "moteurs") == 10