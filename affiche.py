import tkiteasy, time
import bomber
from fonctions_utiles import *
from random import shuffle, randint

WIDTH, HEIGHT = 1200, 800

"""

                    Classe Principale

"""
class Entity:
    def __init__(self, g:object, sprite:dict, size:tuple, y:int,x:int, offset:tuple[int, int]):
        self.x, self.y = x+offset[0],y+offset[1]
        self.sprite = sprite
        self.size = size
        self.g = g
        self.state = "bas"
        self.indexState = 0
        self.obj = self.g.afficherImage(self.x*self.size[0], self.y*self.size[0], self.size , sprite["bas"][self.indexState] )

    def ChangeSprite(self,direct: str):
        self.Model_Choice(direct)


    def Model_Choice(self, state:str) -> None:
        self.g.supprimer(self.obj)
        self.indexState += 1
        if self.indexState >= len(self.sprite[state]):
            self.indexState = 0

        self.obj = self.g.afficherImage( self.x*self.size[0], self.y*self.size[0], self.size, self.sprite[state][self.indexState])
    
    def supprimerEntite(self):
        self.g.supprimer(self.obj)
        del self

"""

                    Dépendance d'Entité

"""


class Mob(Entity):
    def __init__(self, g:object, sprite:dict, size:tuple, x:int,y:int, offset:tuple[int, int]):
        super().__init__(g, sprite, size, x,y, offset)

    def deplacer(self, coords:tuple[int,int], direct:str) -> None:
        # Changement de sprite et de nouvelle coordonnées graphiques
        self.x = coords[1]
        self.y = coords[0]
        self.ChangeSprite(direct)


    def subitDegat(self):
        self.g.supprimer(self.obj)
        self.obj = self.g.afficherImage


class Ethernet(Entity):
    def __init__(self, g:object, sprite:dict, size:tuple, x:int,y:int, offset:tuple[int, int]):
        super().__init__(g, sprite, size, x,y, offset)
    
    def fait_apparaitre():
        pass

class Bombes(Entity):
    def __init__(self, g:object, sprite:dict, size:tuple, x:int,y:int, offset:tuple[int, int]):
        super().__init__(g, sprite, size, x,y, offset)


    def case_valide_pour_explosion(self, grille, y, x) -> bool:
    # Les cases non valides sont celles en dehors de la grille et les colonnes. Les prises ethernet sont considérées comme valides pour une explosion
        if not (0 <= y <= len(grille) - 1 and 0 <= x <= len(grille[0]) - 1) or "C" in grille[y][x]:
            return False
        return True

    def cases_relatives_vers_absolues(self, coord, dic_cases_affectees_relatives):

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


    def calculer_cases_affectees(self, grille, coord, dic_jeu) -> dict[str:list[tuple[int]]]:
        
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
                if not self.case_valide_pour_explosion(grille, coord[0] + propagee[0], coord[1] + propagee[1]):
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

        return self.cases_relatives_vers_absolues(coord, dic_cases_affectees_relatives)

    # coord_a_ne_pas_considerer : pour récursion
    def exploser_bombe(self, grille, g, coord, dic_jeu):

        dic_cases_affectees = self.calculer_cases_affectees(grille, coord, dic_jeu)

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
                    dic_jeu["bomber"]["Score"] += 1
                # à voir
                if "P" in grille[coord_explosion[0]][coord_explosion[1]]:
                    dic_jeu["bomber"]["PV"] -= 1
                for el in grille[coord_explosion[0]][coord_explosion[1]]:
                    if "F" in el:
                        # el est un fantome maintenant
                        
                        
                        dic_jeu["fantomes"][el]["obj"].supprimerEntite()
                        
                        grille[coord_explosion[0]][coord_explosion[1]].remove(el)
                        dic_jeu["fantomes"].pop(el)
                        grille[coord_explosion[0]][coord_explosion[1]].append("U")
                if "U" in grille[coord_explosion[0]][coord_explosion[1]]:
                    grille[coord_explosion[0]][coord_explosion[1]].remove("U")
                if "B" in grille[coord_explosion[0]][coord_explosion[1]]:
                    a_exploser.append(coord_explosion)

        objets_graphiques_explosions = self.render_explosions_apparition(grille, g, dic_cases_affectees)
        #print(coord, objets_graphiques_explosions)
        # l'appel doit se faire une fois que toutes les cases affectées par la première bombe ont été affectées (voir consigne)
        if a_exploser:
            for coord_bombe in a_exploser:
                #print("recursion :", objets_graphiques_explosions)
                return objets_graphiques_explosions + self.exploser_bombe(grille, g, coord_bombe, dic_jeu)

        else:
            return objets_graphiques_explosions

        
    def ignite(self, timer:int):
        self.g.supprimer(self.obj)
        
        if timer < 2:
            self.indexState = 3
            self.obj = self.g.afficherImage(self.x*self.size[0], self.y*self.size[0], self.size,self.sprite[self.state][self.indexState])
        elif timer < 3:
            self.indexState = 2
            self.obj = self.g.afficherImage(self.x*self.size[0], self.y*self.size[0], self.size,self.sprite[self.state][self.indexState])
        elif timer < 4:
            self.indexState = 1
            self.obj = self.g.afficherImage(self.x*self.size[0], self.y*self.size[0], self.size,self.sprite[self.state][self.indexState])
        else:
            self.indexState = 0
            self.obj = self.g.afficherImage(self.x*self.size[0], self.y*self.size[0], self.size,self.sprite[self.state][self.indexState])


