from tkiteasy import ObjetGraphique
from time import sleep

TAILLE_FENETRE = (1200, 1000) # (x, y)


def dimensions_de_case(grille:list[list[list[str]]])-> tuple[int, int]:
    global TAILLE_FENETRE

    # dimmensions de case retournées : tuple de la forme (x, y) !!
    return TAILLE_FENETRE[0] // len(grille[0]), TAILLE_FENETRE[1] // len(grille)


def render(grille, g, dic_jeu, objets_graphiques = None)-> list[ObjetGraphique]:

    dimensions_case = dimensions_de_case(grille)

    # pour qu'il n'y ait pas de superposition : suppresions des objets précédents
    if objets_graphiques is not None:
        for obj in objets_graphiques:
            g.supprimer(obj)

    objets_graphiques = list()

    for y in range(len(grille)):
        for x in range(len(grille[0])):

            coord_x = x * dimensions_case[0]
            coord_y = y * dimensions_case[1]

            if "C" in grille[y][x]:
                obj = g.dessinerRectangle(coord_x, coord_y, dimensions_case[0], dimensions_case[1], "grey")
                objets_graphiques.append(obj)
            if "M" in grille[y][x]:
                obj = g.afficherImage(coord_x, coord_y, (dimensions_case[0], dimensions_case[1]), "sprites/mur.png")
                objets_graphiques.append(obj)
            if "B" in grille[y][x]:
                obj = g.dessinerRectangle(coord_x, coord_y, dimensions_case[0], dimensions_case[1], "red")
                objets_graphiques.append(obj)
            if "E" in grille[y][x]:
                obj = g.dessinerRectangle(coord_x, coord_y, dimensions_case[0], dimensions_case[1], "green")
                objets_graphiques.append(obj)
            if "P" in grille[y][x]:
                obj = g.dessinerRectangle(coord_x, coord_y, dimensions_case[0], dimensions_case[1], "blue")
                objets_graphiques.append(obj)
            if "U" in grille[y][x]:
                obj = g.dessinerRectangle(coord_x, coord_y, dimensions_case[0], dimensions_case[1], "pink")
                objets_graphiques.append(obj)
            for el in grille[y][x]:
                if el in list(dic_jeu["fantomes"].keys()):
                    obj = g.dessinerRectangle(coord_x, coord_y, dimensions_case[0], dimensions_case[1], "white")
                    objets_graphiques.append(obj)


    return objets_graphiques


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
