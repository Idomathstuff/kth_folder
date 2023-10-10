import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the system of differential equations
def system(Y, t=0):
    x, y, vx, vy = Y
    dxdt = vx
    dydt = vy
    r = np.sqrt(x**2 + y**2)
    dvxdt = -x / r**3
    dvydt = -y / r**3
    return [dxdt, dydt, dvxdt, dvydt]

# Time array for simulation
t = np.linspace(0, 20*np.pi, 5000)  # Extended time period

# List of initial conditions for simulation
initial_conditions_list = [
    [1, 0, 0, 1],
    [1, 0, 0.5, 1.5],
    [0.5, 0.5, 0, 1]
]

plt.figure(figsize=(10, len(initial_conditions_list)*5))

for idx, initial_conditions in enumerate(initial_conditions_list, 1):
    # Solve the system of differential equations
    solution = odeint(system, initial_conditions, t)
    x, y = solution[:, 0], solution[:, 1]
    
    plt.subplot(len(initial_conditions_list), 2, 2*idx-1)
    plt.plot(t, x, label='x(t)')
    plt.plot(t, y, label='y(t)')
    plt.legend()
    plt.title(f'x(t) and y(t) vs. time for initial conditions {initial_conditions}')
    
    plt.subplot(len(initial_conditions_list), 2, 2*idx)
    plt.plot(x, y)
    plt.title(f'Orbit in x-y plane for initial conditions {initial_conditions}')
    plt.xlabel('x')
    plt.ylabel('y')

plt.tight_layout()
plt.show()