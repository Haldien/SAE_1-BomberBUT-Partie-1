def get_scenario(nomMap:str) -> tuple[dict, dict, list[list[list[str]]]]:
    """
    Cette fonction permet de générer le dic_jeu qui répertorie tout les objets particulier ainsi que les paramètres du jeu
    bomber, bombes, ethernet et fantôme.
    """
    dic_jeu = {
        "bomber": { 
            
        },

        "bombes" : {
        },

        "ethernet" : {
            "pos" : [(3,6)], "obj" : None
        },

        "fantomes" : {
            # {"obj" :"objetGraphique", "pos": (tuple), "direction" : direction:str}
        },

        "mur" : {
        },

        

    }

    settings = {
        "timer" : 100,
        "timerfantome": 20,
        "nombrefantome": 0,
        "size" : None
    }

    param = get_param(nomMap)
    settings['timer'], settings['timerfantome'] = param[0], param[1]

    grille = create_map(nomMap)
    for y in range(len(grille)):
        for x in range(len(grille[0])):
            if "P" in grille[y][x]:
                dic_jeu["bomber"]["pos"] = (y,x)
            elif "E" in grille[y][x]:
                dic_jeu["ethernet"]["pos"] += [(y,x)]
            elif "F" in grille[y][x]:
                grille[y][x][0] += str(settings["nombrefantome"])
                dic_jeu["fantomes"] = {f"F{settings["nombrefantome"]}" : ["ObjetGraphique", (y,x)]}
                settings["nombrefantome"] += 1

    
    return (dic_jeu, settings, grille)


    
