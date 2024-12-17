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

    "bomber": {},

    "bombes" : {

    },

    "ethernet" : {

    },

    "fantomes" : {

    },

    "mur" : {

    },

    "upgrade" : {
        
    }
 

}

settings = {
    "timer" : 200,
    "timerfantome": 30,
    "nombrefantome": 0,
    "size": None,
    "offset" : None
}

"""
scenario = get_scenario("map0")
main(scenario[2], g, scenario[0], scenario[1])

scenario = get_scenario("map1")
main(scenario[2], g, scenario[0], scenario[1])
"""

main(grille, g, dic_jeu, settings)
