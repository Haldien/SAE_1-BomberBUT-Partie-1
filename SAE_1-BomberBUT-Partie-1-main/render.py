from tkiteasy import ObjetGraphique
from random import shuffle
from fonctions_utiles  import *
from constante import *



def render(grille, g, dic_jeu, objets_graphiques = None) -> list[ObjetGraphique]:

    dimensions_case = dimensions_de_case(grille)

    # pour qu'il n'y ait pas de superposition : suppresions des objets précédents
    if objets_graphiques is not None:
        for obj in objets_graphiques:
            g.supprimer(obj)

    objets = list()

    for y in range(len(grille)):
        for x in range(len(grille[0])):

            coord_x = x * dimensions_case[0]
            coord_y = y * dimensions_case[1]

            if "M" in grille[y][x]:
                obj = g.afficherImage(coord_x, coord_y, (dimensions_case[0], dimensions_case[1]), "sprites/mur.png")
                objets.append(obj)
            if "B" in grille[y][x]:
                obj = g.dessinerRectangle(coord_x, coord_y, dimensions_case[0], dimensions_case[1], "red")
                objets.append(obj)
            if "P" in grille[y][x]:
                obj = g.dessinerRectangle(coord_x, coord_y, dimensions_case[0], dimensions_case[1], "blue")
                objets.append(obj)
            if "U" in grille[y][x]:
                obj = g.dessinerRectangle(coord_x, coord_y, dimensions_case[0], dimensions_case[1], "pink")
                objets.append(obj)
            for el in grille[y][x]:
                if el in list(dic_jeu["fantomes"].keys()):
                    obj = g.dessinerRectangle(coord_x, coord_y, dimensions_case[0], dimensions_case[1], "white")
                    objets.append(obj)
            
            # On place les éléments indestructibles qu'à la première itération de render()
            if objets_graphiques is None:
                if "C" in grille[y][x]:
                    g.dessinerRectangle(coord_x, coord_y, dimensions_case[0], dimensions_case[1], "grey")
                if "E" in grille[y][x]:
                    g.dessinerRectangle(coord_x, coord_y, dimensions_case[0], dimensions_case[1], "green")


    return objets


def render_explosions_apparition(grille, g, case_affectees, offset:tuple[int,int] = (0,0))-> list[ObjetGraphique]:

    dimensions_case = dimensions_de_case(grille)

    coords_affectees = list()
    for liste in list(case_affectees.values()):
        for coord in liste:
                coords_affectees.append(coord)

    objets_graphiques_explosions = list()

    for coord in coords_affectees:
        coord_x =   offset[0] + coord[1] * dimensions_case[0]
        coord_y =   offset[1] + coord[0] * dimensions_case[1]

        obj = g.afficherImage(coord_x, coord_y, (dimensions_case[0], dimensions_case[1]), "sprites/explosion.png")
        objets_graphiques_explosions.append(obj)

    return objets_graphiques_explosions

def render_explosions_suppression(g, objets_graphiques_explosions):

    for obj in objets_graphiques_explosions:

        g.supprimer(obj)

def render_undestructible(g, grille:list[list[list[str]]], offset:tuple[int,int] = (0,0)) -> None:
    """
        Cette fonction va afficher toutes cases qui vont rester inchangés au cours du jeu.
    """

    dim_case = dimensions_de_case(grille)

    for y in range(len(grille)):
        for x in range(len(grille[0])):
            
            
            coord_x =  offset[0] + x * dim_case[0]
            coord_y =  offset[1] + y * dim_case[1]

            if "C" in grille[y][x]:
                g.dessinerRectangle(coord_x,coord_y, dim_case[0], dim_case[1],"white")

def spawn_bomber(g, dic_jeu, settings):
    dic_jeu["bomber"] = Bomber(g, bomber_sprite, settings["size"], dic_jeu["bomber"]["pos"][0], dic_jeu["bomber"]["pos"][1],settings["offset"],3, 0 )

def spawn_fantome(g, dic_jeu, settings):
    for i in dic_jeu["fantomes"]:
        if dic_jeu["fantomes"][i]["obj"] == "objetGraphique":
            dic_jeu["fantomes"][i]["obj"] = Fantome(g, fantome_sprite, settings["size"], dic_jeu["fantomes"][i]["pos"][0], dic_jeu["fantomes"][i]["pos"][1], settings["offset"])

