import tkiteasy

from main import *


#global TAILLE_FENETRE

g = tkiteasy.ouvrirFenetre(TAILLE_FENETRE[0], TAILLE_FENETRE[1])  # taille à changer

# grille : list[list[list[str]]]
grille = [
    [["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"]],
    [["C"], [], [], ["P"], [], [], [], [], ["C"]],
    [["C"], ["M"], ["C"], ["M"], ["C"], ["M"], ["C"], ["M"], ["C"]],
    [["C"], ["M"], ["M"], ["M"], ["M"], [], ["E"], [], ["C"]],
    [["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"]]
]

# grille de test pour le déplacement des fantômes
grille = [
    [["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"]],
    [["C"], [   ], [   ], ["P"], [   ], [   ], [   ], [   ], ["C"]],
    [["C"], ["M"], ["C"], ["M"], ["C"], ["M"], ["C"], ["M"], ["C"]],
    [["C"], [   ], [   ], [   ], [   ], [   ], ["E"], [   ], ["C"]],
    [["C"], ["M"], ["C"], ["M"], ["C"], ["M"], ["C"], ["M"], ["C"]],
    [["C"], ["U"], [   ], ["M"], ["M"], ["M"], [   ], ["U"], ["C"]],
    [["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"]]     
] 

#grille = create_map("map0")

"""
    les Dictionnaires
"""
dic_jeu = {

    "bomber": {
        'pos': (0,0),
        'PV' : 3,
        'Niv': 0,
        'Score': 0,
        'cooldown' : 0,
        'obj': None,
        'direction': 'bas',
        'index_sprite': 0,
       

    },

    "bombes" : {

    },

    "ethernet" : {
        "pos" : [(3,6)],
        "obj" : None
    },

    "fantomes" : {
        # {"obj" :"objetGraphique", "pos": (tuple), "direction" : direction:str}
    },

    "mur" : {},

    "sprite" : {
        "bomber" : {
            "bas" : ["asset/bunny/down/down1.png","asset/bunny/down/down2.png"],
            "gauche": ["asset/bunny/left/left1.png","asset/bunny/left/left2.png"],
            "droite": ["asset/bunny/right/right1.png", "asset/bunny/right/right2.png"],
            "haut": ["asset/bunny/up/up1.png", "asset/bunny/up/up2.png"],
            "pose": ["asset/bunny/pose/poseBombe.png"]
        } ,
        "fantomes" : {
            "bas" : ["asset/bunny/down/down1.png","asset/bunny/down/down2.png"],
            "gauche": ["asset/bunny/left/left1.png","asset/bunny/left/left2.png"],
            "droite": ["asset/bunny/right/right1.png", "asset/bunny/right/right2.png"],
            "haut": ["asset/bunny/up/up1.png", "asset/bunny/up/up2.png"],
        }, 
        
        "bombes" : {
            "bas" : ["sprites/bombe.png","sprites/bombe1.png", "sprites/bombe2.png", "sprites/bombe3s.png"] 
        }
    }

}

settings = {
    "timer" : 200,
    "timerfantome": 30,
    "nombrefantome": 0,
    "size": None
}

"""
scenario = get_scenario("map0")
main(scenario[2], g, scenario[0], scenario[1])
"""






main(grille, g, dic_jeu, settings)
