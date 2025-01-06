import tkinter as tk
from dataclasses import dataclass
from os import PathLike
from time import sleep
from tkinter.font import Font
from typing import Literal, NamedTuple, TypeAlias

from PIL import Image, ImageTk #type: ignore

# fmt: off
_LiteralColor: TypeAlias = Literal[
    "alice blue", "AliceBlue",
    "antique white", "AntiqueWhite", "AntiqueWhite1", "AntiqueWhite2", "AntiqueWhite3", "AntiqueWhite4",
    "agua", "aquamarine", "aquamarine1", "aquamarine2", "aquamarine3", "aquamarine4",
    "azure", "azure1", "azure2", "azure3", "azure4",
    "beige",
    "bisque", "bisque1", "bisque2", "bisque3", "bisque4",
    "black",
    "blanched almond", "BlanchedAlmond",
    "blue", "blue violet", "blue1", "blue2", "blue3", "blue4", "BlueViolet",
    "brown", "brown1", "brown2", "brown3", "brown4",
    "burlywood", "burlywood1", "burlywood2", "burlywood3", "burlywood4",
    "cadet blue", "CadetBlue", "CadetBlue1", "CadetBlue2", "CadetBlue3", "CadetBlue4",
    "chartreuse", "chartreuse1", "chartreuse2", "chartreuse3", "chartreuse4",
    "chocolate", "chocolate1", "chocolate2", "chocolate3", "chocolate4",
    "coral", "coral1", "coral2", "coral3", "coral4",
    "cornflower blue", "CornflowerBlue",
    "cornsilk", "cornsilk1", "cornsilk2", "cornsilk3", "cornsilk4",
    "crymson",
    "cyan", "cyan1", "cyan2", "cyan3", "cyan4",
    "dark blue", "dark cyan", "dark goldenrod", "dark gray", "dark green", "dark grey",
    "dark khaki", "dark magenta", "dark olive green", "dark orange", "dark orchid",
    "dark red", "dark salmon", "dark sea green", "dark slate blue", "dark slate gray",
    "dark slate grey", "dark turquoise", "dark violet",
    "DarkBlue", "DarkCyan",
    "DarkGoldenrod", "DarkGoldenrod1", "DarkGoldenrod2", "DarkGoldenrod3", "DarkGoldenrod4",
    "DarkGray", "DarkGreen", "DarkGrey", "DarkKhaki", "DarkMagenta",
    "DarkOliveGreen", "DarkOliveGreen1", "DarkOliveGreen2", "DarkOliveGreen3", "DarkOliveGreen4",
    "DarkOrange", "DarkOrange1", "DarkOrange2", "DarkOrange3", "DarkOrange4",
    "DarkOrchid", "DarkOrchid1", "DarkOrchid2", "DarkOrchid3", "DarkOrchid4",
    "DarkRed", "DarkSalmon",
    "DarkSeaGreen", "DarkSeaGreen1", "DarkSeaGreen2", "DarkSeaGreen3", "DarkSeaGreen4",
    "DarkSlateBlue",
    "DarkSlateGray", "DarkSlateGray1", "DarkSlateGray2", "DarkSlateGray3", "DarkSlateGray4", "DarkSlateGrey",
    "DarkTurquoise", "DarkViolet",
    "deep pink", "deep sky blue",
    "DeepPink", "DeepPink1", "DeepPink2", "DeepPink3", "DeepPink4",
    "DeepSkyBlue", "DeepSkyBlue1", "DeepSkyBlue2", "DeepSkyBlue3", "DeepSkyBlue4",
    "dim gray", "dim grey", "DimGray", "DimGrey",
    "dodger blue", "DodgerBlue", "DodgerBlue1", "DodgerBlue2", "DodgerBlue3", "DodgerBlue4",
    "firebrick", "firebrick1", "firebrick2", "firebrick3", "firebrick4",
    "floral white", "FloralWhite",
    "forest green", "ForestGreen",
    "fuchsia",
    "gainsboro",
    "ghost white", "GhostWhite",
    "gold", "gold1", "gold2", "gold3", "gold4",
    "goldenrod", "goldenrod1", "goldenrod2", "goldenrod3", "goldenrod4",
    "gray", "gray0", "gray1", "gray2", "gray3", "gray4", "gray5", "gray6", "gray7",
    "gray8", "gray9", "gray10", "gray11", "gray12", "gray13", "gray14", "gray15",
    "gray16", "gray17", "gray18", "gray19", "gray20", "gray21", "gray22", "gray23",
    "gray24", "gray25", "gray26", "gray27", "gray28", "gray29", "gray30", "gray31",
    "gray32", "gray33", "gray34", "gray35", "gray36", "gray37", "gray38", "gray39",
    "gray40", "gray41", "gray42", "gray43", "gray44", "gray45", "gray46", "gray47",
    "gray48", "gray49", "gray50", "gray51", "gray52", "gray53", "gray54", "gray55",
    "gray56", "gray57", "gray58", "gray59", "gray60", "gray61", "gray62", "gray63",
    "gray64", "gray65", "gray66", "gray67", "gray68", "gray69", "gray70", "gray71",
    "gray72", "gray73", "gray74", "gray75", "gray76", "gray77", "gray78", "gray79",
    "gray80", "gray81", "gray82", "gray83", "gray84", "gray85", "gray86", "gray87",
    "gray88", "gray89", "gray90", "gray91", "gray92", "gray93", "gray94", "gray95",
    "gray96", "gray97", "gray98", "gray99", "gray100",
    "green", "green yellow", "green1", "green2", "green3", "green4", "GreenYellow",
    "grey", "grey0", "grey1", "grey2", "grey3", "grey4", "grey5", "grey6", "grey7",
    "grey8", "grey9", "grey10", "grey11", "grey12", "grey13", "grey14", "grey15",
    "grey16", "grey17", "grey18", "grey19", "grey20", "grey21", "grey22", "grey23",
    "grey24", "grey25", "grey26", "grey27", "grey28", "grey29", "grey30", "grey31",
    "grey32", "grey33", "grey34", "grey35", "grey36", "grey37", "grey38", "grey39",
    "grey40", "grey41", "grey42", "grey43", "grey44", "grey45", "grey46", "grey47",
    "grey48", "grey49", "grey50", "grey51", "grey52", "grey53", "grey54", "grey55",
    "grey56", "grey57", "grey58", "grey59", "grey60", "grey61", "grey62", "grey63",
    "grey64", "grey65", "grey66", "grey67", "grey68", "grey69", "grey70", "grey71",
    "grey72", "grey73", "grey74", "grey75", "grey76", "grey77", "grey78", "grey79",
    "grey80", "grey81", "grey82", "grey83", "grey84", "grey85", "grey86", "grey87",
    "grey88", "grey89", "grey90", "grey91", "grey92", "grey93", "grey94", "grey95",
    "grey96", "grey97", "grey98", "grey99", "grey100",
    "honeydew", "honeydew1", "honeydew2", "honeydew3", "honeydew4",
    "hot pink", "HotPink", "HotPink1", "HotPink2", "HotPink3", "HotPink4",
    "indian red", "IndianRed", "IndianRed1", "IndianRed2", "IndianRed3", "IndianRed4",
    "indigo",
    "ivory", "ivory1", "ivory2", "ivory3", "ivory4",
    "khaki", "khaki1", "khaki2", "khaki3", "khaki4",
    "lavender", "lavender blush", "LavenderBlush", "LavenderBlush1", "LavenderBlush2", "LavenderBlush3", "LavenderBlush4",
    "lawn green", "LawnGreen",
    "lemon chiffon", "LemonChiffon", "LemonChiffon1", "LemonChiffon2", "LemonChiffon3", "LemonChiffon4",
    "light blue", "light coral", "light cyan", "light goldenrod", "light goldenrod yellow",
    "light gray", "light green", "light grey", "light pink", "light salmon", "light sea green",
    "light sky blue", "light slate blue", "light slate gray", "light slate grey", "light steel blue", "light yellow",
    "LightBlue", "LightBlue1", "LightBlue2", "LightBlue3", "LightBlue4",
    "LightCoral",
    "LightCyan", "LightCyan1", "LightCyan2", "LightCyan3", "LightCyan4",
    "LightGoldenrod", "LightGoldenrod1", "LightGoldenrod2", "LightGoldenrod3", "LightGoldenrod4", "LightGoldenrodYellow",
    "LightGray", "LightGreen", "LightGrey",
    "LightPink", "LightPink1", "LightPink2", "LightPink3", "LightPink4",
    "LightSalmon", "LightSalmon1", "LightSalmon2", "LightSalmon3", "LightSalmon4",
    "LightSeaGreen",
    "LightSkyBlue", "LightSkyBlue1", "LightSkyBlue2", "LightSkyBlue3", "LightSkyBlue4",
    "LightSlateBlue", "LightSlateGray", "LightSlateGrey",
    "LightSteelBlue", "LightSteelBlue1", "LightSteelBlue2", "LightSteelBlue3", "LightSteelBlue4",
    "LightYellow", "LightYellow1", "LightYellow2", "LightYellow3", "LightYellow4",
    "lime", "lime green", "LimeGreen", "linen",
    "magenta", "magenta1", "magenta2", "magenta3", "magenta4",
    "maroon", "maroon1", "maroon2", "maroon3", "maroon4",
    "medium aquamarine", "medium blue", "medium orchid", "medium purple", "medium sea green",
    "medium slate blue", "medium spring green", "medium turquoise", "medium violet red",
    "MediumAquamarine", "MediumBlue",
    "MediumOrchid", "MediumOrchid1", "MediumOrchid2", "MediumOrchid3", "MediumOrchid4",
    "MediumPurple", "MediumPurple1", "MediumPurple2", "MediumPurple3", "MediumPurple4",
    "MediumSeaGreen", "MediumSlateBlue", "MediumSpringGreen", "MediumTurquoise", "MediumVioletRed",
    "midnight blue", "MidnightBlue",
    "mint cream", "MintCream",
    "misty rose", "MistyRose", "MistyRose1", "MistyRose2", "MistyRose3", "MistyRose4",
    "moccasin",
    "navajo white", "NavajoWhite", "NavajoWhite1", "NavajoWhite2", "NavajoWhite3", "NavajoWhite4",
    "navy", "navy blue", "NavyBlue",
    "old lace", "OldLace",
    "olive", "olive drab", "OliveDrab", "OliveDrab1", "OliveDrab2", "OliveDrab3", "OliveDrab4",
    "orange", "orange red", "orange1", "orange2", "orange3", "orange4",
    "OrangeRed", "OrangeRed1", "OrangeRed2", "OrangeRed3", "OrangeRed4",
    "orchid", "orchid1", "orchid2", "orchid3", "orchid4",
    "pale goldenrod", "pale green", "pale turquoise", "pale violet red", "PaleGoldenrod",
    "PaleGreen", "PaleGreen1", "PaleGreen2", "PaleGreen3", "PaleGreen4",
    "PaleTurquoise", "PaleTurquoise1", "PaleTurquoise2", "PaleTurquoise3", "PaleTurquoise4",
    "PaleVioletRed", "PaleVioletRed1", "PaleVioletRed2", "PaleVioletRed3", "PaleVioletRed4",
    "papaya whip", "PapayaWhip",
    "peach puff", "PeachPuff", "PeachPuff1", "PeachPuff2", "PeachPuff3", "PeachPuff4",
    "peru",
    "pink", "pink1", "pink2", "pink3", "pink4",
    "plum", "plum1", "plum2", "plum3", "plum4",
    "powder blue", "PowderBlue",
    "purple", "purple1", "purple2", "purple3", "purple4",
    "red", "red1", "red2", "red3", "red4",
    "rosy brown", "RosyBrown", "RosyBrown1", "RosyBrown2", "RosyBrown3", "RosyBrown4",
    "royal blue",
    "RoyalBlue", "RoyalBlue1", "RoyalBlue2", "RoyalBlue3", "RoyalBlue4",
    "saddle brown", "SaddleBrown",
    "salmon", "salmon1", "salmon2", "salmon3", "salmon4",
    "sandy brown", "SandyBrown",
    "sea green", "SeaGreen", "SeaGreen1", "SeaGreen2", "SeaGreen3", "SeaGreen4",
    "seashell", "seashell1", "seashell2", "seashell3", "seashell4",
    "sienna", "sienna1", "sienna2", "sienna3", "sienna4",
    "silver",
    "sky blue", "SkyBlue", "SkyBlue1", "SkyBlue2", "SkyBlue3", "SkyBlue4",
    "slate blue", "slate gray", "slate grey",
    "SlateBlue", "SlateBlue1", "SlateBlue2", "SlateBlue3", "SlateBlue4",
    "SlateGray", "SlateGray1", "SlateGray2", "SlateGray3", "SlateGray4", "SlateGrey",
    "snow", "snow1", "snow2", "snow3", "snow4",
    "spring green", "SpringGreen", "SpringGreen1", "SpringGreen2", "SpringGreen3", "SpringGreen4",
    "steel blue", "SteelBlue", "SteelBlue1", "SteelBlue2", "SteelBlue3", "SteelBlue4",
    "tan", "tan1", "tan2", "tan3", "tan4",
    "teal",
    "thistle", "thistle1", "thistle2", "thistle3", "thistle4",
    "tomato", "tomato1", "tomato2", "tomato3", "tomato4",
    "turquoise", "turquoise1", "turquoise2", "turquoise3", "turquoise4",
    "violet", "violet red", "VioletRed", "VioletRed1", "VioletRed2", "VioletRed3", "VioletRed4",
    "wheat", "wheat1", "wheat2", "wheat3", "wheat4",
    "white", "white smoke", "WhiteSmoke",
    "yellow", "yellow1", "yellow2", "yellow3", "yellow4",
    "yellow green", "YellowGreen",
]
# fmt: on
_Color: TypeAlias = _LiteralColor | str

