
def createMap(nomMap:str) -> list:
    """
        Cette fonction prend en argument un nom de map sans l'extension
        Elle reformate cette map pour notre programme
        Elle renvoie ce nouveau formatage.
    """
    mapText = open(f"{nomMap}.txt", "r")

    map = []

    for i in mapText.read().split("\n")[3:]:
        row = []
        for j in i:
            row += [[j]]
        map += [row]
    
    return map

createMap("map0")