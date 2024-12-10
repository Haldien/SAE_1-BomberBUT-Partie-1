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



def explosions(grille, dic_bombes, dic_bomber):

    # Vérifie le timer de chaque bombe
    a_exploser = [coord for coord in dic_bombes if dic_bombes[coord] == 0]

    for coord in a_exploser:
        exploser_bombe(grille, coord, dic_bombes, dic_bomber)



"""
MAIN
"""
def main(grille, g, dic_bombes, dic_bomber):

    while True:

        # affichage dans le terminal pour les tests
        affichage_grille(grille)
        print("dic_bombes:", dic_bombes)
        print("dic_bomber:", dic_bomber)

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

            explosions(grille, dic_bombes, dic_bomber)

            # render()
