import tkiteasy

from main import *


grille_dimensions = (21, 21)  # !! Y, X

fenetre_dimensions = (800, 600)  # !! X, Y (1280, 960)



g = tkiteasy.ouvrirFenetre(fenetre_dimensions[0], fenetre_dimensions[1])


main(g, grille, dic_jeu, default_game_settings)
