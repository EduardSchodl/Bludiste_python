from __future__ import annotations


class Vector2:
    """
    Třída Vector2 reprezentuje souřadnice ve dvourozměrném světě.

    @author Eduard Schödl
    @date 231124
    """
    def __init__(self, x: int, y: int):
        """
        Konstruktor třídy "Vektor2" vytvoří objekt dvourozměrného vektoru o souřadnicích x, y.

        :param x: Souřadnice x vektoru
        :type x: int
        :param y: Souřadnice y vektoru
        :type y: int
        """
        self.__x = x
        self.__y = y

    def __str__(self) -> str:
        """
        Metoda vrací formátovaný výpis vektoru.
        Formát: x; y

        :return: Formátovaný řetězec
        :rtype: str
        """
        return f"{self.__x}; {self.__y}"

    @property
    def x(self) -> int:
        """
        Funkce vrací souřadnici x vektoru.

        :return: Souřadnice x vektoru
        :rtype: int
        """
        return self.__x

    @property
    def y(self) -> int:
        """
        Funkce vrací souřadnici y vektoru.

        :return: Souřadnice y vektoru
        :rtype: int
        """
        return self.__y

    def __add__(self, other: Vector2) -> Vector2:
        """
        Funkce sečte vektor, na kterém se funkce volá, s předaným vektorem a vrátí výsledek.

        :param other: Druhý sčítaný vektor
        :type other: Vector2

        :return: Výsledný sečtený vektor
        :rtype: Vector2
        """
        return Vector2(self.__x + other.x, self.__y + other.y)

    def __eq__(self, other) -> bool:
        """
        Funkce porovná vektor, na kterém se funkce volá, s předaným vektorem.

        :param other: Druhý porovnávaný vektor

        :return: True, pokud se vektory rovnají, False v opačném případě
        :rtype: bool
        """
        return self.__x == other.x and self.__y == other.y

