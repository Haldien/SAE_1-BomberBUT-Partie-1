from tkiteasy import ouvrirFenetre
import random

carre = 50 #taille des carrés
espacement = carre #espacement entre chaque carré
en_tete = 150 #taille de l'en-tête

# Ouverture de fenêtre
larg = 1000
long = 700
g = ouvrirFenetre(larg, long)

#definition
def dessiner_bordure():
    g.dessinerRectangle(1, en_tete+1, carre, larg - en_tete, "orange") #bordure de gauche
    g.dessinerRectangle(1, en_tete+1, larg, carre, "orange")  # bordure du haut
    g.dessinerRectangle(larg - carre +1, en_tete + 1, carre, long, "orange") #bordure de droite
    g.dessinerRectangle(1, long-carre+1, larg, carre+1, "orange")  # bordure du bas

def accueil():
    g.dessinerRectangle(0, 0, larg+21, long+21, "black")
    Bomberman = g.afficherTexte("Bomberman", larg//2, 50, "red", 60)
    Accueil = g.afficherTexte("Accueil", larg//2, 150, "white", 40)
    g.dessinerRectangle(larg//4, long//2, larg//2, 100, "white")
    commencer = g.afficherTexte("COMMENCER", larg // 2, long//2 +50, "red", 40)
    Auteurs = g.afficherTexte("Par Théo GUICHOT, Adrien MIQUEL et Tiago BATALHA", larg//2, long - 20, "red", 10)
    g.attendreClic()
    g.supprimer(Bomberman)
    g.supprimer(Accueil)
    g.supprimer(commencer)
    g.supprimer(Auteurs)

def afficher_coin(x,y):

    return [x-x%20+1, y-y%20+1]