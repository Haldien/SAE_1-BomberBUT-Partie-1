from tkiteasy import ouvrirFenetre
import time
import random

carre = 50 #taille des carrés
espacement = carre #espacement entre chaque carré
en_tete = 150 #taille de l'en-tête
colors = ["orange", "yellow", "dark orange", "light grey"] #couleurs pour le carré 'appuyer pour continuer'
i = 0 # variable pour les couleurs

# Ouverture de fenêtre
larg = 1000
long = 700
g = ouvrirFenetre(larg, long)



#definition
def accueil():
    explosion = g.afficherImage(0, 0, (larg, long), "explosion.jpg")
    auteurs2 = g.dessinerRectangle(10, long - 30, 330, 20, "black")

    #texte
    bomberman = g.afficherTexte("Bomberman", larg//2, 50, "red", 60)
    Accueil = g.afficherTexte("Accueil", larg//2, 200, "black", 40)
    auteurs = g.afficherTexte("Par Théo GUICHOT, Adrien MIQUEL et Tiago BATALHA", 175, long-20, "white", 10)
    attente(i)

    #au clic on supprime tout
    g.supprimer(explosion)
    g.supprimer(bomberman)
    g.supprimer(auteurs2)
    g.supprimer(Accueil)
    g.supprimer(auteurs)




def attente(i): #en attente d'un clic on fait apparaitre des carrés de couleurs
    if g.recupererClic() is not None:
        pass

    else:
        k = i % len(colors)
        rectangle = g.dessinerRectangle(larg // 2 - 190, long // 2 + 20, 390, 60, colors[k])
        commencer = g.afficherTexte("Appuyer pour commencer", larg // 2, long // 2 + 50, "red", 20)
        time.sleep(0.5)
        attente(i+1)
        g.supprimer(commencer)
        g.supprimer(rectangle)



def dessiner_bordure():
    g.dessinerRectangle(1, en_tete+1, carre, larg - en_tete, "orange") #bordure de gauche
    g.dessinerRectangle(1, en_tete+1, larg, carre, "orange")  # bordure du haut
    g.dessinerRectangle(larg - carre +1, en_tete + 1, carre, long, "orange") #bordure de droite
    g.dessinerRectangle(1, long-carre+1, larg, carre+1, "orange")  # bordure du bas

def afficher_coin(x,y):

    return [x-x%20+1, y-y%20+1]

def arene():
    for col in range(en_tete, long, espacement):
        for lig in range(0, larg, espacement):
            coin_x, coin_y = lig + 1, col + 1
            for k in range(0, 6):
                murs = random.randint(0, 5)

                if murs == 0:
                    g.dessinerRectangle(coin_x, coin_y, carre, carre, "orange")  # murs indestructible
                elif murs == 3 or murs == 4:
                    g.afficherImage(coin_x, coin_y, (carre, carre+1), "murs_destructible.png")# murs destructibles
                else:
                    g.dessinerRectangle(coin_x, coin_y, carre, carre, "black")

    dessiner_bordure()

def regles():
    #faire un ecran noir avec les expliactions du jeu (conditions de victoire, ennemis, touches...)
    arriere_plan = g.dessinerRectangle(0, 0, larg+21, long+21, "black")

#1ere page

    #texte
    Regle = g.afficherTexte("Règles du jeu", larg // 2, 50, "red", 40)
    continuer = g.afficherTexte("Appuyer pour continuer", larg - 160, long - 25, "white", 13)
    texte = g.afficherTexte("Votre mission, si vous l'acceptez, va être de sauver notre monde en détruisant un maximum de murs", larg //2, long //4 , "white", 16)
    texte_1 = g.afficherTexte("Pour ce faire, vous serez équipé d'un nombre infini de bombes", larg // 2,long // 4 + 100, "white", 16)
    texte_2 = g.afficherTexte("Vous aurez 120s et vous serez poursuivi par des fantômes qui vous enlève 1 vie si il vous touche !", larg // 2, long // 4 + 200, "white", 16)
    texte_3 = g.afficherTexte("3 vies vous seront attribués d'office ", larg // 2, long // 4 + 300, "white", 14)
    texte_4 = g.afficherTexte(" De plus, vous trouverez des objets magiques sur votre chemin qui vous permettrons d'obtenir des améliorations",larg // 2, long // 4 + 400, "white", 14)

    #images
    fleche = g.afficherImage(larg - 70, long - 35, (60, 25), "fleche.png")  # fleche pour continuer


    g.attendreClic()
# 2ème page
    g.supprimer(texte)
    g.supprimer(texte_1)
    g.supprimer(texte_2)
    g.supprimer(texte_3)
    g.supprimer(texte_4)
    g.supprimer(Regle)

    Astuce = g.afficherTexte("Astuces", larg // 2, 50, "red", 40)
    texte = g.afficherTexte("Pour vous déplacer, il faudra utiliser les touches z (haut), q (gauche) , s (bas) et d (droite)", larg // 2,long // 4, "white", 16)

    #on attend un clic puis on supprime tout
    g.attendreClic()

    g.supprimer(continuer)
    g.supprimer(Astuce)
    g.supprimer(fleche)
    g.supprimer(texte)
    g.supprimer(texte_1)
    g.supprimer(texte_2)
    g.supprimer(texte_3)
    g.supprimer(texte_4)



accueil()
regles()
arene()

#on ferme la fenêtre
g.attendreClic()
g.fermerFenetre()