class Mur(Entity):
    def __init__(self, g:object, sprite:dict, size:tuple, x:int,y:int, offset:tuple[int, int]):
        super().__init__(g, sprite, size, x,y, offset)

"""

                    Dépendance de Mob

"""
class Bomber(Mob):
    def __init__(self, g:object, sprite:dict, size:tuple, x:int,y:int, offset:tuple[int, int], pv:int, niv:int):
        super().__init__(g, sprite, size, x,y, offset)

        self.pv = pv
        self.niv = niv
        self.cooldown = 0
        self.score = 0
        
    def deplacer_bomber(self, grille, y: int, x: int):

        if "U" in grille[y][x]:
            grille[y][x].remove("U")

            #on limite le niveau à 4
            if self.niv < 4:
                self.level_up()


        grille[self.y][self.x].remove("P")
        grille[y][x].append("P")

        self.x, self.y = x,y
    
    def level_up(self):

        self.niv += 1

        if self.niv in [1, 3]:
            self.pv += 1

    def poser_bombe(self, g, grille, dic_jeu):

        if "B" not in grille[self.y][self.x]:
            grille[self.y][self.x].append("B")
            dic_jeu["bombes"][(self.y, self.x)] = {'timer': 6, 'obj': Bombes(g, bombe_sprite ,self.size, self.y, self.x, (0,0) )}

    def action_bomber(self, grille, touche: str, dic_jeu:dict):
    # Mappings des touches vers les vecteurs de mouvements correspondant
        mouvements = {
            "z": [-1, 0],
            "q": [0, -1],
            "s": [1, 0],
            "d": [0, 1]
        }

        match(touche):
            case "z":
                self.state = "haut"
            case "q":
                self.state= "gauche"
            case "s":
                self.state = "bas"
            case "d":
                self.state = "droite"
        

        # Mouvements
        if touche in ["z", "q", "s", "d"] and case_valide(grille, self.y + mouvements[touche][0],
                                                        self.x + mouvements[touche][1], dic_jeu):
            

            self.deplacer_bomber(grille, self.y + mouvements[touche][0], self.x + mouvements[touche][1])

        # Dépose un bombe
        elif touche == "space":
            self.state = "pose"
            self.poser_bombe(self.g, grille, dic_jeu)

        # Passe son tour
        elif touche == "Return":
            pass


