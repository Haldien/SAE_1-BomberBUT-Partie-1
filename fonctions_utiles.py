
# Valables pour le bomberman et les fantomes mais pas pour les bombes
def case_valide(grille, y: int, x: int) -> bool:
    if not (0 <= y <= len(grille) - 1 and 0 <= x <= len(grille[0]) - 1):
        return False
    for el in ["M", "C", "E", "F", "P"]:
        if el in grille[y][x]:
            return False
    return True
