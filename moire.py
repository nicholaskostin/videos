#!/usr/bin/env python
# Flink

from manimlib.imports import *

class ConcentricCirclesTwo(Scene):
    CONFIG = {
        'num_rings' : 20,
        'num_circles' : 2
    }
    
    def construct(self):
    
        circles1, circles2 = VGroup(), VGroup()
        
        radii = np.linspace(0,2,self.num_rings)
        
        for i in range(self.num_rings):
            c = Circle(radius = radii[i], stroke_width = 4, color = WHITE)
            circles1.add(c)
            
        circles2 = circles1.copy()
        
        self.play(GrowFromCenter(circles1))
        self.add(circles2)
        self.wait()
        
        f1 = Line(ORIGIN, np.array([0,2,0]))
        f2 = Line(ORIGIN, np.array([0,-2,0]))
        
        d1 = Dot()
        d1.move_to(np.array([2,2,0]))
        d2 = Dot()
        d2.move_to(np.array([-2,-2,0]))
        self.add(d1)
        self.add(d2)
        p = Dot()
        p.move_to(np.array([1.414,1.414,0]))
        self.add(p)
        
        self.play(
            MoveAlongPath(circles1, f1),
            MoveAlongPath(circles2, f2),
            run_time = 4
        )
        
        s1 = Arc(start_angle = TAU/2, angle = TAU/4, radius = 2)
        s1.move_to(np.array([1.414,1.414,0]))
        s2 = Arc(start_angle = 0, angle = TAU/4, radius = 2)
        s2.move_to(np.array([-2,-2,0]))
        
        self.add(s1)
        self.add(s2)
        
        
        self.play(
            MoveAlongPath(circles1, s1),
            MoveAlongPath(circles2, s2),
            run_time = 4
        )

class ConcentricCirclesFour(Scene):
    CONFIG = {
        'num_rings' : 20,
        'num_circles' : 4
    }
    
    def construct(self):
        
        circles1, circles2 = VGroup(), VGroup()
        circles3, circles4 = VGroup(), VGroup()
        
        radii = np.linspace(0,1.8,self.num_rings)
        
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
        self.wait()
        
        f1 = Line(ORIGIN, np.array([2,2,0]))
        f2 = Line(ORIGIN, np.array([-2,2,0]))
        f3 = Line(ORIGIN, np.array([-2,-2,0]))
        f4 = Line(ORIGIN, np.array([2,-2,0]))
        
        self.play(
            MoveAlongPath(circles1, f1),
            MoveAlongPath(circles2, f2),
            MoveAlongPath(circles3, f3),
            MoveAlongPath(circles4, f4),
            run_time = 4
        )
        
        r1 = Line(np.array([2,2,0]), ORIGIN)
        r2 = Line(np.array([-2,2,0]), ORIGIN)
        r3 = Line(np.array([-2,-2,0]), ORIGIN)
        r4 = Line(np.array([2,-2,0]), ORIGIN)
        
        self.play(
            MoveAlongPath(circles1, r1),
            MoveAlongPath(circles2, r2),
            MoveAlongPath(circles3, r3),
            MoveAlongPath(circles4, r4),
            run_time = 4
        )