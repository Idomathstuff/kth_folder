#inte pang
import numpy as np
import matplotlib.pyplot as plt
import time

def f(x, y):
    return y

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
    return x,y

N=50
k = 9 # går inte att justera k högre än 9
x, y= euler(0.01,f,N,0,2**k)
print(y[-1])
plt.plot(x,y)
plt.show()