import numpy as np, matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# from numerical_ode import rk4
from scipy.integrate import odeint

# Define constants
sigma = 10; beta = (8/3); rho = 28

# Initial conditions
x_init = -5.27; y_init = -5.06; z_init = 23.559
initial_state = np.array([x_init, y_init, z_init])

# Create array of time values to study
t_init = 0; t_fin = 80; h = 0.01
t = np.arange(t_init, t_fin, h)

# Governing system of differential equations
def f(state, t):
    x, y, z = state
    return np.array([sigma*(y - x), x*(rho - z) - y, x*y - beta*z])

states = odeint(f, initial_state, t)

# np.savetxt('butterfly.csv', states, delimiter = ',')

fig = plt.figure()
ax = Axes3D(fig)
ax.plot(states[:, 0], states[:, 1], states[:, 2])
plt.show()