



def pos_bomber(grille:list[list[list[str]]])->list[int]:
    for y in range(len(grille)):
        for x in range(len(grille[0])):
            if "P" in grille[y][x]:
                return [y, x]

def deplacer_bomber(grille, y: int, x: int, dic_jeu):

    if "U" in grille[y][x]:
        grille[y][x].remove("U")

        #on limite le niveau à 4
        if dic_jeu["bomber"]["Niv"] < 4:
            level_up(dic_jeu)


    grille[dic_jeu["bomber"]["pos"][0]][dic_jeu["bomber"]["pos"][1]].remove("P")
    grille[y][x].append("P")

    dic_jeu["bomber"]["pos"] = (y ,x)

def level_up(dic_jeu):

    dic_jeu["bomber"]["Niv"] += 1

    if dic_jeu["bomber"]["Niv"] in [1, 3]:
        dic_jeu["bomber"]["PV"] += 1







