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
x_init_1 = 0.1; y_init_1 = 0.1; z_init_1 = 0.1
x_init_2 = 0.2; y_init_2 = 0.2; z_init_2 = 0.0
x_init_3 = -5.27; y_init_3 = -5.06; z_init_3 = 23.56
x_init_4 = -5.28; y_init_4 = -5.07; z_init_4 = 23.57
x_init_5 = -5.26; y_init_5 = -5.05; z_init_5 = 23.55
initial_state_1 = np.array([x_init_1, y_init_1, z_init_1])
initial_state_2 = np.array([x_init_2, y_init_2, z_init_2])
initial_state_3 = np.array([x_init_3, y_init_3, z_init_3])
initial_state_4 = np.array([x_init_4, y_init_4, z_init_4])
initial_state_5 = np.array([x_init_5, y_init_5, z_init_5])

# Create array of time values to study
t_init = 0; t_fin = 60; h = 0.02
t = np.arange(t_init, t_fin, h)

# Governing system of differential equations
def f(state, t):
    x, y, z = state
    return np.array([sigma*(y - x), x*(rho - z) - y, x*y - beta*z])

states_1 = odeint(f, initial_state_1, t)
states_2 = odeint(f, initial_state_2, t)
states_3 = odeint(f, initial_state_3, t)
states_4 = odeint(f, initial_state_4, t)
states_5 = odeint(f, initial_state_5, t)
        
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
            '\\sigma' : TEAL
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
            '\\rho' : GOLD
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
            '=',
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
            '\\beta' : MAROON
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
        
        lorenz_used = TextMobject('Lorenz used the values ', '$\\sigma = 10$', ', ', '$\\rho = 28$', ', ', 'and ', '$\\beta = {8 \\over 3}$', '.')
        lorenz_used[1].set_color(TEAL)
        lorenz_used[3].set_color(GOLD)
        lorenz_used[6].set_color(MAROON)
        lorenz_used.move_to(2.99*DOWN)
        
        x_vector_colorful = TexMobject(r'\begin{pmatrix} \dot{x} \\ \dot{y} \\ \dot{z} \end{pmatrix}')
        x_vector_colorful[0][2].set_color(BLUE)
        x_vector_colorful[0][3].set_color(BLUE)
        x_vector_colorful[0][4].set_color(GREEN)
        x_vector_colorful[0][5].set_color(GREEN)
        x_vector_colorful[0][6].set_color(RED)
        x_vector_colorful[0][7].set_color(RED)
        x_vector_colorful.move_to(2.5*UP + 2.5*LEFT)
        
        brace_on_x = Brace(x_vector_colorful, DOWN)
        brace_on_x_text = brace_on_x.get_text("$\\mathbf{\\dot{x}}$").set_color("#6F0EED")
        
        x_stuff = VGroup(x_vector_colorful, brace_on_x, brace_on_x_text)
        
        equals = TexMobject(r'=').scale(1.6)
        equals.next_to(x_vector_colorful, buff = LARGE_BUFF)
        
        zero_vector = TexMobject(r'\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}')
        zero_vector[0][2].set_color(BLUE)
        zero_vector[0][3].set_color(GREEN)
        zero_vector[0][4].set_color(RED)
        zero_vector.move_to(2.5*UP + 2.1*RIGHT)
        
        brace_on_zero = Brace(zero_vector, DOWN)
        brace_on_zero_text = brace_on_zero.get_text('$0$').set_color("#6F0EED")
        
        zero_stuff = VGroup(zero_vector, brace_on_zero, brace_on_zero_text)
        
        f_vector_colorful = TexMobject(r'\begin{pmatrix} \sigma (y - x) \\ \rho x - y - xz \\ xy - \beta z \end{pmatrix}')
        f_vector_colorful[0][2].set_color(TEAL)
        f_vector_colorful[0][4].set_color(GREEN)
        f_vector_colorful[0][6].set_color(BLUE)
        f_vector_colorful[0][8].set_color(GOLD)
        f_vector_colorful[0][9].set_color(BLUE)
        f_vector_colorful[0][11].set_color(GREEN)
        f_vector_colorful[0][13].set_color(BLUE)
        f_vector_colorful[0][14].set_color(RED)
        f_vector_colorful[0][15].set_color(BLUE)
        f_vector_colorful[0][16].set_color(GREEN)
        f_vector_colorful[0][18].set_color(MAROON)
        f_vector_colorful[0][19].set_color(RED)
        f_vector_colorful.next_to(equals, buff = LARGE_BUFF)
        
        brace_on_f = Brace(f_vector_colorful, DOWN)
        brace_on_f_text = brace_on_f.get_text('$\\mathbf{f}$').set_color("#6F0EED")
        
        f_stuff = VGroup(f_vector_colorful, brace_on_f, brace_on_f_text)
        
        satisfy = TextMobject('Fixed points of the Lorenz system satisfy ', '$\\mathbf{f} = 0$', '.')
        satisfy[1].set_color("#6F0EED")
        
        there_exists = TextMobject('There exists the ', '$\\mathbb{TRIVIAL}$', ' solution at ', '$(0, 0, 0)$', ', and \\\\ two more fixed points at ', '$\\left(\\pm \\sqrt{\\beta (\\rho - 1)},\\  \\pm \\sqrt{\\beta (\\rho - 1)},\\  \\rho - 1 \\right)$', '.')
        there_exists[3].set_color(ORANGE)
        there_exists[5].set_color(ORANGE)
        there_exists.next_to(satisfy, DOWN, buff = LARGE_BUFF)
        there_exists.set_width(0.8*FRAME_WIDTH)
        
        final_text = TextMobject(
            'Now observe the evolution of some trajectories. \\\\ ',
            'Note the sensitivity to initial conditions.'
        )
        # final_text.set_width(0.8*FRAME_WIDTH)
        
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
        
        self.wait(2)
        
        self.play(
            Write(lorenz_used),
            run_time = 2
        )
        
        self.wait(2)
        
        self.play(
            FadeOut(recast),
            FadeOut(x_vector),
            FadeOut(f_vector),
            FadeOut(becomes),
            FadeOut(parameter_space),
            FadeOut(parameter_space_constraints),
            FadeOut(lorenz_used),
            run_time = 2
        )
        
        self.play(
            Write(x_vector_colorful),
            Write(equals),
            Write(f_vector_colorful),
            run_time = 1.6
        )
        
        self.wait()
        
        self.play(
            Write(brace_on_x),
            Write(brace_on_x_text),
            Write(brace_on_f),
            Write(brace_on_f_text),
            run_time = 1
        )
        
        self.wait(2)
        
        self.play(
            Write(satisfy),
            run_time = 2
        )
        
        self.wait()
        
        self.play(
            ReplacementTransform(x_stuff, zero_stuff),
            ApplyMethod(f_stuff.shift, 3.2*LEFT),
            ApplyMethod(equals.shift, 1.8*RIGHT),
            # ApplyMethod(zero_vector.shift, 3.8*RIGHT),
            run_time = 1.4
        )
        
        self.wait()
        
        self.play(
            Write(there_exists),
            run_time = 3
        )
        
        self.wait(4)
        
        self.play(
            FadeOut(zero_stuff),
            FadeOut(equals),
            FadeOut(f_stuff),
            FadeOut(satisfy),
            FadeOut(there_exists),
            run_time = 2
        )
        
        self.wait()
        
        self.play(
            FadeIn(final_text),
            run_time = 2
        )
        
        self.wait(3)
        
        self.play(
            FadeOut(final_text),
            run_time = 1
        )
        
        
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
        
        x_coords = 0.149*states[:, 0]
        y_coords = 0.149*states[:, 1]
        z_coords = 0.149*states[:, 2] - 3.6
        
        def coord(x,y,z):
            return np.array([x,y,z])
        
        self.tuples = list(zip(x_coords,y_coords,z_coords))
        
        trajectory = VMobject()
        trajectory.set_points_smoothly([*[coord(x,y,z) for x,y,z in self.tuples]])
        
        # self.add(axes)
        self.set_camera_orientation(phi=PI/2, theta=PI, distance = 30)
        self.begin_ambient_camera_rotation(rate=PI/36)
        self.play(ShowCreation(trajectory), run_time=20)
        self.stop_ambient_camera_rotation()
        self.wait(4)
        self.play(
            FadeOut(trajectory),
            run_time = 2
        )
        
