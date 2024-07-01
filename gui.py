from vector2 import Vector2


class Gui:
    """
    Třída Gui představuje plátno, na které se vykreslují všechny objekty.

    @author Eduard Schödl
    @date 231124
    """
    def __init__(self, width: int, height: int):
        """
        Konstruktor třídy "Gui" vytvoří objekt pltátna o dané výšce a šířce.

        :param width:
        :type width:
        :param height:
        :type height:
        """
        self.__width = width
        self.__height = height
        self.__array2D = [[''] * width for i in range(height)]

    def draw(self, x: int, y: int, symbol: str):
        """
        Funkce vykreslí předaný objekt na plátno.

        :param x: Cílová souřadnice x
        :type x: int
        :param y: Cílová souřadnice y
        :type y: int
        :param symbol: Symbol určený k vykreslení
        """
        self.__array2D[y][x] = symbol

    def show(self):
        """
        Funkce vykreslí obsah plátna na výstup do konzole.

        """
        for y in range(self.__height):
            for x in range(self.__width):
                print(f"{self.__array2D[y][x]}", end="")
            print("")

    def clear(self):
        """
        Funkce vyčistí plátno. Všechny prvky na plátně se nastaví na mezeru.

        """
        for y in range(self.__height):
            for x in range(self.__width):
                self.__array2D[y][x] = " "

    def input_direction(self) -> Vector2:
        """
        Funkce načte vstup od uživatele. Na základě vstupu vrátí vektor odpovídající směru pohybu.\n
        Vstup   ->  směr:
          8     ->  nahoru
          4     ->  vlevo
          6     ->  vpravo
          2     ->  dolu

        :return: Vektor směru pohybu
        :rtype: Vector2
        """
        move = int(input())

        if move == 8:
            return Vector2(0, -1)
        elif move == 4:
            return Vector2(-1, 0)
        elif move == 6:
            return Vector2(1, 0)
        elif move == 2:
            return Vector2(0, 1)
        else:
            return Vector2(0, 0)
