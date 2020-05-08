#!/usr/bin/env python
# Pat Kohl

from manimlib.imports import *

class ConcentricCirclesFour(Scene):
    CONFIG = {
        'num_rings' : 20,
        'num_circles' : 4
    }
    
    def construct(self):
        
        circles1, circles2 = VGroup(), VGroup()
        circles3, circles4 = VGroup(), VGroup()
        
        radii = np.linspace(0.2,1.8,self.num_rings)
        
        for i in range(self.num_rings):
            c = Circle(radius = radii[i], stroke_width = 4, color = WHITE)
            circles1.add(c)
            
        circles2 = circles1.copy()
        circles3 = circles1.copy()
        circles4 = circles1.copy()
            
        self.play(GrowFromCenter(circles1))
        self.add(circles2)
        self.add(circles3)
        self.add(circles4)
        self.wait
        
        self.play(
            ApplyMethod(circles1.shift, np.array([2,2,0])),
            ApplyMethod(circles2.shift, np.array([-2,2,0])),
            ApplyMethod(circles3.shift, np.array([-2,-2,0])),
            ApplyMethod(circles4.shift, np.array([2,-2,0])),
            run_time = 12
        )
        
        self.wait()
        
        self.play(
            ApplyMethod(circles1.shift, ORIGIN),
            ApplyMethod(circles2.shift, ORIGIN),
            ApplyMethod(circles3.shift, ORIGIN),
            ApplyMethod(circles4.shift, ORIGIN),
            run_time = 12
        )