import random

from objets import *


def generer_element(g, grille, dic_jeu, y, x):

    random_int = random.randint(1,100)

    if 0 <= random_int <= 65:
        dic_jeu["murs"].append(Mur(g, grille, dic_jeu, (y,x), "M"))
    elif random_int <= 67:
        dic_jeu["upgrades"].append(Upgrade(g, grille, dic_jeu, (y,x), "U"))
    elif random_int <= 69:
        dic_jeu["ethernets"].append(Ethernet(g, grille, dic_jeu, (y,x), "E"))
    elif random_int <= 100:
        pass


def generer_grille_et_dic_jeu(hauteur, largeur, g, dic_jeu):

    grille = list()

    # Création de la grille vide
    for y in range(hauteur+1):
        current = list()
        grille.append(current)
        for x in range(largeur+1):
            current.append([])

    # Colonnes
    for y in range(hauteur):
        for x in range(largeur):
            if y in [0, hauteur-1] or x in [0, largeur-1] or (y%2==0 and x%2==0):
                dic_jeu["colonnes"].append(Colonne(g, grille, dic_jeu, (y,x), "C"))


    # On place le joueur
    while True:
        y = random.randint(0, hauteur-1)
        x = random.randint(0, largeur-1)

        if not grille[y][x]:
            dic_jeu["bomber"] = Bomber(g, grille, dic_jeu, (y,x), "P")
            break

    # On s'assure qu'au moins une prise ethernet a spawné
    while True:
        y = random.randint(0, hauteur - 1)
        x = random.randint(0, largeur - 1)

        if not grille[y][x]:
            dic_jeu["ethernets"].append(Ethernet(g, grille, dic_jeu, (y,x), "E"))
            break

    # On génère le reste des éléments
    for y in range(1, hauteur-1):
        for x in range(1, largeur-1):
            if not grille[y][x]:
                generer_element(g, grille, dic_jeu, y, x)


    # On dégage la zone du joueur
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    for direction in directions:
        if "C" not in grille[dic_jeu["bomber"].pos[0] + direction[0]][dic_jeu["bomber"].pos[1] + direction[1]] and "E" not in grille[dic_jeu["bomber"].pos[0] + direction[0]][dic_jeu["bomber"].pos[1] + direction[1]]:
            for key in dic_jeu:
                if isinstance(dic_jeu[key], list):  # pour éviter case_dimensions
                    for objet in dic_jeu[key]:
                        if objet.pos == (dic_jeu["bomber"].pos[0] + direction[0], dic_jeu["bomber"].pos[1] + direction[1]):
                            objet.se_supprimer()

    return grille
