from objets import *

from fonctions_utiles import *

from generation_grille import *

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

def deplacement_fantomes(dic_jeu):

    for fantome in dic_jeu["fantomes"]:
        fantome.se_deplacer_random()

def attaque_fantomes(dic_jeu):
    for fantome in dic_jeu["fantomes"]:
        fantome.attaquer()

def apparition_fantomes(dic_jeu, game_settings):
    if game_settings["timer_fantome"] == 1:
        for prise_ethernet in dic_jeu["ethernets"]:
            prise_ethernet.spawner()

def explosions(dic_jeu):

    # a_exploser : bombes dont le timer est 0
    a_exploser = [bombe for bombe in dic_jeu["bombes"] if bombe.timer == 0]

    for bombe in a_exploser:
        bombe.s_exploser()

def updater_timers(dic_jeu, game_settings, default_game_settings):
    updater_timers_bombes(dic_jeu)
    updater_timers_game_settings(game_settings, default_game_settings)



"""
MAIN
"""
def main(g, fenetre_dimensions, grille, dic_jeu, default_game_settings):

    # game_settings : live game settings
    game_settings = default_game_settings.copy()

    while game_settings["timer"] > 0 and dic_jeu["bomber"].pv > 0:

        touche = g.recupererTouche()

        if touche is not None:

            if touche in ["z", "q", "s", "d", "space", "Return"]:

                action_bomber(g, grille, touche, dic_jeu)

                deplacement_fantomes(dic_jeu)

                attaque_fantomes(dic_jeu)

                apparition_fantomes(dic_jeu, game_settings)

                updater_timers(dic_jeu, game_settings, default_game_settings)

                explosions(dic_jeu)


                # Affichage pour tester
                affichage_grille(grille)
                affichage_dic_jeu(dic_jeu)
                affichage_game_settings(game_settings)


