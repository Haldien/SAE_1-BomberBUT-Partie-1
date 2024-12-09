from random import randint

#Format Liste Fantome, tuple

def deplacer_fantomes(grille:list, entite:dict) -> None:
    """
    Cette fonction prend en paramètre une grille et une liste d'entités
    Il va update pour chaque fantôme présent dans la partie

    """
    for i in entite:
        xFantome, yFantome = entite[i][1]
  
        match randint(0,4): # Prend une valeur aléatoire entre 0 et 4, pour les 4 directions possibles
            case 1: # Nord
                yFantome -= 1
            case 2: # Est
                xFantome += 1
            case 3: # Sud
                yFantome += 1
            case _: # Ouest
                xFantome -= 1


    

def attaque_fantome(grille:list,playerPos:list, entite:list) -> None:
    pass

def appartition_fantomes() -> None:
    """
    Modifie une dictionnaire en ajoutant les fantômes dans un format
    entites = {
        fantome{index} = [objetGraphique, (coordonnées)]
    }
    La taille du dictionnaire correspond aux nombres de fantômes présents dans la partie actuelle.

    """
    
    pass

fantomes = {
    "fantome1" : ["objetGraphique", (5,8)]
}

print(deplacer_fantomes([], fantomes))
