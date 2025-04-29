from bombes import *
from render import *
from time import sleep

"""
Fonctions principales
"""

def resoudre_action():
    pass



def explosions(grille, g, dic_jeu, offset:tuple[int, int] = (0,0))->list[ObjetGraphique]:

    # a_exploser : bombes dont le timer est 0
    a_exploser = [coord for coord in dic_jeu["bombes"] if dic_jeu["bombes"][coord]['timer'] == 0]

    objets_graphiques_explosions = list()

    for coord in a_exploser:
        objets_graphiques_explosions = exploser_bombe(grille, g, coord, dic_jeu, offset)

    return objets_graphiques_explosions

"""
MAIN
"""
def main(grille, dic_jeu, settings, graphique):
    g = cree_fenetre(graphique)

    DEFAULT_SETTING = settings.copy()
    OnGameSettings = DEFAULT_SETTING.copy()
    
    
    print(OnGameSettings)
    fantomes = dic_jeu["fantomes"]

    # pos initiale
    # affichage initial
    #objets_graphiques = render(grille, g, dic_jeu)
    print(dic_jeu)
    
    objets_graphiques_explosions = list()
    render_undestructible(g, grille, settings["offset"])
    spawn_bomber(g,dic_jeu, OnGameSettings)
    create_object(g, grille, dic_jeu, OnGameSettings)
    affichage_grille(grille)


    while OnGameSettings["timer"] > 0 and dic_jeu["bomber"].pv > 0:

        touche = g.recupererTouche()

        if objets_graphiques_explosions:
            sleep(0.2)
            render_explosions_suppression(g, objets_graphiques_explosions)
            objets_graphiques_explosions = list()

        if touche is not None:

            if touche in ["z", "q", "s", "d", "space", "Return"]:
                # affichage dans le terminal pour les tests
                """
                print("bombes:", dic_jeu["bombes"])
                print("bomber:", dic_jeu["bomber"])
                print("fantome:", dic_jeu["fantomes"])
                print("ethernet:", dic_jeu["ethernet"])
                print(f"TIMER : {OnGameSettings['timer']}              TIMERFANTOME : {OnGameSettings['timerfantome']}")
                print(dic_jeu["bomber"].niv)
                """
                """
                1. décision de l'action du bomber
                2. résolution de l'action
                3. déplacement des fantômes
                4. attaque des fantômes
                5. apparition de nouveaux fantômes
                6. réduction des timers et les explosions
                """
                dic_jeu["bomber"].action_bomber(g, grille, touche, dic_jeu)
                
                dep_bomber(dic_jeu["bomber"])
                resoudre_action()
                print(dic_jeu["fantomes"])

                updater_timers(dic_jeu, OnGameSettings)
    

                if len(fantomes) > 0:
                              
                    for fantome in dic_jeu["fantomes"]:
                        dic_jeu["fantomes"][fantome].deplacer_fantomes(grille, dic_jeu, fantome)
                        if dic_jeu["bomber"].cooldown <= 0:  # Dans le cas où il y a plusieurs dégâts en même temps, ça ne s'additionne pas pendant une courte durée
                            dic_jeu["fantomes"][fantome].attaque_fantome(dic_jeu)
                
                if OnGameSettings["timerfantome"] == 0:
                    apparition_fantomes(g, grille, dic_jeu, OnGameSettings)
    
                    OnGameSettings["timerfantome"] = DEFAULT_SETTING["timerfantome"]

                objets_graphiques_explosions = explosions(grille, g, dic_jeu, OnGameSettings["offset"])
                for pos in dic_jeu["upgrade"]:
                    if dic_jeu["upgrade"][pos] == None:
                        dic_jeu["upgrade"][pos]= Upgrade(g, {"bas": ["sprites/upgrade.png"] }, OnGameSettings["size"], pos[1], pos[0], OnGameSettings["offset"])
       
                affichage_grille(grille)
                g.update()

    for i in range(3):
        print("\n")
    print("---------------------------------------------------------\n\n\n")
    print("Partie Terminée".center(55))
    print("\n\n\n---------------------------------------------------------")

