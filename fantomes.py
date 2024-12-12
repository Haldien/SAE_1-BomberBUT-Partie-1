from random import randint, shuffle
from fonctions_utiles import *

#Format Liste Fantome, tuple les prises sont bloquantes

def deplacer_fantomes(grille:list, dic_jeu) -> None:
    """
    Cette fonction prend en paramètre une grille et une liste d'entités
    Il va update pour chaque fantôme présent dans la partie
    """
    for fantome in dic_jeu["fantomes"]:
        pos_possible = get_pos_possible(grille, dic_jeu["fantomes"][fantome][1], dic_jeu)

        if pos_possible != []:

            x_pos, y_pos = pos_possible[0]
            grille[ dic_jeu["fantomes"][fantome][1][0] ][ dic_jeu["fantomes"][fantome][1][1] ].remove(fantome)
            grille[x_pos][y_pos] += [fantome]
            dic_jeu["fantomes"][fantome][1] = (x_pos, y_pos)

    return


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

def apparition_fantomes(grille:list, dic_jeu:dict, settings:dict) -> None:
    """
    Prend en paramètre une grille, un dictionnaire de fantômes, et un dictionnaire de prises


    Modifie une dictionnaire en ajoutant les fantômes dans un format
    entites = {
        fantome{index} = [objetGraphique, (coordonnées)]
    }
    La taille du dictionnaire correspond aux nombres de fantômes présents dans la partie actuelle.
    """
    entite = dic_jeu["fantomes"]
    pos_prise = dic_jeu["ethernet"]["pos"]
    shuffle(pos_prise)
    pos = pos_prise[0]

    case_disponible = get_pos_possible(grille, pos, dic_jeu)
    if case_disponible == []: # Si la liste est vide on stop la fonction
        return

    shuffle(case_disponible)
    new_entity = f"F{settings["nombrefantome"]}"
    settings["nombrefantome"] += 1
    entite[new_entity] = ["objetGraphique", (case_disponible[0][0],case_disponible[0][1])]
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

def attaque_fantome(grille:list, dic_jeu:dict) -> None:
    """
        Note au développeur: Le player pos peut directement évoluer avec le dico bomber 

        Cette fontion prend en paramètre une grille de jeu, le couple de coordonnée du joueur et les entités 

        Elle permet d'appliquer des dégâts au bomber si un fantôme se situe dans la case adjacente à celui ci.

        Elle ne renvoie rien
    """
    entite = dic_jeu["fantomes"]
    posFantome = []
    for fantome in entite:
        posFantome += [entite[fantome][1]]
    x_bomber, y_bomber = dic_jeu["bomber"]["pos"]
    for pos in posFantome:
        x_fant, y_fant = pos
        if est_proche(x_fant, y_fant, x_bomber, y_bomber):
            print("Tu es touché par un fantome"*6)
            dic_jeu["bomber"]["PV"] -= 1
            return


    print(posFantome)

    return

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
