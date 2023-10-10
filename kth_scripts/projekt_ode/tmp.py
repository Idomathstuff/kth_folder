import numpy as np
import matplotlib.pyplot as plt

#  kutte
def runge_kutta(y_prime, y0, z0, t0, t_end, dt):
    y = y0
    z = z0
    t = t0
    while y > 0:  # Fortsätt tills y korsar x-axeln
        k1_y = dt * z
        k1_z = dt * y_prime(t, y, z)
        
        k2_y = dt * (z + 0.5*k1_z)
        k2_z = dt * y_prime(t + 0.5*dt, y + 0.5*k1_y, z + 0.5*k1_z)
        
        k3_y = dt * (z + 0.5*k2_z)
        k3_z = dt * y_prime(t + 0.5*dt, y + 0.5*k2_y, z + 0.5*k2_z)
        
        k4_y = dt * (z + k3_z)
        k4_z = dt * y_prime(t + dt, y + k3_y, z + k3_z)
        
        y += (k1_y + 2*k2_y + 2*k3_y + k4_y) / 6
        z += (k1_z + 2*k2_z + 2*k3_z + k4_z) / 6
        t += dt
    return t, y

# Definiera differentialekvationen y'' + y = 0
def system(t, y, z):
    return -y

# Initialvillkor
y0 = 1
z0 = 0

dt = 1e-8

t_cross, y_cross = runge_kutta(system, y0, z0, 0, 10, dt)

# Skatta π
pi_estimate = 2 * t_cross

print(f"Skattning av π med Runge-Kutta: {pi_estimate:.20f}")
print(f"actual value: {np.pi}")

# Plotta 
t_values = np.arange(0, t_cross + dt, dt)
y_values = [y0 * np.exp(-t_val) for t_val in t_values]  #  lösning y(t) = y0 * e^(-t)
plt.plot(t_values, y_values, label="Analytisk lösning")
plt.axhline(0, color='black', linewidth=0.5)
plt.legend()
plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("Lösning av y'' + y = 0")
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
