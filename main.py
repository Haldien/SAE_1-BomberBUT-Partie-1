from bomber import *
from fantomes import *
from bombes import *
from timers import *
from fonctions_utiles import *


"""
Fonctions principales
"""
def action_bomber(grille, touche: str, dic_jeu):

    # Mappings des touches vers les vecteurs de mouvements correspondant
    mouvements = {
        "z": [-1, 0],
        "q": [0, -1],
        "s": [1, 0],
        "d": [0, 1]
    }

    # Mouvements
    if touche in ["z", "q", "s", "d"] and case_valide(grille, dic_jeu["bomber"]["pos"][0] + mouvements[touche][0], dic_jeu["bomber"]["pos"][1] + mouvements[touche][1]):

        deplacer_bomber(grille, dic_jeu["bomber"]["pos"][0] + mouvements[touche][0], dic_jeu["bomber"]["pos"][1] + mouvements[touche][1], dic_jeu)

    # Dépose un bombe
    elif touche == "space":

        poser_bombe(grille, dic_jeu, dic_jeu["bomber"]["pos"][0], dic_jeu["bomber"]["pos"][1])

    # Passe son tour
    elif touche == "Return":
        pass

def resoudre_action():
    pass

def updater_timers(dic_jeu):
    updater_timers_bombes(dic_jeu)

def explosions(grille, dic_jeu):

    # Vérifie le timer de chaque bombe
    a_exploser = [coord for coord in dic_jeu["bombes"] if dic_jeu["bombes"][coord] == 0]

    for coord in a_exploser:
        exploser_bombe(grille, coord, dic_jeu)



"""
MAIN
"""
def main(grille, g, dic_jeu, settings):

    DEFAULT_SETTING = settings.copy() 
    OnGameSettings = DEFAULT_SETTING.copy()

    fantomes = dic_jeu["fantomes"]
    ethernet = dic_jeu["ethernet"]

    # pos initiale
    dic_jeu["bomber"]["pos"] = pos_bomber(grille)
    
    while OnGameSettings["timer"] > 0 and dic_jeu["bomber"]["PV"] > 0:

        # affichage dans le terminal pour les tests
        affichage_grille(grille)
        print("bombes:", dic_jeu["bombes"])
        print("bomber:", dic_jeu["bomber"])

        print("fantome:", dic_jeu["fantomes"])
        print("ethernet:", dic_jeu["ethernet"])
        print(f"TIMER : {OnGameSettings['timer']}              TIMERFANTOME : {OnGameSettings['timerfantome']}")

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
            action_bomber(grille, touche, dic_jeu)

            resoudre_action()
            
            updater_timers(dic_jeu)

            explosions(grille, dic_jeu)
            
            if len(fantomes) > 0:
                if dic_jeu["bomber"]["cooldown"] <= 0: # Dans le cas où il y a plusieurs dégâts en même temps, ça ne s'additionne pas pendant une courte durée
                    attaque_fantome(grille,dic_jeu)
                deplacer_fantomes(grille, fantomes)

            
    
            if OnGameSettings["timerfantome"] == 0:
                apparition_fantomes(grille,dic_jeu, OnGameSettings)
                OnGameSettings["timerfantome"] = DEFAULT_SETTING["timerfantome"]
            
            round_timer(OnGameSettings)
            # render()


    
    for i in range(3):
        print("\n")
    print("---------------------------------------------------------\n\n\n")
    print("Partie Terminée".center(55))
    print("\n\n\n---------------------------------------------------------")

