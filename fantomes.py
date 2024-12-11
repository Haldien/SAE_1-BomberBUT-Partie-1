from random import randint, shuffle
from fonctions_utiles import *

#Format Liste Fantome, tuple les prises sont bloquantes

def deplacer_fantomes(grille:list, entite:dict) -> None:
    """
    Cette fonction prend en paramètre une grille et une liste d'entités
    Il va update pour chaque fantôme présent dans la partie

    """
    for fantome in entite:
        pos_possible = get_pos_possible(grille, entite[fantome][1], entite)

        if pos_possible != []:

            x_pos, y_pos = pos_possible[0]
            grille[ entite[fantome][1][0] ][ entite[fantome][1][1] ].remove(fantome)
            grille[x_pos][y_pos] += [fantome]
            entite[fantome][1] = (x_pos, y_pos)

    return


def get_pos_possible(grille:list, pos:tuple, entite) -> list:
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
        if case_valide(grille, x_tmp, y_tmp): # On fait un tri des positions
            valide = True
            for fant in list(entite):
                for el in grille[x_tmp][y_tmp]:
                    if fant in el:
                        valide = False
                        break
        
            if valide:   
                case_disponible += [i] 
           
    
    shuffle(case_disponible)
    return case_disponible

def apparition_fantomes(grille:list, entite: dict, ethernet: dict) -> None:
    """
    Prend en paramètre une grille, un dictionnaire de fantômes, et un dictionnaire de prises


    Modifie une dictionnaire en ajoutant les fantômes dans un format
    entites = {
        fantome{index} = [objetGraphique, (coordonnées)]
    }
    La taille du dictionnaire correspond aux nombres de fantômes présents dans la partie actuelle.
    """
    global globalData ## > Cette donnée va être remplacer plus tard pour un truc plus propre
    pos_prise = ethernet["pos"]
    shuffle(pos_prise)
    pos = pos_prise[0]

    case_disponible = get_pos_possible(grille, pos, entite)
    if case_disponible == []: # Si la liste est vide on stop la fonction
        return

    shuffle(case_disponible)
    new_entity = f"F{globalData}"
    globalData += 1
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

def attaque_fantome(grille:list,player_pos:tuple, entite:dict) -> None:
    """
        Note au développeur: Le player pos peut directement évoluer avec le dico bomber 

        Cette fontion prend en paramètre une grille de jeu, le couple de coordonnée du joueur et les entités 

        Elle permet d'appliquer des dégâts au bomber si un fantôme se situe dans la case adjacente à celui ci.

        Elle ne renvoie rien
    """
    for fantome in entite:
        x_fantome, y_fantome = entite[fantome][1]
        x_bomber, y_bomber = player_pos
        if x_bomber + 1 == x_fantome or x_fantome - 1 == x_fantome \
            or y_bomber + 1 == y_fantome or y_bomber -1 == y_fantome:
                print("Un fantôme a touché le joueur")
                """
                    Faudra aussi faire des tours d'invulnérabilité au cas où la RNG est éclaté
                """
        else:
            print("rien ne se passe")

    return


globalData = 0
