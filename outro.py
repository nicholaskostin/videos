#!/usr/bin/env python
# Flink

from manimlib.imports import *

class Outro(Scene):

    def construct(self):
       
        github_logo = SVGMobject('github').scale(0.6)
        github_logo.set_color(WHITE)
        github_logo.move_to(1.6*LEFT)
        
        github = TexMobject('\\texttt{github.com/nicholaskostin}').scale(0.6)
        github.next_to(github_logo, RIGHT)
        github_3b1b = TexMobject('\\texttt{github.com/3b1b/manim}').scale(0.6)
        github_3b1b.next_to(github_logo, RIGHT)
        
        see_description = TextMobject('See description for source code').scale(1.2)
        see_description.set_color_by_gradient(RED, BLUE, RED)
        
        acknowledge_3b1b = TextMobject(
            'Created using Manim ',
            '(by ',
            '3Blue',
            '1Brown',
            ')'
        ).scale(1.2)
        acknowledge_3b1b[0].set_color_by_gradient(YELLOW, GREEN)
        acknowledge_3b1b[1].set_color(WHITE)
        acknowledge_3b1b[2].set_color(BLUE)
        acknowledge_3b1b[3].set_color(GREY_BROWN)
        acknowledge_3b1b[4].set_color(WHITE)
        acknowledge_3b1b.move_to(1.2*UP)
        
        self.play(
            Write(see_description),
            run_time = 2
        )
        
        self.play(
            ApplyMethod(see_description.shift, 1.2*UP)
        )
        
        self.play(
            Write(github_logo),
            Write(github),
            run_time = 2
        )
        
        self.wait()
        
        self.play(
            Transform(github, github_3b1b),
            Transform(see_description, acknowledge_3b1b),
            run_time = 2
        )
        
        self.wait(2)
        
        self.play(
            FadeOut(github_3b1b),
            FadeOut(acknowledge_3b1b),
            run_time = 2
        )