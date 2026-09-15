releve1 = ("laser_avant", 2.35, "m")
releve2 = ("laser_arriere", 1.10, "m")
releve3 = ("gyroscope", 87.5, "deg")
releves = [releve1, releve2, releve3]

# Question 1

def afficher_releve(releve):
    capteur, valeur, unite = releve
    return f"Capteur {capteur} : {valeur} {unite}"

assert len(releves) == 3
assert releves[0][0] == "laser_avant"
assert afficher_releve(releve1) == "Capteur laser_avant : 2.35 m"

# Question 2

def recalibrer(releves, capteur_a_changer, nouvelle_valeur):
    for i in range(len(releves)) :
        capteur, _, unite = releves[i]
        if capteur == capteur_a_changer :
            nouveau_releve = capteur, nouvelle_valeur, unite
            releves[i] = nouveau_releve
    return releves

nouveaux_releves = recalibrer(releves, "laser_avant", 2.40)

assert nouveaux_releves[0] == ("laser_avant", 2.40, "m")
assert nouveaux_releves[1] == releve2
assert nouveaux_releves[2] == releve3