from __future__ import annotations
import random

from bombes import *

from fonctions_utiles import *

from render import *


class Entite:

    def __init__(self, g, grille, dic_jeu, pos_de_depart, id_grille):

        self.g = g
        self.grille = grille
        self.dic_jeu = dic_jeu

        # Position de l'entité dans la grille
        self.pos = pos_de_depart  # (y, x)

        # Identifiant de l'objet dans la grille (la variable 'grille')
        self.id_grille = id_grille

        # Création dans la grille
        self.grille[pos_de_depart[0]][pos_de_depart[1]].append(id_grille)

        # Partie graphique
        self.objet_graphique = None  # Pour appeler cet attribut dans se_supprimer()

    def __str__(self):
        return f"Objet de type {self.__class__.__name__} à la positon : {self.pos} avec objet graphique : {self.objet_graphique}"

    def se_supprimer(self):
        # 1) suppression dans la grille
        self.grille[self.pos[0]][self.pos[1]].remove(self.id_grille)

        # 2) suppression de l'objet graphique
        if self.objet_graphique:  # à enlever ?
            self.g.supprimer(self.objet_graphique)

        # 3) suppression dans dic_jeu
        for key in list(self.dic_jeu.keys()):
            # cas où la valeur est un objet unique et non une liste (bomber)
            if not isinstance(self.dic_jeu[key], list):
                if self == self.dic_jeu[key]:
                    del self.dic_jeu[key]
            # cas où la valeur est une liste d'objets (le reste)
            else:
                if self in self.dic_jeu[key]:
                    self.dic_jeu[key].remove(self)

        # 4) suppression de l'objet
        del self


"""
                    Classes héritant d'Entité
"""


class Mur(Entite):

    def __init__(self, g, grille, dic_jeu, pos_de_depart, id_grille):
        super().__init__(g, grille, dic_jeu, pos_de_depart, id_grille)

        # Partie graphique
        self.sprite = "sprites/mur.png"

        self.objet_graphique = self.g.afficherImage(self.pos[1] * dic_jeu["case_dimensions"][0],
                                                    self.pos[0] * dic_jeu["case_dimensions"][1],
                                                    dic_jeu["case_dimensions"], self.sprite)


class Colonne(Entite):

    def __init__(self, g, grille, dic_jeu, pos_de_depart, id_grille):
        super().__init__(g, grille, dic_jeu, pos_de_depart, id_grille)

        # Partie graphique
        self.sprite = "sprites/colonne.png"

        self.objet_graphique = self.g.afficherImage(self.pos[1] * dic_jeu["case_dimensions"][0],
                                                    self.pos[0] * dic_jeu["case_dimensions"][1],
                                                    dic_jeu["case_dimensions"], self.sprite)


class Ethernet(Entite):

    def __init__(self, g, grille, dic_jeu, pos_de_depart, id_grille):
        super().__init__(g, grille, dic_jeu, pos_de_depart, id_grille)

        # Partie graphique
        self.sprite = "sprites/ethernet.png"

        self.objet_graphique = self.g.afficherImage(self.pos[1] * dic_jeu["case_dimensions"][0],
                                                    self.pos[0] * dic_jeu["case_dimensions"][1],
                                                    dic_jeu["case_dimensions"], self.sprite)

    def spawner(self)->bool:
        cases_voisines_valides = get_cases_voisines_valides(self.grille, self.pos)

        if len(cases_voisines_valides) > 0:
            random.shuffle(cases_voisines_valides)
            self.dic_jeu["fantomes"].append(Fantome(self.g, self.grille, self.dic_jeu, cases_voisines_valides[0], "F"))
            return True

        return False


class Personnage(Entite):

    def __init__(self, g, grille, dic_jeu, pos_de_depart, id_grille):
        super().__init__(g, grille, dic_jeu, pos_de_depart, id_grille)

        self.pos_precedente = None  # Sert au déplacement des fantômes ET à calculer la direction du personnage (sprite)

        # Partie graphique
        self.sprites = None

        self.direction = "bas"  # par défaut

        self.sprite_number = 0


    def se_deplacer(self, coords: tuple[int, int], id_grille):
        self.pos_precedente = self.pos

        self.grille[self.pos[0]][self.pos[1]].remove(id_grille)
        self.grille[coords[0]][coords[1]].append(id_grille)

        self.pos = coords

        # Pour updater self.direction :
        dic_directions = {
            (-1, 0): "haut",
            (0, 1): "droite",
            (1, 0): "bas",
            (0, -1): "gauche"
        }

        for direction in dic_directions:
            if direction == (self.pos[0] - self.pos_precedente[0], self.pos[1] - self.pos_precedente[1]):
                self.direction = dic_directions[direction]
                break

        # Partie graphique
        self.g.supprimer(self.objet_graphique)

        self.sprite_number = 1 if self.sprite_number == 0 else 0


