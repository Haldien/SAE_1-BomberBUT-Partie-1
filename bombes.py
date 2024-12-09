def poser_bombe(grille, dic_bombes, y: int, x: int):
    if "B" not in grille[y][x]:
        grille[y][x].append("B")
        ajouter_a_dic_bombes(dic_bombes, y, x)

def ajouter_a_dic_bombes(dic_bombes, y, x):
    dic_bombes[(y, x)] = 5




def case_valide_pour_explosion(grille, y, x)->bool:
    # Les cases non valides sont celles en dehors de la grille et les colonnes. Les prises ethernet sont considérées comme valides pour une explosion
    if not (0 <= y <= len(grille) - 1 and 0 <= x <= len(grille[0]) - 1) or "C" in grille[y][x]:
        return False
    return True

def cases_relatives_vers_absolues(coord, dic_cases_affectees_relatives):

    dic_cases_affectees_absolues = {
        "haut":[],
        "droite":[],
        "bas":[],
        "gauche":[]
    }

    for direction in dic_cases_affectees_relatives.keys():
        for el in dic_cases_affectees_relatives[direction]:
            # pour passer de coordonnées relatives à absolues : coord[0]+el[0], coord[1]+el[1]. coord sont les coordonnées absolues du point à partir desquelles les coordonnées relatives de el sont basées. L'addition des deux donnent les coordonnées absolues de el, càd dans la grille plutôt que par rapport au point de coordonnées coord, càd la bombe
            dic_cases_affectees_absolues[direction].append((coord[0]+el[0], coord[1]+el[1]))

    return dic_cases_affectees_absolues


def calculer_cases_affectees(grille, coord, dic_bomber) -> dict[str:list[tuple[int]]]:
    """
    L'effet d'une explosion dépend de ce qui se trouve dans la case:
    sur une colonne ou une prise ethernet, aucun effet
    sur un mur, il est détruit (la case devient vide) et le bomber marque 1 point
    un upgrade est détruit
    un fantôme est détruit et à sa place on place un upgrade
    un bomber perd un point de vie
    une autre bombe qui subit une explosion va exploser à son tour
    une fois tous les effets cidessus résolus pour la première bombe. On peut ainsi avoir des explosions en chaîne.
    """
    portee = 1 + dic_bomber["Niv"] // 2

    dic_cases_affectees_relatives = {
        "haut":[],
        "droite":[],
        "bas":[],
        "gauche":[]
    }

    directions_valides = list(dic_cases_affectees_relatives.keys())

    # Pour les 4 cases adjacentes
    if case_valide_pour_explosion(grille, coord[0]-1, coord[1]):
        dic_cases_affectees_relatives["haut"].append((-1, 0))
        if "M" in grille[coord[0]-1][coord[1]]:
            directions_valides.remove("haut") # Le mur est détruit mais l'explosion s'arrête là
    else:
        directions_valides.remove("haut")

    if case_valide_pour_explosion(grille, coord[0], coord[1]+1):
        dic_cases_affectees_relatives["droite"].append((0, 1))
        if "M" in grille[coord[0]][coord[1]+1]:
            directions_valides.remove("droite") # Le mur est détruit mais l'explosion s'arrête là
    else:
        directions_valides.remove("droite")

    if case_valide_pour_explosion(grille, coord[0]+1, coord[1]):
        dic_cases_affectees_relatives["bas"].append((1, 0))
        if "M" in grille[coord[0]+1][coord[1]]:
            directions_valides.remove("bas") # Le mur est détruit mais l'explosion s'arrête là
    else:
        directions_valides.remove("bas")

    if case_valide_pour_explosion(grille, coord[0], coord[1]-1):
        dic_cases_affectees_relatives["gauche"].append((0, -1))
        if "M" in grille[coord[0]][coord[1]-1]:
            directions_valides.remove("gauche") # Le mur est détruit mais l'explosion s'arrête là
    else:
        directions_valides.remove("gauche")


    if portee == 1:
        return dic_cases_affectees_relatives


    # Généralisation aux cases plus lointaines si la portée le permet
    for i in range(2, portee+1):
        for direction in directions_valides:
            # i sert comme un scalaire pour les 4 vecteurs donnant les directions à l'explosion
            propagee = (dic_cases_affectees_relatives[direction][-1][0]*i, dic_cases_affectees_relatives[direction][-1][1]*i)
            # pour passer de coordonnées relatives à absolues : coord[0]+el[0], coord[1]+el[1]. coord sont les coordonnées absolues du point à partir desquelles les coordonnées relatives de el sont basées. L'addition des deux donnent les coordonnées absolues de el, càd dans la grille plutôt que par rapport au point de coordonnées coord, càd la bombe
            if not case_valide_pour_explosion(grille, coord[0]+propagee[0], coord[1]+propagee[1]):
                directions_valides.remove(direction)
                # On a rencontré une colonne : la direction n'est plus valide
            elif "M" in grille[coord[0]+propagee[0]][coord[1]+propagee[1]]:
                dic_cases_affectees_relatives[direction].append(propagee)
                directions_valides.remove(direction)
                # Le mur est détruit mais l'explosion s'arrête là
            else:
                dic_cases_affectees_relatives[direction].append(propagee)

    return cases_relatives_vers_absolues(coord, dic_cases_affectees_relatives)




def exploser_bombe(grille, coord, dic_bomber):  # niv = None à changer

    # "La portée de ses bombes, égale à 1 + Niv / 2" = +1 case de portée tous les 2 niveaux, à part au niveau 2 où il gagne directement 1 case de portée

    """
    # Vérifie la zone d'explosion
    # Portée de 1 dans les 4 directions par défaut
    for coord_explosion in [(coord[0] - 1, coord[1]), (coord[0], coord[1] + 1), (coord[0] + 1, coord[1]),
                            (coord[0], coord[1] - 1)]:
        if 0 <= coord_explosion[0] <= len(grille) - 1 and 0 <= coord_explosion[1] <= len(grille[0]) - 1:
            if "M" in grille[coord_explosion[0]][coord_explosion[1]]:
                grille[coord_explosion[0]][coord_explosion[1]].remove("M")
            if "P" in grille[coord_explosion[0]][coord_explosion[1]]:
                pass  # à voir
    """
    dic_cases_affectees = calculer_cases_affectees(grille, coord, dic_bomber)

    for direction in dic_cases_affectees.keys():
        for coord_explosion in dic_cases_affectees[direction]:
            if "M" in grille[coord_explosion[0]][coord_explosion[1]]:
                grille[coord_explosion[0]][coord_explosion[1]].remove("M")
                dic_bomber["Score"] += 1
            # à voir
            if "P" in grille[coord_explosion[0]][coord_explosion[1]]:
                pass
            if "F" in grille[coord_explosion[0]][coord_explosion[1]]:
                pass
            if "B" in grille[coord_explosion[0]][coord_explosion[1]]:
                pass
            if "U" in grille[coord_explosion[0]][coord_explosion[1]]:
                pass

    # Supprime la bombe
    grille[coord[0]][coord[1]].remove("B")
