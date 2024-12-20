from tkiteasy import ObjetGraphique
from time import sleep
from affiche import *


#TAILLE_FENETRE = (1200, 1000) # (x, y)
TAILLE_FENETRE = (1280, 720) # (x, y)

"""


"""
"""

def dimensions_de_case(grille:list[list[list[str]]])-> tuple[int, int]:
    global TAILLE_FENETRE

    # dimmensions de case retournées : tuple de la forme (x, y) !!
    return TAILLE_FENETRE[1] // len(grille[0]), TAILLE_FENETRE[1] // len(grille)

    nouvelle versions de 

    720/720 

    
    
    
    """
def playground(g):
    g.dessinerRectangle(0, 0, TAILLE_FENETRE[0]//2, TAILLE_FENETRE[1], "red")

def dimensions_de_case(grille:list[list[list[str]]])-> tuple[int, int]:
    """
    un redimensionnement pour une taille plus petite
    """
    # dimmensions de case retournées : tuple de la forme (x, y) !!
    return (TAILLE_FENETRE[1] // len(grille), TAILLE_FENETRE[1] // len(grille)) if TAILLE_FENETRE[1]//len(grille) < 100 else (96,96)

def get_offset(grille) -> tuple[int,int]:
    dim_case = dimensions_de_case(grille)
    return ((300+ (TAILLE_FENETRE[0] - ( (len(grille[0])) )*dim_case[0]) )//2, (TAILLE_FENETRE[1] - ((len(grille)))*dim_case[1])//2 )
    

def render(grille, g, dic_jeu, objets_graphiques = None) -> list[ObjetGraphique]:

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
                obj = g.dessinerRectangle(coord_x, coord_y, dimensions_case[0], dimensions_case[1], "red")
                objets.append(obj)
            if "P" in grille[y][x]:
                obj = g.dessinerRectangle(coord_x, coord_y, dimensions_case[0], dimensions_case[1], "blue")
                objets.append(obj)
            if "U" in grille[y][x]:
                obj = g.dessinerRectangle(coord_x, coord_y, dimensions_case[0], dimensions_case[1], "pink")
                objets.append(obj)
            for el in grille[y][x]:
                if el in list(dic_jeu["fantomes"].keys()):
                    obj = g.dessinerRectangle(coord_x, coord_y, dimensions_case[0], dimensions_case[1], "white")
                    objets.append(obj)
            
            # On place les éléments indestructibles qu'à la première itération de render()
            if objets_graphiques is None:
                if "C" in grille[y][x]:
                    g.dessinerRectangle(coord_x, coord_y, dimensions_case[0], dimensions_case[1], "grey")
                if "E" in grille[y][x]:
                    g.dessinerRectangle(coord_x, coord_y, dimensions_case[0], dimensions_case[1], "green")


    return objets


def render_explosions_apparition(grille, g, case_affectees, offset:tuple[int,int] = (0,0))-> list[ObjetGraphique]:

    dimensions_case = dimensions_de_case(grille)

    coords_affectees = list()
    for liste in list(case_affectees.values()):
        for coord in liste:
                coords_affectees.append(coord)

    objets_graphiques_explosions = list()

    for coord in coords_affectees:
        coord_x =   offset[0] + coord[1] * dimensions_case[0]
        coord_y =   offset[1] + coord[0] * dimensions_case[1]

        obj = g.afficherImage(coord_x, coord_y, (dimensions_case[0], dimensions_case[1]), "sprites/explosion.png")
        objets_graphiques_explosions.append(obj)

    return objets_graphiques_explosions

def render_explosions_suppression(g, objets_graphiques_explosions):

    for obj in objets_graphiques_explosions:

        g.supprimer(obj)

def render_undestructible(g, grille:list[list[list[str]]], offset:tuple[int,int] = (0,0)) -> None:
    """
        Cette fonction va afficher toutes cases qui vont rester inchangés au cours du jeu.
    """

    dim_case = dimensions_de_case(grille)

    for y in range(len(grille)):
        for x in range(len(grille[0])):
            
            
            coord_x =  offset[0] + x * dim_case[0]
            coord_y =  offset[1] + y * dim_case[1]

            if "C" in grille[y][x]:
                g.dessinerRectangle(coord_x,coord_y, dim_case[0], dim_case[1],"white")

def spawn_bomber(g, dic_jeu, settings):
    dic_jeu["bomber"] = Bomber(g, bomber_sprite, settings["size"], dic_jeu["bomber"]["pos"][0], dic_jeu["bomber"]["pos"][1],settings["offset"],3, 0 )

def spawn_fantome(g, dic_jeu, settings):
    for i in dic_jeu["fantomes"]:
        if dic_jeu["fantomes"][i]["obj"] == "objetGraphique":
            dic_jeu["fantomes"][i]["obj"] = Fantome(g, fantome_sprite, settings["size"], dic_jeu["fantomes"][i]["pos"][0], dic_jeu["fantomes"][i]["pos"][1], settings["offset"])

def dep_fantome(dic_jeu):
    for i in dic_jeu["fantomes"]:
        dic_jeu["fantomes"][i].deplacer((dic_jeu["fantomes"][i].y, dic_jeu["fantomes"][i].x), dic_jeu["fantomes"][i].state)

def dep_bomber(bomber:Bomber):
    bomber.deplacer((bomber.y, bomber.x), bomber.state)



def create_object(g, grille: list[list[list[str]]], dic_jeu,settings) -> None:
    dim_case = dimensions_de_case(grille)
    for y in range(len(grille)):
        for x in range(len(grille[0])):
            if "M" in grille[y][x]:
                dic_jeu["mur"][(x,y)] = Mur(g, {"bas": ["sprites/mur.png"] },dim_case, y, x, settings["offset"])
            elif "U" in grille[y][x]:
                dic_jeu["upgrade"][(x,y)] = Upgrade(g, {"bas": ["sprites/upgrade.png"] },dim_case, y, x, settings["offset"])
            elif "E" in grille[y][x]:
                dic_jeu["ethernet"][(y,x)] = Ethernet(g, {"bas" : ["sprites/ethernet.png"]}, dim_case, y,x, settings["offset"])
    




    




