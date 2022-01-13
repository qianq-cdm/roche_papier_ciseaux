from re import S


class AttackAnimation():
    def __init__(self, animation_update_time, frame_list_0, frame_list_1):
        self.activate_animation = False
        self.frame_count = 0
        self.since_last_frame_update = 0
        
        self.animation_update_time = animation_update_time
        
        self.frame_list_0 = frame_list_0
        self.frame_list_1 = frame_list_1
        
    def set_activate_animation(self, activate_animation):
        self.activate_animation = activate_animation
        
    def draw(self):
        if self.activate_animation and self.frame_count == 1:
            self.frame_list_1.draw()
            self.frame_list_1.draw_hit_boxes()
        else:
            self.frame_list_0.draw()
            self.frame_list_0.draw_hit_boxes()
        
    def update(self, delta_time):
        if self.activate_animation:
            self.since_last_frame_update += delta_time
            if (self.since_last_frame_update > self.animation_update_time):
                self.frame_count = (self.frame_count + 1) % 2
                self.since_last_frame_update = 0.0
                print("Animation updated")
        else:
            self.since_last_frame_update = 0.0
        
