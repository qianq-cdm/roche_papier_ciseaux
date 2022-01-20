"""
Fait par: Qian Qian
Groupe: 407
"""

# Importer arcade
import arcade
from module.my_game import MyGame

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Roche, papier, ciseaux"


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
