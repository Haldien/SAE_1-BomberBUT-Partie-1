from random import randint, shuffle
from fonctions_utiles import *

from format import createMap

#Format Liste Fantome, tuple les prises sont bloquantes

def deplacerFantomes(grille:list, entite:dict) -> None:
    """
    Cette fonction prend en paramètre une grille et une liste d'entités
    Il va update pour chaque fantôme présent dans la partie

    """
    for fantome in entite:
        posPossible = getPosPossible(grille, entite[fantome][1], entite)

        if posPossible != []:

            xPos, yPos = posPossible[0]
            grille[ entite[fantome][1][0] ][ entite[fantome][1][1] ].remove(fantome)
            grille[xPos][yPos] += [fantome]
            entite[fantome][1] = (xPos, yPos)

    return


def getPosPossible(grille:list, pos:tuple, entite) -> list:
    """
        Cette fonction prend en paramètre :
        Une grille : notre niveau
        pos : un couple de coordonnée
        entite : un dictionnaire qui répertorie tout les fantômes vivants

        Cette fonction nous sert à déterminer toute les cases vides proches d'une case cible dont on connaît les coordonnées (pos)
        Elle retourne une liste de tuple de toutes les cases possibles mélangées. Si il n'y a plus de chemin possible elle renvoie une liste vide.
    """
    xPos, yPos = pos
    caseDisponible = []
    posPossible = [ (xPos,yPos-1), (xPos+1,yPos), (xPos,yPos+1), (xPos-1,yPos) ] # Une liste avec toutes les positions possibles par défaut
    for i in posPossible:
        xTmp, yTmp = i
        if case_valide(grille, xTmp, yTmp): # On fait un tri des positions
            valide = True
            for fant in list(entite):
                for el in grille[xTmp][yTmp]:
                    if fant in el:
                        valide = False
                        break
        
            if valide:   
                caseDisponible += [i] 
           
    
    shuffle(caseDisponible)
    return caseDisponible

def apparition_fantomes(grille:list, entite: dict, prise: dict) -> None:
    """
    Prend en paramètre une grille, un dictionnaire de fantômes, et un dictionnaire de prises


    Modifie une dictionnaire en ajoutant les fantômes dans un format
    entites = {
        fantome{index} = [objetGraphique, (coordonnées)]
    }
    La taille du dictionnaire correspond aux nombres de fantômes présents dans la partie actuelle.
    """
    global globalData ## > Cette donnée va être remplacer plus tard pour un truc plus propre
    posPrise = prise["E"]
    shuffle(posPrise)
    pos = posPrise[0]

    caseDisponible = getPosPossible(grille, pos, entite)
    print
    if caseDisponible == []: # Si la liste est vide on stop la fonction
        return
    print(caseDisponible)
    
    shuffle(caseDisponible)
    newEntity = f"F{globalData}"
    globalData += 1
    entite[newEntity] = ["objetGraphique", (caseDisponible[0][0],caseDisponible[0][1])]
    grille[caseDisponible[0][0]][caseDisponible[0][1]] += [newEntity]
    
    
def getPriseEthernet(grille:list) -> list :
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

def attaque_fantome(grille:list,playerPos:tuple, entite:dict) -> None:
    """
        Note au développeur: Le player pos peut directement évoluer avec le dico bomber 

        Cette fontion prend en paramètre une grille de jeu, le couple de coordonnée du joueur et les entités 

        Elle permet d'appliquer des dégâts au bomber si un fantôme se situe dans la case adjacente à celui ci.

        Elle ne renvoie rien
    """
    for fantome in entite:
        xFantome, yFantome = entite[fantome][1]
        xBomber, yBomber = playerPos
        if xBomber + 1 == xFantome or xBomber - 1 == xFantome \
            or yBomber + 1 == yFantome or yBomber -1 == yFantome:
                print("Un fantôme a touché le joueur")
                """
                    Faudra aussi faire des tours d'invulnérabilité au cas où la RNG est éclaté
                """
        else:
            print("rien ne se passe")

    return


fantomes = { }

prise = {
    "E" : []}

globalData = 0

