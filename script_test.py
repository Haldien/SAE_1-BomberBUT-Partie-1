from menu import *

"""
===============================================================================================

                            Bombes

===============================================================================================
"""
def test_case_valide_explosion():
    grille1 = [ # petite grille théorique
        [[], [], ["C"]],
        [[], [], []],
        [[], [], []]
    ]
    assert case_valide_pour_explosion(grille1, 0, 0) == True # Dans le cas où on est dans une grille
    assert case_valide_pour_explosion(grille1, 1, 1) == True # idem
    assert case_valide_pour_explosion(grille1, 0, 2) == False # Si la case est une colonne
    assert case_valide_pour_explosion(grille1, -1, 0) == False # Si on est en dehors de la grille via les colonnes
    assert case_valide_pour_explosion(grille1, 2, 7) == False # si on est en dehors de la grille via les lignes
#test_case_valide_explosion()

"""
===============================================================================================

                            Fonction utiles

===============================================================================================
"""
def test_case_valide():
    grille2 = [ # petite grille théorique
            [[], ["E"], ["F"]],
            [[], ["M"], ["C"]],
            [[], ["P"], []]
        ]
    assert case_valide(grille2, 0, 0) == True # Si une case est bien vide
    assert case_valide(grille2, 4, 0) == False # Si on est en dehors de la grille
    assert case_valide(grille2, 0, 1) == False # Si on est sur un élément existant
    assert case_valide(grille2, 0, 2) == False # Si on est sur un élément existant
    assert case_valide(grille2, 1, 1) == False # Si on est sur un élément existant
    assert case_valide(grille2, 1, 2) == False # Si on est sur un élément existant
    assert case_valide(grille2, 2, 1) == False # Si on est sur un élément existant

def test_case_valide_voisine():
    grille3 = [ # petite grille théorique
            [["A"], [], []],
            [[], ["X"], []],
            [["C"], ["C"], []]
        ]

    assert get_cases_voisines_valides(grille3, (1,1)) == [(0,1), (1,2), (2,1), (1,0)] # lorsqu'on cible X
    assert get_cases_voisines_valides(grille3, (0,0)) == [(0,1), (1,0)] # Lorsque A est bloqué par des bordures
    assert get_cases_voisines_valides(grille3, (2,1)) == [(1,1), (2,2)] # Lorsque C est bloqué par un élément existant

"""
    Pour la génération aléatoire comment est-il possible de tester convenablement ?
    Cela inclut gererer_element(), generer_grille_et_dic_jeu()
"""
def test_create_map():
    grille_temoin = [
        [["C"],["C"],["C"],["C"],["C"],["C"],["C"],["C"],["C"]],
        [["C"],[   ],["P"],[   ],[   ],[   ],[   ],[   ],["C"]],
        [["C"],["M"],["C"],["M"],["C"],["M"],["C"],["M"],["C"]],
        [["C"],["U"],["M"],["M"],["M"],[   ],["E"],[   ],["C"]],
        [["C"],["C"],["C"],["C"],["C"],["C"],["C"],["C"],["C"]]
    ]

    assert create_map("map1") == grille_temoin

def test_get_param():
    assert get_param("map0") == (250, 20)
    assert get_param("map1") == (150, 30)
    assert get_param("map2") == (200, 25)

"""
===============================================================================================

                            Fonction utiles

===============================================================================================
"""

def creation_entite():
    grille4 = [ # petite grille théorique
            [[], [], []],
            [[], [], []],
            [[], [], []]
        ]
    grille4_temoin = [ # petite grille théorique
            [["P"], [], []],
            [[], [], []],
            [[], [], []]
        ]

    # Objet entite
    g = ouvrirFenetre(200,200)
    test1 = Entite(g, grille4, {}, (0,0), "P")
    assert grille4 == grille4_temoin


# Ethernet
def test_spawn_fantome():
    grille5 = [ # petite grille théorique
                [[], [], []],
                [[], [], []],
                [[], [], []]
            ]
    grille5_temoinA = [ # petite grille théorique
                [["E"], [], []],
                [["F"], [], []],
                [[], [], []]
            ]
    grille5_temoinB= [ # petite grille théorique
                [["E"], ["F"], []],
                [[], [], []],
                [[], [], []]
            ]
    g = ouvrirFenetre(200,200)
    test2 = Ethernet(g, grille5,{"fantomes":[],"case_dimensions":(96,96)}, (0,0), "E")
    test2.spawner()
    assert grille5 == grille5_temoinA or grille5 == grille5_temoinB 

def test_deplacement():
    grille6 = [ # petite grille théorique
                    [[], [], []],
                    [[], [], []],
                    [[], [], []]
                ]
    grille6_temoin = [ # petite grille théorique
                    [[], [], []],
                    [[], [], []],
                    [[], ["X"],[]] 
                    ]

    grille7= [ 
                    [[], [], []],
                    [[], [], []],
                    [[], [], []]
                ]
    grille7_temoin = [ 
                    [[], [], []],
                    [[], [], ["F"]],
                    [[], [],[]] 
                    ]
    g = ouvrirFenetre(400,400)
    perso = Bomber(g, grille6, {"case_dimensions":(96,96)},(1,1),"X" ) 
    perso.se_deplacer((2,1), "X", {})
    fantome = Fantome(g, grille7, {"case_dimensions":(96,96)}, (1,1), "F")
    fantome.se_deplacer((1,2), "F")

    assert grille6 == grille6_temoin
    assert grille7 == grille7_temoin

def test_poser_bombe():
    grille8 = [
                        [[], [], []],
                        [[], [], []],
                        [[], [], []]
                    ]
    grille8_temoin = [
                        [[], [], []],
                        [[], ["P", "B"], []],
                        [[], [], []]
                    ]
    g = ouvrirFenetre(400,400)
    bomber = Bomber(g, grille8, {"bombes": [],"case_dimensions":(96,96)},(1,1),"P" ) 
    bomber.poser_bombe((1,1))
    assert grille8 == grille8_temoin

def test_attaque():
    grille9 = [
                            [[], [], []],
                            [[], [], []],
                            [[], [], []]
                        ]
    g = ouvrirFenetre(400,400)
    bomber = Bomber(g, grille9, {"bombes": [],"case_dimensions":(96,96)},(1,1),"P" ) 
    fantome = Fantome(g, grille9, {"case_dimensions":(96,96)},(1,2),"F" )
    print(grille9)
    assert bomber.pv == 3  # Par défaut
    bomber.se_faire_attaquer()
    assert bomber.pv == 2 # Trop proche d'un fantôme
    bomber.se_deplacer((0,0), "P", {})
    bomber.se_faire_attaquer()
    assert bomber.pv == 2  # Trop loin cette fois

def test_level_up():
    grille10 = [
                                [[], [], []],
                                [[], [], []],
                                [[], [], []]
                            ]

    g = ouvrirFenetre(400,400)
    dic_jeu_temp = {"bombes": [],"upgrades": [],"case_dimensions":(96,96)}
    dic_jeu_temp["upgrades"] += [Upgrade(g, grille10, dic_jeu_temp, (1,1), "U")]
    bomber = Bomber(g, grille10, dic_jeu_temp,(1,0),"P" ) 

    assert bomber.niv == 0
    bomber.se_deplacer((1,1), "P",{})
    assert bomber.niv == 1
