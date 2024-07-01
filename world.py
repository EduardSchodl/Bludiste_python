from gui import Gui
from vector2 import Vector2


class World:
    """
    Třída World reprezentuje samotné bludiště.

    @author Eduard Schödl
    @date 231124
    """
    def __init__(self, data: list[list[int]], symbols: list[str]):
        """
        Konstruktor třídy "World" vytvoří nový objekt bludiště.

        :param data: List reprezentující rozložení bludiště
        :type data: list[list[int]]
        :param symbols: List symbolů k vykreslení bludiště
        :type symbols: list[str]
        """
        self.__data = data
        self.__symbols = symbols

    @property
    def width(self) -> int:
        """
        Funkce vrátí šířku bludiště.

        :return: Celková šířka bludiště
        :rtype: int
        """
        return len(self.__data[0])

    @property
    def height(self) -> int:
        """
        Funkce vrátí výšku bludiště.

        :return: Celková výška bludiště
        :rtype: int
        """
        return len(self.__data)

    def is_empty(self, position: Vector2) -> bool:
        """
        Funkce zkontroluje, jestli je předané pole volné, nebo obsahuje překážku.

        :param position: Kontrolované pole
        :type position: Vector2

        :return: True, pokud je předané pole volné, v opačném případě False
        :rtype: bool
        """
        if self.__data[position.y][position.x] == 0:
            return True
        else:
            return False

    def draw(self, gui: Gui):
        """
        Funkce vykreslí objekt na plátno.

        :param gui: Plátno
        :type gui: Gui
        """
        for y in range(self.height):
            for x in range(self.width):
                n = self.__data[y][x]
                gui.draw(x, y, self.__symbols[n])
