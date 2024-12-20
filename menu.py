from constante import *
from main import *
from tkiteasy import *

class Button:
    def __init__(self,g, x,y,text):
        self.g = g
        self.x, self.y = x, y
        self.text = text
        self.lenght = 300
        self.height = 100
        self.area = None
        self.text_box = None
        self.state = "inactive"

        self.dessinerBouton()
    
    def dessinerBouton(self):
        self.area = self.g.dessinerRectangle(
            self.x-self.lenght//2, 
            self.y-self.height//2, 
            self.lenght,
            self.height,
            "black"
        )
        self.text_box = self.g.afficherTexte(self.text,self.x, self.y, "white",20, "normal", "Consolas", "center")
        
    
    def isHover(self):
        posSouris = self.g.recupererPosition()

        if self.x-self.lenght//2 < posSouris.x < self.x+self.lenght//2 \
            and self.y-self.height//2 < posSouris.y < self.y+self.height//2:
                self.g.changerCouleur(self.area, "red")
                self.state = "active"
                
        elif self.state == "active":
                self.g.changerCouleur(self.area, "black")
                self.state = "inactive"


    
    def onClick(self, clic:tuple[int,int]) -> bool:
        if clic == None:
             return False
        if self.x-self.lenght//2 < clic.x < self.x+self.lenght//2 \
            and self.y-self.height//2 < clic.y < self.y+self.height//2:
             return True
        return False
    
    def supprimer_bouton(self):
        self.g.supprimer(self.text_box)
        self.g.supprimer(self.area)
        del self

def create_text_menu(g:Canevas):
        title = g.afficherTexte("BOMBERMAN UT",fenetre_dimensions[0]//2, 150,newWeight="bold", taille=50 )
        second_title = g.afficherTexte("La Rénovation de Maryse Bastier",fenetre_dimensions[0]//2,220,newWeight="bold", taille=20)
        """"""
        play = Button(g,fenetre_dimensions[0]//2, fenetre_dimensions[1]//2, "JOUEZ")
        scoreBoard = Button(g,fenetre_dimensions[0]//2, fenetre_dimensions[1]//2+120, "SCOREBOARD")
        settingButton = Button(g, fenetre_dimensions[0]//2, fenetre_dimensions[1]//2+ 240, "PARAMÈTRE")
        exitButton = Button(g,fenetre_dimensions[0]//2, fenetre_dimensions[1]//2+360, "FERMER LE JEU")


        return  [title, second_title, play, scoreBoard,settingButton, exitButton]

g = ouvrirFenetre(fenetre_dimensions[0], fenetre_dimensions[1])

def menu(g):
    touche = None
    element = create_text_menu(g)

    while touche != 'space':
        touche = g.recupererTouche()
        clic = g.recupererClic()
        for i in element:
                if type(i) is Button:
                    i.isHover()


        if element[2].onClick(clic):
            for i in element:
                if type(i) == Button:
                    i.supprimer_bouton()
                else:
                    g.supprimer(i)
            main(g)
            element=create_text_menu(g)
            
        elif element[3].onClick(clic):
            pass
        elif element[4].onClick(clic):
            pass

        elif element[5].onClick(clic):
            quit()

        g.update()
    g.fermerFenetre()

menu(g)
