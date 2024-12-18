def pos_bomber(grille:list[list[list[str]]])->list[int]:
    for y in range(len(grille)):
        for x in range(len(grille[0])):
            if "P" in grille[y][x]:
                return [y, x]
