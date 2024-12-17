import tkiteasy, time
import bomber

WIDTH, HEIGHT = 1200, 800

"""

                    Classe Principale

"""
"""
def create_sprite(g, sprite:dict, settings:dict, dic_jeu:dict, entite:str) -> None:

    return g.afficherImage(
        dic_jeu[entite]["pos"][1]*settings["size"][1], # x, graphique
        dic_jeu[entite]["pos"][0]*settings["size"][0], # y, graphique
        settings["size"], # la valeur de redimension
        sprite[dic_jeu[entite]["direction"]][dic_jeu[entite]["index_sprite"]]) # le sprite de l'entité à un certain stade

def deplacer_entite(g, dic_jeu, sprite:dict, settings, direct, entite):
    g.supprimer(dic_jeu[entite]["obj"])

    dic_jeu[entite]["index_sprite"] += 1
    if dic_jeu[entite]["index_sprite"] >= len(sprite[direct]):
        dic_jeu[entite]["index_sprite"] = 0

    dic_jeu[entite]["obj"] = g.afficherImage(
        dic_jeu[entite]["pos"][1]*settings["size"][1],
        dic_jeu[entite]["pos"][0]*settings["size"][0],
        settings["size"],
        sprite[direct][dic_jeu[entite]["index_sprite"]]
        )
"""

class Entity:
    def __init__(self, g:object, sprite:dict, size:tuple, y:int,x:int, offset:tuple[int, int]):
        self.x, self.y = x+offset[0],y+offset[1]
        self.sprite = sprite
        self.size = size
        self.g = g
        self.state = "bas"
        self.indexState = 0
        #self.obj = self.g.dessinerRectangle(self.x, self.y, self.size[1], self.size[0], "red")
        self.obj = self.g.afficherImage(self.x*self.size[0], self.y*self.size[0], self.size , sprite["bas"][self.indexState] )

    def ChangeSprite(self,direct: str):
        self.Model_Choice(direct)


    def Model_Choice(self, state:str) -> None:
        self.g.supprimer(self.obj)
        self.indexState += 1
        if self.indexState >= len(self.sprite[state]):
            self.indexState = 0

        self.obj = self.g.afficherImage( self.x, self.y, self.size, self.sprite[state][self.indexState])
    
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
        self.x = coords[1]*self.size[0]
        self.y = coords[0]*self.size[1]
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
    def __init__(self, g:object, sprite:dict, size:tuple, x:int,y:int, offset:tuple[int, int]):
        super().__init__(g, sprite, size, x,y, offset)
        



class Fantome(Mob):
    def __init__(self, g:object, sprite:dict, size:tuple, x:int,y:int, offset:tuple[int, int]):
        super().__init__(g, sprite, size, x,y, offset)

"""




grille = [
    [["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"]],
    [["C"], [   ], [   ], ["P"], [   ], [   ], [   ], [   ], ["C"]],
    [["C"], ["M"], ["C"], ["M"], ["C"], ["M"], ["C"], ["M"], ["C"]],
    [["C"], [   ], [   ], [   ], [   ], [   ], ["E"], [   ], ["C"]],
    [["C"], ["M"], ["C"], ["M"], ["C"], ["M"], ["C"], ["M"], ["C"]],
    [["C"], ["U"], [   ], ["M"], ["M"], ["M"], [   ], ["U"], ["C"]],
    [["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"]]
]


coord = bomber.pos_bomber(grille)

CASE = HEIGHT//len(grille)

g = tkiteasy.ouvrirFenetre(len(grille[0])*CASE, len(grille)*CASE+100)
g.dessinerRectangle(0,0,WIDTH, 100,"grey")

affiche_plateau(g, grille)

bunny = {
    "bas" : ["asset/bunny/down/down1.png","asset/bunny/down/down2.png"],
    "gauche": ["asset/bunny/left/left1.png"],
    "droite": ["asset/bunny/right/right1.png", "asset/bunny/right/right2.png"],
    "up": ["asset/bunny/up/up.png"]
}

"""
"""
dict de sprite

dcit_sprite = {
    "bomber" : {
        "up" : ["up1.png", "up2.png"]
        "up" : ["up1.png", "up2.png"]
        "up" : ["up1.png", "up2.png"]
        "up" : ["up1.png", "up2.png"]
    }

    ...
}

l'appel d'une image grâce au dico sprite

dict_sprite     /  bomber    / up        / up1.png
clé dict Sprite / clé entité / direction / image
"""



