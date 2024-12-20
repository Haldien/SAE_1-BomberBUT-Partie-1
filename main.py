from objets import *

from time import sleep

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
    if touche in ["z", "q", "s", "d"]:
        # On ne passe pas de tout si la case n'est pas valide
        if not case_valide(grille, dic_jeu["bomber"].pos[0] + mouvements[touche][0], dic_jeu["bomber"].pos[1] + mouvements[touche][1]):
            while True:
                touche = g.attendreTouche()
                if touche in ["z", "q", "s", "d"] and case_valide(grille, dic_jeu["bomber"].pos[0] + mouvements[touche][0], dic_jeu["bomber"].pos[1] + mouvements[touche][1]):
                    dic_jeu["bomber"].se_deplacer((dic_jeu["bomber"].pos[0] + mouvements[touche][0], dic_jeu["bomber"].pos[1] + mouvements[touche][1]), "P")
                    break
                elif touche in ["Return", "space"]:
                    break

        else:
            dic_jeu["bomber"].se_deplacer((dic_jeu["bomber"].pos[0] + mouvements[touche][0], dic_jeu["bomber"].pos[1] + mouvements[touche][1]),"P")


    # Dépose un bombe
    if touche == "space":
        dic_jeu["bomber"].poser_bombe(dic_jeu["bomber"].pos)

    # Passe son tour
    if touche == "Return":
        pass

def deplacement_fantomes(dic_jeu):

    for fantome in dic_jeu["fantomes"]:
        fantome.se_deplacer_random()

def attaque_fantomes(dic_jeu):
    dic_jeu["bomber"].se_faire_attaquer()

def apparition_fantomes(dic_jeu, game_settings):
    if game_settings["timer_fantome"] == 1:
        random_liste_ethernets = dic_jeu["ethernets"].copy()
        random.shuffle(random_liste_ethernets)

        for prise in random_liste_ethernets:
            if prise.spawner():  # Jusqu'à ce que un prise spawn un fantôme
                break  # Un seul spawn de fantôme

def explosions(dic_jeu):

    # a_exploser : bombes dont le timer est 0
    a_exploser = [bombe for bombe in dic_jeu["bombes"] if bombe.timer == 0]

    objets_graphiques_explosions = list()

    for bombe in a_exploser:
        objets_graphiques_explosions = bombe.s_exploser()

    return objets_graphiques_explosions


def updater_timers(dic_jeu, game_settings, default_game_settings):
    updater_timers_bombes(dic_jeu)
    updater_timers_game_settings(game_settings, default_game_settings)



"""
MAIN
"""
def main(g):
    zone_affichage_largeur = fenetre_dimensions[0]//4

    # game_settings : live game settings
    game_settings = default_game_settings.copy()

    objets_graphiques_explosions = None  # Pour la 1ère itération

    render_timers_et_score(g, dic_jeu, game_settings)  # Partie graphique, pour avoir l'overlay dès le début

    while game_settings["timer"] > 0 and dic_jeu["bomber"].pv > 0:

        touche = g.recupererTouche()

        # Partie graphique. Doit être après "touche = g.recupererTouche()" pour que les explosions apparaissent
        if objets_graphiques_explosions:
            sleep(0.2)
            render_explosions_suppression(g, objets_graphiques_explosions)
            objets_graphiques_explosions = list()

        if touche is not None:

            if touche in ["z", "q", "s", "d", "space", "Return"]:

                action_bomber(g, grille, touche, dic_jeu)

                deplacement_fantomes(dic_jeu)

                attaque_fantomes(dic_jeu)

                apparition_fantomes(dic_jeu, game_settings)

                updater_timers(dic_jeu, game_settings, default_game_settings)

                objets_graphiques_explosions = explosions(dic_jeu)
                # Partie graphique ^

                render_timers_et_score(g, dic_jeu, game_settings)  # Partie graphique


                # Affichage pour tester
                affichage_grille(grille)
                affichage_dic_jeu(dic_jeu)
                # affichage_game_settings(game_settings)


    render_supprimer_jeu(g, dic_jeu)
