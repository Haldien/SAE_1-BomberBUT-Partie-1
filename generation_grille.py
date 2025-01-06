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
    for y in range(hauteur):
        current = list()
        grille.append(current)
        for x in range(largeur):
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

"""
===============================================================================================

                            Importation de map

===============================================================================================
"""
def create_map(nomMap:str) -> list:
    """
        Cette fonction prend en argument un nom de map sans l'extension
        Elle reformate cette map pour notre programme

        On cherche à formater tel qu'une liste (la map entière) contienne une liste (pour chaque ligne) qui contient également une liste (pour chaque case)
        Ce système sert à prévenir des objets pouvant être plusieurs sur une même case.
        EX : Un joueur ou un fantôme peuvent être sur la même case
        [" "] -> [ "Bombe" ] -> [ "Bombe", "Fantôme ]
        
        Elle renvoie ce nouveau formatage.
    """
    mapText = open(f"map/{nomMap}.txt", "r")

    carte = []

    for i in mapText.read().split("\n")[3:]:
        row = []
        for j in i:
            if j == ' ':
                row += [ [ ] ]
            else:
                row += [[j]]
        carte += [row]
    
    return carte

def get_param( nomMap:str) -> tuple[int,int]:
    """
        Cette fonction prend en paramètre une nom de map sans l'extension

        Elle permet de récupérer le scénario d'une map
        
        Elle retourne les valeurs de ces paramètres
    """

    param = open(f"map/{nomMap}.txt", "r")
    tmp = param.readlines()[0:2]
    val = (int(tmp[0].split()[1]), int(tmp[1].split()[1]))
    param.close()
    
    return val

def get_scenario(g,nomMap:str) -> tuple[dict, dict, list[list[list[str]]], int]:
    """
    Cette fonction prend en paramètre un nom de map

    Cette fonction permet de générer le dic_jeu qui répertorie tout les objets particulier ainsi que les paramètres du jeu
    bomber, bombes, ethernet et fantôme. Elle sert notamment à l'initialisation d'une map

    Elle renvoie un tuple de 3 éléments
        le dic_jeu, qui va contenir tout les objets
    
        settings, qui va contenir les paramètres du scénarios

        graphique, qui nous permet de savoir si on veut lancer graphiquement ou non notre jeu (Il est plutôt conseiller de se servir du 
        mode non graphique sur des petites grilles)
    """
    zone_affichage_largeur = fenetre_dimensions[0]//4
    dic_jeu = {
        "murs": [],
        "colonnes": [],
        "ethernets": [],
        "bomber": None,
        "fantomes": [],
        "upgrades": [],
        "bombes": [],

        "case_dimensions": None,

        "fenetre_dimensions": fenetre_dimensions,

        "objets_graphiques_overlay": []
    }

    settings = {
            "timer": 200,
            "timer_fantome": 20,
            "nombre_fantomes": 0,
    }
    grille = create_map(nomMap)
    param = get_param(nomMap)
    settings['timer'], settings['timer_fantome'] = param[0], param[1]
    dic_jeu["case_dimensions"] = ((fenetre_dimensions[0])-zone_affichage_largeur)//len(grille[0]), fenetre_dimensions[1]//len(grille) if fenetre_dimensions[1]//len(grille[0]) else (96/96)

    # On a besoin de remove, car pour la version aléatoire, les objets posent leurs propres identitiants
    # Ce qui fait qu'en temps normal, on a les cases qui se dédoublent
    for y in range(len(grille)):
        for x in range(len(grille[0])):
            if "P" in grille[y][x]:
                dic_jeu["bomber"] = Bomber(g, grille, dic_jeu, (y,x),"P" )
                grille[y][x].remove("P")
            elif "E" in grille[y][x]:
                dic_jeu["ethernets"] += [Ethernet(g, grille, dic_jeu, (y,x), "E")]
                grille[y][x].remove("E")
            elif "C" in grille[y][x]:
                dic_jeu["colonnes"] += [Colonne(g, grille, dic_jeu, (y,x), "C")]
                grille[y][x].remove("C")
            elif "M" in grille[y][x]:
                dic_jeu["murs"] += [Mur(g, grille, dic_jeu, (y,x), "M")]
                grille[y][x].remove("M")
    return (dic_jeu, settings, grille)
