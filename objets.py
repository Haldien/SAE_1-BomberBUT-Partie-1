import random
from bombes import *
from fonctions_utiles import *
from render import *

"""
===============================================================================================

                            Classe d'Entite

===============================================================================================
"""
class Entite:
    """
        Cette classe permet de faire les fondations de tout les éléments pouvant effectuer une action
    """
    def __init__(self, g, grille, dic_jeu, pos_de_depart, id_grille) -> None:

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

    def __str__(self) -> str:
        """
            Cette Méthode permet de surcharger la fonction __str__ présente nativement,
            Elle retourne une chaîne de caractère donnant des informations liées à cette objet en jeu
        """
        return f"Objet de type {self.__class__.__name__} à la positon : {self.pos} avec objet graphique : {self.objet_graphique}"

    def se_supprimer(self) -> None:
        """
            Cette méthode permet de supprimer proprement l'objet dans le jeu
            Elle ne renvoie rien
        """
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
===============================================================================================

                            Classe dérivé d'Entite

===============================================================================================
"""
class Mur(Entite):
    """
        Cette classe est dérivée d'Entite; elle permet de faire apparaître un objet mur
        Cette objet est destructible par les bombes
    """
    def __init__(self, g, grille, dic_jeu, pos_de_depart, id_grille):
        super().__init__(g, grille, dic_jeu, pos_de_depart, id_grille)

        # Partie graphique
        self.sprite = "asset/carton/carton.png"

        self.objet_graphique = self.g.afficherImage(self.pos[1] * dic_jeu["case_dimensions"][0],
                                                    self.pos[0] * dic_jeu["case_dimensions"][1],
                                                    dic_jeu["case_dimensions"], self.sprite)


class Colonne(Entite):
    """
        Cette classe est dérivée d'Entite; elle permet de faire apparaître un objet colonne
        Cette objet est indestructible par les bombes
    """
    def __init__(self, g, grille, dic_jeu, pos_de_depart, id_grille):
        super().__init__(g, grille, dic_jeu, pos_de_depart, id_grille)

        # Partie graphique
        #Purement esthétique
        print(len(grille[0]))
        print(grille)
        if self.pos[0] == 0 and self.pos[1] == 0:
            self.sprite = "asset/mur/coin_g_h.png"   
        elif self.pos[0] == 0 and self.pos[1] == len(grille[0])-1:
            self.sprite = "asset/mur/coin_d_h.png"
        elif self.pos[0] == len(grille)-1 and self.pos[1] == 0:
            self.sprite = "asset/mur/coin_g_b.png"
        elif self.pos[0] == len(grille)-1 and self.pos[1] == len(grille[0])-1:
            self.sprite = "asset/mur/coin_d_b.png"
        elif self.pos[0] == 0:
            self.sprite = "asset/mur/mur_haut.png"
        elif self.pos[0] == len(grille)-1:
            self.sprite = "asset/mur/mur_bas.png"
        elif self.pos[1] == len(grille[0])-1:
            self.sprite = "asset/mur/mur_droite.png"
        elif self.pos[1] == 0:
            self.sprite = "asset/mur/mur_gauche.png"
        else:
            self.sprite = "asset/table/table.png"

        self.objet_graphique = self.g.afficherImage(self.pos[1] * dic_jeu["case_dimensions"][0],
                                                    self.pos[0] * dic_jeu["case_dimensions"][1],
                                                    dic_jeu["case_dimensions"], self.sprite)


class Ethernet(Entite):
    """
        Cette classe est dérivée d'Entite; elle permet de faire apparaître un objet "prise ethernet"
        Cette objet est indestructible par les bombes
    """
    def __init__(self, g, grille, dic_jeu, pos_de_depart, id_grille):
        super().__init__(g, grille, dic_jeu, pos_de_depart, id_grille)

        # Partie graphique
        self.sprite = {1: "asset/ethernet/off.png", 2: "asset/ethernet/on.png"}
        self.enable = 0
        self.objet_graphique = self.g.afficherImage(self.pos[1] * dic_jeu["case_dimensions"][0],
                                                    self.pos[0] * dic_jeu["case_dimensions"][1],
                                                    dic_jeu["case_dimensions"], self.sprite[1])

    def spawner(self)->bool:
        """
            Cette méthode permet de faire apparaître un fantôme proche de sa case en jeu
            Elle renvoie une valeur booléenne
        """
        cases_voisines_valides = get_cases_voisines_valides(self.grille, self.pos)

        if len(cases_voisines_valides) > 0:
            self.g.supprimer(self.objet_graphique)
            self.objet_graphique = self.g.afficherImage(self.pos[1]*self.dic_jeu["case_dimensions"][0],
                                                        self.pos[0]*self.dic_jeu["case_dimensions"][1],
                                                        self.dic_jeu["case_dimensions"],self.sprite[2])
            self.enable = 5
            
            random.shuffle(cases_voisines_valides)
            self.dic_jeu["fantomes"].append(Fantome(self.g, self.grille, self.dic_jeu, cases_voisines_valides[0], "F"))
            return True
        return False
    
    def has_spawned(self):
        if self.enable < 0:
            self.g.supprimer(self.objet_graphique)
            self.objet_graphique = self.g.afficherImage(self.pos[1]*self.dic_jeu["case_dimensions"][0],
                                                        self.pos[0]*self.dic_jeu["case_dimensions"][1],
                                                        self.dic_jeu["case_dimensions"],self.sprite[1])
        else:
            self.enable -= 1



class Personnage(Entite):
    """
        Cette classe est dérivée d'Entite; elle permet de faire apparaître un objet "personnage" va être fortement utile pour la création d'un bomber ou d'un fantôme
    """
    def __init__(self, g, grille, dic_jeu, pos_de_depart, id_grille):
        super().__init__(g, grille, dic_jeu, pos_de_depart, id_grille)

        self.pos_precedente = None  # Sert au déplacement des fantômes ET à calculer la direction du personnage (sprite)
        # Partie graphique
        self.sprites = None
        self.direction = "bas"  # par défaut
        self.sprite_number = 0

    def se_deplacer(self, coords: tuple[int, int], id_grille:int) -> None:
        """
            Cette méthode prend en paramètre un tuple de coordonnée et un id_grille
            Elle permet à un objet d'effectuer un déplacement
            Elle ne renvoie rien
        """
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
    """
        Cette classe est dérivée d'Entite; elle permet de faire apparaître un objet "upgrade"
    """
    def __init__(self, g, grille, dic_jeu, pos_de_depart, id_grille):
        super().__init__(g, grille, dic_jeu, pos_de_depart, id_grille)

        # Partie graphique
        self.sprite = "asset/upgrade/upgrade.png"
        self.immune = 3

        self.objet_graphique = self.g.afficherImage(self.pos[1] * dic_jeu["case_dimensions"][0],
                                                    self.pos[0] * dic_jeu["case_dimensions"][1],
                                                    dic_jeu["case_dimensions"], self.sprite)


class Bombe(Entite):
    """
        Cette classe est dérivée d'Entite; elle permet de faire apparaître un objet "personnage" va être fortement utile pour la création d'un bomber ou d'un fantôme
    """
    def __init__(self, g, grille, dic_jeu, pos_de_depart, id_grille):

        super().__init__(g, grille, dic_jeu, pos_de_depart, id_grille)
        self.timer = 5
        # Partie graphique
        self.sprites = {
            "4": "asset/bombe/bombe_timer4et5.png",
            "3": "asset/bombe/bombe_timer3.png",
            "2": "asset/bombe/bombe_timer2.png",
            "1": "asset/bombe/bombe_timer1.png",
        }
        self.objet_graphique = self.g.afficherImage(self.pos[1] * dic_jeu["case_dimensions"][0],
                                                    self.pos[0] * dic_jeu["case_dimensions"][1],
                                                    dic_jeu["case_dimensions"], self.sprites["4"])

    def decrementer_son_timer(self) -> None:
        """
            Cette méthode permet de décrémenter le timer d'une bombe à chaque tour
            Elle ne renvoie rien
        """
        self.timer -= 1
        # Partie graphique
        self.g.supprimer(self.objet_graphique)

        if self.timer > 0:  # si self.timer == 0, la bombe va exploser et il ne sert à rien de change le sprite
            self.objet_graphique = self.g.afficherImage(self.pos[1] * self.dic_jeu["case_dimensions"][0],
                                                        self.pos[0] * self.dic_jeu["case_dimensions"][1],
                                                        self.dic_jeu["case_dimensions"], self.sprites[str(self.timer)])

    def s_exploser(self):
        """
            Cette méthode permet à la bombe de s'exploser, cette fonction est récursive
            Elle permet de créer des déflagrations qui vont affecter plusieurs éléments du jeu.
            Une déflagration est bloqué par les murs (destructible et indestructible)
            Affecte également les fantômes et le bombers
            Elle ne renvoie rien
        """
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
                            self.dic_jeu["bomber"].score += 10
                            
                            number = random.randint(0,32)
                            print(number)
                            if number % 3 == 0:
                                print("une bombe a été ajouté")
                                self.dic_jeu["upgrades"].append(Upgrade(self.g, self.grille, self.dic_jeu, coord_explosion, "U"))


                if "P" in self.grille[coord_explosion[0]][coord_explosion[1]]:
                    self.dic_jeu["bomber"].pv -= 1

                if "F" in self.grille[coord_explosion[0]][coord_explosion[1]]:

                    for fantome in self.dic_jeu["fantomes"]:
                        if fantome.pos == coord_explosion:
                            fantome.se_supprimer()
                        self.dic_jeu["bomber"].score += 30
                        self.dic_jeu["upgrades"].append(
                            Upgrade(self.g, self.grille, self.dic_jeu, coord_explosion, "U"))

                if "U" in self.grille[coord_explosion[0]][coord_explosion[1]]:
                    for upgrade in self.dic_jeu["upgrades"]:
                        if upgrade.pos == coord_explosion and upgrade.immune < 0:
                            upgrade.se_supprimer()

                if "B" in self.grille[coord_explosion[0]][coord_explosion[1]]:
                    for bombe in self.dic_jeu["bombes"]:
                        if bombe.pos == coord_explosion:
                            a_exploser.append(bombe)

        # Partie graphique :
        objets_graphiques_explosions = render_explosions_apparition( self.g, dic_cases_affectees, self.dic_jeu)

        if a_exploser:
            for bombe in a_exploser:
                return objets_graphiques_explosions + bombe.s_exploser()

        else:
            return objets_graphiques_explosions
"""
===============================================================================================

                            Classe dérivé de Personnage