class Fantome(Mob):
    def __init__(self, g:object, sprite:dict, size:tuple, x:int,y:int, offset:tuple[int, int]):
        super().__init__(g, sprite, size, x,y, offset)
    
    def deplacer_fantomes(self, grille:list, dic_jeu, num:str) -> None:
        """
        Cette fonction prend en paramètre une grille et une liste d'entités
        Il va update pour chaque fantôme présent dans la partie
        """

        pos_possible = self.get_pos_possible(grille, (self.y, self.x), dic_jeu)

        if pos_possible != []:
            ancien_y,ancien_x = self.y, self.x
            y_pos, x_pos = pos_possible[0]

            if pos_possible[0] == (ancien_y,ancien_x-1):
                self.state = "gauche"
            elif pos_possible[0] == (ancien_y,ancien_x+1):
                self.state= "droite"
            elif pos_possible[0] == (ancien_y-1,ancien_x):
                self.state = "haut"
            elif pos_possible[0] == (ancien_y+1,ancien_x):
                self.state = "bas"
    


            grille[ ancien_y ][ ancien_x ].remove(num)
            grille[y_pos][x_pos] += [num]
            self.deplacer((y_pos, x_pos), self.state)

        return
    
    def get_pos_possible(self, grille:list, pos:tuple, dic_jeu) -> list:
        """
            Cette fonction prend en paramètre :
            Une grille : notre niveau
            pos : un couple de coordonnée
            entite : un dictionnaire qui répertorie tout les fantômes vivants

            Cette fonction nous sert à déterminer toute les cases vides proches d'une case cible dont on connaît les coordonnées (pos)
            Elle retourne une liste de tuple de toutes les cases possibles mélangées. Si il n'y a plus de chemin possible elle renvoie une liste vide.
        """
        x_pos, y_pos = pos
        case_disponible = []
        pos_possible = [ (x_pos,y_pos-1), (x_pos+1,y_pos), (x_pos,y_pos+1), (x_pos-1,y_pos) ] # Une liste avec toutes les positions possibles par défaut
        for i in pos_possible:
            x_tmp, y_tmp = i
            if case_valide(grille, x_tmp, y_tmp, dic_jeu): # On fait un tri des positions
                case_disponible += [i]
            
        
        shuffle(case_disponible)
        return case_disponible
    

    def est_proche(self, x_fant:int,y_fant:int, x_bomb:int, y_bomb:int) -> bool:
        """
            Cette fonction prend en paramètre 
            les coordonnées du bomber et les coordonnées d'un fantôme

            renvoie un booléen
        """

        if (x_fant + 1 == x_bomb and y_fant == y_bomb ) \
            or (x_fant == x_bomb and y_fant - 1 == y_bomb ) \
                or (x_fant == x_bomb and y_fant + 1 == y_bomb ) \
                    or (x_fant - 1 == x_bomb and y_fant == y_bomb ):

            return True
        return False

bomber_sprite = {
            "bas" : ["asset/bunny/down/down1.png","asset/bunny/down/down2.png"],
            "gauche": ["asset/bunny/left/left1.png","asset/bunny/left/left2.png"],
            "droite": ["asset/bunny/right/right1.png", "asset/bunny/right/right2.png"],
            "haut": ["asset/bunny/up/up1.png", "asset/bunny/up/up2.png"],
            "pose": ["asset/bunny/pose/poseBombe.png"]
        }

fantome_sprite = {
            "bas" : ["asset/bunny/down/down1.png","asset/bunny/down/down2.png"],
            "gauche": ["asset/bunny/left/left1.png","asset/bunny/left/left2.png"],
            "droite": ["asset/bunny/right/right1.png", "asset/bunny/right/right2.png"],
            "haut": ["asset/bunny/up/up1.png", "asset/bunny/up/up2.png"],
        }

bombe_sprite = {
        "bas" : ["sprites/bombe.png","sprites/bombe1.png", "sprites/bombe2.png", "sprites/bombe3.png"] 
    }

