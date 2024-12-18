from objets import *

from fonctions_utiles import *

from timers import *



"""
FONCTIONS PRINCIPALES
"""

def action_bomber(g, grille, touche: str, dic_jeu):

    # Mappings des touches vers les vecteurs de mouvements correspondant
    mouvements = {
        "z": [-1, 0],
        "q": [0, -1],
        "s": [1, 0],
        "d": [0, 1]
    }

    # Mouvements
    if touche in ["z", "q", "s", "d"] and case_valide(grille, dic_jeu["bomber"].pos[0] + mouvements[touche][0], dic_jeu["bomber"].pos[1] + mouvements[touche][1]):
        dic_jeu["bomber"].se_deplacer((dic_jeu["bomber"].pos[0] + mouvements[touche][0], dic_jeu["bomber"].pos[1] + mouvements[touche][1]), "P")

    # Dépose un bombe
    elif touche == "space":
        dic_jeu["bomber"].poser_bombe(dic_jeu["bomber"].pos)

    # Passe son tour
    elif touche == "Return":
        pass

def explosions(grille, g, dic_jeu):

    # a_exploser : bombes dont le timer est 0
    a_exploser = [bombe for bombe in dic_jeu["bombes"] if bombe.timer == 0]

    for bombe in a_exploser:
        bombe.s_exploser()


def updater_timers(dic_jeu):
    updater_timers_bombes(dic_jeu)


"""
MAIN
"""
def main(g, grille, dic_jeu):


    while True:

        touche = g.recupererTouche()

        if touche is not None:

            if touche in ["z", "q", "s", "d", "space", "Return"]:


                action_bomber(g, grille, touche, dic_jeu)

                explosions(grille, g, dic_jeu)

                updater_timers(dic_jeu)

                # affichage
                affichage_grille(grille)
                affichage_dic_jeu(dic_jeu)


