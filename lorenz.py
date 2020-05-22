#!/usr/bin/env python
# Flink

from manimlib.imports import *

class LorenzSystem(Scene):
    
    def construct(self):
        
        x_eqn = TexMobject(
            '{d',
            'x',
            '\\over',
            'dt}',
            '=',
            '\\sigma',
            '(',
            'y',
            '-',
            'x',
            ')'
        ).scale(1)
        
        x_eqn.set_color_by_tex_to_color_map({
            'x' : BLUE,
            'y' : GREEN,
            '\\sigma' : YELLOW
        })
        
        y_eqn = TexMobject(
            '{d',
            'y',
            '\\over',
            'dt}',
            '=',
            'x',
            '(',
            '\\rho',
            '-',
            'z',
            ')',
            '-',
            'y'
        ).scale(1)
        
        y_eqn.set_color_by_tex_to_color_map({
            'x' : BLUE,
            'y' : GREEN,
            'z' : RED,
            '\\rho' : YELLOW
        })
        
        z_eqn = TexMobject(
            '{d',
            'z',
            '\\over',
            'dt}',
            'x',
            'y',
            '-',
            '\\beta',
            'z'
        ).scale(1)
        
        z_eqn.set_color_by_tex_to_color_map({
            'x' : BLUE,
            'y' : GREEN,
            'z' : RED,
            '\\betra' : YELLOW
        })
        
        