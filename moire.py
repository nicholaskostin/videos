#!/usr/bin/env python
# Flink

from manimlib.imports import *

class TwoCircles(MovingCameraScene):
    CONFIG = {
        'num_rings' : 40,
        'num_circles' : 2
    }
    
    def construct(self):
        
        ellipse = ParametricFunction(
            lambda t : np.array([0.09*np.cos(8*t), 0.096*np.sin(8*t), 0]),
            t_min = 0,
            t_max = 1.6
        )
    
        circles, rot_circles = VGroup(), VGroup()
        
        radii = np.linspace(0,3.8,self.num_rings)
        
        for i in range(self.num_rings):
            c = Circle(radius = radii[i], stroke_width = 4, color = WHITE)
            circles.add(c)
            
        rot_circles = circles.copy()
        rot_circles.move_to([0.09, 0, 0])
        
        self.play(Write(circles))
        self.play(FadeIn(rot_circles), run_time = 4)
        
        self.play(
            MoveAlongPath(rot_circles, ellipse),
            rate_func = linear,
            run_time = 16,
        )
        
        self.play(FadeOut(rot_circles), run_time = 2)
        self.play(FadeOut(circles), run_time = 1)

class ThreeCircles(MovingCameraScene):
    CONFIG = {
        'num_rings' : 30,
        'num_circles' : 3
    }
    
    def construct(self):
        
        circles1, circles2, circles3 = VGroup(), VGroup(), VGroup()
        
        radii = np.linspace(0,2.4,self.num_rings)
        
        for i in range(self.num_rings):
            c = Circle(radius = radii[i], stroke_width = 4, color = WHITE)
            circles1.add(c)
            
        circles2 = circles1.copy()
        circles3 = circles1.copy()
        
        self.play(GrowFromCenter(circles1))
        self.add(circles2)
        self.add(circles3)
        self.wait()        
        
        rt = 30
        
        self.play(
            MoveAlongPath(
                circles1, Line(ORIGIN, np.array([-2.286,1.32,0])),
                rate_func = there_and_back,
                run_time = rt
            ),
            MoveAlongPath(
                circles2, Line(ORIGIN, np.array([2.286,1.32,0])),
                rate_func = there_and_back,
                run_time = rt
            ),
            MoveAlongPath(
                circles3, Line(ORIGIN, np.array([0,-2.64,0])),
                rate_func = there_and_back,
                run_time = rt
            ),
            self.camera_frame.set_height, 11,
            rate_func = there_and_back,
            run_time = rt
        )
        
        self.remove(circles2)
        self.remove(circles3)
        
        self.play(FadeOut(circles1), run_time = 2.5)

class FourCircles(MovingCameraScene):
    CONFIG = {
        'num_rings' : 40,
        'num_circles' : 4
    }
    
    def construct(self):
        
        circles1, circles2 = VGroup(), VGroup()
        circles3, circles4 = VGroup(), VGroup()
        
        radii = np.linspace(0,2.8,self.num_rings)
        
        for i in range(self.num_rings):
            c = Circle(radius = radii[i], stroke_width = 2, color = WHITE)
            circles1.add(c)
            
        circles2 = circles1.copy()
        circles3 = circles1.copy()
        circles4 = circles1.copy()
            
        self.play(GrowFromCenter(circles1))
        self.add(circles2)
        self.add(circles3)
        self.add(circles4)
        self.wait()
        
        rt = 16
        
        self.play(
            MoveAlongPath(
                circles1, Line(ORIGIN, np.array([2,2,0])),
                rate_func = linear,
                run_time = rt
            ),
            MoveAlongPath(
                circles2, Line(ORIGIN, np.array([-2,2,0])),
                rate_func = linear,
                run_time = rt
            ),
            MoveAlongPath(
                circles3, Line(ORIGIN, np.array([-2,-2,0])),
                rate_func = linear,
                run_time = rt
            ),
            MoveAlongPath(
                circles4, Line(ORIGIN, np.array([2,-2,0])),
                rate_func = linear,
                run_time = rt
            ),
            self.camera_frame.set_height, 13,
            rate_func = smooth,
            run_time = rt
        )

        archimedean_spiral_1 = ParametricFunction(
            lambda t : np.array([0.4*t*np.cos(t), 0.4*t*np.sin(t), 0]),
            t_min = -7.0681739678,
            t_max = 0
        )
        
        archimedean_spiral_2 = ParametricFunction(
            lambda t : np.array([-0.4*t*np.cos(t), 0.4*t*np.sin(t), 0]),
            t_min = -7.0681739678,
            t_max = 0
        )
        
        archimedean_spiral_3 = ParametricFunction(
            lambda t : np.array([-0.4*t*np.cos(t), -0.4*t*np.sin(t), 0]),
            t_min = -7.0681739678,
            t_max = 0
        )
        
        archimedean_spiral_4 = ParametricFunction(
            lambda t : np.array([0.4*t*np.cos(t), -0.4*t*np.sin(t), 0]),
            t_min = -7.0681739678,
            t_max = 0
        )
        
        rt2 = 30
        
        self.play(
            MoveAlongPath(
                circles1, archimedean_spiral_2,
                rate_func = smooth,
                run_time = rt2
            ),
            MoveAlongPath(
                circles2, archimedean_spiral_1,
                rate_func = smooth,
                run_time = rt2
            ),
            MoveAlongPath(
                circles3, archimedean_spiral_4,
                rate_func = smooth,
                run_time = rt2
            ),
            MoveAlongPath(
                circles4, archimedean_spiral_3,
                rate_func = smooth,
                run_time = rt2
            ),
            self.camera_frame.set_height, 8,
            rate_func = smooth,
            run_time = rt2
        )
        
        self.remove(circles2)
        self.remove(circles3)
        self.remove(circles4)
        
        self.play(FadeOut(circles1), run_time = 2.5)
        
