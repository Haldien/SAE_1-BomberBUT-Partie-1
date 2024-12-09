

def pos_bomber(grille:list[list[list[str]]])->list[int]:
    for y in range(len(grille)):
        for x in range(len(grille[0])):
            if "P" in grille[y][x]:
                return [y, x]

def deplacer_bomber(grille, y: int, x: int):

    if grille[y][x] == "U":
        pass # à voir

    grille[pos_bomber(grille)[0]][pos_bomber(grille)[1]].remove("P")
    grille[y][x].append("P"))
