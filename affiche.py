import tkiteasy, time
import bomber

WIDTH, HEIGHT = 1200, 800

"""

                    Classe Principale

"""
class Entity:
    def __init__(self, g:object, sprite:dict, size:tuple, y:int,x:int):
        self.x, self.y = x,y
        self.sprite = sprite
        self.size = size
        self.g = g
        self.state = "bas"
        self.indexState = 0
        #self.obj = self.g.dessinerRectangle(self.x, self.y, self.size[1], self.size[0], "red")
        self.obj = self.g.afficherImage(self.x, self.y, self.size , sprite["bas"][self.indexState] )

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
    def __init__(self, g:object, sprite:dict, size:tuple, x:int,y:int):
        super().__init__(g, sprite, size, x,y )

    def deplacer(self, coords:tuple[int,int], direct:str) -> None:
        # Changement de sprite
        self.x = coords[1]*self.size[0]
        self.y = coords[0]*self.size[1]
        print(self.x, self.y)
        self.g.deplacer(self.obj, coords[0], coords[1])
        self.ChangeSprite(direct)


    def subitDegat(self):
        self.g.supprimer(self.obj)
        self.obj = self.g.afficherImage


class Ethernet(Entity):
    def __init__(self, g:object, sprite:dict, size:tuple, x:int,y:int):
        super().__init__(g, sprite, size, x,y )
    
    def fait_apparaitre():
        pass

class Bombes(Entity):
    def __init__(self, g:object, sprite:dict, size:tuple, x:int,y:int):
        super().__init__(g, sprite, size, x,y )
    
    def explose(self):
        pass

class Mur(Entity):
    def __init__(self, g:object, sprite:dict, size:tuple, x:int,y:int):
        super().__init__(g, sprite, size, x,y )

"""

                    Dépendance de Mob

"""
class Bomber(Mob):
    def __init__(self, g:object, sprite:dict, size:tuple, x:int,y:int):
        super().__init__(g, sprite, size, x,y )

    def poseBombe(self):
        pass


class Fantome(Mob):
    def __init__(self, g:object, sprite:dict, size:tuple, x:int,y:int):
        super().__init__(g, sprite, size, x,y )

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



