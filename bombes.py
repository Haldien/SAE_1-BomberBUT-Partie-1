
def poser_bombe(grille, dic_bombes, y:int, x:int):
    if "B" not in grille[y][x] :
        grille[y][x].append("B")
        ajouter_a_dic_bombes(dic_bombes, y ,x)

def ajouter_a_dic_bombes(dic_bombes, y, x):
    dic_bombes[(y, x)] = 5




def exploser_bombe(grille, coord, niv=None):# niv = None à changer

    # Vérifie la zone d'explosion
    # Portée de 1 dans les 4 directions par défaut
    for coord_explosion in [(coord[0]-1, coord[1]), (coord[0], coord[1]+1), (coord[0]+1, coord[1]),(coord[0], coord[1]-1)]:
        if 0 <= coord_explosion[0] <= len(grille) - 1 and 0 <=  coord_explosion[1] <= len(grille[0]) - 1:
            if "M" in grille[coord_explosion[0]][coord_explosion[1]]:
                grille[coord_explosion[0]][coord_explosion[1]].remove("M")
            if "P" in grille[coord_explosion[0]][coord_explosion[1]]:
                pass # à voir

    # Supprime la bombe
    grille[coord[0]][coord[1]].remove("B")
