# Importer arcade
import arcade
import random
from module.game_state import GameState
from module.attacks import Attacks
from module.attack_animation import AttackAnimation


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        # Height and Width for screen
        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height
        # Background color
        arcade.set_background_color(arcade.csscolor.SLATE_GRAY)
        # State of the game
        self.game_state = None
        # List of players' sprites
        self.player_list = arcade.SpriteList()
        # Player's attacks
        self.player_attack_rock = None
        self.player_attack_paper = None
        self.player_attack_scissors = None
        # What's the attack the player made
        self.player_attack = None
        # What's the attack the computer made
        self.computer_attack = None
        # Did computer attacked
        self.computer_attacked = None
        # Text on top of the screen
        self.state_text = None
        # Player's score
        self.player_score = None
        # Computer's score
        self.computer_score = None
        # The name of winner
        self.winner = None
        # The text showing who wins
        self.winner_text = None
        # Attack animation class
        self.attack_animation = None

    def setup(self):
        """
        Configurer les variables de votre jeu ici. Il faut appeler la méthode une nouvelle
        fois si vous recommencer une nouvelle partie.
        """
        # C'est ici que vous allez créer vos listes de sprites et vos sprites.
        # C'est aussi ici que vous charger les sons de votre jeu.
        # The game is not started
        self.game_state = GameState.NOT_STARTED
        # Tell player to press the key to start the game
        self.state_text = "Appuyer sur \"Space\" pour commencer"
        # No winner and text for it
        self.winner = ""
        self.winner_text = ""
        # Computer has NOT attacked
        self.computer_attacked = False
        # Player and computer don't have scores
        self.player_score = 0
        self.computer_score = 0
        # Sprites for players
        self.player_list.append(arcade.Sprite("assets/faceBeard.png",
                                              scale=0.5, center_x=self.SCREEN_WIDTH / 5 * 1.5,
                                              center_y=self.SCREEN_HEIGHT / 5 * 2.5))
        self.player_list.append(arcade.Sprite("assets/compy.png",
                                              scale=2.5, center_x=self.SCREEN_WIDTH / 5 * 3.5,
                                              center_y=self.SCREEN_HEIGHT / 5 * 2.5))
        # Sprite for computer's attack
        self.computer_attack = arcade.Sprite("assets/srock.png",
                                             scale=0.5, center_x=self.SCREEN_WIDTH / 5 * 3.5,
                                             center_y=self.SCREEN_HEIGHT / 5 * 1.2, hit_box_algorithm="None")
        # Player's attacks
        self.player_attack_rock = AttackAnimation(Attacks.ROCK, self.SCREEN_WIDTH / 5 * 1,
                                                  self.SCREEN_HEIGHT / 5 * 1.2)
        self.player_attack_paper = AttackAnimation(Attacks.PAPER, self.SCREEN_WIDTH / 5 * 1.5,
                                                   self.SCREEN_HEIGHT / 5 * 1.2)
        self.player_attack_scissors = AttackAnimation(Attacks.SCISSORS, self.SCREEN_WIDTH / 5 * 2,
                                                      self.SCREEN_HEIGHT / 5 * 1.2)

    def draw_box_for_player_attacks(self):
        # Draw the box for player attacks
        # Box of player attack rock
        arcade.draw_rectangle_outline(
            center_x=self.player_attack_rock.center_x,
            center_y=self.player_attack_rock.center_y,
            width=75,
            height=75,
            color=arcade.color.BLACK
        )
        # Box of player attack paper
        arcade.draw_rectangle_outline(
            center_x=self.player_attack_paper.center_x,
            center_y=self.player_attack_paper.center_y,
            width=75,
            height=75,
            color=arcade.color.BLACK
        )
        # Box of player attack scissors
        arcade.draw_rectangle_outline(
            center_x=self.player_attack_scissors.center_x,
            center_y=self.player_attack_scissors.center_y,
            width=75,
            height=75,
            color=arcade.color.BLACK
        )

    def draw_scores(self):
        # Score of player
        arcade.draw_text(f"Le pointage du joueur est {self.player_score}", self.SCREEN_WIDTH / 5 * 0.7,
                         self.SCREEN_HEIGHT / 5 * 0.7,
                         arcade.color.WHITE, font_size=16)
        # Score of computer
        arcade.draw_text(f"Le pointage d'ordinateur est {self.computer_score}", self.SCREEN_WIDTH / 5 * 2.7,
                         self.SCREEN_HEIGHT / 5 * 0.7,
                         arcade.color.WHITE, font_size=16)

    def draw_player_attack(self):
        if self.player_attack == Attacks.ROCK:
            self.player_attack_rock.draw()
        elif self.player_attack == Attacks.PAPER:
            self.player_attack_paper.draw()
        elif self.player_attack == Attacks.SCISSORS:
            self.player_attack_scissors.draw()
        else:
            self.player_attack_rock.draw()
            self.player_attack_paper.draw()
            self.player_attack_scissors.draw()

    def on_draw(self):
        """
        C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
        de votre jeu à l'écran.
        """

        # Cette commande permet d'effacer l'écran avant de dessiner. Elle va dessiner l'arrière
        # plan selon la couleur spécifié avec la méthode "set_background_color".
        arcade.start_render()
        # Draw the game title
        arcade.draw_text("Roche, papier, ciseaux", 40, self.SCREEN_HEIGHT - 40,
                         arcade.color.WHITE, font_size=32)
        # Draw the status text
        arcade.draw_text(self.state_text, 40, self.SCREEN_HEIGHT - 75,
                         arcade.color.WHITE, font_size=24)
        # Draw the winner text
        arcade.draw_text(self.winner_text, 40, self.SCREEN_HEIGHT - 110,
                         arcade.color.WHITE, font_size=24)
        # Draw sprites for both players
        self.player_list.draw()
        # Draw attacks for player
        self.draw_player_attack()
        # Draw the attack animation
        self.draw_box_for_player_attacks()
        # If computer attacked
        if self.computer_attacked:
            # Draw the attack of animation
            self.computer_attack.draw()
        # Draw the border line for computer's attack
        self.computer_attack.draw_hit_box()
        self.draw_scores()

    def set_activate_animation(self, activate):
        self.player_attack_rock.set_activate_animation(activate)
        self.player_attack_paper.set_activate_animation(activate)
        self.player_attack_scissors.set_activate_animation(activate)

    def update_animation(self, delta_time):
        self.player_attack_rock.on_update(delta_time)
        self.player_attack_paper.on_update(delta_time)
        self.player_attack_scissors.on_update(delta_time)

    def on_update(self, delta_time):
        """
        Toute la logique pour déplacer les objets de votre jeu et de
        simuler sa logique vont ici. Normalement, c'est ici que
        vous allez invoquer la méthode "update()" sur vos listes de sprites.
        Paramètre:
            - delta_time : le nombre de milliseconde depuis le dernier update.
        """
        if self.game_state == GameState.ROUND_DONE:
            # Round is done
            # Stop the animation
            self.set_activate_animation(False)
            # Tell player how to start a new round
            self.state_text = "Appuyer sur \"Space\" pour commencer\nune nouvelle ronde!"
            # Show who wins
            self.winner_text = f"{self.winner} a gagné la ronde!"

            if self.player_score >= 3:
                # If player have 3 points
                # Player wins
                self.winner = "vous avez"
                # Game over
                self.game_state = GameState.GAME_OVER
            elif self.computer_score >= 3:
                # Computer have 3 points
                # Computer wins
                self.winner = "l'ordinateur a"
                # Game over
                self.game_state = GameState.GAME_OVER

        elif self.game_state == GameState.GAME_OVER:
            # Game is over
            # Stop the animation
            self.set_activate_animation(False)
            # Tell the player game is over
            self.state_text = "Appuyer sur \"Space\" pour débuter une nouvelle partie!"
            # How to start a new game
            self.winner_text = f"La partie est terminée, {self.winner} gagné la partie!"

        elif self.game_state == GameState.NOT_STARTED:
            # Game not started
            # Stop the animation
            self.set_activate_animation(False)
            # How to start the game
            self.state_text = "Appuyer sur \"Space\" pour commencer"

        elif self.game_state == GameState.ROUND_ACTIVE:
            # Round is active
            # Reset computer attack
            self.computer_attacked = False
            # Start the animation
            self.set_activate_animation(True)
            # Tell the player how to attack
            self.state_text = "Appuyer sur une image pour faire une attaque!"
            # Clear the winner text
            self.winner_text = ""

        self.update_animation(delta_time)

    def on_key_release(self, key, key_modifiers):
        """
        Méthode invoquée à chaque fois que l'usager enlève son doigt d'une touche.
        Paramètres:
            - key: la touche relâchée
            - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?
        """
        if key == arcade.key.SPACE:
            # If space is pressed
            if self.game_state == GameState.GAME_OVER:
                # Game was over
                # Setup new game
                self.setup()
                # Start new game
                self.game_state = GameState.ROUND_ACTIVE
            else:
                # Start a new game
                self.game_state = GameState.ROUND_ACTIVE
                self.player_attack = None

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Méthode invoquée lorsque l'usager relâche le bouton cliqué de la souris.
        Paramètres:
            - x, y: coordonnées où le bouton a été relâché
            - button: le bouton de la souris relâché
            - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?
        """
        if button == arcade.MOUSE_BUTTON_LEFT and self.game_state == GameState.ROUND_ACTIVE:
            # Left mouse button clicked AND the round is active
            if self.player_attack_rock.left < x < self.player_attack_rock.right \
                    and self.player_attack_rock.bottom < y < self.player_attack_rock.top:
                # Clicked on rock
                self.player_attack = Attacks.ROCK
                self.player_attacked()
            elif self.player_attack_paper.left < x < self.player_attack_paper.right \
                    and self.player_attack_paper.bottom < y < self.player_attack_paper.top:
                # Click on paper
                self.player_attack = Attacks.PAPER
                self.player_attacked()
            elif self.player_attack_scissors.left < x < self.player_attack_scissors.right \
                    and self.player_attack_scissors.bottom < y < self.player_attack_scissors.top:
                # Click on scissors
                self.player_attack = Attacks.SCISSORS
                self.player_attacked()
            else:
                # Clicked on nothing
                pass

    def player_attacked(self):
        """
        Le joueur a déjà attaqué
        :return: None
        """
        # Random choose an attack for computer
        computer_attack = random.choice(list(Attacks))
        if computer_attack == Attacks.ROCK:
            # Computer's attack is rock
            # Draw attack
            self.computer_attack = arcade.Sprite("assets/srock-attack.png",
                                                 scale=0.5, center_x=self.SCREEN_WIDTH / 5 * 3.5,
                                                 center_y=self.SCREEN_HEIGHT / 5 * 1.2, hit_box_algorithm="None")
            if self.player_attack == Attacks.ROCK:
                # Nobody wins
                self.winner = "Personne"
            elif self.player_attack == Attacks.PAPER:
                # Player wins
                self.player_score += 1
                self.winner = "Le joueur"
            else:
                # Computer wins
                self.computer_score += 1
                self.winner = "L'ordinateur"
        elif computer_attack == Attacks.PAPER:
            # Computer's attack is paper
            # Draw attack
            self.computer_attack = arcade.Sprite("assets/spaper-attack.png",
                                                 scale=0.5, center_x=self.SCREEN_WIDTH / 5 * 3.5,
                                                 center_y=self.SCREEN_HEIGHT / 5 * 1.2, hit_box_algorithm="None")
            if self.player_attack == Attacks.PAPER:
                # Nobody wins
                self.winner = "Personne"
            elif self.player_attack == Attacks.SCISSORS:
                # player wins
                self.player_score += 1
                self.winner = "Le joueur"
            else:
                # Computer wins
                self.computer_score += 1
                self.winner = "L'ordinateur"
        else:
            # Computer's attack is scissors
            # Draw attack
            self.computer_attack = arcade.Sprite("assets/scissors.png",
                                                 scale=0.5, center_x=self.SCREEN_WIDTH / 5 * 3.5,
                                                 center_y=self.SCREEN_HEIGHT / 5 * 1.2, hit_box_algorithm="None")
            if self.player_attack == Attacks.SCISSORS:
                # Nobody wins
                self.winner = "Personne"
            elif self.player_attack == Attacks.ROCK:
                # Player wins
                self.player_score += 1
                self.winner = "Le joueur"
            else:
                # Computer wins
                self.computer_score += 1
                self.winner = "L'ordinateur"
        # Computer attacked
        self.computer_attacked = True
        # This round is done
        self.game_state = GameState.ROUND_DONE
