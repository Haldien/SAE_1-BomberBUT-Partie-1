from tkiteasy import ObjetGraphique
from time import sleep

TAILLE_FENETRE = (800, 800) # (x, y)


def dimensions_de_case(grille:list[list[list[str]]])-> tuple[int, int]:
    global TAILLE_FENETRE

    # dimmensions de case retournées : tuple de la forme (x, y) !!
    return TAILLE_FENETRE[0] // len(grille[0]), (TAILLE_FENETRE[1]-TAILLE_FENETRE[1]//7) // len(grille)
    # On réserve 1/7 de la fenêtre en bas pour l'affichage du score, etc :            ^

def render(grille, g, dic_jeu, OnGameSettings, objets_graphiques = None)-> list[ObjetGraphique]:
    global TAILLE_FENETRE

    dimensions_case = dimensions_de_case(grille)

    # pour qu'il n'y ait pas de superposition : suppresions des objets précédents
    if objets_graphiques is not None:
        for obj in objets_graphiques:
            g.supprimer(obj)

    objets = list()

    for y in range(len(grille)):
        for x in range(len(grille[0])):

            coord_x = x * dimensions_case[0]
            coord_y = y * dimensions_case[1]

            if "M" in grille[y][x]:
                obj = g.afficherImage(coord_x, coord_y, (dimensions_case[0], dimensions_case[1]), "sprites/mur.png")
                objets.append(obj)
            if "B" in grille[y][x]:
                obj = g.afficherImage(coord_x, coord_y, (dimensions_case[0], dimensions_case[1]), "sprites/bombe.png")
                objets.append(obj)
            if "P" in grille[y][x]:
                obj = g.afficherImage(coord_x, coord_y, (dimensions_case[0], dimensions_case[1]), "sprites/bomberman.png")
                objets.append(obj)
            if "U" in grille[y][x]:
                obj = g.afficherImage(coord_x, coord_y, (dimensions_case[0], dimensions_case[1]), "sprites/upgrade.png")
                objets.append(obj)
            for el in grille[y][x]:
                if el in list(dic_jeu["fantomes"].keys()):
                    obj = g.afficherImage(coord_x, coord_y, (dimensions_case[0], dimensions_case[1]), "sprites/fantome.png")
                    objets.append(obj)

            # On place les éléments indestructibles qu'à la première itération de render()
            if objets_graphiques is None:
                if "C" in grille[y][x]:
                    g.afficherImage(coord_x, coord_y, (dimensions_case[0], dimensions_case[1]), "sprites/colonne.png")
                if "E" in grille[y][x]:
                    g.afficherImage(coord_x, coord_y, (dimensions_case[0], dimensions_case[1]), "sprites/ethernet.png")


    # Affichages textes
    obj = g.afficherTexte(f"Score : {dic_jeu['bomber']['Score']}", TAILLE_FENETRE[0]//5, 6*TAILLE_FENETRE[1]//7+0.25*TAILLE_FENETRE[1]//7, "white", TAILLE_FENETRE[1]//25)
    objets.append(obj)
    obj = g.afficherTexte(f"PV : {dic_jeu['bomber']['PV']}", TAILLE_FENETRE[0] // 5, 6 * TAILLE_FENETRE[1] // 7 + 0.7 * TAILLE_FENETRE[1] // 7, "white", TAILLE_FENETRE[1]//25)
    objets.append(obj)
    obj = g.afficherTexte(f"Timer : {OnGameSettings['timer']}", 3.5*TAILLE_FENETRE[0] // 5, 6 * TAILLE_FENETRE[1] // 7 + 0.25 * TAILLE_FENETRE[1] // 7, "white", TAILLE_FENETRE[1]//25)
    objets.append(obj)
    obj = g.afficherTexte(f"Timer fantome : {OnGameSettings['timerfantome']}", 3.5 * TAILLE_FENETRE[0] // 5,6 * TAILLE_FENETRE[1] // 7 + 0.7 * TAILLE_FENETRE[1] // 7, "white", TAILLE_FENETRE[1]//25)
    objets.append(obj)

    return objets


def render_explosions_apparition(grille, g, case_affectees)-> list[ObjetGraphique]:

    dimensions_case = dimensions_de_case(grille)

    coords_affectees = list()
    for liste in list(case_affectees.values()):
        for coord in liste:
                coords_affectees.append(coord)

    objets_graphiques_explosions = list()

    for coord in coords_affectees:
        coord_x =  coord[1] * dimensions_case[0]
        coord_y =  coord[0] * dimensions_case[1]

        obj = g.afficherImage(coord_x, coord_y, (dimensions_case[0], dimensions_case[1]), "sprites/explosion.png")
        objets_graphiques_explosions.append(obj)

    return objets_graphiques_explosions

def render_explosions_suppression(g, objets_graphiques_explosions):

    for obj in objets_graphiques_explosions:

        g.supprimer(obj)
