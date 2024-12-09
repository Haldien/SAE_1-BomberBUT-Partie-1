import tkiteasy

#  PV : pv du bomber, NIV : niveau du bomber

g = tkiteasy.ouvrirFenetre(400, 400)  # taille à changer

# grille est une liste, pas besoin de global
# grille : list[list[list[str]]]
grille = [
    [["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"]],
    [["C"], [   ], [   ], ["P"], [   ], [   ], [   ], [   ], ["C"]],
    [["C"], ["M"], ["C"], ["M"], ["C"], ["M"], ["C"], ["M"], ["C"]],
    [["C"], ["M"], ["M"], ["M"], ["M"], [   ], ["E"], [   ], ["C"]],
    [["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"], ["C"]]
]

dic_bombes = {}



# Fonctions annexes

def pos_bomber(grille:list[list[list[str]]])->list[int]:
    for y in range(len(grille)):
        for x in range(len(grille[0])):
            if "P" in grille[y][x]:
                return [y, x]

    # Mouvements
def case_valide(y: int, x: int) -> bool:
    if not (0 <= y <= len(grille) - 1 and 0 <= x <= len(grille[0]) - 1):
        return False
    if grille[y][x] in [["M"], ["C"], ["E"], ["F"]]:
        return False
    return True


def deplacer_bomber(y: int, x: int):

    pos = pos_bomber(grille)

    if grille[y][x] == "U":
        pass

    grille[pos_bomber(grille)[0]][pos_bomber(grille)[1]].remove("P")
    grille[y][x].append("P")


    # Pose de bombe
def poser_bombe(y:int, x:int):
    if "B" not in grille[y][x] :
        grille[y][x].append("B")
        ajouter_à_dic_bombes(y ,x)

def ajouter_à_dic_bombes(y, x):
    global dic_bombes

    dic_bombes[(y, x)] = 5


# Fonctions principales

def action_bomber(touche: str):


    # Mappings des touches vers les vecteurs de mouvements correspondant
    mouvements = {
        "z": [-1, 0],
        "q": [0, -1],
        "s": [1, 0],
        "d": [0, 1]
    }

    # Mouvements
    if touche in ["z", "q", "s", "d"] and case_valide(pos_bomber(grille)[0] + mouvements[touche][0], pos_bomber(grille)[1] + mouvements[touche][1]):

        # Jusqu'à ce que le mouvement correspondant soit valide

        deplacer_bomber(pos_bomber(grille)[0] + mouvements[touche][0], pos_bomber(grille)[1] + mouvements[touche][1])


    # Dépose un bombe
    elif touche == "space":
        poser_bombe(pos_bomber(grille)[0], pos_bomber(grille)[1])

    # Passe son tour
    elif touche == "Return":
        pass


def resoudre_action():
    pass


def deplacer_fantomes():
    pass


def attaque_fantomes():
    pass


def faire_apparaitre_fantomes():
    pass


def updater_timers():
    pass


def explosions():
    pass


def main():



    while True:

        # affichage de la grille dans le terminal pour test
        print("-----------------------------")
        for el in grille:
            print(el)
        print("dic_bombes:", dic_bombes)

        touche = g.attendreTouche()

        if touche in ["z", "q", "s", "d", "space", "Return"]:
            """
            1. décision de l'action du bomber
            2. résolution de l'action
            3. déplacement des fantômes
            4. attaque des fantômes
            5. apparition de nouveaux fantômes
            6. réduction des timers et les explosions
            """
            action_bomber(touche)

            resoudre_action()

            deplacer_fantomes()

            attaque_fantomes()

            faire_apparaitre_fantomes()

            updater_timers()

            explosions()

            # render()


main()
