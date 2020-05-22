#!/usr/bin/env python
# Flink --- John Martin Knuth

from manimlib.imports import *
from scipy.integrate import odeint


# Hopefully destined for obsolescence
# Fetch data from CSV
def get_coords_from_csv(file_name):
        import csv
        coords = []
        with open(f'{file_name}', 'r') as csvFile:
            reader = csv.reader(csvFile)
            x, y, z = row
            coord = [float(x), float(y), float(z)]
            coords.append(coord)
        csvFile.close()
        return coords
        
# Numerically solve ODEs
# Define constants
sigma = 10; beta = (8/3); rho = 28

# Initial conditions
x_init = 0.1; y_init = 0.1; z_init = 0.1
initial_state = np.array([x_init, y_init, z_init])

# Create array of time values to study
t_init = 0; t_fin = 200; h = 0.01
t = np.arange(t_init, t_fin, h)

# Governing system of differential equations
def f(state, t):
    x, y, z = state
    return np.array([sigma*(y - x), x*(rho - z) - y, x*y - beta*z])

states = odeint(f, initial_state, t)        
        
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
        
        x_eqn_v2 = TexMobject(
            '\\dot{x}',
            '=',
            '\\sigma',
            '(',
            'y',
            '-',
            'x',
            ')'
        ).scale(1)
        
        x_eqn_v2.set_color_by_tex_to_color_map({
            '\\dot{x}' : BLUE,
            'x' : BLUE,
            'y' : GREEN,
            '\\sigma' : TEAL
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
        
        y_eqn.shift(1.4*DOWN)
        
        y_eqn.set_color_by_tex_to_color_map({
            'x' : BLUE,
            'y' : GREEN,
            'z' : RED,
            '\\rho' : YELLOW
        })
        
        y_eqn_v2 = TexMobject(
            '\\dot{y}',
            '=',
            '\\rho',
            'x',
            '-',
            'y',
            '-',
            'x',
            'z',
        ).scale(1)
        
        y_eqn_v2.shift(1.4*DOWN)
        
        y_eqn_v2.set_color_by_tex_to_color_map({
            '\\dot{y}' : GREEN,
            'x' : BLUE,
            'y' : GREEN,
            'z' : RED,
            '\\rho' : GOLD
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
        
        z_eqn.shift(2.8*DOWN)
        
        z_eqn.set_color_by_tex_to_color_map({
            'x' : BLUE,
            'y' : GREEN,
            'z' : RED,
            '\\beta' : YELLOW
        })
        
        z_eqn_v2 = TexMobject(
            '\\dot{z}',
            '=',
            'x',
            'y',
            '-',
            '\\beta',
            'z'
        ).scale(1)
        
        z_eqn_v2.shift(2.8*DOWN)
        
        z_eqn_v2.set_color_by_tex_to_color_map({
            '\\dot{z}' : RED,
            'x' : BLUE,
            'y' : GREEN,
            'z' : RED,
            '\\beta' : MAROON
        })
        
        y_eqn.align_to(x_eqn, LEFT)
        z_eqn.align_to(y_eqn, LEFT)
        
        y_eqn_v2.align_to(x_eqn_v2, LEFT)
        z_eqn_v2.align_to(y_eqn_v2, LEFT)
        
        coupled_odes = VGroup(x_eqn, y_eqn, z_eqn)
        coupled_odes.move_to(ORIGIN)
        brace = Brace(coupled_odes, LEFT)
        
        coupled_odes_v2 = VGroup(x_eqn_v2, y_eqn_v2, z_eqn_v2)
        coupled_odes_v2.move_to(ORIGIN)
        brace_v2 = Brace(coupled_odes_v2, LEFT, buff = SMALL_BUFF)
        
        top_text = TextMobject(
            'The ',
            'Lorenz system ',
            'is'
        ).scale(1)
        top_text[1].set_color_by_gradient(BLUE, GREEN, RED)
        top_text.move_to(2.8*UP)
        
        bottom_text = TextMobject(
            'where ',
            '$\\sigma$ ',
            'is the ',
            'Prandtl number',
            ', ',
            '$\\rho$ ',
            'is the rescaled ',
            'Rayleigh number',
            ', ',
            'and ',
            '$\\beta$ ',
            'is ',
            'some ',
            'parameter',
            '.'
        ).scale(1.2)
        bottom_text[1].set_color(TEAL)
        bottom_text[3].set_color(TEAL)
        bottom_text[5].set_color(GOLD)
        bottom_text[7].set_color(GOLD)
        bottom_text[10].set_color(MAROON)
        bottom_text[13].set_color(MAROON)
        bottom_text.set_width(0.8*FRAME_WIDTH)
        bottom_text.move_to(2.8*DOWN)
        
        
        x_vector = TexMobject(r'\text{Let } \mathbf{x} = \begin{pmatrix} x \\ y \\ z \end{pmatrix}')
        x_vector[0][3].set_color("#6F0EED")
        x_vector[0][7].set_color(BLUE)
        x_vector[0][8].set_color(GREEN)
        x_vector[0][9].set_color(RED)
        x_vector.move_to(2.36*DOWN + 2.7*LEFT)
        
        f_vector = TexMobject(r'\text{and } \mathbf{f} = \begin{pmatrix} \sigma (y - x) \\ \rho x - y - xz \\ xy - \beta z \end{pmatrix}')
        f_vector[0][3].set_color("#6F0EED")
        f_vector[0][7].set_color(TEAL)
        f_vector[0][9].set_color(GREEN)
        f_vector[0][11].set_color(BLUE)
        f_vector[0][13].set_color(GOLD)
        f_vector[0][14].set_color(BLUE)
        f_vector[0][16].set_color(GREEN)
        f_vector[0][18].set_color(BLUE)
        f_vector[0][19].set_color(RED)
        f_vector[0][20].set_color(BLUE)
        f_vector[0][21].set_color(GREEN)
        f_vector[0][23].set_color(MAROON)
        f_vector[0][24].set_color(RED)
        f_vector.next_to(x_vector, RIGHT)
        
        parameter_space = TexMobject(r'\mathfrak{S} = \begin{pmatrix} \sigma \\ \rho \\ \beta \end{pmatrix}')
        parameter_space[0][4].set_color(TEAL)
        parameter_space[0][5].set_color(GOLD)
        parameter_space[0][6].set_color(MAROON)
        parameter_space.move_to(1.4*DOWN + 2*LEFT)
        
        parameter_space_constraints = TextMobject(
            'for ',
            '$\\sigma$',
            ',',
            '$\\rho$',
            ',',
            '$\\beta$',
            '$ > 0$',
            '.'
        )
        parameter_space_constraints[1].set_color(TEAL)
        parameter_space_constraints[3].set_color(GOLD)
        parameter_space_constraints[5].set_color(MAROON)
        parameter_space_constraints.next_to(parameter_space, RIGHT, buff = LARGE_BUFF)
        
        recast = TextMobject('We can recast this system.')
        recast.move_to(0.8*DOWN)
        
        recasting = VGroup(recast, x_vector, f_vector)
        
        becomes = TextMobject('Then the system becomes ', '$\\dot{\\mathbf{x}} = \\mathbf{f}$', ', ', 'with parameter space')
        becomes[1].set_color("#6F0EED")
        becomes.move_to(ORIGIN)
        
        self.play(
            Write(top_text),
            Write(bottom_text),
            FadeIn(brace),
            Write(coupled_odes),
            run_time = 4
        )
        
        self.wait(3.6)
        
        self.play(
            ReplacementTransform(brace, brace_v2),
            ReplacementTransform(coupled_odes, coupled_odes_v2),
            run_time = 2
        )
        
        self.wait(4)
        
        self.play(
            FadeOut(top_text),
            FadeOut(bottom_text),
            run_time = 2
        )
        
        self.wait()
        
        def move_system(bra):
            bra.next_to(coupled_odes_v2, LEFT, buff = SMALL_BUFF)
            
        brace_v2.add_updater(move_system)
        self.add(brace_v2)
        self.play(
            ApplyMethod(coupled_odes_v2.shift, 2*UP),
            run_time = 1
        )
        brace_v2.remove_updater(move_system)
        
        self.wait()
        
        self.play(
            Write(recast),
            Write(x_vector),
            Write(f_vector),
            run_time = 2
        )
        
        self.play(
            FadeOut(brace_v2),
            FadeOut(coupled_odes_v2),
            run_time = 2
        )               
        
        self.play(
            ApplyMethod(recasting.shift, 4*UP),
            run_time = 1
        )
        
        self.play(
            Write(becomes),
            Write(parameter_space),
            Write(parameter_space_constraints),
            run_time = 2
        )
        
        self.wait(4)
        
        
        
class Butterfly(ThreeDScene):
    CONFIG = {
        'x_min' : -100,
        'x_max' : 100,
        
        'y_min' : -100,
        'y_max' : 100,
        
        'z_min' : -100,
        'z_max' : 100,
        
        'exclude_zero_label' : True,
        
        'axes_color': WHITE,
        
        'stroke_width' : 0.02
    }
        
    def construct(self):
    
        axes = ThreeDAxes()
        
        x_coords = 0.15*states[:, 0]
        y_coords = 0.15*states[:, 1]
        z_coords = 0.15*states[:, 2] - 3.6
        
        def coord(x,y,z):
            return np.array([x,y,z])
        
        self.tuples = list(zip(x_coords,y_coords,z_coords))
        
        path = VMobject()
        path.set_points_smoothly([*[coord(x,y,z) for x,y,z in self.tuples]])
        
        # self.add(axes)
        self.set_camera_orientation(phi=PI/2, theta=PI, distance = 30)        
        self.begin_ambient_camera_rotation(rate=0.2)
        self.play(ShowCreation(path), run_time=20)
        self.wait(2)