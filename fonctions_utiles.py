
# Valables pour le bomberman et les fantomes mais pas pour les bombes
def case_valide(grille: list, y: int, x: int, dic_jeu) -> bool:
    """
        Cette fonction prend en paramètre,
        une grille de jeu, des coordonnées x et y

        Elle renvoie False si la case n'est pas valide et True si elle est valide
    """
    if not (0 <= y <= len(grille) - 1 and 0 <= x <= len(grille[0]) - 1):
        return False
    for el in ["M", "C", "E", "P"] + list(dic_jeu["fantomes"].keys()):
        if el in grille[y][x]:
            return False
    return True

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
                print("           ", end = " ")
            elif len(case) == 1:
                print(f"   {case}   ", end = " ")
            elif len(case) == 2:
                print(f"{case}", end = " ")
        print("\n")

def get_param( nomMap:str) -> tuple[int,int]:
    """
        Cette fonction prend en paramètre une nom de map sans l'extension

        Elle permet de récupérer le scénario d'une map
        
        Elle retourne les valeurs de ces paramètres
    """

    param = open(f"{nomMap}.txt", "r")
    tmp = param.readlines()[0:2]
    val = (int(tmp[0].split()[1]), int(tmp[1].split()[1]))
    param.close()
    
    return val
    

    

def get_scenario(nomMap:str) -> tuple[dict, dict, list[list[list[str]]]]:
    """
    Cette fonction permet de générer le dic_jeu qui répertorie tout les objets particulier ainsi que les paramètres du jeu
    bomber, bombes, ethernet et fantôme.
    """
    dic_jeu = {
        "bomber" :{ 'pos' : None, 'PV': 3, 'Niv': 0, 'Score': 0, 'cooldown' : 0 },

        "fantomes": {},
        "bombes" : {},

        "ethernet" : { "pos" : [] }
        
    }

    settings = {
        "timer" : 100,
        "timerfantome": 20,
        "nombrefantome": 0
    }

    param = get_param(nomMap)
    settings['timer'], settings['timerfantome'] = param[0], param[1]

    grille = create_map(nomMap)
    for y in range(len(grille)):
        for x in range(len(grille[0])):
            if "P" in grille[y][x]:
                dic_jeu["bomber"]["pos"] = (y,x)
            elif "E" in grille[y][x]:
                dic_jeu["ethernet"]["pos"] += [(y,x)]
            elif "F" in grille[y][x]:
                grille[y][x][0] += str(settings["nombrefantome"])
                dic_jeu["fantomes"] = {f"F{settings["nombrefantome"]}" : ["ObjetGraphique", (y,x)]}
                settings["nombrefantome"] += 1

    
    return (dic_jeu, settings, grille)


    