class Upgrade(Entite):

    def __init__(self, g, grille, dic_jeu, pos_de_depart, id_grille):
        super().__init__(g, grille, dic_jeu, pos_de_depart, id_grille)

        # Partie graphique
        self.sprite = "sprites/upgrade.png"

        self.objet_graphique = self.g.afficherImage(self.pos[1] * dic_jeu["case_dimensions"][0],
                                                    self.pos[0] * dic_jeu["case_dimensions"][1],
                                                    dic_jeu["case_dimensions"], self.sprite)


class Bombe(Entite):

    def __init__(self, g, grille, dic_jeu, pos_de_depart, id_grille):

        super().__init__(g, grille, dic_jeu, pos_de_depart, id_grille)

        self.timer = 5

        # Partie graphique
        self.sprites = {
            "4": "sprites/bombe_timer4et5.png",
            "3": "sprites/bombe_timer3.png",
            "2": "sprites/bombe_timer2.png",
            "1": "sprites/bombe_timer1.png",
        }

        self.objet_graphique = self.g.afficherImage(self.pos[1] * dic_jeu["case_dimensions"][0],
                                                    self.pos[0] * dic_jeu["case_dimensions"][1],
                                                    dic_jeu["case_dimensions"], self.sprites["4"])

    def decrementer_son_timer(self):

        self.timer -= 1

        # Partie graphique
        self.g.supprimer(self.objet_graphique)

        if self.timer > 0:  # si self.timer == 0, la bombe va exploser et il ne sert à rien de change le sprite
            self.objet_graphique = self.g.afficherImage(self.pos[1] * self.dic_jeu["case_dimensions"][0],
                                                        self.pos[0] * self.dic_jeu["case_dimensions"][1],
                                                        self.dic_jeu["case_dimensions"], self.sprites[str(self.timer)])

    def s_exploser(self):

        dic_cases_affectees = calculer_case_affectees(self.grille, self.pos, self.dic_jeu)

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

                        self.dic_jeu["upgrades"].append(
                            Upgrade(self.g, self.grille, self.dic_jeu, coord_explosion, "U"))

                if "U" in self.grille[coord_explosion[0]][coord_explosion[1]]:
                    for upgrade in self.dic_jeu["upgrades"]:
                        if upgrade.pos == coord_explosion:
                            upgrade.se_supprimer()

                if "B" in self.grille[coord_explosion[0]][coord_explosion[1]]:
                    for bombe in self.dic_jeu["bombes"]:
                        if bombe.pos == coord_explosion:
                            a_exploser.append(bombe)

        # Partie graphique :
        objets_graphiques_explosions = render_explosions_apparition(self.grille, self.g, dic_cases_affectees, self.dic_jeu)

        if a_exploser:
            for bombe in a_exploser:
                return objets_graphiques_explosions + bombe.s_exploser()

        else:
            return objets_graphiques_explosions



"""
                    Classes héritant de Personnage
"""


