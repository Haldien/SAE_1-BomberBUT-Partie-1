from main import *
from tkiteasy import *
from datetime import datetime

"""
===============================================================================================

                            Classe Buton

===============================================================================================
"""
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
    
    def dessinerBouton(self) -> None:
        """
            Cette Méthode permet de dessiner le fond du bouton
            Elle ne renvoie rien
        """
        self.area = self.g.dessinerRectangle(
            self.x-self.lenght//2, 
            self.y-self.height//2, 
            self.lenght,
            self.height,
            "black"
        )
        self.text_box = self.g.afficherTexte(self.text,self.x, self.y, "white",20, "normal", "Consolas", "center")
        
    
    def isHover(self) -> None:
        """
            Cette méthode permet de changer la couleur du fond du bouton au survol
            Elle ne renvoie rien
        """
        posSouris = self.g.recupererPosition()

        if self.x-self.lenght//2 < posSouris.x < self.x+self.lenght//2 \
            and self.y-self.height//2 < posSouris.y < self.y+self.height//2:
                self.g.changerCouleur(self.area, "red")
                self.state = "active"
                
        elif self.state == "active":
                self.g.changerCouleur(self.area, "black")
                self.state = "inactive"

    def onClick(self, clic:tuple[int,int]) -> bool:
        """
            Cette méthode permet d'éxécuter une action au clic d'un utilisateur
            Elle prend un tuple de coordonnée d'un clic
            Elle renvoie une valeur booléeenne
        """
        if clic == None:
             return False
        if self.x-self.lenght//2 < clic.x < self.x+self.lenght//2 \
            and self.y-self.height//2 < clic.y < self.y+self.height//2:
             return True
        return False
    
    def supprimer_bouton(self) -> None:
        """
            Cette méthode permet de supprimer cette objet proprement
            Elle ne renvoie rien
        """
        self.g.supprimer(self.text_box)
        self.g.supprimer(self.area)
        del self
"""
===============================================================================================

                            Menu Principal

===============================================================================================
"""
def supprime_elem(g, element:list) -> None:
    """
        Cette fonction prend en paramètre une liste d'objets graphiques d'un menu ainsi qu'une fenêtre graphique
        Elle supprime tout les éléments de cette liste
        Elle ne renvoie rien
    """
    while element != []:
        if type(element[0]) == Button:
            element[0].supprimer_bouton()
            del element[0]
        else:
            g.supprimer(element[0])
            del element[0]

