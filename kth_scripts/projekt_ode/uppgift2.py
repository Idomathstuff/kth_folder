#pang

import numpy as np
import matplotlib.pyplot as plt
import time

def tic():
    return time.time()

def toc(start_time):
    end_time = time.time()
    return end_time - start_time



for i in range(2):
    C=10**i
    def f(x, y):
        return float(C*y**2)

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
        for a, b in zip(x, y):
            print(round(a, 2), round(b, 2))
        return x,y
    x,y = euler(0.01, f, -5,0,10)
    plt.grid(True)
    plt.plot(x, y, label="C= "+str(C))
    plt.title('Euler Method')
plt.legend()
plt.show()