import numpy as np
import matplotlib.pyplot as plt

G, M, m = 10**-10, 10**7, 10  # Sun and Earth mass
vx_0, vy_0 = 5, 5  # Initial velocities (set vy_0 to a non-zero value for a circular orbit)
x_0, y_0 = 50, 50  # Initial position


# r = lambda x,y: np.sqrt(x**2 + y**2)
# vxprime = lambda x,y: -(G * M * m / r(x,y)**3) * x
# vyprime = lambda x,y: -(G * M * m / r(x,y)**3) * y

def ode_func(x, y, vx, vy):
    r = np.sqrt(x**2 + y**2)
    vxprime = -(G * M * m / r**3) * x
    vyprime = -(G * M * m / r**3) * y
    x_prime = vx
    y_prime = vy
    return np.array([vx, vy, x_prime, y_prime])

def euler(timestop):
    x_values = []
    y_values = []
    X = np.array([vx_0, vy_0, x_0, y_0])
    dt = 1
    n = round(timestop / dt)
    x_values.append(X[2])
    y_values.append(X[3])
    for i in range(n):
        X = X + dt * ode_func(X[2], X[3], X[0], X[1])
        x_values.append(X[2])
        y_values.append(X[3])
    return x_values, y_values

def plot_orbit(x_values, y_values):
    fig, ax = plt.subplots()
    plt.scatter([x_0], [y_0], color="green", marker="o", label="Initial point")
    plt.scatter([0], [0], color="red", marker="o", label="Sun")
    ax.plot(x_values, y_values, '.-', label='Position')
    for i in range(len(x_values) - 1):
        ax.annotate('', xy=(x_values[i + 1], y_values[i + 1]), xytext=(x_values[i], y_values[i]),
                    arrowprops=dict(arrowstyle='->', lw=1))
    ax.legend()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Orbit of Earth around Sun')
    plt.grid(True)
    plt.show()

x_values, y_values = euler(20)
plot_orbit(x_values, y_values)
