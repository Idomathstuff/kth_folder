import numpy as np
import matplotlib.pyplot as plt
G = 6.67430e-11  # gravitations konstant 
M = 1.989e30    # mass of sun kg
m = 5.97e24 # mass of earth
AU = 1.496e11 # astronomical unit
x_0 = 1.496e11 # orbital radius m
y_0 = 0
vx_0 = 0
vy_0 = 2.978e4 # orbit velocity m/s
time_step = 60*60*24


plt.style.use('seaborn-darkgrid')

def ode_func(X):
    x,y,vx,vy = X
    r = np.sqrt(x**2+y**2)
    vx_prime = -x*G*M/r**3
    vy_prime = -y*G*M/r**3
    x_prime = vx
    y_prime = vy
    return np.array([x_prime,y_prime,vx_prime,vy_prime])

def simp_euler(X0):
    X = X0
    x_values = []
    y_values = []
    vx_values = []
    vy_values = []
    n = 365*int(60*60*24/time_step) # days in a year
    for i in range(n):
        x_values.append(X[0])
        y_values.append(X[1])
        vx_values.append(X[2])
        vy_values.append(X[3])
        x_prime,y_prime,vx_prime,vy_prime = ode_func(X)
        X[2] += vx_prime*time_step
        X[3] += vy_prime*time_step
        X[0] += X[2]*time_step
        X[1] += X[3]*time_step
    return [vx_values,vy_values,x_values,y_values]

def forward_euler(X0):
    X = X0
    x_values = []
    y_values = []
    vx_values = []
    vy_values = []
    n = 365*int(60*60*24/time_step) # days in a year
    for i in range(n):
        x_values.append(X[0])
        y_values.append(X[1])
        vx_values.append(X[2])
        vy_values.append(X[3])
        X += time_step*ode_func(X )
    return [vx_values,vy_values,x_values,y_values]

def RK4_euler(X0):
    X = X0
    vx_values,vy_values = [], []
    x_values, y_values = [], []
    for _ in range(365):
        x_values.append(X[0])
        y_values.append(X[1])
        vx_values.append(X[2])
        vy_values.append(X[3])
        k1 = time_step * ode_func(X)
        k2 = time_step * ode_func(X + k1 / 2)
        k3 = time_step * ode_func(X + k2 / 2)
        k4 = time_step * ode_func(X + k3)
        X += (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return [vx_values,vy_values,x_values,y_values]


def plot_orbit(axes, x_values, y_values, X0):
    x_0,y_0,vx_0,vy_0 = X0
    axes.scatter([x_0], [y_0], color="green", marker="o", label="Initial point")
    axes.scatter([0], [0], color="red", marker="o", label="Sun")
    axes.plot(x_values, y_values, '.-', label='Position')
    axes.set_xlabel('x (meters)')
    axes.set_ylabel('y (meters)')

    def format_scientific(num):
        return f"{num:.1e}"
    title = axes.set_title(f'Initial x, y, x velocity, y velocity: [{format_scientific(x_0)}, {format_scientific(y_0)}, {format_scientific(vx_0)}, {format_scientific(vy_0)}]')
    title.set_position([0.5, 1.30]) 
    plt.grid(True)



def plot_different_inital_values():
    x_0 = 1*AU
    y_0 = 0
    vx_0 = 0
    vy_0 = 2.978e4 # orbit velocity /s

    fig, axes = plt.subplots(3, 1   , figsize=(8, 8))

    fig.suptitle("Different initial values (simplectic)")
    plt.subplots_adjust(hspace=0.5, wspace=0.5)
    X0 = [x_0,y_0,vx_0,vy_0]
    vx_values,vy_values,x_values,y_values = simp_euler([x_0,y_0,vx_0,vy_0])
    plot_orbit(axes[0], x_values,y_values,X0)
    X0 = [x_0,y_0,vx_0,vy_0+1e4]
    vx_values,vy_values,x_values,y_values = simp_euler([x_0,y_0,vx_0,vy_0+1e4])
    plot_orbit(axes[1],x_values,y_values,X0)
    X0 = [x_0,y_0,vx_0,vy_0-2e4]
    vx_values,vy_values,x_values,y_values = simp_euler([x_0,y_0,vx_0,vy_0-2e4])
    plot_orbit(axes[2], x_values,y_values,X0)

    plt.show()


def plot_energy(axes, vx_values, vy_values, x_values, y_values):
    def energy(x, y, vx, vy):
        r = np.sqrt(x**2+y**2)
        T = m*(vx**2 + vy**2)/2
        U = -G*M*m / r
        return T + U
    energy_vals = []
    for i in range(len(x_values)):
        energi = energy(x_values[i],y_values[i],vx_values[i],vy_values[i])
        energy_vals.append(energi)
    time = list(range(len(x_values)))
    axes.scatter(time,energy_vals, s=1, color = "orange", facecolor='black')
    axes.set_title("Total energi över tiden")
    axes.set_xlabel('t  (dagar)')
    axes.set_ylabel('E(t)  (Joules)')
    plt.grid(True)


def plot_different_energy():
    
    x_0 = 1*AU # orbital radius m
    y_0 = 0
    vx_0 = 0
    vy_0 = 2.978e4 #-1e4 # orbit velocity m/s

    fig, axes = plt.subplots(2, 2   , figsize=(8, 8))

    fig.suptitle("Different initial values (simplectic)")
    plt.subplots_adjust(hspace=0.5, wspace=0.5)


    X0 = [x_0,y_0,vx_0,vy_0+1e4]
    vx_values,vy_values,x_values,y_values = RK4_euler([x_0,y_0,vx_0,vy_0+1e4])
    plot_orbit(axes[0,0],x_values,y_values,X0)
    plot_energy(axes[0,1], vx_values,vy_values,x_values,y_values)


    X0 = [x_0,y_0,vx_0,vy_0-2e4]
    vx_values,vy_values,x_values,y_values = RK4_euler([x_0,y_0,vx_0,vy_0-2e4])
    plot_orbit(axes[1,0],x_values,y_values,X0)
    plot_energy(axes[1,1], vx_values,vy_values,x_values,y_values)

    
    plt.show()

plot_different_energy()
# plot_different_inital_values()