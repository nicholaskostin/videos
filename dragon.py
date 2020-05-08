#!/usr/bin/env python
# https://www.youtube.com/watch?v=v678Em6qyzk

from manimlib.imports import *

class DragonCurve(MovingCameraScene):
    CONFIG = {
        'iterations' : 6,
        'angle' : TAU/4,
        'colors' : [RED, BLUE]
    }
    
    def construct(self):
    
        path = VGroup()
        future_path = VGroup()
        first_line = Line(ORIGIN, np.array([0,1,0]))
        first_line.set_color(color=[BLUE, RED])
        path.add(first_line)
        
        self.camera_frame.set_height(path.get_height() * 1.2)
        self.camera_frame.move_to(path)
        self.play(ShowCreation(path), run_time = 0.5)
        self.wait()
        
        for i in range(self.iterations):
            self.duplicate_and_rotate(path, i)
        self.wait()
        
    def duplicate_and_rotate(self, path, i):
        new_path = path.copy()
        self.add(new_path)
        height = (path.get_height() + new_path.get_width())*1.8
        pivot = self.get_last_point(path)
        self.play(
            Rotating(
                new_path,
                radians = self.angle,
                about_point = path[-1].points[pivot],
                rate_func = smooth,
                run_time = 1
            ),
            self.camera_frame.move_to, new_path,
            self.camera_frame.set_height, height,
            rate_func = smooth, run_time = 1
        )
        self.add(new_path)
        post_path = reversed([*new_path])
        path.add(*post_path)        
            
    def get_last_point(self, path):
            return 0 if len(path) > 1 else -1