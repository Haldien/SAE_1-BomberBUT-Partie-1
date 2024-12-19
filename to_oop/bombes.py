

def cases_relatives_vers_absolues(coord, dic_cases_affectees_relatives):
    dic_cases_affectees_absolues = {
        "haut": [],
        "droite": [],
        "bas": [],
        "gauche": []
    }

    for direction in dic_cases_affectees_relatives.keys():
        for el in dic_cases_affectees_relatives[direction]:
            # pour passer de coordonnées relatives à absolues : coord[0]+el[0], coord[1]+el[1]. coord sont les coordonnées absolues du point à partir desquelles les coordonnées relatives de el sont basées. L'addition des deux donnent les coordonnées absolues de el, càd dans la grille plutôt que par rapport au point de coordonnées coord, càd la bombe
            dic_cases_affectees_absolues[direction].append((coord[0] + el[0], coord[1] + el[1]))

    return dic_cases_affectees_absolues

def case_valide_pour_explosion(grille, y, x) -> bool:
    # Les cases non valides sont celles en dehors de la grille et les colonnes. Les prises ethernet sont considérées comme valides pour une explosion
    if not (0 <= y <= len(grille) - 1 and 0 <= x <= len(grille[0]) - 1) or "C" in grille[y][x]:
        return False
    return True



