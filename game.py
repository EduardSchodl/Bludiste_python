from gameobject import GameObject
from gui import Gui
from world import World


class Game:
    """
    Třída Game spouští hru.

    @author Eduard Schödl
    @date 231124
    """
    def __init__(self, world: World, hero: GameObject, home: GameObject):
        """
        Konstruktor třídy "Game". Vytvoří nový objekt typu Game.

        :param world: Instance světa
        :type world: World
        :param hero: Instance GameObject představující postavu
        :type hero: GameObject
        :param home: Instance GameObject představující domov
        :type home: GameObject
        """
        self.__world = world
        self.__hero = hero
        self.__home = home

    def run(self) -> bool:
        """
        Funkce spustí smyčku hry. Vytvoří plátno a vykreslí na něj všechny herní prvky - svět, postavu a domov.
        Poté načte od uživatele vstup a podle něj pohne s postavou. Hra běží, dokud postava nestoupne na
        neprázné pole, nebo se nedostane domů.

        :return: True, pokud bezpečně dorazil domů a False, pokud po cestě zabloudil
        :rtype: bool
        """
        gui = Gui(self.__world.width, self.__world.height)
        self.__world.draw(gui)
        self.__hero.draw(gui)
        self.__home.draw(gui)
        gui.show()
        while True:
            direction = gui.input_direction()
            self.__hero.move(direction)
            self.__world.draw(gui)
            self.__home.draw(gui)
            self.__hero.draw(gui)
            gui.show()
            if not self.__world.is_empty(self.__hero.position):
                return False
            if self.__hero.position == self.__home.position:
                return True