class Squares(MovingCameraScene):

    def construct(self):
    
        num_squares = 50
    
        squares1, squares2 = VGroup(), VGroup()
        squares3, squares4, = VGroup(), VGroup()
        
        side_lengths = np.linspace(0, 6, num_squares)
        
        for i in range(num_squares):
            s = Square(side_length = side_lengths[i], stroke_width = 0.8, color = WHITE)
            squares1.add(s)
            
        squares2, squares3, squares4 = squares1.copy(), squares1.copy(), squares1.copy()
        
        self.play(Write(squares1), run_time = 4)
        self.add(squares2)
        self.add(squares3)
        self.add(squares4)
        self.wait()
        
        rt = 20
        
        self.play(
            MoveAlongPath(
                squares1, Line(ORIGIN, np.array([3,3,0])),
                rate_func = there_and_back,
                run_time = rt
            ),
            MoveAlongPath(
                squares2, Line(ORIGIN, np.array([-3,3,0])),
                rate_func = there_and_back,
                run_time = rt
            ),
            MoveAlongPath(
                squares3, Line(ORIGIN, np.array([-3,-3,0])),
                rate_func = there_and_back,
                run_time = rt
            ),
            MoveAlongPath(
                squares4, Line(ORIGIN, np.array([3,-3,0])),
                rate_func = there_and_back,
                run_time = rt
            ),
            self.camera_frame.set_height, 14,
            rate_func = there_and_back,
            run_time = rt
        )
        
        rt2 = 10
        
        self.play(
            MoveAlongPath(
                squares1, Line(ORIGIN, np.array([2,0,0])),
                rate_func = smooth,
                run_time = rt2
            ),
            MoveAlongPath(
                squares2, Line(ORIGIN, np.array([0,2,0])),
                rate_func = smooth,
                run_time = rt2
            ),
            MoveAlongPath(
                squares3, Line(ORIGIN, np.array([-2,0,0])),
                rate_func = smooth,
                run_time = rt2
            ),
            MoveAlongPath(
                squares4, Line(ORIGIN, np.array([0,-2,0])),
                rate_func = smooth,
                run_time = rt2
            ),
            self.camera_frame.set_height, 8,
            rate_func = smooth,
            run_time = rt2
        )
        
        path1 = Arc(start_angle = 0, angle = TAU, radius = 2)
        path2 = Arc(start_angle = TAU/4, angle = TAU+3*TAU/4, radius = 2)
        path3 = Arc(start_angle = TAU/2, angle = TAU+TAU/2, radius = 2)
        path4 = Arc(start_angle = 3*TAU/4, angle = TAU+TAU/4, radius = 2)
        
        squares1.save_state()
        squares2.save_state()
        squares3.save_state()
        squares4.save_state()
        
        all_squares = VGroup(squares1, squares2, squares3, squares4)
        
        def update_rotate_move_1(mob, alpha):
            squares1.restore()
            squares1.move_to(path1.point_from_proportion(alpha))
            squares1.rotate(2*PI*alpha)
            
        def update_rotate_move_2(mob, alpha):
            squares2.restore()
            squares2.move_to(path2.point_from_proportion(alpha))
            squares2.rotate(3*PI*alpha)
            
        def update_rotate_move_3(mob, alpha):
            squares3.restore()
            squares3.move_to(path3.point_from_proportion(alpha))
            squares3.rotate(4*PI*alpha)
            
        def update_rotate_move_4(mob, alpha):
            squares4.restore()
            squares4.move_to(path4.point_from_proportion(alpha))
            squares4.rotate(5*PI*alpha)            
            
        self.play(
            UpdateFromAlphaFunc(squares1, update_rotate_move_1),
            UpdateFromAlphaFunc(squares2, update_rotate_move_2),
            UpdateFromAlphaFunc(squares3, update_rotate_move_3),
            UpdateFromAlphaFunc(squares4, update_rotate_move_4),
            self.camera_frame.move_to, squares1.get_center(),
            self.camera_frame.set_height, 6.8,
            rate_func = linear,
            run_time = 64
        )
        
        self.play(
            self.camera_frame.set_height, 8,            
            rate_func = smooth,
            run_time = 6
        )
        
        self.remove(squares2)
        self.remove(squares3)
        self.remove(squares4)
        
        self.play(FadeOut(squares1))