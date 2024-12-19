import tkiteasy

from main import *


fenetre_dimensions = (500, 500) # (1280, 960)
g = tkiteasy.ouvrirFenetre(fenetre_dimensions[0], fenetre_dimensions[1])

dic_jeu = {

    "murs": [],

    "colonnes": [],

    "ethernets": [],
    # On considère qu'il peut y avoir plusieurs bombers en préparation de la partie 2 de la SAE
    "bombers": [],

    "fantomes": [],

    "upgrades": [],

    "bombes": [],



    "sprites": {
        "bomber": {
            "bas": ["asset/bunny/down/down1.png", "asset/bunny/down/down2.png"],
            "gauche": ["asset/bunny/left/left1.png", "asset/bunny/left/left2.png"],
            "droite": ["asset/bunny/right/right1.png", "asset/bunny/right/right2.png"],
            "haut": ["asset/bunny/up/up1.png", "asset/bunny/up/up2.png"],
            "pose": ["asset/bunny/pose/poseBombe.png"]
        },
        "fantomes": {
            "bas": ["asset/bunny/down/down1.png", "asset/bunny/down/down2.png"],
            "gauche": ["asset/bunny/left/left1.png", "asset/bunny/left/left2.png"],
            "droite": ["asset/bunny/right/right1.png", "asset/bunny/right/right2.png"],
            "haut": ["asset/bunny/up/up1.png", "asset/bunny/up/up2.png"],
        },

        "bombes": {
            "bas": ["sprites/bombe.png", "sprites/bombe1.png", "sprites/bombe2.png", "sprites/bombe3.png"]
        }
    }

}

grille = generer_grille_et_dic_jeu(7, 7, g, dic_jeu)

default_game_settings = {
    "timer" : 200,
    "timer_fantome": 20,
    "nombre_fantomes": 0
}




main(g, fenetre_dimensions, grille, dic_jeu, default_game_settings)