def dep_fantome(dic_jeu):
    for i in dic_jeu["fantomes"]:
        dic_jeu["fantomes"][i].deplacer((dic_jeu["fantomes"][i].y, dic_jeu["fantomes"][i].x), dic_jeu["fantomes"][i].state)

def dep_bomber(bomber):
    bomber.deplacer((bomber.y, bomber.x), bomber.state)

def create_object(g, grille: list[list[list[str]]], dic_jeu,settings) -> None:
    dim_case = dimensions_de_case(grille)
    for y in range(len(grille)):
        for x in range(len(grille[0])):
            if "M" in grille[y][x]:
                dic_jeu["mur"][(x,y)] = Mur(g, {"bas": ["sprites/mur.png"] },dim_case, y, x, settings["offset"])
            elif "U" in grille[y][x]:
                dic_jeu["upgrade"][(x,y)] = Upgrade(g, {"bas": ["sprites/upgrade.png"] },dim_case, y, x, settings["offset"])
            elif "E" in grille[y][x]:
                dic_jeu["ethernet"][(y,x)] = Ethernet(g, {"bas" : ["sprites/ethernet.png"]}, dim_case, y,x, settings["offset"])

"""

                    Classe Principale

"""
class Entity:
    def __init__(self, g:object, sprite:dict, size:tuple, y:int,x:int, offset:tuple[int, int]):
        self.x, self.y =  x ,y
        self.sprite = sprite
        self.size = size
        self.offset = offset
        self.g = g
        self.state = "bas"
        self.indexState = 0
        self.obj = self.g.afficherImage(self.offset[0] + self.x * self.size[0], self.offset[1] + self.y*self.size[1], self.size , sprite["bas"][self.indexState] )

    def ChangeSprite(self,direct: str):
        self.Model_Choice(direct)


    def Model_Choice(self, state:str) -> None:
        self.g.supprimer(self.obj)
        self.indexState += 1
        if self.indexState >= len(self.sprite[state]):
            self.indexState = 0

        self.obj = self.g.afficherImage(self.offset[0] + self.x * self.size[0], self.offset[1] + self.y*self.size[1], self.size, self.sprite[state][self.indexState])
    
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

class Upgrade(Entity):
    def __init__(self, g, sprite, size, y, x, offset):
        super().__init__(g, sprite, size, y, x, offset)

class Bombes(Entity):
    def __init__(self, g:object, sprite:dict, size:tuple, x:int,y:int, offset:tuple[int, int]):
        super().__init__(g, sprite, size, x,y, offset)
        
    def ignite(self, timer:int):
        self.g.supprimer(self.obj)
        
        if timer < 2:
            self.indexState = 3
            self.obj = self.g.afficherImage(self.offset[0] + self.x * self.size[0], self.offset[1] + self.y*self.size[1], self.size,self.sprite[self.state][self.indexState])
        elif timer < 3:
            self.indexState = 2
            self.obj = self.g.afficherImage(self.offset[0] + self.x * self.size[0], self.offset[1] + self.y*self.size[1], self.size,self.sprite[self.state][self.indexState])
        elif timer < 4:
            self.indexState = 1
            self.obj = self.g.afficherImage(self.offset[0] + self.x * self.size[0], self.offset[1] + self.y*self.size[1], self.size,self.sprite[self.state][self.indexState])
        else:
            self.indexState = 0
            self.obj = self.g.afficherImage(self.offset[0] + self.x * self.size[0], self.offset[1] + self.y*self.size[1], self.size,self.sprite[self.state][self.indexState])


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
        
    def deplacer_bomber(self, grille, y: int, x: int, dic_jeu):

        if "U" in grille[y][x]:
            dic_jeu["upgrade"][(x,y)].supprimerEntite()
            del dic_jeu["upgrade"][(x,y)]
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
            dic_jeu["bombes"][(self.y, self.x)] = {'timer': 6, 'obj': Bombes(g, bombe_sprite ,self.size, self.y, self.x, self.offset )}

    def action_bomber(self, g, grille, touche: str, dic_jeu:dict):
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
        if touche in ["z", "q", "s", "d"] :

          if not case_valide(grille, self.y + mouvements[touche][0], self.x + mouvements[touche][1], dic_jeu):
            while True :

                touche = g.attendreTouche()

                if touche in ["space", "Return"]:
                    break

                if touche in ["z", "q", "s", "d"] and case_valide(grille, self.y + mouvements[touche][0], self.x + mouvements[touche][1], dic_jeu):
                    match(touche):
                        case "z":
                            self.state = "haut"
                        case "q":
                            self.state= "gauche"
                        case "s":
                            self.state = "bas"
                        case "d":
                            self.state = "droite"
                    self.deplacer_bomber(grille, self.y + mouvements[touche][0], self.x + mouvements[touche][1], dic_jeu)
                    break
                    
        # Cas normal
          else:
            self.deplacer_bomber(grille, self.y + mouvements[touche][0],
                            self.x+ mouvements[touche][1], dic_jeu)
          
        if touche == "space":
            self.state = "pose"
            self.poser_bombe(self.g, grille, dic_jeu)

        # Passe son tour
        if touche == "Return":
            pass


