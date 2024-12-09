import tkiteasy

from main import *


g = tkiteasy.ouvrirFenetre(400, 400)  # taille à changer

# grille : list[list[list[str]]]
grille = [
    [["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"]],
    [["C"], [], [], ["P"], [], [], [], [], ["C"]],
    [["C"], ["M"], ["C"], ["M"], ["C"], ["M"], ["C"], ["M"], ["C"]],
    [["C"], ["M"], ["M"], ["M"], ["M"], [], ["E"], [], ["C"]],
    [["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"]]
]

dic_bombes = {}

dic_bomber = {
    "PV":3,
    "Niv":1,
    "Score":0
}

# timer global = 100; comment gérer sans 'global' ?


main(grille, g, dic_bombes, dic_bomber)
