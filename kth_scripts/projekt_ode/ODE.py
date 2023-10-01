# # euler method
# import numpy as np
# import matplotlib as matlib
# import matplotlib.pyplot as plt
# import time

# def tic():
#     return time.time()
# def toc(start_time):
#     end_time = time.time()
#     return end_time-start_time


# def f(x,y):
#     return float(np.sqrt(abs(y)))

# def eulery(step_size, f, starty,startx, stopy):
#     tau = 10**-4
#     dx = step_size
#     x = [startx]
#     y = [starty]
#     k = 0
#     while abs(y[k]-stopy)>tau:
#         y.append(x[k])
#         x.append(y[k])
#         y[k+1] = y[k]+f(x[k],y[k])*dx
#         x[k+1] += dx
#         k+=1
#     plt.plot(x,y)
#     plt.show()
#     for a,b in zip(x,y):
#         print(round(a,2),round(b,2))
# # def euler(step_size, f, starty,startx, stopx):
# #     dx = step_size
# #     n = round(abs(stopx-startx)/dx)
# #     x = [float(dx*(e))+startx for e in list(range(n))]
# #     y = [starty]*n
# #     for k in range(n):
# #         if k == 0:
# #             continue
# #         y[k] = y[k-1]+f(x[k-1],y[k-1])*dx
# #     for a,b in zip(x,y):
# #         print(round(a,2),round(b,2))
# #     plt.plot(x,y)
# #     plt.show()

# def euler(step_size, f, startx, starty, stopx):
#     num_steps = round(abs(stopx - startx) / step_size)
#     x = np.linspace(startx, stopx, num=num_steps)
#     y = np.zeros_like(x)
#     y[0] = starty

#     for k in range(1, num_steps):
#         y[k] = y[k - 1] + f(x[k - 1], y[k - 1]) * step_size

#     plt.plot(x, y)
#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.title('Euler Method Approximation')
#     plt.grid(True)
#     plt.show()

# def backward_euler(step_size, f, start_y, start_x, stop_x):
#     dx = step_size
#     n = round(abs(stop_x - start_x) / dx)
#     x = [float(dx * e) + start_x for e in list(range(n))]
#     y = [start_y]

#     for k in range(1, n):
#         x_k = x[k]
#         y_k_prev = y[k - 1]
#         y_k = y_k_prev + dx * f(x_k, y_k_prev)

#         y.append(y_k)

#     plt.plot(x, y)
#     plt.show()
#     print(x)

# def runge_kutta(step_size, f, start_y, start_x, stop_x):
#     dx = step_size
#     n = round(abs(stop_x - start_x) / dx)
#     x = [float(dx * e) + start_x for e in list(range(n))]
#     y = [-start_y] * n

#     for k in range(n):
#         if k == 0:
#             continue
#         x_k = x[k - 1]
#         y_k = y[k - 1]
#         k1 = dx * f(x_k, y_k)
#         k2 = dx * f(x_k + dx / 2, y_k + k1 / 2)
#         k3 = dx * f(x_k + dx / 2, y_k + k2 / 2)
#         k4 = dx * f(x_k + dx, y_k + k3)
#         y[k] = y_k + (k1 + 2 * k2 + 2 * k3 + k4) / 6

#     plt.plot(x, y)
#     plt.show()
#     print(x)

# euler(0.001,f,12.5,-5,5)

# # backward_euler(0.01,f,-1,-1,0)
# # eulery(0.01,f,-1,-1,0)

import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return np.sqrt(abs(y))

def euler_method(f, x0, y0, h, x_end):
    x_values = [x0]
    y_values = [y0]
    while x0 < x_end:
        y0 = y0 + h * f(x0, y0)
        x0 = x0 + h
        x_values.append(x0)
        y_values.append(y0)

    return x_values, y_values


def plot(method,x0,y0,x_end):
    h = 0.0001    
    x_values, y_values = method(f, x0, y0, h, x_end)
    plt.plot(x_values, y_values, label='Approximate Solution', color='b')
    plt.xlabel('x')
    plt.ylabel('y')
    # plt.title('Euler\'s Method for y\' = f(x, y)')
    plt.grid()
    plt.legend()
    plt.show()
    for a,b in zip(x_values,y_values):
        print(a,b)

plot(euler_method,-1,-1+0.0001,15)
