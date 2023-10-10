import numpy as np
import matplotlib.pyplot as plt

# r = lambda x,y: np.sqrt(x**2 + y**2)
# G = 0.001  # Gravitationskonstanten (m^3 kg^-1 s^-2)
# M = 1000    # Massan av solen (kg)
# m = 0.0001
x_0 = 100   # 1 AU i meter
y_0 = 0
vx_0 = -0.1
vy_0 = -0.01


# vxprime = lambda x,y: -(G * M * m / r(x,y)**3) * x
# vyprime = lambda x,y: -(G * M * m / r(x,y)**3) * y

# def ode_func(x, y, vx, vy):
#     r = np.sqrt(x**2 + y**2)
#     vxprime = -(G * M * m / r**3) * x
#     vyprime = -(G * M * m / r**3) * y
#     x_prime = vx
#     y_prime = vy
#     return np.array([vx, vy, vyprime, vxprime])

def ode_func(x, y, vx, vy):
    r = np.sqrt(x**2 + y**2)
    vxprime = -(x/ r**3)
    vyprime = -(y/ r**3)
    x_prime = vx
    y_prime = vy
    return np.array([x_prime, y_prime, vyprime, vxprime])

def euler(timestop):

    X = np.array([x_0, y_0, vx_0, vy_0])
    dt = 1
    n = round(timestop / dt)
    x_values=[X[0]]
    y_values=[X[1]]
    for i in range(n):
        print(i)
        X = X - dt * ode_func(X[0], X[1], X[2], X[3])
        x_values.append(X[0])
        y_values.append(X[1])
    return x_values, y_values

def plot_orbit(x_values, y_values):
    fig, ax = plt.subplots()
    plt.scatter([x_0], [y_0], color="green", marker="o", label="Initial point")
    plt.scatter([0], [0], color="red", marker="o", label="Sun")
    ax.plot(x_values, y_values, '.-', label='Position')
    # for i in range(len(x_values) - 1):
    #     ax.annotate('', xy=(x_values[i + 1], y_values[i + 1]), xytext=(x_values[i], y_values[i]),
    #                 arrowprops=dict(arrowstyle='->', lw=1))
    ax.legend()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Orbit of Earth around Sun')
    plt.grid(True)
    plt.show()

x_values, y_values = euler(200)
plot_orbit(x_values, y_values)
