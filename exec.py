import tkiteasy

from main import *

#  PV : pv du bomber, NIV : niveau du bomber

g = tkiteasy.ouvrirFenetre(400, 400)  # taille à changer

# grille est une liste, pas besoin de global
# grille : list[list[list[str]]]
grille = [
    [["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"]],
    [["C"], [   ], [   ], ["P"], [   ], [   ], [   ], [   ], ["C"]],
    [["C"], ["M"], ["C"], ["M"], ["C"], ["M"], ["C"], ["M"], ["C"]],
    [["C"], ["M"], ["M"], ["M"], ["M"], [   ], ["E"], [   ], ["C"]],
    [["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"]]
]

dic_bombes = {}

timer_global = 20 # à voir



main(grille, g, dic_bombes)
