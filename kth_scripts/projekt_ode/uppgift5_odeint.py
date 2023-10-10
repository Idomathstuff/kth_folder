import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

G = 6.67430e-11  # Gravitationskonstanten (m^3 kg^-1 s^-2)
M = 1.989e30    # mass of sun kg
m = 5.97e24      # mass of earth
x_0 = 1.496e11   # orbital radius m
y_0 = 0
vx_0 = 0
vy_0 = 2.978e4   # orbit velocity m/s

def ode_system(X, t):
    x, y, vx, vy = X
    r = np.sqrt(x**2 + y**2)
    vx_prime = -x * G * M / r**3
    vy_prime = -y * G * M / r**3
    x_prime = vx
    y_prime = vy
    return [x_prime, y_prime, vx_prime, vy_prime]

X0 = [x_0, y_0, vx_0, vy_0]
t = np.linspace(0, 365 * 24 * 60 * 60, 366)  # 1 year in seconds

def ODE_solve(X0):
    sol = odeint(ode_system, X0, t)
    x_values = sol[:, 0]
    y_values = sol[:, 1]
    vx_values = sol[:, 2]
    vy_values = sol[:, 3]
    return [vx_values,vy_values,x_values,y_values]

def plot_orbit(x_values, y_values, X0):
    x_0,y_0,vx_0,vy_0 = X0
    fig, ax = plt.subplots(figsize=(9,6))
    plt.scatter([x_0], [y_0], color="green", marker="o", label="Initial point")
    plt.scatter([0], [0], color="red", marker="o", label="Sun")
    ax.plot(x_values, y_values, '.', label='Position')
    
    def add_arrows():
        skip_val = 10
        for i in range(len(x_values)-skip_val):
            if i%skip_val!=0:
                continue
            ax.annotate('', xy=(x_values[skip_val+i], y_values[skip_val+i]), xytext=(x_values[i], y_values[i]), arrowprops=dict(arrowstyle='->', lw=2))
    # add_arrows()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    def format_scientific(num):
        return f"{num:.1e}"
    title = ax.set_title(f'     Initial x, y, x velocity, y velocity: [{format_scientific(x_0)}, {format_scientific(y_0)}, {format_scientific(vx_0)}, {format_scientific(vy_0)}]')
    title.set_position([0.5, 1.30]) 
    plt.grid(True)

def plot_different_inital_values():
    x_0 = 1.496e11 # orbital radius m
    y_0 = 0
    vx_0 = 0
    vy_0 = 2.978e4 # orbit velocity m/s

    X0 = [x_0,y_0,vx_0,vy_0]
    vx_values,vy_values,x_values,y_values = ODE_solve(X0)
    plot_orbit(x_values,y_values,X0)

    X0 = [x_0,y_0,vx_0,vy_0+1e4]
    vx_values,vy_values,x_values,y_values = ODE_solve(X0)
    plot_orbit(x_values,y_values,X0)

    X0 = [x_0,y_0,vx_0,vy_0-2e4]
    vx_values,vy_values,x_values,y_values = ODE_solve(X0)
    plot_orbit(x_values,y_values,X0)

    plt.show()

def plot_energy():
    def energy(x, y, vx, vy):
        r = np.sqrt(x**2+y**2)
        T = 0.5 * m*(vx**2 + vy**2)
        U = -G*M*m / r
        return T + U
    energy_vals = []
    vx_values,vy_values,x_values,y_values = ODE_solve(X0)
    for i in range(len(x_values)):
        energi = energy(x_values[i],y_values[i],vx_values[i],vy_values[i])
        energy_vals.append(energi)
    time = list(range(len(x_values)))
    fig, ax = plt.subplots(figsize=(9,6))
    plt.plot(time,energy_vals)
    ax.set_title("Total energi över tiden")
    ax.set_xlabel('t  (dagar)')
    ax.set_ylabel('E(t)  (Joules)')
    plt.show()

# plot_different_inital_values()
plot_energy()