def render_explosions_apparition(grille, g, cases_affectees, dic_jeu):

    dimensions_case = dic_jeu["case_dimensions"]

    coords_affectees = list()
    for liste in list(cases_affectees.values()):
        for coord in liste:
                coords_affectees.append(coord)

    objets_graphiques_explosions = list()

    for coord in coords_affectees:
        coord_x = coord[1] * dimensions_case[0]
        coord_y = coord[0] * dimensions_case[1]

        obj = g.afficherImage(coord_x, coord_y, (dimensions_case[0], dimensions_case[1]), "sprites/explosion.png")
        objets_graphiques_explosions.append(obj)

    return objets_graphiques_explosions

def render_explosions_suppression(g, objets_graphiques_explosions):

    for obj in objets_graphiques_explosions:

        g.supprimer(obj)


def render_timers_et_score(g, dic_jeu, game_settings):

    if dic_jeu["objets_graphiques_overlay"]:
        for objet in dic_jeu["objets_graphiques_overlay"]:
            g.supprimer(objet)

    dic_jeu["objets_graphiques_overlay"].append(
        g.afficherTexte(f"PV: {dic_jeu['bomber'].pv}", 3 * dic_jeu["fenetre_dimensions"][0] // 4,
                        1.5 * dic_jeu["fenetre_dimensions"][1] // 5, taille=15, ancre="w"))
    dic_jeu["objets_graphiques_overlay"].append(
        g.afficherTexte(f"Niveau: {dic_jeu['bomber'].niv}", 3*dic_jeu["fenetre_dimensions"][0]//4,
                        2 * dic_jeu["fenetre_dimensions"][1] // 5, taille = 15, ancre = "w"))
    dic_jeu["objets_graphiques_overlay"].append(
        g.afficherTexte(f"Score: {dic_jeu['bomber'].score}", 3 * dic_jeu["fenetre_dimensions"][0] // 4,
                        2.5 * dic_jeu["fenetre_dimensions"][1] // 5, taille=15, ancre="w"))
    dic_jeu["objets_graphiques_overlay"].append(
        g.afficherTexte(f"Timer global: {game_settings["timer"]}", 3*dic_jeu["fenetre_dimensions"][0]//4,
                        3 * dic_jeu["fenetre_dimensions"][1] // 5, taille = 15, ancre = "w"))
    dic_jeu["objets_graphiques_overlay"].append(
        g.afficherTexte(f"Timer fantome: {game_settings["timer_fantome"]}", 3*dic_jeu["fenetre_dimensions"][0]//4,
                        3.5 * dic_jeu["fenetre_dimensions"][1] // 5, taille = 15, ancre = "w"))
