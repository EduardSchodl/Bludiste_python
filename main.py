from game import Game
from gameobject import GameObject
from vector2 import Vector2
from world import World

if __name__ == "__main__":
    world = World(
                [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
                 [1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
                 [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
                 [1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
                 [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
                 [' ','#'])
    hero = GameObject(Vector2(1, 1), "@")
    home = GameObject(Vector2(10, 5), "^")

    destination = Game(world, hero, home).run()
    if destination:
        print("Vitej doma!")
    else:
        print("... a uz ho nikdy nikdo nevidel... ")
