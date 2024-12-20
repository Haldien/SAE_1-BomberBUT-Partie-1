def updater_timers_bombes(dic_jeu):
    for key in dic_jeu["bombes"].keys():
        dic_jeu["bombes"][key]["timer"] -= 1
        dic_jeu["bombes"][key]["obj"].ignite(dic_jeu["bombes"][key]["timer"])
        
def round_timer(gameSetting:dict) -> None:
    """
        Cette fonction prend en paramètre un dictionnaire qui répertorie 
        les détails du "scénario" du niveau.

        Cette fonction doit être appelé à chaque boucle pour actualiser le tour.
    """
    gameSetting['timer'] -= 1
    gameSetting['timerfantome'] -= 1
