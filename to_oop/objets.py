from __future__ import annotations

from bombes import *



class Entite:

    def __init__(self, g, grille, dic_jeu, pos_de_depart, id_grille):

        self.g = g
        self.grille = grille
        self.dic_jeu = dic_jeu

        # Position de l'entité dans la grille
        self.pos = pos_de_depart # (y, x)

        # Identifiant de l'objet dans la grille (variable grille)
        self.id_grille = id_grille

        # Création dans la grille
        self.grille[pos_de_depart[0]][pos_de_depart[1]].append(id_grille)

    def __str__(self):
        return f"Objet de type {self.__class__.__name__} à la positon : {self.pos}"

    def se_supprimer(self):
        # 1) suppression dans la grille
        self.grille[self.pos[0]][self.pos[1]].remove(self.id_grille)

        # 2) supression dans dic_jeu
        for key in list(self.dic_jeu.keys()):
            # cas où la valeur est un objet unique et non une liste (bomber)
            if not isinstance(self.dic_jeu[key], list) :
                if self == self.dic_jeu[key]:
                    del self.dic_jeu[key]
            # cas où la valeur est une liste d'objets (le reste)
            else:
                if self in self.dic_jeu[key]:
                    self.dic_jeu[key].remove(self)

        # 3) suprression de l'objet
        del self


"""
                    Classes héritant d'Entité
"""
class Mur(Entite):

    def __init__(self, g, grille, dic_jeu, pos_de_depart, id_grille):

        super().__init__(g, grille, dic_jeu, pos_de_depart, id_grille)

class Colonne(Entite):

    def __init__(self, g, grille, dic_jeu, pos_de_depart, id_grille):

        super().__init__(g, grille, dic_jeu, pos_de_depart, id_grille)

class Ethernet(Entite):

    def __init__(self, g, grille, dic_jeu, pos_de_depart, id_grille):

        super().__init__(g, grille, dic_jeu, pos_de_depart, id_grille)

class Personnage(Entite):

    def __init__(self, g, grille, dic_jeu, pos_de_depart, id_grille):

        super().__init__(g, grille, dic_jeu, pos_de_depart, id_grille)

    def se_deplacer(self, coords: tuple[int, int], id_grille):
        self.grille[self.pos[0]][self.pos[1]].remove(id_grille)
        self.grille[coords[0]][coords[1]].append(id_grille)

        self.pos = coords

class Upgrade(Entite):

    def __init__(self, g, grille, dic_jeu, pos_de_depart, id_grille):

        super().__init__(g, grille, dic_jeu, pos_de_depart, id_grille)


class Bombe(Entite):

    def __init__(self, g, grille, dic_jeu, pos_de_depart, id_grille):

        super().__init__(g, grille, dic_jeu, pos_de_depart, id_grille)

        self.timer = 5


    def s_exploser(self):

        dic_cases_affectees = self.cases_affectees_par_explosion()

        # Supprime la bombe
        self.se_supprimer()

        a_exploser = list()  # pour récursion

        # On regarde les cases affectées
        for direction in dic_cases_affectees.keys():
            for coord_explosion in dic_cases_affectees[direction]:

                if "M" in self.grille[coord_explosion[0]][coord_explosion[1]]:
                    for mur in self.dic_jeu["murs"]:
                        if mur.pos == coord_explosion:
                            mur.se_supprimer()
                            self.dic_jeu["bomber"].score += 1

                if "P" in self.grille[coord_explosion[0]][coord_explosion[1]]:
                    self.dic_jeu["bomber"].pv -= 1

                if "F" in self.grille[coord_explosion[0]][coord_explosion[1]]:

                    for fantome in self.dic_jeu["fantomes"]:
                        if fantome.pos == coord_explosion:
                            fantome.se_supprimer()

                        self.dic_jeu["upgrades"].append(Upgrade(self.g, self.grille, self.dic_jeu, coord_explosion, "U"))

                if "U" in self.grille[coord_explosion[0]][coord_explosion[1]]:
                    for upgrade in self.dic_jeu["upgrades"]:
                        if upgrade.pos == coord_explosion:
                            upgrade.se_supprimer()

                if "B" in self.grille[coord_explosion[0]][coord_explosion[1]]:
                    for bombe in self.dic_jeu["bombes"]:
                        if bombe.pos == coord_explosion:
                            a_exploser.append(bombe)

        if a_exploser:
            for bombe in a_exploser:
                bombe.s_exploser()

    def cases_affectees_par_explosion(self):

        # "La portée de ses bombes, égale à 1 + Niv / 2" = +1 case de portée tous les 2 niveaux, à part au niveau 2 où il gagne directement 1 case de portée
        portee = int(1 + self.dic_jeu["bomber"].niv / 2)

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
                if not case_valide_pour_explosion(self.grille, self.pos[0] + propagee[0], self.pos[1] + propagee[1]):
                    directions_a_enlever.append(direction)
                    # On a rencontré une colonne ou on est en dehors de la grille : la direction n'est plus valide

                elif "M" in self.grille[self.pos[0] + propagee[0]][self.pos[1] + propagee[1]]:
                    dic_cases_affectees_relatives[direction].append(propagee)
                    directions_a_enlever.append(direction)
                    # Le mur est détruit mais l'explosion s'arrête là

                else:
                    dic_cases_affectees_relatives[direction].append(propagee)
                    # Tout autre élément

            for direction in directions_a_enlever:
                directions_valides.remove(direction)

        return cases_relatives_vers_absolues(self.pos, dic_cases_affectees_relatives)

"""
                    Classes héritant de Personnage
"""

class Bomber(Personnage):
    def __init__(self, g, grille, dic_jeu, pos_de_depart, id_grille):

        super().__init__(g, grille, dic_jeu, pos_de_depart, id_grille)

        self.pv = 3
        self.niv = 0
        self.score = 0
        self.cooldown = 0

    def se_deplacer(self, coords: tuple[int, int], id_grille):

        super().se_deplacer(coords, id_grille)

        if "U" in self.grille[coords[0]][coords[1]]:
            for upgrade in self.dic_jeu["upgrades"]:
                if upgrade.pos == coords:
                    upgrade.se_supprimer()
                    self.dic_jeu["bomber"].score += 1


    def poser_bombe(self, coords):

        if "B" not in self.grille[coords[0]][coords[1]]:
            self.dic_jeu["bombes"].append(Bombe(self.g, self.grille, self.dic_jeu, coords, "B"))


    def level_up(self):

        self.dic_jeu["bomber"].niv += 1

        if self.dic_jeu["bomber"].niv in [1, 3]:
            self.dic_jeu["bomber"].pv += 1




class Fantome(Personnage):
    def __init__(self, g, grille, dic_jeu, pos_de_depart, id_grille):

        super().__init__(g, grille, dic_jeu, pos_de_depart, id_grille)





