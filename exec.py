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


dic_fantome = {}
dic_prise = { "E" : []}

dic_bombes = {}
dic_bomber = {
    "PV":3,
    "Niv":0,
    "Score":0
}

# timer global = 100; comment gérer sans 'global' ?

"""
    Faudrait que dans la fonction main, avant l'appel de la boucle énorme on est une première definition du timer
    du style un int, ou même une variable dans un dico
    Et comme ça à chaque appel de boucle on fait en sorte que le timer se modifie
"""

main(grille, g, dic_bombes, dic_bomber)
