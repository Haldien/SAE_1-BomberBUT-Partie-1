import tkiteasy

from main import *


global TAILLE_FENETRE

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

grille = create_map("map0")

"""
    les Dictionnaires
"""
dic_jeu = {

    "bomber": {
        'pos': (0,0),
        'PV' : 3,
        'Niv': 0,
        'Score': 0,
        'cooldown' : 0

    },

    "bombes" : {

    },

    "ethernet" : {
        "pos" : [(3,6)],
    },

    "fantomes" : {
    }

}


settings = {
    "timer" : 200,
    "timerfantome": 20,
    "nombrefantome": 0
}


"""
    Faudrait que dans la fonction main, avant l'appel de la boucle énorme on est une première definition du timer
    du style un int, ou même une variable dans un dico
    Et comme ça à chaque appel de boucle on fait en sorte que le timer se modifie
"""

main(grille, g, dic_jeu, settings)
