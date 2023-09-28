# euler method
import numpy as np
import matplotlib as matlib
import matplotlib.pyplot as plt
def f(y):
    if y<0:
        return float(np.sqrt(-y))
    elif 0<=y:
        return float(np.sqrt(y))



def euler(step_size, f, starty,startx, stopx):
    dx = step_size
    n = round(abs(stopx-startx)/dx)
    x = [float(dx*(e))+startx for e in list(range(n))]
    y = [-starty]*n
    for k in range(n):
        if k == 0:
            continue
        y[k] = y[k-1]+f(y[k-1])*dx
    plt.plot(x,y)
    
    plt.show()
    print(x)

euler(0.01,f,-1,-1,0)
