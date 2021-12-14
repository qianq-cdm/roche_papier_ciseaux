# Importer arcade
import arcade
import random
from module.game_state import GameState
from module.attacks import Attacks


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height
        arcade.set_background_color(arcade.csscolor.SLATE_GRAY)
        self.game_state = None
        self.player_list = arcade.SpriteList()
        self.player_attack_list = arcade.SpriteList()
        self.computer_attack = None
        self.computer_attacked = None
        self.state_text = None
        self.player_score = None
        self.computer_score = None

    def setup(self):
        """
        Configurer les variables de votre jeu ici. Il faut appeler la méthode une nouvelle
        fois si vous recommencer une nouvelle partie.
        """
        # C'est ici que vous allez créer vos listes de sprites et vos sprites.
        # C'est aussi ici que vous charger les sons de votre jeu.
        self.game_state = GameState.NOT_STARTED
        self.state_text = "Appuyer sur \"Space\" pour commencer"
        self.player_list.append(arcade.Sprite("assets/faceBeard.png",
                                              scale=0.5, center_x=self.SCREEN_WIDTH / 5 * 1.5,
                                              center_y=self.SCREEN_HEIGHT / 5 * 2.5))
        self.player_list.append(arcade.Sprite("assets/compy.png",
                                              scale=2.5, center_x=self.SCREEN_WIDTH / 5 * 3.5,
                                              center_y=self.SCREEN_HEIGHT / 5 * 2.5))
        self.player_attack_list.append(arcade.Sprite("assets/srock.png",
                                                     scale=0.5, center_x=self.SCREEN_WIDTH / 5 * 1,
                                                     center_y=self.SCREEN_HEIGHT / 5 * 1.2, hit_box_algorithm="None"))
        self.player_attack_list.append(arcade.Sprite("assets/spaper.png",
                                                     scale=0.5, center_x=self.SCREEN_WIDTH / 5 * 1.5,
                                                     center_y=self.SCREEN_HEIGHT / 5 * 1.2, hit_box_algorithm="None"))
        self.player_attack_list.append(arcade.Sprite("assets/scissors.png",
                                                     scale=0.5, center_x=self.SCREEN_WIDTH / 5 * 2,
                                                     center_y=self.SCREEN_HEIGHT / 5 * 1.2, hit_box_algorithm="None"))
        self.computer_attack = arcade.Sprite("assets/srock.png",
                                             scale=0.5, center_x=self.SCREEN_WIDTH / 5 * 3.5,
                                             center_y=self.SCREEN_HEIGHT / 5 * 1.2, hit_box_algorithm="None")
        self.computer_attacked = False
        self.player_score = 0
        self.computer_score = 0

    def on_draw(self):
        """
        C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
        de votre jeu à l'écran.
        """

        # Cette commande permet d'effacer l'écran avant de dessiner. Elle va dessiner l'arrière
        # plan selon la couleur spécifié avec la méthode "set_background_color".
        arcade.start_render()
        arcade.draw_text("Roche, papier, ciseaux", self.SCREEN_WIDTH / 5, self.SCREEN_HEIGHT - 40,
                         arcade.color.WHITE, font_size=32)
        arcade.draw_text(self.state_text, self.SCREEN_WIDTH / 8, self.SCREEN_HEIGHT - 75,
                         arcade.color.WHITE, font_size=24)
        self.player_list.draw()
        self.player_attack_list.draw()
        self.player_attack_list.draw_hit_boxes()
        if self.computer_attacked:
            self.computer_attack.draw()
        self.computer_attack.draw_hit_box()
        arcade.draw_text(f"Le pointage du joueur est {self.player_score}", self.SCREEN_WIDTH / 5 * 0.7, self.SCREEN_HEIGHT / 5 * 0.7,
                         arcade.color.WHITE, font_size=16)
        arcade.draw_text(f"Le pointage du joueur est {self.computer_score}", self.SCREEN_WIDTH / 5 * 2.7, self.SCREEN_HEIGHT / 5 * 0.7,
                         arcade.color.WHITE, font_size=16)

    def on_update(self, delta_time):
        """
        Toute la logique pour déplacer les objets de votre jeu et de
        simuler sa logique vont ici. Normalement, c'est ici que
        vous allez invoquer la méthode "update()" sur vos listes de sprites.
        Paramètre:
            - delta_time : le nombre de milliseconde depuis le dernier update.
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Méthode invoquée à chaque fois que l'usager enlève son doigt d'une touche.
        Paramètres:
            - key: la touche relâchée
            - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?
        """
        if key == arcade.key.SPACE:
            self.game_state = GameState.ROUND_ACTIVE
            self.state_text = "Appuyer sur une image pour faire une attaque!"

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Méthode invoquée lorsque l'usager relâche le bouton cliqué de la souris.
        Paramètres:
            - x, y: coordonnées où le bouton a été relâché
            - button: le bouton de la souris relâché
            - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?
        """
        if button == arcade.MOUSE_BUTTON_LEFT and self.game_state == GameState.ROUND_ACTIVE:
            rock = self.player_attack_list.sprite_list[Attacks.ROCK.value]
            paper = self.player_attack_list.sprite_list[Attacks.PAPER.value]
            scissors = self.player_attack_list.sprite_list[Attacks.SCISSORS.value]
            if rock.left < x < rock.right and rock.bottom < y < rock.top:
                self.player_attacked(Attacks.ROCK)
            elif paper.left < x < paper.right and paper.bottom < y < paper.top:
                self.player_attacked(Attacks.PAPER)
            elif scissors.left < x < scissors.right and scissors.bottom < y < scissors.top:
                self.player_attacked(Attacks.SCISSORS)
            else:
                pass

    def player_attacked(self, player_attack):
        """
        Le joueur a déjà attaqué
        :return: None
        """
        computer_attack = random.choice(list(Attacks))
        if computer_attack == Attacks.ROCK:
            self.computer_attack = arcade.Sprite("assets/srock-attack.png",
                                                 scale=0.5, center_x=self.SCREEN_WIDTH / 5 * 3.5,
                                                 center_y=self.SCREEN_HEIGHT / 5 * 1.2, hit_box_algorithm="None")
            if player_attack == Attacks.PAPER:
                self.player_score += 1
        self.computer_attacked = True