################################################################################
# Classe ObjetGraphique
################################################################################


@dataclass
class ObjetGraphique:
    id: int
    x: float
    y: float
    couleur: str


class Position(NamedTuple):
    x: float
    y: float


################################################################################
# Classe Canevas
################################################################################


class Canevas(tk.Canvas):
    def __init__(self, parent: tk.Misc, largeur: float, hauteur: float) -> None:
        super().__init__(
            parent, width=largeur, height=hauteur, bg="black", confine=True
        )
        # Attributs
        self.images: dict[
            str | PathLike[str], ImageTk.PhotoImage
        ] = {}  # Pour garder une réréfence sur les objets
        self.lastkey: str | None = None  # Dernière touche tapée
        self.lastclic: tk.Event[Canevas] | None = None  # Dernier clic effectué
        self.lastpos: Position = Position(0, 0)  # Dernière position souris

        # Bindings
        self.bind_all("<Key>", self._evenementClavier)
        self.bind("<Button-1>", self._evenementClicG)
        self.bind("<Button-3>", self._evenementClicD)
        self.bind("<Motion>", self._evenementDeplaceSouris)
        self.pack()

    ################################################################################
    # CREATION D'OBJETS
    ################################################################################

    def afficherTexte(
        self,
        texte: str,
        x: float,
        y: float,
        couleur: _Color = "white",
        taille: int = 18,
        newWeight : str ="normal",
        newFont : str = "Consolas",
        ancre: Literal["n", "s", "w", "e", "nw", "sw", "ne", "se", "center"] = "center",
    ) -> ObjetGraphique:
        """Affiche un texte sur le canevas

        Args:
            texte (str): Le texte à afficher
            x (float): La position x (abscisse) en pixels du texte sur le canevas
            y (float): La position y (ordonnée) en pixels du texte sur le canevas
            couleur (str, optional): La couleur du texte. Par défaut à "white".
            taille (int, optional): La taille de la police d'écriture. Par défaut à 18.

        Returns:
            ObjetGraphique: Retourne un objet graphique représentant ce texte sur le canevas
        """
        font = Font(family=newFont, size=taille, weight=newWeight)
        return ObjetGraphique(
            self.create_text(x, y, fill=couleur, text=texte, font=font, anchor=ancre), x, y, couleur
        )

    def dessinerRectangle(
        self, x: float, y: float, largeur: float, hauteur: float, couleur: _Color
    ) -> ObjetGraphique:
        """Dessine un rectangle aux coordonnées souhaitées sur le canevas

        Args:
            x (float): La position x (abscisse) en pixels du coin haut-gauche du rectangle sur le canevas
            y (float): La position y (ordonnée) en pixels du coin haut-gauche du rectangle sur le canevas
            largeur (float): La largeur en pixels du rectangle
            hauteur (float): La hauteur en pixels du rectangle
            couleur (str): La couleur de remplissage du rectangle

        Returns:
            ObjetGraphique: Retourne un objet graphique représentant ce rectangle sur le canevas
        """
        return ObjetGraphique(
            self.create_rectangle(
                x, y, x + largeur, y + hauteur, fill=couleur, width=0
            ),
            x,
            y,
            couleur,
        )

    def dessinerLigne(
        self, x: float, y: float, x2: float, y2: float, couleur: _Color
    ) -> ObjetGraphique:
        """Dessine une ligne entre les coordonnées (x,y) et (x2,y2) sur le canevas

        Args:
            x (float): La position x (abscisse) en pixels du point de départ de la ligne
            y (float): La position y (ordonnée) en pixels du point de départ de la ligne
            x2 (float): La position x (abscisse) en pixels du point d'arrivé de la ligne
            y2 (float): La position y (ordonnée) en pixels du point d'arrivé de la ligne
            couleur (str): La couleur de la ligne

        Returns:
            ObjetGraphique: Retourne un objet graphique représentant cette ligne sur le canevas
        """
        return ObjetGraphique(
            self.create_line(x, y, x2, y2, fill=couleur), x, y, couleur
        )

    def dessinerCercle(
        self, x: float, y: float, r: float, couleur: _Color
    ) -> ObjetGraphique:
        """Dessine un cercle de milieu positionné en (x,y) et de rayon r en pixels sur le canevas.

        Args:
            x (float): La position x (abscisse) en pixels du milieu du cercle
            y (float): La position y (ordonnée) en pixels du milieu du cercle
            r (float): Le rayon du cercle en pixels
            couleur (_Color): La couleur de remplissage du cercle

        Returns:
            ObjetGraphique: Retourne un objet graphique représentant ce cercle sur le canevas
        """
        return ObjetGraphique(
            self.create_oval(x - r, y - r, x + r, y + r, width=1, outline=couleur),
            x,
            y,
            couleur,
        )

    def dessinerDisque(
        self, x: float, y: float, r: float, couleur: _Color
    ) -> ObjetGraphique:
        """Dessine un disque de milieu positionné en (x,y) et de rayon r en pixels sur le canevas.

        Args:
            x (float): La position x (abscisse) en pixels du milieu du disque
            y (float): La position y (ordonnée) en pixels du milieu du disque
            r (float): Le rayon du disque en pixels
            couleur (_Color): La couleur du contour du disque

        Returns:
            ObjetGraphique: Retourne un objet graphique représentant ce disque sur le canevas
        """
        return ObjetGraphique(
            self.create_oval(x - r, y - r, x + r, y + r, width=0, fill=couleur),
            x,
            y,
            couleur,
        )

    def changerPixel(self, x: float, y: float, couleur: _Color) -> ObjetGraphique:
        """Dessine un pixel aux coordonnées (x,y)

        Args:
            x (float): La position x (abscisse) du pixel
            y (float): La position y (ordonnée) du pixel
            couleur (_Color): La couleur du pixel

        Returns:
            ObjetGraphique: Retourne un objet graphique représentant ce pixel sur le canevas
        """
        return self.dessinerRectangle(x, y, 1, 1, couleur)

    def afficherImage(
        self,
        x: float,
        y: float,
        size:tuple[int, int],
        fichier: str | PathLike[str],
        ancre: Literal["n", "s", "w", "e", "nw", "sw", "ne", "se", "center"] = "nw",
    ) -> ObjetGraphique:
        """Affiche une image spécifiée par son chemin au coordonnées données.

        Args:
            x (float): La position x (abscisse) du coin haut-gauche de l'image
            y (float): La position y (ordonnée) du coin haut-gauche de l'image
            fichier (str | PathLike[str]): Le chemin du fichier de l'image
            ancre (Literal[&quot;n&quot;, &quot;s&quot;, &quot;w&quot;, &quot;e&quot;, &quot;nw&quot;, &quot;sw&quot;, &quot;ne&quot;, &quot;se&quot;, &quot;center&quot;], optional): _description_. Le point d'ancrage des coordonnées.

        Returns:
            ObjetGraphique: Retourne un objet graphique représentant cette image sur le canevas
        """
        if fichier in self.images:
            photo_image = self.images[fichier]
        else:
            img = Image.open(fichier)
            img = img.resize(size)
            photo_image = ImageTk.PhotoImage(img)
            self.images[fichier] = photo_image

        return ObjetGraphique(
            self.create_image(x, y, image=photo_image, anchor=ancre),  # type: ignore
            x,
            y,
            "",
        )

    ################################################################################
    # MODIFICATEURS
    ################################################################################
    def deplacer(self, obj: ObjetGraphique, x: float, y: float) -> None:
        """Déplace un objet graphique de `x` pixels horizontalement et `y` pixels verticalement sur le canevas.

        Args:
            obj (ObjetGraphique): L'objet graphique à déplacer
            x (float): Le nombre de pixels de déplacement horizontal, peut être négatif
            y (float): Le nombre de pixels de déplacement vertical, peut être négatif
        """
        obj.x += x
        obj.y += y
        self.move(obj.id, x, y)  # type: ignore

    def supprimer(self, obj: ObjetGraphique) -> None:
        """Supprime un objet graphique du canevas

        Args:
            obj (ObjetGraphique): L'objet graphique à supprimer
        """
        self.delete(obj.id)

    def changerCouleur(self, obj: ObjetGraphique, couleur: _Color) -> None:
        """Change la couleur d'un objet graphique.

        Args:
            obj (ObjetGraphique): L'objet graphique à modifier
            couleur (_Color): La nouvelle couleur à appliquer
        """
        obj.couleur = couleur
        self.itemconfigure(obj.id, fill=couleur)

    def changerTexte(self, obj: ObjetGraphique, texte: str) -> None:
        """Change le texte d'un objet graphique (ne fonctionne que sur les objets de type texte).

        Args:
            obj (ObjetGraphique): L'objet graphique représentant un texte
            texte (str): Le nouveau texte à afficher
        """
        self.itemconfigure(obj.id, text=texte)

    ################################################################################
    # EVENEMENTS
    ################################################################################
    def _evenementClicG(self, event: "tk.Event[Canevas]") -> None:
        self.lastclic = event

    def _evenementClicD(self, event: "tk.Event[Canevas]") -> None:
        self.lastclic = event

    def _evenementClavier(self, event: "tk.Event[tk.Misc]") -> None:
        self.lastkey = event.keysym

    def _evenementDeplaceSouris(self, event: "tk.Event[Canevas]") -> None:
        self.lastpos = Position(event.x, event.y)

    def recupererTouche(self) -> str | None:
        """Permet de récupérer la dernière touche préssée depuis le dernier appel à recupererTouche() ou attendreTouche().
        Cet appel ne bloque pas l'exécution du code, si aucune touche n'a été préssée la fonction sort immédiatement.

        Returns:
            str | None: Le nom de la touche préssée ou `None`.
        """
        self.update()
        touche = self.lastkey
        self.lastkey = None
        return touche

    def attendreTouche(self) -> str:
        """Bloque l'exécution du code jusqu'à ce qu'une touche du clavier soit préssée

        Returns:
            str: Le nom de la touche préssée par l'utilisateur
        """
        touche = None
        while touche is None:
            self.pause(0.1)
            touche = self.recupererTouche()
        return touche

    def recupererClic(self) -> "tk.Event[Canevas] | None":
        """Permet de récupérer le dernier clic effectué depuis le dernier appel à recupererClic() ou attendreClic().
        Cet appel ne bloque pas l'exécution du code, si aucun clic n'a été effectué la fonction sort immédiatement.

        Returns:
            tk.Event[Canevas] | None: L'evènement du clic, contenant notamment les coordonnées du clic (x et y). None si aucun clic n'a eu lieu

        Examples:
            >>> clic = canevas.recupererClic()
            >>> if clic:
            >>>     print(f"x = {clic.x} | y = {clic.y}")
            >>> else:
            >>>     print("Aucun clic")
        """
        self.update()
        clic = self.lastclic
        self.lastclic = None
        return clic

    def attendreClic(self) -> "tk.Event[Canevas]":
        """Bloque l'exécution du code jusqu'à ce qu'un clic (gauche ou droite) est fait sur la fenêtre

        Returns:
            tk.Event[Canevas]: L'evènement du clic, contenant notamment les coordonnées du clic (x et y)

        Examples:
            >>> clic = canevas.attendreClic()
            >>> print(f"x = {clic.x} | y = {clic.y}")
        """
        clic = None
        while clic is None:
            self.pause(0.1)
            clic = self.recupererClic()
        return clic

    def recupererPosition(self) -> Position:
        """Permet de récupérer la dernière position (x,y) connue de la souris

        Returns:
            Position: Un tuple nommé contenant la position x et y.

        Examples:
            >>> pos = canevas.recupererPosition()
            >>> print(f"x = {pos.x} | y = {pos.y}")
        """
        self.update()
        return self.lastpos

    ################################################################################
    # AUTRES FONCTIONS
    ################################################################################
    def actualiser(self) -> None:
        """Permet à tkeasy/tkinter de prendre en compte tous les évènements empilés"""
        self.update()

    def fermerFenetre(self) -> None:
        """Ferme la fenêtre précédement ouverte via ouvrirFenetre()"""
        self.master.destroy()

    def pause(self, sleeptime: float = 0.0005) -> None:
        """Retarde l'exécution pour un nombre donné de secondes. L'argument peut être un nombre à virgule flottante pour une précision inférieure à la seconde.

        Args:
            sleeptime (float, optional): Le nombre de secondes de délai. Valeur par défaut à 0.0005 secondes.
        """
        sleep(sleeptime)


def ouvrirFenetre(largeur: float = 400, hauteur: float = 200) -> Canevas:
    """Ouvre une nouvelle fenêtre graphique d'une taille souhaitée avec un canevas pour dessiner.

    Args:
        largeur (float, optional): La largeur de la fenêtre (et du canevas) en pixels. Par défaut à 400.
        hauteur (float, optional): La hauteur de la fenêtre (et du canevas) en pixels. Par défaut à 200.

    Returns:
        Canevas: Retourne une référence au canevas permetant de dessiner dessus.
    """
    return Canevas(tk.Tk(), largeur, hauteur)


if __name__ == "__main__":
    ouvrirFenetre()
    tk.mainloop()