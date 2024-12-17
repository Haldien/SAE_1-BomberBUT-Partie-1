from render import *

def poser_bombe(g, grille, dic_jeu, settings, y: int, x: int):

    if "B" not in grille[y][x]:
        grille[y][x].append("B")
        ajouter_a_dic_bombes(g, dic_jeu,settings, y, x)

def ajouter_a_dic_bombes(g, dic_jeu,settings, y, x):
    dic_jeu["bombes"][(y, x)] = {'timer': 6, 'obj': Bombes(g, dic_jeu['sprite']["bombes"],settings["size"], y, x, (0,0) )}
    
def case_valide_pour_explosion(grille, y, x) -> bool:
    # Les cases non valides sont celles en dehors de la grille et les colonnes. Les prises ethernet sont considérées comme valides pour une explosion
    if not (0 <= y <= len(grille) - 1 and 0 <= x <= len(grille[0]) - 1) or "C" in grille[y][x]:
        return False
    return True

def cases_relatives_vers_absolues(coord, dic_cases_affectees_relatives):

    dic_cases_affectees_absolues = {
        "haut": [],
        "droite": [],
        "bas": [],
        "gauche": []
    }

    for direction in dic_cases_affectees_relatives.keys():
        for el in dic_cases_affectees_relatives[direction]:
            # pour passer de coordonnées relatives à absolues : coord[0]+el[0], coord[1]+el[1]. coord sont les coordonnées absolues du point à partir desquelles les coordonnées relatives de el sont basées. L'addition des deux donnent les coordonnées absolues de el, càd dans la grille plutôt que par rapport au point de coordonnées coord, càd la bombe
            dic_cases_affectees_absolues[direction].append((coord[0] + el[0], coord[1] + el[1]))

    return dic_cases_affectees_absolues

def calculer_cases_affectees(grille, coord, dic_jeu) -> dict[str:list[tuple[int]]]:
    
    # "La portée de ses bombes, égale à 1 + Niv / 2" = +1 case de portée tous les 2 niveaux, à part au niveau 2 où il gagne directement 1 case de portée
    portee = int(1 + dic_jeu["bomber"].niv // 2)


    dic_cases_affectees_relatives = {
        "haut": [(0, 0)],
        "droite": [],
        "bas": [],
        "gauche": []
    }

    dic_vecteurs = {
        "haut": (-1, 0),
        "droite": (0, 1),
        "bas": (1, 0),
        "gauche": (0, -1)
    }

    directions_valides = list(dic_cases_affectees_relatives.keys())

    for k in range(1, portee + 1):

        directions_a_enlever = list()

        # Ne pas .remove() sur directions_valides dans la boucle, crée des problèmes d'index (éléments sautés)
        for direction in directions_valides:

            # k sert comme un scalaire pour les 4 vecteurs donnant les directions à l'explosion
            propagee = (dic_vecteurs[direction][0] * k, dic_vecteurs[direction][1] * k)

            # pour passer de coordonnées relatives à absolues : coord[0]+el[0], coord[1]+el[1]. coord sont les coordonnées absolues du point à partir desquelles les coordonnées relatives de el sont basées. L'addition des deux donnent les coordonnées absolues de el, càd dans la grille plutôt que par rapport au point de coordonnées coord, càd la bombe
            if not case_valide_pour_explosion(grille, coord[0] + propagee[0], coord[1] + propagee[1]):
                directions_a_enlever.append(direction)
                # On a rencontré une colonne ou on est en dehors de la grille : la direction n'est plus valide

            elif "M" in grille[coord[0] + propagee[0]][coord[1] + propagee[1]]:
                dic_cases_affectees_relatives[direction].append(propagee)
                directions_a_enlever.append(direction)
                # Le mur est détruit mais l'explosion s'arrête là

            else:
                dic_cases_affectees_relatives[direction].append(propagee)
                # Tout autre élément

        for direction in directions_a_enlever:
            directions_valides.remove(direction)

    return cases_relatives_vers_absolues(coord, dic_cases_affectees_relatives)

# coord_a_ne_pas_considerer : pour récursion
def exploser_bombe(grille, g, coord, dic_jeu):

    dic_cases_affectees = calculer_cases_affectees(grille, coord, dic_jeu)

    # Supprime la bombe du dic.
    dic_jeu["bombes"][coord]['obj'].supprimerEntite()
    del dic_jeu["bombes"][coord]
    # Supprime la réprésentation de la bombe de la grille
    grille[coord[0]][coord[1]].remove("B")

    a_exploser = list() # pour récursion

    for direction in dic_cases_affectees.keys():
        for coord_explosion in dic_cases_affectees[direction]:

            if "M" in grille[coord_explosion[0]][coord_explosion[1]]:
                dic_jeu["mur"][(coord_explosion[1], coord_explosion[0])].supprimerEntite()
                grille[coord_explosion[0]][coord_explosion[1]].remove("M")
                dic_jeu["bomber"].score += 1
            # à voir
            if "P" in grille[coord_explosion[0]][coord_explosion[1]]:
                dic_jeu["bomber"].pv -= 1
            
            for el in grille[coord_explosion[0]][coord_explosion[1]]:
                if "F" in el:
                    # el est un fantome maintenant
                    
                    dic_jeu["fantomes"][el].supprimerEntite()
                    
                    grille[coord_explosion[0]][coord_explosion[1]].remove(el)
                    dic_jeu["fantomes"].pop(el)
                    grille[coord_explosion[0]][coord_explosion[1]].append("U")
            
            if "U" in grille[coord_explosion[0]][coord_explosion[1]]:
                grille[coord_explosion[0]][coord_explosion[1]].remove("U")
            if "B" in grille[coord_explosion[0]][coord_explosion[1]]:
                a_exploser.append(coord_explosion)

    objets_graphiques_explosions = render_explosions_apparition(grille, g, dic_cases_affectees)
    #print(coord, objets_graphiques_explosions)
    # l'appel doit se faire une fois que toutes les cases affectées par la première bombe ont été affectées (voir consigne)
    if a_exploser:
        for coord_bombe in a_exploser:
            #print("recursion :", objets_graphiques_explosions)
            return objets_graphiques_explosions + exploser_bombe(grille, g, coord_bombe, dic_jeu)

    else:
        return objets_graphiques_explosions
