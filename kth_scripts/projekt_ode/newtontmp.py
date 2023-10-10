import numpy as np
import matplotlib.pyplot as plt
G = 6.67430e-11  # Gravitationskonstanten (m^3 kg^-1 s^-2)
M = 1.989e30    # Massan av solen (kg)
m = 1
x_0 = 1.496e11    # 1 AU i meter
y_0 = 0
vx_0 = 0
vy_0 = 2.978e4    # Jordens genomsnittliga orbitalhastighet (m/s)

P = np.array([x_0,y_0]) # initial position
V = np.array([vx_0,vy_0]) #initial velocity
time_step = 60 * 60 * 24  # Time step in seconds (1 day)

# r = lambda x,y: np.sqrt(x**2 + y**2)
# vxprime = lambda x,y: -(G * M * m / r(x,y)**3) * x
# vyprime = lambda x,y: -(G * M * m / r(x,y)**3) * y

positions_x = []
positions_y = []

def calc_acceleration(position):
    r = np.linalg.norm(position)
    return (G * M / r**2) * (-position / r)

n = 365
for i in range(n):
    positions_x.append(P[0])
    positions_y.append(P[1])
    accleration = calc_acceleration(P)
    V += accleration * time_step
    P += V*time_step

plt.plot(positions_x,positions_y)
plt.scatter(0, 0, c='yellow', s=1000, label='Sun')  # Sun
plt.scatter(positions_x[0], positions_y[0], c='blue', s=100, label='Earth (Start)')  # Earth (Start)
plt.scatter(positions_x[-1], positions_y[-1], c='red', s=100, label='Earth (End)')  # Earth (End)
plt.title('Earth Orbiting the Sun')
plt.xlabel('X Position (meters)')
plt.ylabel('Y Position (meters)')
# plt.legend()
plt.axis('equal')
plt.show()


# def ode_func(X):
#     x, y, vx, vy = X[0],X[1],X[2],X[3]
#     r = np.sqrt(x**2 + y**2)
#     vxprime = -(G * M * m / r**3) * x
#     vyprime = -(G * M * m / r**3) * y
#     x_prime = vx
#     y_prime = vy
#     return np.array([vx, vy, vyprime, vxprime])

# def euler(timestop):
#     X = np.array([x_0, y_0, vx_0, vy_0])
#     dt = time_step
#     n = int(timestop * 60 * 60 * 24 / dt)
#     x_values=[X[0]]
#     y_values=[X[1]]
#     for i in range(n):
#         X += time_step * ode_func(X)
#         x_values.append(X[0])
#         y_values.append(X[1])
#     return x_values, y_values

# def plot_orbit(x_values, y_values):
#     fig, ax = plt.subplots()
#     plt.scatter([x_0], [y_0], color="green", marker="o", label="Initial point")
#     plt.scatter([0], [0], color="red", marker="o", label="Sun")
#     ax.plot(x_values, y_values, '.-', label='Position')
#     # for i in range(len(x_values) - 1):
#     #     ax.annotate('', xy=(x_values[i + 1], y_values[i + 1]), xytext=(x_values[i], y_values[i]),
#     #                 arrowprops=dict(arrowstyle='->', lw=1))
#     ax.legend()
#     ax.set_xlabel('X')
#     ax.set_ylabel('Y')
#     ax.set_title('Orbit of Earth around Sun')
#     plt.grid(True)
#     plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# G = 6.67430e-11  # Gravitationskonstanten (m^3 kg^-1 s^-2)
# M = 1.989e30    # Massan av solen (kg)
# m = 1
# x_0 = 1.496e11    # 1 AU i meter
# y_0 = 0
# vx_0 = 0
# vy_0 = 29.78e3    # Jordens genomsnittliga orbitalhastighet (m/s)


# # r = lambda x,y: np.sqrt(x**2 + y**2)
# # vxprime = lambda x,y: -(G * M * m / r(x,y)**3) * x
# # vyprime = lambda x,y: -(G * M * m / r(x,y)**3) * y

# def ode_func(x, y, vx, vy):
#     r = np.sqrt(x**2 + y**2)
#     vxprime = -(G * M * m / r**3) * x
#     vyprime = -(G * M * m / r**3) * y
#     x_prime = vx
#     y_prime = vy
#     return np.array([vx, vy, vyprime, vxprime])

# def euler(timestop):

#     X = np.array([x_0, y_0, vx_0, vy_0])
#     dt = 1
#     n = round(timestop / dt)
#     x_values=[X[0]]
#     y_values=[X[1]]
#     for i in range(n):
#         print(i)
#         X = X - dt * ode_func(X[0], X[1], X[2], X[3])
#         x_values.append(X[0])
#         y_values.append(X[1])
#     return x_values, y_values

# def plot_orbit(x_values, y_values):
#     fig, ax = plt.subplots()
#     plt.scatter([x_0], [y_0], color="green", marker="o", label="Initial point")
#     plt.scatter([0], [0], color="red", marker="o", label="Sun")
#     ax.plot(x_values, y_values, '.-', label='Position')
#     # for i in range(len(x_values) - 1):
#     #     ax.annotate('', xy=(x_values[i + 1], y_values[i + 1]), xytext=(x_values[i], y_values[i]),
#     #                 arrowprops=dict(arrowstyle='->', lw=1))
#     ax.legend()
#     ax.set_xlabel('X')
#     ax.set_ylabel('Y')
#     ax.set_title('Orbit of Earth around Sun')
#     plt.grid(True)
#     plt.show()

# x_values, y_values = euler(50000)
# plot_orbit(x_values, y_values)