class TwoButterflies(ThreeDScene):
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
        
        orange_label = TextMobject("fixed points").scale(0.5)
        orange_label.set_color(ORANGE)

        # self.add_fixed_in_frame_mobjects(orange_label)
        orange_label.to_corner(DL)
        
        sphere = ParametricSurface(
            lambda u, v : np.array([
                0.1*np.cos(u)*np.cos(v),
                0.1*np.cos(u)*np.sin(v),
                0.1*np.sin(u)
            ]), v_min = 0, v_max = TAU, u_min = -PI/2, u_max = PI/2, checkerboard_colors=[ORANGE, ORANGE], resolution = (2,2)
        ).scale(0.5)
        
        origin = sphere.copy()
        origin.move_to(np.array([0, 0, -3.65]))        
        q_negative = sphere.copy()
        q_negative.move_to(np.array([-0.15*np.sqrt(beta*(rho - 1)), -0.15*np.sqrt(beta*(rho - 1)), 0.15*(rho - 1) - 3.65]))
        q_positive = sphere.copy()
        q_positive.move_to(np.array([0.15*np.sqrt(beta*(rho - 1)), 0.15*np.sqrt(beta*(rho - 1)), 0.15*(rho - 1) - 3.65]))
        
        x_coords_1 = 0.148*states_1[:, 0]
        y_coords_1 = 0.148*states_1[:, 1]
        z_coords_1 = 0.148*states_1[:, 2] - 3.65
        
        x_coords_2 = 0.148*states_2[:, 0]
        y_coords_2 = 0.148*states_2[:, 1]
        z_coords_2 = 0.148*states_2[:, 2] - 3.65
        
        def coord(x,y,z):
            return np.array([x,y,z])
        
        self.tuples_1 = list(zip(x_coords_1, y_coords_1, z_coords_1))
        self.tuples_2 = list(zip(x_coords_2, y_coords_2, z_coords_2))
        
        trajectory_1 = VMobject()
        trajectory_1.set_color(RED)
        trajectory_1.set_points_smoothly([*[coord(x,y,z) for x,y,z in self.tuples_1]])
        
        trajectory_2 = VMobject()
        trajectory_2.set_color(BLUE)
        trajectory_2.set_points_smoothly([*[coord(x,y,z) for x,y,z in self.tuples_2]])
        
        # self.add(axes)
        self.set_camera_orientation(phi=PI/2, theta=25*PI/16, distance = 30)        
        self.play(ShowCreation(trajectory_1), ShowCreation(trajectory_2), run_time=50)
        self.wait(2)
        
        self.play(            
            FadeIn(origin),
            FadeIn(q_negative),
            FadeIn(q_positive),
            run_time = 1
        )
        
        self.add_fixed_in_frame_mobjects(orange_label)
        
        self.wait(2)
        
        self.play(
            FadeOut(origin),
            FadeOut(q_negative),
            FadeOut(q_positive),
            FadeOut(orange_label),
            run_time = 1
        )
        
        self.wait()
        self.begin_ambient_camera_rotation(rate = 2*PI/40)
        self.wait(40)
        self.stop_ambient_camera_rotation()
        self.wait(2.5)
        
        self.play(
            FadeOut(trajectory_1),
            FadeOut(trajectory_2),
            run_time = 3
        )
        
