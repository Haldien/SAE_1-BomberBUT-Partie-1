from bomber import *
from fantomes import *
from bombes import *
from timers import *
from fonctions_utiles import *


"""
Fonctions principales
"""
def action_bomber(grille, touche: str, dic_bombes):

    # Mappings des touches vers les vecteurs de mouvements correspondant
    mouvements = {
        "z": [-1, 0],
        "q": [0, -1],
        "s": [1, 0],
        "d": [0, 1]
    }

    # Mouvements
    if touche in ["z", "q", "s", "d"] and case_valide(grille, pos_bomber(grille)[0] + mouvements[touche][0], pos_bomber(grille)[1] + mouvements[touche][1]):

        deplacer_bomber(grille, pos_bomber(grille)[0] + mouvements[touche][0], pos_bomber(grille)[1] + mouvements[touche][1])


    # Dépose un bombe
    elif touche == "space":
        poser_bombe(grille, dic_bombes, pos_bomber(grille)[0], pos_bomber(grille)[1])

    # Passe son tour
    elif touche == "Return":
        pass

def resoudre_action():
    pass


def deplacer_fantomes():
    pass


def attaque_fantomes():
    pass


def faire_apparaitre_fantomes():
    pass


def updater_timers(dic_bombes):
    updater_timers_bombes(dic_bombes)


def explosions(grille, dic_bombes):


    for key in list(dic_bombes.keys()): # list() évite RuntimeError: dictionary changed size during iteration
        # timer écoulé :
        if dic_bombes[key] == 0:
            exploser_bombe(grille, key)
            dic_bombes.pop(key)


"""
MAIN
"""
def main(grille, g, dic_bombes):

    while True:

        # affichage de la grille dans le terminal pour test
        print("-----------------------------")
        for el in grille:
            print(el)
        print("dic_bombes:", dic_bombes)

        touche = g.attendreTouche()

        if touche in ["z", "q", "s", "d", "space", "Return"]:
            """
            1. décision de l'action du bomber
            2. résolution de l'action
            3. déplacement des fantômes
            4. attaque des fantômes
            5. apparition de nouveaux fantômes
            6. réduction des timers et les explosions
            """
            action_bomber(grille, touche, dic_bombes)

            resoudre_action()

            deplacer_fantomes()

            attaque_fantomes()

            faire_apparaitre_fantomes()

            updater_timers(dic_bombes)

            explosions(grille, dic_bombes)

            # render()
