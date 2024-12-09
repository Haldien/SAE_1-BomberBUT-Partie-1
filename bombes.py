
def poser_bombe(grille, dic_bombes, y:int, x:int):
    if "B" not in grille[y][x] :
        grille[y][x].append("B")
        ajouter_a_dic_bombes(dic_bombes, y ,x)

def ajouter_a_dic_bombes(dic_bombes, y, x):

    dic_bombes[(y, x)] = 5