import numpy as np
import matplotlib.pyplot as plt

G = 6.67430e-11  # Gravitational constant
M = 1.989e30    # Mass of the Sun in kg
m_j = 1.898e27   # Mass of Jupiter in kg
m_e = 5.97e24    # Mass of Earth in kg
AU = 1.496e11    # Astronomical unit in meters

X0_e = [AU, 0, 0, 2.978e4]   # Initial conditions for Earth [x, y, vx, vy]
X0_j = [5*AU, 0, 0, 1.307e4]  # Initial conditions for Jupiter [x, y, vx, vy]

def ode_func(X_e, X_j):
    x_e, y_e, vx_e, vy_e = X_e
    x_j, y_j, vx_j, vy_j = X_j
    
    r_e = np.sqrt(x_e**2 + y_e**2)
    r_j = np.sqrt(x_j**2 + y_j**2)
    r_ej = np.sqrt((x_j - x_e)**2 + (y_j - y_e)**2)
    
    ax_e = (-G * M * x_e / r_e**3) + (-G * m_j * (x_e - x_j) / r_ej**3)
    ay_e = (-G * M * y_e / r_e**3) + (-G * m_j * (y_e - y_j) / r_ej**3)
    
    ax_j = (-G * M * x_j / r_j**3) + (-G * m_e * (x_j - x_e) / r_ej**3)
    ay_j = (-G * M * y_j / r_j**3) + (-G * m_e * (y_j - y_e) / r_ej**3)
    
    x_e_prime = vx_e
    y_e_prime = vy_e
    vx_e_prime = ax_e
    vy_e_prime = ay_e
    
    x_j_prime = vx_j
    y_j_prime = vy_j
    vx_j_prime = ax_j
    vy_j_prime = ay_j
    
    X_e_derivs = [x_e_prime, y_e_prime, vx_e_prime, vy_e_prime]
    X_j_derivs = [x_j_prime, y_j_prime, vx_j_prime, vy_j_prime]
    
    return X_e_derivs, X_j_derivs

def euler(X0_e, X0_j, m_e, m_j, num_steps):
    X_e = np.array(X0_e, dtype=float)
    X_j = np.array(X0_j, dtype=float)
    
    time_step = 60 * 60 * 24  # 1 day in seconds
    x_e_values = []
    y_e_values = []
    x_j_values = []
    y_j_values = []
    
    for _ in range(num_steps):
        x_e_values.append(X_e[0])
        y_e_values.append(X_e[1])
        x_j_values.append(X_j[0])
        y_j_values.append(X_j[1])
        
        X_e_derivs, X_j_derivs = ode_func(X_e, X_j)
        
        X_e += time_step * np.array(X_e_derivs)
        X_j += time_step * np.array(X_j_derivs)
    
    return x_e_values, y_e_values, x_j_values, y_j_values

num_steps = 366  # Number of steps (days in a year)
earth_x, earth_y, jupiter_x, jupiter_y = euler(X0_e, X0_j, m_e, m_j, num_steps)

# Plot the orbits
plt.figure(figsize=(8, 6))
plt.plot(earth_x, earth_y, label='Earth Orbit')
plt.plot(jupiter_x, jupiter_y, label='Jupiter Orbit')
plt.scatter(0, 0, color='yellow', label='Sun', marker='o', s=1000)
plt.xlabel('X Position (meters)')
plt.ylabel('Y Position (meters)')
plt.title('Orbits of Earth and Jupiter around the Sun')
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# import time

# def tic():
#     return time.time()

# def toc(start_time):
#     end_time = time.time()
#     return end_time - start_time

# def f(arr):
#     x, y, z = arr[0], arr[1], arr[2]
#     x_prime = 1
#     y_prime = z
#     z_prime = -y
#     return np.array([x_prime, y_prime, z_prime])

# def euler(step_size, f, start_vals, stopx):
#     dx = step_size
#     startx, starty, startz = start_vals[0], start_vals[1], start_vals[2]
#     n = round(abs(stopx - startx) / dx)
#     xyz_vals = [start_vals]
    
#     for i in range(n):
#         print(xyz_vals[-1][0],xyz_vals[-1][1])
#         next_val = xyz_vals[-1] + f(xyz_vals[-1]) * dx
#         xyz_vals.append(next_val)
#         if xyz_vals[-1][1]<0: 
#             print(xyz_vals[-1][0],xyz_vals[-1][1])
#             break
    
#     x_grid = [point[0] for point in xyz_vals]
#     y_grid = [point[1] for point in xyz_vals]
    
#     plt.grid(True)
#     plt.plot(x_grid, y_grid)  # Fixed the variables used here
#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.title('Euler Method')
#     plt.show()

# euler(1e-4, f, [0, 1, 0], 2*np.pi)
