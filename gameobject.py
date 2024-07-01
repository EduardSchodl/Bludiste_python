from gui import Gui
from vector2 import Vector2


class GameObject:
    """
    Třída GameObject reprezentuje herní prvky.

    @author Eduard Schödl
    @date 231124
    """
    def __init__(self, position: Vector2, symbol: str):
        """
        Konstruktor třídy "GameObject". Vytvoří nový objekt herního prvku.

        :param position: Aktuální pozice GameObject
        :type position: Vector2
        :param symbol: Symbol zastupující GameObject
        :type symbol: str
        """
        self.__position = position
        self.__symbol = symbol

    @property
    def position(self) -> Vector2:
        """
        Funkce vrací aktuální pozici objektu ve hře.

        :return: Aktuální pozice objektu
        :rtype: Vector2
        """
        return self.__position

    def move(self, direction: Vector2):
        """
        Funkce pohne s objektem o předaný vektor.

        :param direction: Směr pohybu
        :type direction: Vector2
        """
        self.__position += direction

    def draw(self, gui: Gui):
        """
        Funkce vykreslí objekt na plátno.

        :param gui: Plátno
        :type gui: Gui
        """
        gui.draw(self.__position.x, self.__position.y, self.__symbol)
