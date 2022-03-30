"""
Author: Qian Qian
Class for animation for player's attacks
"""

import arcade
from module.attacks import Attacks


class AttackAnimation(arcade.Sprite):
    ATTACK_SCALE = 0.50
    ANIMATION_SPEED = 5.0

    def __init__(self, attack_type, center_x, center_y):
        # Initialize the Sprite
        super().__init__(center_x=center_x, center_y=center_y)

        self.attack_type = attack_type
        if self.attack_type == Attacks.ROCK:
            # Textures for ROCK
            self.textures = [
                arcade.load_texture("assets/srock.png"),
                arcade.load_texture("assets/srock-attack.png")
            ]
        elif self.attack_type == Attacks.PAPER:
            # Textures for PAPER
            self.textures = [
                arcade.load_texture("assets/spaper.png"),
                arcade.load_texture("assets/spaper-attack.png")
            ]
        else:
            # Textures for SCISSORS
            self.textures = [
                arcade.load_texture("assets/scissors.png"),
                arcade.load_texture("assets/scissors-close.png")
            ]

        # Scale of the image
        self.scale = self.ATTACK_SCALE
        self.current_texture = 0
        self.set_texture(self.current_texture)
        self.animation_update_time = 1.0 / AttackAnimation.ANIMATION_SPEED
        self.time_since_last_swap = 0.0

    def set_activate_animation(self, activate_animation):
        # activate/deactivate animation
        self.activate_animation = activate_animation

    def on_update(self, delta_time: float = 1 / 60):
        # Update the animation.
        # Animation note activated
        if not self.activate_animation:
            return

        # Add time to timer
        self.time_since_last_swap += delta_time
        # If timer meets the requirement
        if self.time_since_last_swap > self.animation_update_time:
            # Change texture
            self.current_texture += 1
            if self.current_texture >= len(self.textures):
                # Prevent array out of bound
                self.current_texture = 0
            self.set_texture(self.current_texture)
            # Reset the timer
            self.time_since_last_swap = 0.0

