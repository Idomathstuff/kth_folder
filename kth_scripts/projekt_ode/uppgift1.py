import numpy as np
import matplotlib.pyplot as plt
import time

def tic():
    return time.time()

def toc(start_time):
    end_time = time.time()
    return end_time - start_time

def y(x,c):
    if x>-c:
        return ((x+c)/2)**2
    else:
        return -((x+c)/2)**2

def f(x, y):
    return float(np.sqrt(abs(y)))

def euler(step_size, f, starty, startx, stopx):
    dx = step_size
    n = round(abs(stopx - startx) / dx)
    x = [startx]
    y = [starty]
    for k in range(n):
        next_x = x[-1]+dx
        next_y = y[-1]+ dx*f(x[-1],y[-1])
        x.append(next_x)
        y.append(next_y)
    # for a, b in zip(x, y):
    #     print(round(a, 2), round(b, 2))
    return x,y


x1,y1 = euler(0.01, f, -9/4, 0, 5)
x2,y2 = euler(0.1, f, -1, -1, 5)

plt.grid(True)
# plt.plot(x1, y1)
plt.scatter(x2,y2, marker=".", label=r"numerisk lösning, $h=0.1$")
plt.plot(x2,[y(np.array(x),-1) for x in x2],color="orange", label=r"analytisk lösning")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()



def runge_kutta(step_size, f, start_y, start_x, stop_x):
    dx = step_size
    n = round(abs(stop_x - start_x) / dx)
    x = [float(dx * e) + start_x for e in list(range(n))]
    y = [-start_y] * n

    for k in range(n):
        if k == 0:
            continue
        x_k = x[k - 1]
        y_k = y[k - 1]
        k1 = dx * f(x_k, y_k)
        k2 = dx * f(x_k + dx / 2, y_k + k1 / 2)
        k3 = dx * f(x_k + dx / 2, y_k + k2 / 2)
        k4 = dx * f(x_k + dx, y_k + k3)
        y[k] = y_k + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    plt.plot(x, y)
    plt.show()
    print(x)