def create_text_menu(g:Canevas) -> None:
        """
            Cette fonction prend en paramètre une fenêtre graphique
            Elle affiche tout les boutons et textes du menu principal
            Elle renvoie rien
        """
        title = g.afficherTexte("BOMBERMAN UT",fenetre_dimensions[0]//2, 150,newWeight="bold", taille=50 )
        second_title = g.afficherTexte("La Rénovation de Maryse Bastier",fenetre_dimensions[0]//2,220,newWeight="bold", taille=20)
        play = Button(g,fenetre_dimensions[0]//2, fenetre_dimensions[1]//2, "JOUEZ")
        scoreBoard = Button(g,fenetre_dimensions[0]//2, fenetre_dimensions[1]//2+120, "SCOREBOARD")
        settingButton = Button(g, fenetre_dimensions[0]//2, fenetre_dimensions[1]//2+ 240, "PARAMÈTRE")
        exitButton = Button(g,fenetre_dimensions[0]//2, fenetre_dimensions[1]//2+360, "FERMER LE JEU")


        return  [title, second_title, play, scoreBoard,settingButton, exitButton]

def menu(g:Canevas, carte: str = "") -> None:
    """
        Cette fonction prend en paramètre une fenêtre graphique
        Elle permet d'afficher et de naviguer à travers les différeents menu ( Jouer, Tableaux des score, paramètre et quitter)
        Elle ne renvoie rien
    """
    touche = None
    element = create_text_menu(g)


    while touche != "Escape":
        touche = g.recupererTouche()
        clic = g.recupererClic()
        for i in element:
                if type(i) is Button:
                    i.isHover()


        if element[2].onClick(clic):
            supprime_elem(g,element)
            
            
            choice_random_import(g, carte)
            element=create_text_menu(g)
            
        elif element[3].onClick(clic):
            supprime_elem(g, element)
            scoreboard(g)
            element = create_text_menu(g)


        elif element[4].onClick(clic):
            supprime_elem(g, element)
            parametre(g)
            element = create_text_menu(g)

        elif element[5].onClick(clic):
            quit()

        g.update()
    g.fermerFenetre()

def create_mode(g:Canevas) -> list:
    """
        Cette fonction permet de créer les boutons et textes graphiques sur la fenêtre de choix de mode
        Elle renvoie une liste d'objet graphique
    """
    enonce = g.afficherTexte("Quel mode de jeu ?", fenetre_dimensions[0]//2, fenetre_dimensions[1]//2-100, taille=25, newWeight="bold")
    aleatoire = Button(g, fenetre_dimensions[0]//3, fenetre_dimensions[1]//2+200, "ALEATOIRE")
    importe = Button(g, fenetre_dimensions[0]*2//3, fenetre_dimensions[1]//2+200, "IMPORT")

    return [enonce, aleatoire, importe]


def choice_random_import(g:Canevas, carte:str) -> None:
    """
        Cette fonction permet de faire un choix entre un mode de génération aléatoire ou d'un niveau importé
        Le niveau importé doit être défini au dans le script exec.py
        Cette fonction ne renvoie rien
    """
    touche = None
    clic = None
    element = create_mode(g)

    while touche != "Escape":
        touche = g.recupererTouche()
        clic = g.recupererClic()

        for i in element:
            if type(i) == Button:
                i.isHover()
        
        if element[1].onClick(clic):
            supprime_elem(g, element)
            choice_size(g)
            return
        elif element[2].onClick(clic):
            supprime_elem(g, element)
            data = main(g, carte)
            nouveau_score(g, data[0], data[1], data[2])
            return
    supprime_elem(g,element)

def create_choice_size(g:Canevas) -> list:
    """
        Cette fonction prend en argument une fenêtre graphique
        Elle permet d'afficher tout les boutons et textes sur la fenêtre
        Elle renvoie une liste d'objet graphique
    """
    title = g.afficherTexte("Chosissez la taille de votre grille", fenetre_dimensions[0]//2, 200)
    row_minus_button = Button(g, fenetre_dimensions[0]//3, fenetre_dimensions[0]//3, "- Ligne")
    row_plus_button = Button(g, fenetre_dimensions[0]*2//3, fenetre_dimensions[0]//3, "+ Ligne")
    column_minus_button = Button(g, fenetre_dimensions[0]//3, fenetre_dimensions[0]*2//3-200, "- Colonne")
    column_plus_button = Button(g, fenetre_dimensions[0]*2//3, fenetre_dimensions[0]*2//3-200, "+ Colonne")

    valide = Button(g, fenetre_dimensions[0]//2, fenetre_dimensions[1] -200, "JOUEZ !")

    return [title, row_minus_button, row_plus_button, column_minus_button, column_plus_button, valide]

def choice_size(g:Canevas):
    """
        Cette fonction permet de créer une fenêtre qui permet au joueur de choisir la taille de la grille qu'il souhaite générer
    """
    touche = None
    clic = None
    element = create_choice_size(g)
    row = 5
    column = 5

    text_row = g.afficherTexte(str(row), fenetre_dimensions[0]//2, fenetre_dimensions[0]//3, taille=25,newWeight="bold")
    text_column = g.afficherTexte(str(column), fenetre_dimensions[0]//2, fenetre_dimensions[0]*2//3-200, taille=25,newWeight="bold")
    while touche != "Escape":
        touche = g.recupererTouche()
        clic = g.recupererClic()

        for i in element:
            if type(i) == Button:
                i.isHover()
        
        if element[1].onClick(clic):
            g.supprimer(text_row)
            if row-1 > 4:
                row -= 1
            text_row = g.afficherTexte(str(row), fenetre_dimensions[0]//2, fenetre_dimensions[0]//3, taille=25,newWeight="bold")
        elif element[2].onClick(clic):
            g.supprimer(text_row)
            if row +1 < 100:
                row += 1
            text_row = g.afficherTexte(str(row), fenetre_dimensions[0]//2, fenetre_dimensions[0]//3, taille=25,newWeight="bold")
        elif element[3].onClick(clic):
            g.supprimer(text_column)
            if column-1 > 4:
                column -= 1
            text_column = g.afficherTexte(str(column), fenetre_dimensions[0]//2, fenetre_dimensions[0]*2//3-200, taille=25,newWeight="bold")
        elif element[4].onClick(clic):
            g.supprimer(text_column)
            if column+1 < 100:
                column += 1
            text_column = g.afficherTexte(str(column), fenetre_dimensions[0]//2, fenetre_dimensions[0]*2//3-200, taille=25,newWeight="bold")
        
        elif element[5].onClick(clic):
            supprime_elem(g, element)
            g.supprimer(text_row)
            g.supprimer(text_column)
            del text_row
            del text_column
            data = main(g, row = row, column= column)
            nouveau_score(g, data[0], data[1], data[2])
            return
     
    g.supprimer(text_row)
    g.supprimer(text_column)
    del text_row
    del text_column
    supprime_elem(g, element)
"""
===============================================================================================

                            Gestion des Scores

===============================================================================================
"""

def scoreboard(g:Canevas) -> None:
    """
        Cette fonction prend en paramètre une fenêtre graphique
        Elle permet d'afficher le premier sous-menu, celui du tableau des scores
        Elle ne renvoie rien 
    """
    dic_score = create_dic_score()
    podium_score = order_by_score(dic_score) if len(dic_score) > 0 else []
    podium_date = list(dic_score.values())[::-1]

    element = []
    order_score_button = Button(g, fenetre_dimensions[0]//8+150, 750, "par Score")
    order_date_button = Button(g, fenetre_dimensions[0]//8+500,750, "par Date")
    back = Button(g, fenetre_dimensions[0]//8 + 800, 750, "Revenir ")

    element += [order_score_button, order_date_button, back]
    element += create_text_scoreBoard(g, podium_score) 
    touche = None
    while touche != "Escape":
        touche = g.recupererTouche()
        clic = g.recupererClic()

        for i in element:
                if type(i) is Button:
                    i.isHover()
        
        if element[0].onClick(clic):
            while len(element) != 3:
                g.supprimer(element[3])
                del element[3]
            element += create_text_scoreBoard(g,podium_score)

        elif element[1].onClick(clic):
            while len(element) != 3:
                g.supprimer(element[3])
                del element[3]
            element += create_text_scoreBoard(g,podium_date)
        
        elif element[2].onClick(clic):
            break
        
        g.update()
    
    for i in element:
        if type(i) == Button:
            i.supprimer_bouton()
        else:
            g.supprimer(i)


def create_text_scoreBoard(g:Canevas, podium:list) -> None:
    """
        Cette fonction prend en paramètre une liste de dico trié selon soit la date d'insertion ou le score et une fenêtre graphique.
        Elle permet d'afficher le podium des 5 meilleurs ou derniers joueurs ayant joué.
        Elle ne renvoie rien
    """
    command_line = g.afficherTexte("C:/IUT/Tableau_des_Scores.exe", fenetre_dimensions[0]//8, 200, taille=40, newWeight="bold",ancre="w")
    title = g.afficherTexte("===[ ScoreBoard ]===", fenetre_dimensions[0]//8, 300, taille=20, ancre='w')

    if (len(podium)>0):
        first = g.afficherTexte(f"1 - {podium[0]["nom"]} {podium[0]["mode"]} {podium[0]["score"]} {podium[0]["date"]}", fenetre_dimensions[0]//8, 350, "gold", 20, "bold", ancre='w')
    else:
        first = g.afficherTexte(f"1 - Error404 : NOTFOUND", fenetre_dimensions[0]//8, 350, "gold", 20, "bold", ancre='w')
    if (len(podium)>1):
        second = g.afficherTexte(f"2 - {podium[1]["nom"]} {podium[1]["mode"]} {podium[1]["score"]} {podium[1]["date"]}", fenetre_dimensions[0]//8, 400, "silver", 20, "bold", ancre='w')
    else:
        second = g.afficherTexte(f"2 - Error404 : NOTFOUND", fenetre_dimensions[0]//8, 400, "white", 20, "bold", ancre='w')
    if (len(podium)>2):
        third = g.afficherTexte(f"3 - {podium[2]["nom"]} {podium[2]["mode"]} {podium[2]["score"]} {podium[2]["date"]}", fenetre_dimensions[0]//8, 450, "brown", 20, "bold", ancre='w')
    else:
        third = g.afficherTexte(f"3 - Error404 : NOTFOUND", fenetre_dimensions[0]//8, 450, "brown", 20, "bold", ancre='w')
    if (len(podium)>3):
        fourth = g.afficherTexte(f"4 - {podium[3]["nom"]} {podium[3]["mode"]} {podium[3]["score"]} {podium[3]["date"]}", fenetre_dimensions[0]//8, 500, "gray6", 20, "bold", ancre='w')
    else:
        fourth = g.afficherTexte(f"4 - Error404 : NOTFOUND", fenetre_dimensions[0]//8, 500, "gray8", 20, "bold", ancre='w')
    if (len(podium)>4):
        fifth = g.afficherTexte(f"5 - {podium[4]["nom"]} {podium[4]["mode"]} {podium[4]["score"]} {podium[4]["date"]}", fenetre_dimensions[0]//8, 550, "gray6", 20, "bold", ancre='w')
    else:
        fifth = g.afficherTexte(f"5 - Error404 : NOTFOUND", fenetre_dimensions[0]//8, 550, "gray8", 20, "bold", ancre='w')

    return [command_line, title, first, second, third, fourth, fifth]

def insert_into_scoreboard(name:str, mode:str, score:str, level:str) -> None:
    """
        Cette fonction prend en paramètre;
            name, str, un nom de joueur
            mode, str, le mode qu'il a joué
            score, str, le score qu'il a obtenu
            et le niveau qu'il a atteint
        Cette fonction permet de sauvegarder son haut-fait dans un fichier texte (scoreboard.txt)
        Elle ne renvoie rien
    """
    date = datetime.today()
    d_format = date.strftime("%d-%b-%y")
    ressource = open("scoreboard.txt", "a")
    new_line = f"{name} {mode} {score} {level} {d_format}\n"
    ressource.write(new_line)
    ressource.close()

def del_in_scoreboard(dic_score:str, name: str="" ) -> None:
    """
        Cette fonction prend en paramètre un dictionnaire de score, et un nom
        Elle permet de supprimer un nom de la liste de joueur
        Elle ne renvoie rien
    """
    id_a_supp = research_by_name(dic_score,name)
    del dic_score[id_a_supp]

    ressource = open("scoreboard.txt", "w+", encoding="utf-8")
    dic_score_val = dic_score.values()
    for values in list(dic_score_val):
        ressource.write(f"{values["nom"]} {values["mode"]} {values["score"]} {values["level"]} {values["date"]}\n")
    ressource.close()

def research_by_name(dic_score:dict, name:str) -> int:
    """
        Cette fonction prend en paramètre 2 paramètres, un dictionnaire de score, et un nom
        Elle retourne l'identifiant de ce joueur dans cette liste de joueur, si elle ne trouve pas, elle renverra -1
    """
    for i in range(len(dic_score)):
        if dic_score[i]["nom"] == name:
            ident = i
            return ident
    return -1

def order_by_score(dic_score:dict) -> list:
    """
        Cette fonction prend en paramètre un dictionnaire de score
        Elle permet de trier les joueurs selon leurs scores obtenues par ordres décroissant, selon un algorithme de tri par insertions
        Elle renvoie une liste de dictionnaires triés par scores.
    """
    result = list(dic_score.values())   
    
    for i in range(1, len(result)):
        val = result[i]
        j = i-1
        while j>=0 and int(result[j]["score"]) > int(val["score"]):
            result[j+1] = result[j]
            j -= 1
        result[j+1] = val
    print(result)
    return result[::-1]
    

def create_dic_score() -> None:
    """
    
        Cette fonction permet de crée un dictionnaire de score à partir d'un fichier texte
        Elle ne renvoie rien
        # Format du scoreboard ( name, mode, score, level, date )
    """
    dic_score = {}
    
    ressource = open("scoreboard.txt", "r", encoding="utf_8")
    line = ressource.readlines()
    for i in range(len(line)):
        content = line[i].split(" ")
        dic_score[i] = {"nom" : content[0], "mode" : content[1], "score": content[2], "level" : content[3], "date": content[4].removesuffix("\n") }

    ressource.close()

    return dic_score

def est_present(order:list, name:str, score:str) -> bool:
    """
        Cette fonction prend en paramètre une liste de joueur trié, un nom et un score
        Elle permet de savoir si un joueur est déjà existant et en plus son score est supérieur à son essai précédent
        Elle renvoie une valeur booléeene
    """
    for el in order:
        if el["nom"] == name and int(el["score"]) < score:
            return True
    return False

def update_score(pseudo:str, score:str, niv:str, mode: str) -> None:
    """
        Cette fonction prend en paramètre un pseudo, un score et un niveau
        Elle permet d'insérer un nouveau joueur dans le fichier texte tout en vérifiant si il existant ou non
        Elle ne renvoie rien
    """
    dic_score :dict= create_dic_score()
    order :list = order_by_score(dic_score)
    recherche = research_by_name(dic_score, pseudo)
    if  recherche == -1: # Pseudo non trouvé
        insert_into_scoreboard(pseudo, mode, score,niv)
    else:
        if est_present(order, pseudo, score):
            del_in_scoreboard(dic_score, pseudo) # On supprime l'ancien score
            insert_into_scoreboard(pseudo, mode, score,niv)
                

def nouveau_score(g: Canevas, score : int, niv : int, mode:str) -> None:
    """
        Cette fonction prend en paramètre une fenêtre graphique, un score un niveau
        Elle permet de créé un nouveau sous-menu qui permet de rentrer un nouveau joueur, l'utilisateur peut entrer du texte 
        Elle ne renvoie rien
    """

    touche = None
    pseudo = ""
    enonce = g.afficherTexte("Entrez un nom", fenetre_dimensions[0]//2, fenetre_dimensions[1]//2-200, taille=35, newWeight="bold")
    pseudo_affiche = g.afficherTexte(pseudo, fenetre_dimensions[0]//2, fenetre_dimensions[1]//2, taille=35, newWeight="bold")

    while touche != "Escape":
        touche = g.recupererTouche()
        if touche in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'z', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'q', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'w', 'x', 'c', 'v', 'b', 'n'] and len(pseudo) < 10: #uniques caractères possibles
            pseudo += touche
            g.supprimer(pseudo_affiche)
            pseudo_affiche = g.afficherTexte(pseudo, fenetre_dimensions[0]//2, fenetre_dimensions[1]//2, taille=35, newWeight="bold")
        elif touche == "BackSpace":
            pseudo = pseudo[:-1]
            g.supprimer(pseudo_affiche)
            pseudo_affiche = g.afficherTexte(pseudo, fenetre_dimensions[0]//2, fenetre_dimensions[1]//2, taille=35, newWeight="bold")
        elif touche == "Return" and len(pseudo) > 3:
            update_score(pseudo, score, niv, mode)
            g.supprimer(pseudo_affiche)
            del pseudo_affiche
            g.supprimer(enonce)
            del enonce
            return
  
    g.supprimer(pseudo_affiche)
    del pseudo_affiche
    g.supprimer(enonce)
    del enonce
"""
===============================================================================================

                            Option Paramètres

===============================================================================================
"""

def parametre(g) -> None:
    """
        Cette fonction prend en paramètre une fenêtre graphique
        Elle permet d'afficher un nouveau sous-menu
        Elle ne renvoie rien
    """
    element = create_text_param(g)
    touche = None
    clic = None

    while touche != "Escape":
        touche = g.recupererTouche()
        clic = g.recupererClic()
        for i in element:
            if type(i) == Button:
                i.isHover()
        
        if element[2].onClick(clic):
            pop_up_confirmation(g)
    supprime_elem(g, element)

def create_text_param(g:Canevas) -> list:
    """
        Cette fonction prend en paramètre une fenêtre graphique.
        Elle permet d'afficher tout les textes et boutons du menu
        elle ne renvoie rien
    """
    title = g.afficherTexte("PARAMETRE", fenetre_dimensions[0]//8, 200, taille=35, newWeight="bold", ancre="w")
    supp_scoreboard = g.afficherTexte("Suppression des scores", fenetre_dimensions[0]*1.5//8, 300, taille=20, ancre="w")
    supp_button = Button(g, fenetre_dimensions[0]*6//8, 300, "Supprimer" )

    element = [title, supp_scoreboard, supp_button]
    return element

def pop_up_confirmation(g:Canevas) -> None:
    """
        Cette fonction prend en paramètre une fenêtre graphique
        Elle permet d'afficher une fenêtre pop-up pour confirmer la suppression des données contenuent le fichier scoreboard.txt
        Elle ne renvoie rien
    """
    backWindow = g.dessinerRectangle(50, 50, fenetre_dimensions[0]-100, fenetre_dimensions[1]-100, "gray9")
    yes_button = Button(g, fenetre_dimensions[0]//3, fenetre_dimensions[1]-350, "Oui")
    no_button = Button(g, fenetre_dimensions[0]*2//3, fenetre_dimensions[1]-350, "Non")
    question = g.afficherTexte("Êtes-vous sûr de supprimer le tableau des scores ?", fenetre_dimensions[0]//2, fenetre_dimensions[1]//2-100)
    element = [backWindow, yes_button, no_button, question]
    touche = None
    clic = None
    while True:
        clic = g.recupererClic()
        touche = g.recupererTouche()
        
        for i in element:
            if type(i) == Button:
                i.isHover()
        
        if element[1].onClick(clic):
            ress = open("scoreboard.txt", "w+", encoding="utf-8")
            ress.close()
            supprime_elem(g, element)
            return
        
        elif element[2].onClick(clic):
            supprime_elem(g, element)
            return
