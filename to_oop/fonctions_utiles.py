import random


"""
DETERMINATION DES CASES VALIDES
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

def get_cases_voisines_valides(grille, coords):

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
PARTIE GRAPHIQUE TKINTER
"""



"""
Remplir le dic_jeu à partir d'une grille prédéfinie
def remplir_dic_jeu_initial(g, grille, dic_jeu):
    for y in range(len(grille)):
        for x in range(len(grille[y])):
            if "M" in grille[y][x]:
                dic_jeu["murs"].append(Mur(g, grille, dic_jeu, (y, x), "M"))
            elif "C" in grille[y][x]:
                dic_jeu["colonnes"].append(Colonne(g, grille, dic_jeu, (y,x),"C"))
            elif "E" in grille[y][x]:
                dic_jeu["ethernets"].append(Ethernet(g, grille, dic_jeu, (y,x),"E"))

            elif "P" in grille[y][x]:
                dic_jeu["bomber"] = (Bomber(g, grille, dic_jeu, (y,x), "P"))
            elif "F" in grille[y][x]:
                dic_jeu["fantomes"].append(Fantome(g, grille, dic_jeu, (y, x), "F"))
            elif "U" in grille[y][x]:
                dic_jeu["upgrades"].append(Upgrade(g, grille, dic_jeu, (y, x), "U"))
"""


"""
AFFICHAGE
"""
def affichage_grille(grille):
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


def affichage_dic_jeu(dic_jeu):
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

def affichage_game_settings(game_settings):
    for key in game_settings:
        print(key, ":", game_settings[key], end = " -- ")

    print("\n")


