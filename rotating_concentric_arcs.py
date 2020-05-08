#!/usr/bin/env python
# Simon Pampena

from manimlib.imports import *

class Dancing(Scene):
    CONFIG = {
        'num' : 50,
        'angle' : TAU/2
    }
    
    def construct(self):
    
        arcs = VGroup()
    
        radii = np.linspace(0.2, 3.8, self.num)
        colors = [RED, BLUE]
        
        for i in range(self.num):
            bin_alter = (len(colors) - i) % 2
            arc = Arc(radius = radii[i], angle = self.angle, stoke_width=4, color=colors[bin_alter])
            arcs.add(arc)
            
        self.play(GrowFromCenter(arcs))
        self.wait(1)
        
        self.play(*[(Rotating(j, about_point = ORIGIN, radians = 26.315789*PI*j.get_arc_length(), rate_function = linear, run_time=200)) for j in arcs])
        
        self.wait()