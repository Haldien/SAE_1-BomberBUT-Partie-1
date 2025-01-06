import random
from constante import *
"""
===============================================================================================

                            Détermination des cases valides

===============================================================================================
"""
# Valable pour le bomberman et les fantomes mais pas pour les bombes
def case_valide(grille: list, y: int, x: int) -> bool:
    """
        Cette fonction prend en paramètre,
        une grille de jeu, des coordonnées x et y

        Elle renvoie False si la case n'est pas valide et True si elle est valide
    """
    if not (0 <= y <= len(grille) - 1 and 0 <= x <= len(grille[0]) - 1):
        return False

    for el in ["M", "C", "E", "P", "F"]:
        if el in grille[y][x]:
            return False

    return True

def get_cases_voisines_valides(grille:list, coords:tuple) -> list:
    """
        Cette fonction prend en paramètres une grille et un tuple de cordonnée (y,x)
        Elle vérifie chaque case autour d'une coordonées si elle est valide ou non
        ELle renvoie une liste de case valide
    """
    cases_voisines_valides = list()

    dic_vecteurs = {
        "haut": (-1, 0),
        "droite": (0, 1),
        "bas": (1, 0),
        "gauche": (0, -1)
    }

    for direction in dic_vecteurs:
        if case_valide(grille, coords[0] + dic_vecteurs[direction][0], coords[1] + dic_vecteurs[direction][1]):
            cases_voisines_valides.append(
                (coords[0] + dic_vecteurs[direction][0], coords[1] + dic_vecteurs[direction][1]))

    return cases_voisines_valides

"""
===============================================================================================

                                 Affichage

===============================================================================================
"""
def affichage_grille(grille:list) -> None:
    """
        Cette fonction prend en argument une grille
        Cette fonction permet d'afficher le plateau de jeu dans la console
        Elle renvoie rien
    """
    print("-------------------------------------------------------------------")
    for line in grille:
        for case in line:
            if len(case) == 0:
                print("           ", end = " ")
            elif len(case) == 1:
                print(f"   {case}   ", end = " ")
            elif len(case) == 2:
                print(f"{case}", end = " ")
        print("\n")


def affichage_dic_jeu(dic_jeu:dict) -> None:
    """
        Cette fonction permet de d'afficher toutes les données contenue dans le dic_jeu avec un formatage particulier
        Elle ne renvoie rien
    """
    for key in dic_jeu:
        if not isinstance(dic_jeu[key], list):
            if key != "sprites":
                print(dic_jeu[key])
                print("\n")
        elif isinstance(dic_jeu[key], list) :
            for el in dic_jeu[key]:
                print(el, end = ", ")
            if dic_jeu[key]:
                print("\n")

def affichage_game_settings(game_settings:dict) -> None:
    """
        Cette fonction permet de d'afficher toutes les données contenue dans le dictionnaire de paramètre avec un formatage particulier
        Elle ne renvoie rien
    """
    for key in game_settings:
        print(key, ":", game_settings[key], end = " -- ")
    print("\n")

"""
===============================================================================================

                            TIMER

===============================================================================================
"""

def updater_timers_bombes(dic_jeu:dict) -> None:
    """
        Cette fonction permet d'actualiser les timers des bombes à partir du dictionnaire de jeu (dic_jeu)
        Elle ne renvoie rien
    """
    for bombe in dic_jeu["bombes"]:
        bombe.decrementer_son_timer()


def updater_timers_game_settings(game_settings:dict, default_game_settings:dict):
    """
        Cette fonction permet d'actualiser les timers des paramètres du jeu, timer et timerfantome à partir du dictionnaire de jeu (dic_jeu)
        Elle ne renvoie rien
    """
    game_settings['timer'] -= 1

    game_settings['timer_fantome'] -= 1
    if game_settings['timer_fantome'] == 0:
        game_settings['timer_fantome'] = default_game_settings["timer_fantome"]

def updater_timer_ethernet(dic_jeu:dict) -> None:
    """
        Cette fonction permet d'actualiser les timers des prises ethernet à partir du dictionnaire de jeu (dic_jeu)
        Elle ne renvoie rien
    """
    for ethernet in dic_jeu["ethernets"]:
        ethernet.has_spawned()

def get_vanilla() -> str:
    """
        Cette fonction permet de récupérer le paramètre si on souhaite ou non jouez dans une version classique
    """
    ress = open("parametre.txt", "r", encoding="utf-8")
    data = ress.readlines()[0].split(" ")[1]
    ress.close()
    return data

def set_vanilla(option: int) -> None:
    """
        Cette fonction permet de modifier la valeur du paramètre vanilla
    """
    ress = open("parametre.txt", "w+", encoding="utf-8")
    ress.write("Vanilla "+str(option))
    ress.close()
