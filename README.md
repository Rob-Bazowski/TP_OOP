# TP_OOP

Travaux pratiques de programmation Python pour la robotique.

## Contenu de `TP0/`

- `tuples.py` : manipulation de tuples représentant des relevés de capteurs, affichage et recalibrage.
- `ensembles.py` : opérations sur des ensembles de robots affectés à des missions.
- `dictionnaires.py` : gestion d'un stock de pièces détachées par modèle de robot.
- `qualite.py` : calcul du coût d'un déplacement selon le type de sol.
- `test.py` : tests unitaires des fonctions principales avec le module standard `unittest`.
- `regard_critique.txt` : remarques sur la qualité du code.

Les fichiers `tuples.py`, `ensembles.py` et `dictionnaires.py` contiennent également des assertions exécutées lors de leur lancement ou de leur importation.

## Prérequis

- Python 3
- Aucune bibliothèque externe n'est nécessaire.

Un fichier `environment.yml` est fourni pour recréer l'environnement Conda du projet si nécessaire.

## Lancer les exercices

Depuis la racine du dépôt :

```bash
python TP0/tuples.py
python TP0/ensembles.py
python TP0/dictionnaires.py
python TP0/qualite.py
```

Les trois premiers scripts vérifient leurs résultats avec des assertions. `qualite.py` affiche le coût calculé pour l'appel défini dans le fichier.

## Lancer les tests

Depuis la racine du dépôt :

```bash
python -m unittest discover -s TP0 -p "test.py" -v
```

Il est également possible de lancer les tests depuis le dossier `TP0` :

```bash
cd TP0
python -m unittest test -v
```

Pour exécuter uniquement les tests de `TestJournalDeBord` :

```bash
cd TP0
python -m unittest test.TestJournalDeBord -v
```
