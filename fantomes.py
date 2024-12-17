from random import randint, shuffle
from fonctions_utiles import *
from affiche import *

#Format Liste Fantome, tuple les prises sont bloquantes



def get_pos_possible(grille:list, pos:tuple, dic_jeu) -> list:
    """
        Cette fonction prend en paramètre :
        Une grille : notre niveau
        pos : un couple de coordonnée
        entite : un dictionnaire qui répertorie tout les fantômes vivants

        Cette fonction nous sert à déterminer toute les cases vides proches d'une case cible dont on connaît les coordonnées (pos)
        Elle retourne une liste de tuple de toutes les cases possibles mélangées. Si il n'y a plus de chemin possible elle renvoie une liste vide.
    """
    x_pos, y_pos = pos
    case_disponible = []
    pos_possible = [ (x_pos,y_pos-1), (x_pos+1,y_pos), (x_pos,y_pos+1), (x_pos-1,y_pos) ] # Une liste avec toutes les positions possibles par défaut
    for i in pos_possible:
        x_tmp, y_tmp = i
        if case_valide(grille, x_tmp, y_tmp, dic_jeu): # On fait un tri des positions
            case_disponible += [i]
           
    
    shuffle(case_disponible)
    return case_disponible

def apparition_fantomes(g,grille:list, dic_jeu:dict, settings:dict) -> None:
    """
    Prend en paramètre une grille, un dictionnaire de fantômes, et un dictionnaire de prises


    Modifie une dictionnaire en ajoutant les fantômes dans un format
    entites = {
        fantome{index} = [objetGraphique, (coordonnées)]
    }
    La taille du dictionnaire correspond aux nombres de fantômes présents dans la partie actuelle.
    """
    entite = dic_jeu["fantomes"]
    pos_prise = []
    for pos in dic_jeu["ethernet"]:
        pos_prise += [pos]
    shuffle(pos_prise)
    if pos_prise == []:
        return 
    pos = pos_prise[0]

    case_disponible = get_pos_possible(grille, pos, dic_jeu)
    if case_disponible == []: # Si la liste est vide on stop la fonction
        return

    shuffle(case_disponible)
    new_entity = f"F{settings["nombrefantome"]}"
    settings["nombrefantome"] += 1
    entite[new_entity] = Fantome(g, fantome_sprite, settings["size"], case_disponible[0][0], case_disponible[0][1], (0,0))
    grille[case_disponible[0][0]][case_disponible[0][1]] += [new_entity]
    
def get_Ethernet(grille:list) -> list :
    """
    Cette fonction prend en paramètre une grille et retourne tout les spaw.. les prises ethernet du niveau
    Renvoie une liste contenant des couples de coordonnées.
    """
    prise = []
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            for el in grille[i][j]:
                if el == "E":
                    prise += [(i,j)]
    return prise



def est_proche(x_fant:int,y_fant:int, x_bomb:int, y_bomb:int) -> bool:
    """
        Cette fonction prend en paramètre 
        les coordonnées du bomber et les coordonnées d'un fantôme

        renvoie un booléen
    """

    if (x_fant + 1 == x_bomb and y_fant == y_bomb ) \
        or (x_fant == x_bomb and y_fant - 1 == y_bomb ) \
            or (x_fant == x_bomb and y_fant + 1 == y_bomb ) \
                or (x_fant - 1 == x_bomb and y_fant == y_bomb ):

        return True
    return False
