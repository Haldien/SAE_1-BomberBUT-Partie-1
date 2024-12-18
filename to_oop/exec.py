import tkiteasy

from main import *

g = tkiteasy.ouvrirFenetre(500, 500)  # taille à changer


dic_jeu = {

    "murs": [],

    "colonnes": [],

    "ethernets": [],

    "bomber": None,

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

grille = generer_grille_et_dic_jeu(6, 6, g, dic_jeu)



main(g, grille, dic_jeu)
