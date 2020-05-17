#!/usr/bin/env python
# Flink

from manimlib.imports import *

class Outro(Scene):

    def construct(self):
    
        github_logo = SVGMobject("github")
        github_logo.set_color(GOLD_A)
        
        github = TextMobject("nicholaskostin")
        github.set_color(GOLD_A)
        github.next_to(github_logo.get_center(), 1.6*RIGHT)
        
        github_3b1b = TextMobject("manim")
        github_3b1b.set_color(GOLD_A)
        github_3b1b.next_to(github_logo.get_center(), 1.6*RIGHT)
        
        outro_text = TextMobject("See description for source code!")
        outro_text.move_to(2*UP)
        
        credit_text = TextMobject("Creating using 3Blue1Brown's Manim library")
        credit_text.move_to(2*UP)
        
        self.play(
            Write(outro_text),
            Write(github_logo),
            Write(github),
            run_time = 2
        )
        
        self.wait(2)
        
        self.play(
            Transform(outro_text, credit_text),
            Transform(github, github_3b1b),
            run_time = 1
        )
        
        self.wait(2)
        
        self.play(
            FadeOut(credit_text),
            FadeOut(github_3b1b),
            FadeOut(github_logo),
            run_time = 1.6
        )