from bomber import *
from fantomes import *
from bombes import *
from timers import *
from render import *
from fonctions_utiles import *
from time import sleep

"""
Fonctions principales
"""
"""


16:9

avec le jeu au centre de l'écran


"""







def action_bomber(g, grille,settings, touche: str, dic_jeu):
    # Mappings des touches vers les vecteurs de mouvements correspondant
    mouvements = {
        "z": [-1, 0],
        "q": [0, -1],
        "s": [1, 0],
        "d": [0, 1]
    }

    match(touche):
        case "z":
            dic_jeu["bomber"]["direction"] = "haut"
        case "q":
            dic_jeu["bomber"]["direction"] = "gauche"
        case "s":
            dic_jeu["bomber"]["direction"] = "bas"
        case "d":
            dic_jeu["bomber"]["direction"] = "droite"
    

    # Mouvements
    if touche in ["z", "q", "s", "d"] and case_valide(grille, dic_jeu["bomber"]["pos"][0] + mouvements[touche][0],
                                                      dic_jeu["bomber"]["pos"][1] + mouvements[touche][1], dic_jeu):
        

        deplacer_bomber(grille, dic_jeu["bomber"]["pos"][0] + mouvements[touche][0],
                        dic_jeu["bomber"]["pos"][1] + mouvements[touche][1], dic_jeu)

    # Dépose un bombe
    elif touche == "space":
        dic_jeu["bomber"]["direction"] = "pose"
        poser_bombe(g, grille, dic_jeu, settings, dic_jeu["bomber"]["pos"][0], dic_jeu["bomber"]["pos"][1])

    # Passe son tour
    elif touche == "Return":
        pass


def resoudre_action():
    pass


def updater_timers(dic_jeu, settings):
    updater_timers_bombes(dic_jeu)
    round_timer(settings)


def explosions(grille, g, dic_jeu)->list[ObjetGraphique]:

    # a_exploser : bombes dont le timer est 0
    a_exploser = [coord for coord in dic_jeu["bombes"] if dic_jeu["bombes"][coord]['timer'] == 0]

    objets_graphiques_explosions = list()

    for coord in a_exploser:
        objets_graphiques_explosions = exploser_bombe(grille, g, coord, dic_jeu)

    return objets_graphiques_explosions

"""
MAIN
"""
def main(grille, g, dic_jeu, settings):

    settings["size"] = dimensions_de_case(grille)

    DEFAULT_SETTING = settings.copy()
    OnGameSettings = DEFAULT_SETTING.copy()
    print(OnGameSettings)
    fantomes = dic_jeu["fantomes"]
    ethernet = dic_jeu["ethernet"]

    # pos initiale
    dic_jeu["bomber"]["pos"] = pos_bomber(grille)
    # affichage initial
    #objets_graphiques = render(grille, g, dic_jeu)


    objets_graphiques_explosions = list()
    render_undestructible(g, grille)
    spawn_bomber(g,dic_jeu, OnGameSettings)
    get_wall(g, grille, dic_jeu)



        
    
    while OnGameSettings["timer"] > 0 and dic_jeu["bomber"]["PV"] > 0:

        touche = g.recupererTouche()

        if objets_graphiques_explosions:
            sleep(0.2)
            render_explosions_suppression(g, objets_graphiques_explosions)
            objets_graphiques_explosions = list()

        if touche is not None:

            if touche in ["z", "q", "s", "d", "space", "Return"]:
                # affichage dans le terminal pour les tests
                """
                affichage_grille(grille)
                print("bombes:", dic_jeu["bombes"])
                print("bomber:", dic_jeu["bomber"])

                print("fantome:", dic_jeu["fantomes"])
                print("ethernet:", dic_jeu["ethernet"])
                print(f"TIMER : {OnGameSettings['timer']}              TIMERFANTOME : {OnGameSettings['timerfantome']}")
                """
                """
                1. décision de l'action du bomber
                2. résolution de l'action
                3. déplacement des fantômes
                4. attaque des fantômes
                5. apparition de nouveaux fantômes
                6. réduction des timers et les explosions
                """
                action_bomber(g, grille,OnGameSettings, touche, dic_jeu)
                dep_bomber(dic_jeu)

                resoudre_action()

                updater_timers(dic_jeu, OnGameSettings)

                if len(fantomes) > 0:
                    if dic_jeu["bomber"]["cooldown"] <= 0:  # Dans le cas où il y a plusieurs dégâts en même temps, ça ne s'additionne pas pendant une courte durée
                        attaque_fantome(grille, dic_jeu)
                    
                    
                    

                if OnGameSettings["timerfantome"] == 0:
                    apparition_fantomes(grille, dic_jeu, OnGameSettings)
                    spawn_fantome(g, dic_jeu,OnGameSettings)
                    OnGameSettings["timerfantome"] = DEFAULT_SETTING["timerfantome"]

                objets_graphiques_explosions = explosions(grille, g, dic_jeu)

                dep_fantome(dic_jeu)
                deplacer_fantomes(grille, dic_jeu)

            #objets_graphiques = render(grille, g, dic_jeu, objets_graphiques)


    for i in range(3):
        print("\n")
    print("---------------------------------------------------------\n\n\n")
    print("Partie Terminée".center(55))
    print("\n\n\n---------------------------------------------------------")

