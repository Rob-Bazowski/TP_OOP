"""Exercice 4 - Ensembles"""

# Question 1

robots_exploration = {"R2", "R5", "R7"}
robots_transport = {"R5", "R9", "R7", "R3"}

def robots_double_mission(ensemble1, ensemble2):
    """Retourne les robots qui participent aux deux missions"""
    return ensemble1 & ensemble2

def robots_toutes_missions(ensemble1, ensemble2):
    """Retourne les robots participant à des missions"""
    return ensemble1 | ensemble2

def robots_exploration_seulement(ensemble1, ensemble2):
    """Retourne les robots participant seulement à l'exploration"""
    return ensemble1 - (ensemble1 & ensemble2)

double_mission = robots_double_mission(robots_exploration, robots_transport)
toutes_missions = robots_toutes_missions(robots_exploration, robots_transport)
exploration_seule = robots_exploration_seulement(robots_exploration, robots_transport)
assert double_mission == {"R5", "R7"}
assert toutes_missions == {"R2", "R3", "R5", "R7", "R9"}
assert exploration_seule == {"R2"}

# Question 2

def ajouter_robot_mission(ensemble, robot_a_ajouter):
    """Ajoute un robot à une mission"""
    nouveau_ensemble = set()
    for robot in ensemble:
        nouveau_ensemble.add(robot)
    nouveau_ensemble.add(robot_a_ajouter)
    return nouveau_ensemble

def retirer_robot_mission(ensemble, robot_a_retirer):
    """Retire un robot d'une mission"""
    nouveau_ensemble = set()
    for robot in ensemble:
        if robot != robot_a_retirer:
            nouveau_ensemble.add(robot)
    return nouveau_ensemble

ajout = ajouter_robot_mission(robots_exploration, "R8")
retrait = retirer_robot_mission(robots_transport, "R9")
assert ajout == {"R2", "R5", "R7", "R8"}
assert retrait == {"R3", "R5", "R7"}
# L’ensemble d’origine ne doit pas avoir été modifié
assert robots_transport == {"R5", "R9", "R7", "R3"}
