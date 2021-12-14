import arcade
import pathlib

SPRITE_SCALING = 0.5


class AttackAnimation(arcade.Sprite):
    def __init__(self, center_x, center_y):
        super().__init__()
        self.scale = SPRITE_SCALING
        self.textures = []
        self.using_texture = 0
        self.delta_time = 0

        self.center_x = center_x
        self.center_y = center_y

    def add_texture(self, path: str):
        texture = arcade.load_texture(f"{path}")
        self.textures.append(texture)

    def draw(self):
        self.texture = self.textures[self.using_texture]

    def update(self, delta_time):
        self.delta_time += delta_time
        if 1000 <= self.delta_time:
            if self.using_texture == len(self.textures) - 1:
                self.using_texture = 0
            else:
                self.using_texture += 1
            self.delta_time = 0