class Bomber(Personnage):

    def __init__(self, g, grille, dic_jeu, pos_de_depart, id_grille):

        super().__init__(g, grille, dic_jeu, pos_de_depart, id_grille)

        self.pv = 3
        self.niv = 0
        self.score = 0

        # Partie graphique
        self.sprites = {
            "bas": ["asset/bunny/down/down1.png", "asset/bunny/down/down2.png"],
            "gauche": ["asset/bunny/left/left1.png", "asset/bunny/left/left2.png"],
            "droite": ["asset/bunny/right/right1.png", "asset/bunny/right/right2.png"],
            "haut": ["asset/bunny/up/up1.png", "asset/bunny/up/up2.png"],
            "pose": ["asset/bunny/pose/poseBombe.png"]
        }

        self.objet_graphique = self.g.afficherImage(self.pos[1] * dic_jeu["case_dimensions"][0],
                                                    self.pos[0] * dic_jeu["case_dimensions"][1],
                                                    dic_jeu["case_dimensions"],
                                                    self.sprites[self.direction][self.sprite_number])

    def __str__(self):
        return f"Bomber à la position {self.pos}, PV : {self.pv}, NIV : {self.niv}, Score : {self.score}"

    def se_deplacer(self, coords: tuple[int, int], id_grille):

        super().se_deplacer(coords, id_grille)

        # Prendre un upgrade
        if "U" in self.grille[coords[0]][coords[1]]:
            for upgrade in self.dic_jeu["upgrades"]:
                if upgrade.pos == coords:
                    upgrade.se_supprimer()
                    if self.dic_jeu["bomber"].niv < 4:
                        self.dic_jeu["bomber"].niv += 1

        # Partie graphique en plus
        self.objet_graphique = self.g.afficherImage(self.pos[1] * self.dic_jeu["case_dimensions"][0],
                                                    self.pos[0] * self.dic_jeu["case_dimensions"][1],
                                                    self.dic_jeu["case_dimensions"],
                                                    self.sprites[self.direction][self.sprite_number])

    def poser_bombe(self, coords):

        if "B" not in self.grille[coords[0]][coords[1]]:
            self.dic_jeu["bombes"].append(Bombe(self.g, self.grille, self.dic_jeu, coords, "B"))

        # Partie graphiqe
        self.g.supprimer(self.objet_graphique)

        self.objet_graphique = self.g.afficherImage(self.pos[1] * self.dic_jeu["case_dimensions"][0],
                                                    self.pos[0] * self.dic_jeu["case_dimensions"][1],
                                                    self.dic_jeu["case_dimensions"],
                                                    self.sprites["pose"][0])

    # On délègue la gestion des attaques des fantômes au bomberman par souci d'optimisation
    def se_faire_attaquer(self):

        cases_voisines = list()

        dic_vecteurs = {
            "haut": (-1, 0),
            "droite": (0, 1),
            "bas": (1, 0),
            "gauche": (0, -1)
        }

        for direction in dic_vecteurs:
            cases_voisines.append((self.pos[0] + dic_vecteurs[direction][0], self.pos[1] + dic_vecteurs[direction][1]))

        for coords in cases_voisines:
            if "F" in self.grille[coords[0]][coords[1]]:
                self.pv -= 1
                break  # On limite les dégâts au bomberman à 1 pv max par tour

    def level_up(self):

        self.dic_jeu["bomber"].niv += 1

        if self.dic_jeu["bomber"].niv in [1, 3]:
            self.dic_jeu["bomber"].pv += 1


class Fantome(Personnage):

    def __init__(self, g, grille, dic_jeu, pos_de_depart, id_grille):

        super().__init__(g, grille, dic_jeu, pos_de_depart, id_grille)

        # Partie graphique
        self.sprites = {
            "bas": ["asset/bunny/down/down1.png", "asset/bunny/down/down2.png"],
            "gauche": ["asset/bunny/left/left1.png", "asset/bunny/left/left2.png"],
            "droite": ["asset/bunny/right/right1.png", "asset/bunny/right/right2.png"],
            "haut": ["asset/bunny/up/up1.png", "asset/bunny/up/up2.png"]
        }

        self.objet_graphique = self.g.afficherImage(self.pos[1] * dic_jeu["case_dimensions"][0],
                                                    self.pos[0] * dic_jeu["case_dimensions"][1],
                                                    dic_jeu["case_dimensions"],
                                                    self.sprites[self.direction][self.sprite_number])

    def se_deplacer(self, coords: tuple[int, int], id_grille):

        super().se_deplacer(coords, id_grille)

        # Partie graphique en plus
        self.objet_graphique = self.g.afficherImage(self.pos[1] * self.dic_jeu["case_dimensions"][0],
                                                    self.pos[0] * self.dic_jeu["case_dimensions"][1],
                                                    self.dic_jeu["case_dimensions"],
                                                    self.sprites[self.direction][self.sprite_number])

    def se_deplacer_random(self):

        cases_voisines_valides = get_cases_voisines_valides(self.grille, self.pos)

        if len(cases_voisines_valides) == 0:
            return

        elif len(cases_voisines_valides) == 1:
            self.se_deplacer((cases_voisines_valides[0][0], cases_voisines_valides[0][1]), "F")

        elif len(cases_voisines_valides) >= 2:

            for case in cases_voisines_valides:
                if case == self.pos_precedente:
                    cases_voisines_valides.remove(case)

            random.shuffle(cases_voisines_valides)
            self.se_deplacer((cases_voisines_valides[0][0], cases_voisines_valides[0][1]), "F")