class ThreeButterflies(ThreeDScene):
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
        
        x_coords_3 = 0.148*states_3[:, 0]
        y_coords_3 = 0.148*states_3[:, 1]
        z_coords_3 = 0.148*states_3[:, 2] - 3.65
        
        x_coords_4 = 0.148*states_4[:, 0]
        y_coords_4 = 0.148*states_4[:, 1]
        z_coords_4 = 0.148*states_4[:, 2] - 3.65
        
        x_coords_5 = 0.148*states_5[:, 0]
        y_coords_5 = 0.148*states_5[:, 1]
        z_coords_5 = 0.148*states_5[:, 2] - 3.65
        
        def coord(x,y,z):
            return np.array([x,y,z])
        
        self.tuples_3 = list(zip(x_coords_3, y_coords_3, z_coords_3))
        self.tuples_4 = list(zip(x_coords_4, y_coords_4, z_coords_4))
        self.tuples_5 = list(zip(x_coords_5, y_coords_5, z_coords_5))
        
        trajectory_3 = VMobject()
        trajectory_3.set_color(RED)
        trajectory_3.set_points_smoothly([*[coord(x,y,z) for x,y,z in self.tuples_3]])
        
        trajectory_4 = VMobject()
        trajectory_4.set_color(GREEN)
        trajectory_4.set_points_smoothly([*[coord(x,y,z) for x,y,z in self.tuples_4]])
        
        trajectory_5 = VMobject()
        trajectory_5.set_color(BLUE)
        trajectory_5.set_points_smoothly([*[coord(x,y,z) for x,y,z in self.tuples_5]])
        
        # self.add(axes)
        self.set_camera_orientation(phi=PI/2, theta=25*PI/16, distance = 30)        
        self.play(ShowCreation(trajectory_3), ShowCreation(trajectory_4), ShowCreation(trajectory_5), run_time=60)
        self.wait(2)
        
        self.begin_ambient_camera_rotation(rate = 2*PI/40)
        self.wait(40)
        self.stop_ambient_camera_rotation()
        self.wait(2.5)
        
        self.play(
            FadeOut(trajectory_3),
            FadeOut(trajectory_4),
            FadeOut(trajectory_5),
            run_time = 3
        )
        
class Farfalle(ThreeDScene):
    CONFIG = {
        'x_min' : -100,
        'x_max' : 100,
        
        'y_min' : -100,
        'y_max' : 100,
        
        'z_min' : -100,
        'z_max' : 100
    }
    
    def construct(self):
        
        axes = ThreeDAxes()
        
        x_coords_6 = 0.148*states_4[:, 0]
        y_coords_6 = 0.148*states_4[:, 1]
        z_coords_6 = 0.148*states_4[:, 2] - 3.65
        
        def coord(x,y,z):
            return np.array([x,y,z])
                
        self.tuples_6 = list(zip(x_coords_6, y_coords_6, z_coords_6))
        
        trajectory_6 = VMobject()
        trajectory_6.set_color(color=[RED, BLUE, WHITE])
        trajectory_6.set_points_smoothly([*[coord(x,y,z) for x,y,z in self.tuples_6]])
        
        # self.add(axes)
        self.set_camera_orientation(phi=PI/2, theta=25*PI/16, distance = 30)        
        self.play(ShowCreation(trajectory_6), run_time=10)
        self.wait(2)