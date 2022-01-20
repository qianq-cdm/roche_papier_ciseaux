"""
Author: Qian Qian
Class for animation for player's attacks
"""

class AttackAnimation():
    def __init__(self, animation_update_time, frame_list_0, frame_list_1):
        """
        Initialize an attack animation class
        :param animation_update_time: time between updates
        :param frame_list_0: first set of frame
        :param frame_list_1: second set of frame
        """
        self.activate_animation = False
        self.frame_count = 0
        self.since_last_frame_update = 0

        # Time between updates
        self.animation_update_time = animation_update_time

        # Sets of frames
        self.frame_list_0 = frame_list_0
        self.frame_list_1 = frame_list_1
        
    def set_activate_animation(self, activate_animation):
        # activate/deactivate animation
        self.activate_animation = activate_animation
        
    def draw(self):
        # Draw frames
        if self.activate_animation and self.frame_count == 1:
            # Draw second set of frame
            self.frame_list_1.draw()
            self.frame_list_1.draw_hit_boxes()
        else:
            # Draw first set of frame
            self.frame_list_0.draw()
            self.frame_list_0.draw_hit_boxes()
        
    def update(self, delta_time):
        # Update frame
        if self.activate_animation:
            # Animation activated
            # Calculate the time from last update
            self.since_last_frame_update += delta_time
            if self.since_last_frame_update > self.animation_update_time:
                # If it is long enough for update
                # Switch the set of frame
                self.frame_count = (self.frame_count + 1) % 2
                # Clear the timer
                self.since_last_frame_update = 0.0
        else:
            # Animation not activated
            # Keep the timer at 0
            self.since_last_frame_update = 0.0
        