class Fantome(Mob):
    def __init__(self, g:object, sprite:dict, size:tuple, x:int,y:int, offset:tuple[int, int]):
        super().__init__(g, sprite, size, x,y, offset)
        self.ancien_coord = []
    
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
            self.ancien_coord += [(self.y, self.x)]
            if len(self.ancien_coord) > 3:
                self.ancien_coord = self.ancien_coord[1:]
            self.deplacer((y_pos, x_pos), self.state)

        return
    def attaque_fantome(self, dic_jeu:dict) -> None:
        """
            Note au développeur: Le player pos peut directement évoluer avec le dico bomber 
            Cette fontion prend en paramètre une grille de jeu, le couple de coordonnée du joueur et les entités 
            Elle permet d'appliquer des dégâts au bomber si un fantôme se situe dans la case adjacente à celui ci.
            Elle ne renvoie rien
        """
        entite = dic_jeu["fantomes"]
        posFantome = []
        for fantome in entite:
            posFantome += [(self.x, self.y)]
        x_bomber, y_bomber = dic_jeu["bomber"].x, dic_jeu["bomber"].y
        for pos in posFantome:
            x_fant, y_fant = pos
            if self.est_proche(x_fant, y_fant, x_bomber, y_bomber):

                dic_jeu["bomber"].pv -= 1
                dic_jeu["bomber"].cooldown = 5 # Pour éviter le multi-dégât
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
                if len(self.ancien_coord) >= 3:
                    x_last, y_last = self.ancien_coord[2]
                    if x_tmp == x_last and y_last == y_tmp:
                        continue
                case_disponible += [i]
            
        if case_disponible == [] and len(self.ancien_coord) >= 3:
            case_disponible = [(self.ancien_coord[-1][0], self.ancien_coord[-1][1])]
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

def get_pos_possible(grille:list, pos:tuple, dic_jeu) -> list:
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

def apparition_fantomes(g,grille:list, dic_jeu:dict, settings:dict) -> None:
    """
    Prend en paramètre une grille, un dictionnaire de fantômes, et un dictionnaire de prises


    Modifie une dictionnaire en ajoutant les fantômes dans un format
    entites = {
        fantome{index} = [objetGraphique, (coordonnées)]
    }
    La taille du dictionnaire correspond aux nombres de fantômes présents dans la partie actuelle.
    """
    entite = dic_jeu["fantomes"]
    pos_prise = []
    for pos in dic_jeu["ethernet"]:
        pos_prise += [pos]
    shuffle(pos_prise)
    if pos_prise == []:
        return 
    pos = pos_prise[0]

    case_disponible = get_pos_possible(grille, pos, dic_jeu)
    if case_disponible == []: # Si la liste est vide on stop la fonction
        return

    shuffle(case_disponible)
    new_entity = f"F{settings["nombrefantome"]}"
    settings["nombrefantome"] += 1
    entite[new_entity] = Fantome(g, fantome_sprite, settings["size"], case_disponible[0][0], case_disponible[0][1], settings["offset"])
    grille[case_disponible[0][0]][case_disponible[0][1]] += [new_entity]
