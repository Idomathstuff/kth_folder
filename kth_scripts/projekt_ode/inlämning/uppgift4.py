#vad är pi
import numpy as np
import matplotlib.pyplot as plt
import json
from decimal import Decimal, getcontext


def f(arr):
    x, y, z = arr[0], arr[1], arr[2]
    x_prime = 1
    y_prime = z
    z_prime = -y
    return np.array([x_prime, y_prime, z_prime])

def linear_interpolate(x_1,x_2,y_1,y_2):
    m = (y_2-y_1)/(x_2-x_1)
    y_noll = 0
    x_noll = (y_noll-y_1)/m + x_1
    return x_noll




def runge_kutta(step_size, f, start_vals, stopx):
    dx = step_size
    startx, starty, startz = start_vals[0], start_vals[1], start_vals[2]
    n = round(abs(stopx - startx) / dx)
    xyz_vals = [start_vals]
    for i in range(n):
        print(i, xyz_vals[-1][0], xyz_vals[-1][1])
        if xyz_vals[-1][1] < 0: 
            print("Before interpolation skattning: ",2*xyz_vals[-1][0])
            break

        k1 = f(xyz_vals[-1])
        k2 = f(xyz_vals[-1] + 0.5 * dx * k1)
        k3 = f(xyz_vals[-1] + 0.5 * dx * k2)
        k4 = f(xyz_vals[-1] + dx * k3)
        
        next_val = xyz_vals[-1] + dx * (k1 + 2 * k2 + 2 * k3 + k4) / 6.0 
        xyz_vals.append(next_val)
    
    x = [point[0] for point in xyz_vals]
    y = [point[1] for point in xyz_vals]
    
    return x,y


def make_json_file():
    x_values, y_values = runge_kutta(1e-6 , f, [0, 1, 0], 2*np.pi)
    data = {
        "x_values": x_values,
        "y_values": y_values
    }
    json_file = "runge_kutta_data.json"
    with open(json_file, "w") as json_out:
        json.dump(data, json_out)

# make_json_file()

def get_json_data():
    json_file = "runge_kutta_data.json"
    with open(json_file, "r") as json_in:
        data = json.load(json_in)
    x_values = data["x_values"]
    y_values = data["y_values"]
    return x_values, y_values

x_values, y_values = get_json_data()



def interpolation(t1, t2, y1, y2):
    a = (y2 - y1)/(t2 - t1)
    b =(y1 - t1*a)
    return (-2*b/a)

pi_estimate = interpolation(x_values[-2],x_values[-1],y_values[-2],y_values[-1])
print(pi_estimate)

print("målet: ", round(np.pi,20))

