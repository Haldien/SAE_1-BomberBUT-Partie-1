import tkiteasy

from main import *


grille_dimensions = (21, 21)  # !! Y, X

fenetre_dimensions = (800, 600)  # !! X, Y (1280, 960)

zone_affichage_largeur = fenetre_dimensions[0]//4

g = tkiteasy.ouvrirFenetre(fenetre_dimensions[0], fenetre_dimensions[1])

dic_jeu = {

    "murs": [],

    "colonnes": [],

    "ethernets": [],

    "bombers": None,

    "fantomes": [],

    "upgrades": [],

    "bombes": [],



    "case_dimensions": ((fenetre_dimensions[0]-zone_affichage_largeur)//grille_dimensions[1], fenetre_dimensions[1]//grille_dimensions[0]) if fenetre_dimensions[1]//grille_dimensions[0] < 100 else (96, 96),

    "fenetre_dimensions": fenetre_dimensions,

    "objets_graphiques_overlay": []
}

grille = generer_grille_et_dic_jeu(grille_dimensions[0], grille_dimensions[1], g, dic_jeu)

default_game_settings = {
    "timer": 200,
    "timer_fantome": 20,
    "nombre_fantomes": 0
}

main(g, grille, dic_jeu, default_game_settings)
