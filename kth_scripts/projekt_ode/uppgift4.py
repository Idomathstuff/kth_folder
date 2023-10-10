#vad är pi
import numpy as np
import matplotlib.pyplot as plt
import time

def f(arr):
    x, y, z = arr[0], arr[1], arr[2]
    x_prime = 1
    y_prime = z
    z_prime = -y
    return np.array([x_prime, y_prime, z_prime])


def runge_kutta(step_size, f, start_vals, stopx):
    dx = step_size
    startx, starty, startz = start_vals[0], start_vals[1], start_vals[2]
    n = round(abs(stopx - startx) / dx)
    xyz_vals = [start_vals]

    for i in range(n):
        print(i, xyz_vals[-1][0], xyz_vals[-1][1])
        if xyz_vals[-1][1] < 0: 
            print(xyz_vals[-1][0])
            return
        k1 = f(xyz_vals[-1])
        k2 = f(xyz_vals[-1] + 0.5 * dx * k1)
        k3 = f(xyz_vals[-1] + 0.5 * dx * k2)
        k4 = f(xyz_vals[-1] + dx * k3)
        
        next_val = xyz_vals[-1] + (dx / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        xyz_vals.append(next_val)
    
    x_grid = [point[0] for point in xyz_vals]
    y_grid = [point[1] for point in xyz_vals]
    
    plt.grid(True)
    plt.plot(x_grid, y_grid)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Runge-Kutta Method')
    plt.show()

runge_kutta(1e-5 , f, [0, 1, 0], 2*np.pi)

print(round(np.pi/2,20))
