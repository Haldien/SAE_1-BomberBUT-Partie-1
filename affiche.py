import tkiteasy, time
import bomber

WIDTH, HEIGHT = 1200, 800

"""

                    Classe Principale

"""
class Entity:
    def __init__(self, g:object, sprite:dict, size:tuple, y:int,x:int):
        self.x, self.y = x,y +100
        self.sprite = sprite
        self.size = size
        self.g = g
        self.state = "bas"
        self.indexState = 0
        self.obj = self.g.afficherImage(self.x, self.y, self.size , sprite["bas"][self.indexState] )

    def ChangeSprite(self,model:int):
        match model:
            case 0: 
                self.Model_Choice("bas")
            case 1: 
                self.Model_Choice("droite")

    def Model_Choice(self, state:str) -> None:
        self.g.supprimer(self.obj)
        self.indexState += 1
        if self.indexState >= len(self.sprite[state]):
            self.indexState = 0

        self.obj = self.g.afficherImage( self.x, self.y, self.size, self.sprite[state][self.indexState])

"""

                    Dépendance d'Entité

"""


class Mob(Entity):
    def __init__(self, g:object, sprite:dict, size:tuple, x:int,y:int):
        super().__init__(g, sprite, size, x,y )

    def deplacer(self, coords:tuple[int,int]) -> None:
        # Changement de sprite
        self.g.deplacer(self.obj, coords[0], coords[1])
    
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

def affiche_plateau(g, grille:list[list[list]]):
    for x in range(len(grille)):
        for y in range(len(grille[0])):
            if grille[x][y] == ['C']:
                g.dessinerRectangle(y*CASE,100+x*CASE, CASE, CASE, "white")







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


new = Bomber(g, bunny, (CASE,CASE), coord[0]*CASE, coord[1]*CASE)

for i in range(5):
    g.update()
    time.sleep(.5)
    new.ChangeSprite(1)
    g.update()
    time.sleep(.5)

for i in range(5):
    g.update()
    time.sleep(.5)
    new.ChangeSprite(0)
    g.update()
    time.sleep(.5)



while not g.recupererClic():

    pass

g.fermerFenetre()