===============================================================================================
"""
class Bomber(Personnage):
    """
        Cette classe hérite des propriétés de Personnage, et permet de créer un joueur
    """
    def __init__(self, g, grille, dic_jeu, pos_de_depart, id_grille):

        super().__init__(g, grille, dic_jeu, pos_de_depart, id_grille)
        self.pv = 3
        self.niv = 0
        self.score = 0
        # Partie graphique
        self.sprites = {
            "bas": ["asset/bomber/down/down1.png", "asset/bomber/down/down2.png"],
            "gauche": ["asset/bomber/left/left1.png", "asset/bomber/left/left2.png"],
            "droite": ["asset/bomber/right/right1.png", "asset/bomber/right/right2.png"],
            "haut": ["asset/bomber/up/up1.png", "asset/bomber/up/up2.png"],
            "pose": ["asset/bomber/pose/poseBombe.png"]
        }
        self.objet_graphique = self.g.afficherImage(self.pos[1] * dic_jeu["case_dimensions"][0],
                                                    self.pos[0] * dic_jeu["case_dimensions"][1],
                                                    dic_jeu["case_dimensions"],
                                                    self.sprites[self.direction][self.sprite_number])

    def __str__(self):
        """
            Cette méthode renvoie une chaîne de caractère donnant des informations relatives au bomber
        """
        return f"Bomber à la position {self.pos}, PV : {self.pv}, NIV : {self.niv}, Score : {self.score}"

    def se_deplacer(self, coords: tuple[int, int], id_grille: int, settings:dict) -> None:
        """
            Cette méthode est une surcharge de la classe Personnage
            Elle permet d'effectuer un déplacement par rapport au bomber, si il passe au-dessus d'un upgrade..etc
            Cette fonction ne renvoie rien
        """
        super().se_deplacer(coords, id_grille)
        # Prendre un upgrade
        if "U" in self.grille[coords[0]][coords[1]]:
            for upgrade in self.dic_jeu["upgrades"]:
                if upgrade.pos == coords:
                    self.score += 45
                    upgrade.se_supprimer()
                    self.level_up(settings)
        # Partie graphique en plus
        self.objet_graphique = self.g.afficherImage(self.pos[1] * self.dic_jeu["case_dimensions"][0],
                                                    self.pos[0] * self.dic_jeu["case_dimensions"][1],
                                                    self.dic_jeu["case_dimensions"],
                                                    self.sprites[self.direction][self.sprite_number])

    def poser_bombe(self, coords:tuple) -> None:
        """
            Cette méthode permet au bomber de créer une bombe
            Elle prend en paramètre un tuple de coordonnées
            On l'ajoute au dictionnaire globale, Elle ne renvoie rien
        """
        if "B" not in self.grille[coords[0]][coords[1]]:
            self.dic_jeu["bombes"].append(Bombe(self.g, self.grille, self.dic_jeu, coords, "B"))

        # Partie graphiqe
        self.g.supprimer(self.objet_graphique)

        self.objet_graphique = self.g.afficherImage(self.pos[1] * self.dic_jeu["case_dimensions"][0],
                                                    self.pos[0] * self.dic_jeu["case_dimensions"][1],
                                                    self.dic_jeu["case_dimensions"],
                                                    self.sprites["pose"][0])

    # On délègue la gestion des attaques des fantômes au bomberman par souci d'optimisation
    def se_faire_attaquer(self) -> None:
        """
            Cette méthode permet d'affecter les points de vies du bomber lorsqu'un fantôme est trop proche d'un bomber
            Elle ne renvoie rien
        """
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
                return  # On limite les dégâts au bomberman à 1 pv max par tour

    def level_up(self, settings):
        """
            Cette méthode prend en paramètre un dictionnaire settings, qui reprend les paramètres du jeu actuelle
            Elle fait la gestion des niveaux du bomber
        """
        self.niv += 1
        if self.niv in [1, 3, 5, 7, 11, 13]:
            self.pv += 1
        else:
            number = random.randint(0,10)
            if number == 5:
                self.pv += 1
            elif number %2 == 0:
                settings["timer"] += 10
            else:
                settings["timer_fantome"] += 5
            


class Fantome(Personnage):
    """
        Cette classe hérite des propriétés de Personnage, et permet de créer un joueur
    """
    def __init__(self, g, grille, dic_jeu, pos_de_depart, id_grille):
        super().__init__(g, grille, dic_jeu, pos_de_depart, id_grille)
        # Partie graphique
        self.sprites = {
            "bas": ["asset/ghost/down/down1.png", "asset/ghost/down/down2.png"],
            "gauche": ["asset/ghost/left/left1.png", "asset/ghost/left/left2.png"],
            "droite": ["asset/ghost/right/right1.png", "asset/ghost/right/right2.png"],
            "haut": ["asset/ghost/up/up1.png", "asset/ghost/up/up2.png"]
        }
        self.objet_graphique = self.g.afficherImage(self.pos[1] * dic_jeu["case_dimensions"][0],
                                                    self.pos[0] * dic_jeu["case_dimensions"][1],
                                                    dic_jeu["case_dimensions"],
                                                    self.sprites[self.direction][self.sprite_number])

    def se_deplacer(self, coords: tuple[int, int], id_grille:int):
        """
            Cette méthode est une surcharge de la classe Personnage
            Cette fonction prend en argument un tuple de coordonnée et un identifiant de grille (id_grille)
        """
        super().se_deplacer(coords, id_grille)
        # Partie graphique en plus
        self.objet_graphique = self.g.afficherImage(self.pos[1] * self.dic_jeu["case_dimensions"][0],
                                                    self.pos[0] * self.dic_jeu["case_dimensions"][1],
                                                    self.dic_jeu["case_dimensions"],
                                                    self.sprites[self.direction][self.sprite_number])

    def se_deplacer_random(self) -> None:
        """
            Cette méthode permet de faire le déplacement des fantomes de manière aléatoire
            Elle ne renvoie rien
        """
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
