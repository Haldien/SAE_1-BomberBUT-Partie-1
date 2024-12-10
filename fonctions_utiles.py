# Valables pour le bomberman et les fantomes mais pas pour les bombes
def case_valide(grille: list, y: int, x: int) -> bool:
    """
        Cette fonction prend en paramètre,
        une grille de jeu, des coordonnées x et y

        Elle renvoie False si la case n'est pas valide et True si elle est valide
    """
    if not (0 <= y <= len(grille) - 1 and 0 <= x <= len(grille[0]) - 1):
        return False
    for el in ["M", "C", "E", "F", "P"]:
        if el in grille[y][x]:
            return False
    return True

def createMap(nomMap:str) -> list:
    """
        Cette fonction prend en argument un nom de map sans l'extension
        Elle reformate cette map pour notre programme

        On cherche à formater tel qu'une liste (la map entière) contienne une liste (pour chaque ligne) qui contient également une liste (pour chaque case)
        Ce système sert à prévenir des objets pouvant être plusieurs sur une même case.
        EX : Un joueur ou un fantôme peuvent être sur la même case
        [" "] -> [ "Bombe" ] -> [ "Bombe", "Fantôme ]
        
        Elle renvoie ce nouveau formatage.
    """
    mapText = open(f"{nomMap}.txt", "r")

    map = []

    for i in mapText.read().split("\n")[3:]:
        row = []
        for j in i:
            if j == ' ':
                row += [ [ ] ]
            else:
                row += [[j]]
        map += [row]
    
    return map

def affichage_grille(grille):
    print("----------------------------")
    for line in grille:
        for case in line:
            if len(case) == 0:
                print("          ", end = " ")
            elif len(case) == 1:
                print(f"  {case}   ", end = " ")
            elif len(case) == 2:
                print(f"{case}", end = " ")
        print("\n")
