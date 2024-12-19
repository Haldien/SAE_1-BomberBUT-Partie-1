import random, tkiteasy
from constante import HEIGHT, WIDTH

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
    

    

def get_scenario(nomMap:str) -> tuple[dict, dict, list[list[list[str]]], int]:
    """
    Cette fonction prend en paramètre un nom de map

    Cette fonction permet de générer le dic_jeu qui répertorie tout les objets particulier ainsi que les paramètres du jeu
    bomber, bombes, ethernet et fantôme. Elle sert notamment à l'initialisation d'une map

    Elle renvoie un tuple de 3 éléments
        le dic_jeu, qui va contenir tout les objets
    
        settings, qui va contenir les paramètres du scénarios

        graphique, qui nous permet de savoir si on veut lancer graphiquement ou non notre jeu (Il est plutôt conseiller de se servir du 
        mode non graphique sur des petites grilles)
    """
    dic_jeu = {
        "bomber": { },
        "bombes" : { },
        "ethernet" : { },
        "fantomes" : { },
        "mur" : { },
        "upgrade": { }
    }

    settings = {
        "timer" : 100,
        "timerfantome": 20,
        "nombrefantome": 0,
        "size" : None,
        "offset" : None
    }

    param = get_param(nomMap)
    settings['timer'], settings['timerfantome'] = param[0], param[1]

    grille = create_map(nomMap)
    settings["size"] = dimensions_de_case(grille)
    settings["offset"] = get_offset(grille)

    for y in range(len(grille)):
        for x in range(len(grille[0])):
            if "P" in grille[y][x]:
                dic_jeu["bomber"]["pos"] = (y,x)
            elif "E" in grille[y][x]:
                dic_jeu["ethernet"][(y,x)] = "obj"
            elif "F" in grille[y][x]:
                grille[y][x][0] += str(settings["nombrefantome"])
                dic_jeu["fantomes"] = {f"F{settings["nombrefantome"]}" : ["ObjetGraphique", (y,x)]}
                settings["nombrefantome"] += 1

    graphique = int(input("Voulez vous que ce soit graphique ?\n1: Oui\t\t2: Non\n\n"))
    return (dic_jeu, settings, grille, graphique)


def generer_element():

    random_int = random.randint(1,100)

    if 0 <= random_int <= 65:
        return "M"
    elif random_int <= 67:
        return "U"
    elif random_int <= 69:
        return "E"
    elif random_int <= 100:
        pass


def generer_grille(hauteur, largeur):

    grille = list()

    # Création de la grille vide
    for y in range(hauteur+1):
        current = list()
        grille.append(current)
        for x in range(largeur+1):
            current.append([])

    # Colonnes
    for y in range(hauteur):
        for x in range(largeur):
            if y in [0, hauteur-1] or x in [0, largeur-1] or (y%2==0 and x%2==0):
                grille[y][x].append("C")


    # On place le joueur
    while True:
        y = random.randint(0, hauteur-1)
        x = random.randint(0, largeur-1)

        if not grille[y][x]:
            grille[y][x].append("P")
            pos_joueur = (y, x)
            break

    # On s'assure qu'au moins une prise ethernet a spawné
    while True:
        y = random.randint(0, hauteur - 1)
        x = random.randint(0, largeur - 1)

        if not grille[y][x]:
            grille[y][x].append("E")
            break

    # On génère le reste des éléments
    for y in range(1, hauteur-1):
        for x in range(1, largeur-1):
            if not grille[y][x]:
                el = generer_element()
                if el:
                    grille[y][x].append(el)


    # On dégage la zone du joueur
    directions =  [(-1, 0), (0, -1), (1, 0), (0, 1)]

    for direction in directions:
        if "C" not in grille[pos_joueur[0] + direction[0]][pos_joueur[1] + direction[1]] and "E" not in grille[pos_joueur[0] + direction[0]][pos_joueur[1] + direction[1]]:
            grille[pos_joueur[0] + direction[0]][pos_joueur[1] + direction[1]].clear()

    return grille


def updater_timers_bombes(dic_jeu:dict) -> None:
    """
    Cette fonction prends en arguments un dictionnaire.
    Cette fonction permet de gérer le timer des bombes
    Elle ne renvoie rienS
    """
    for key in dic_jeu["bombes"].keys():
        dic_jeu["bombes"][key]["timer"] -= 1
        dic_jeu["bombes"][key]["obj"].ignite(dic_jeu["bombes"][key]["timer"])
        
def round_timer(gameSetting:dict, dic_jeu) -> None:
    """
        Cette fonction prend en paramètre un dictionnaire qui répertorie 
        les détails du "scénario" du niveau.

        Cette fonction doit être appelé à chaque boucle pour actualiser le tour.
    """
    dic_jeu["bomber"].cooldown -= 1
    gameSetting['timer'] -= 1
    gameSetting['timerfantome'] -= 1

def updater_timers(dic_jeu, settings):
    updater_timers_bombes(dic_jeu)
    round_timer(settings, dic_jeu)

def cree_fenetre(graphique):
    match graphique:
        case 1:
            fenetre = tkiteasy.ouvrirFenetre(WIDTH, HEIGHT)  # taille à changer
        case 2:
            fenetre = tkiteasy.ouvrirFenetre(100,100)  # taille à changer
    return fenetre

def dimensions_de_case(grille:list[list[list[str]]])-> tuple[int, int]:
    """
    un redimensionnement pour une taille plus petite
    
    """
    # dimmensions de case retournées : tuple de la forme (x, y) !!
    return (HEIGHT // len(grille), HEIGHT // len(grille)) if HEIGHT//len(grille) < 100 else (96,96)

def get_offset(grille) -> tuple[int,int]:
    dim_case = dimensions_de_case(grille)
    return ((300+ (WIDTH- ( (len(grille[0])) )*dim_case[0]) )//2, (HEIGHT - ((len(grille)))*dim_case[1])//2 )