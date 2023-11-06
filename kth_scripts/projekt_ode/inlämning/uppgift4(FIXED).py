import math
import numpy as np
from mpmath import mp
mp.dps = 21  
from decimal import Decimal, getcontext
getcontext().prec = 30

def interpolation(t1, t2, y1, y2):
    a = Decimal(y2 - y1)/Decimal(t2 - t1)
    b =Decimal(y1 - t1*a)
    return Decimal(-b/a)

def get_approx(tyz_vals):
    t1, t2 = tyz_vals[-2][0], tyz_vals[-1][0]
    y1, y2 = tyz_vals[-2][1], tyz_vals[-1][1]
    return interpolation(t1,t2,y1,y2)

def yprime(t, y, z):
    return Decimal(z)

def zprime(t, y, z):
    return Decimal(-y)


root_data = []


def RK4_euler(step_size, start_vals, stopt):
    t_0, y_0, z_0 = Decimal(start_vals[0]), Decimal(start_vals[1]), Decimal(start_vals[2])
    tyz_vals = [[t_0,y_0,z_0]]
    dt = Decimal(step_size)
    n = round(abs(stopt-float(t_0))/step_size)
    for i in range(n):
        try:
            if np.sign(tyz_vals[-1][1]) != np.sign(tyz_vals[-2][1]) and tyz_vals[-1][0]!=stopt:
                # print("Before interp", tyz_vals[-1][0])
                root_data.append(get_approx(tyz_vals))
                # break
        except:
            pass
        tn, yn, zn = tyz_vals[-1]
        k1, v1 = yprime(tn, yn, zn), zprime(tn, yn, zn)
        k2, v2 = yprime(tn + dt/Decimal(2), yn + dt*k1/Decimal(2), zn + dt*v1/Decimal(2)), zprime(tn + dt/Decimal(2), yn + dt*k1/Decimal(2), zn + dt*v1/Decimal(2))
        k3, v3 = yprime(tn + dt/Decimal(2), yn + dt*k2/Decimal(2), zn + dt*v2/Decimal(2)), zprime(tn + dt/Decimal(2), yn + dt*k2/Decimal(2), zn + dt*v2/Decimal(2))
        k4, v4 = yprime(tn + dt, yn + dt*k3, zn + dt*v3), zprime(tn + dt, yn + dt*k3, zn + dt*v3)
        
        t_next = tn+dt
        y_next = yn + dt*(k1 + 2*k2 + 2*k3 + k4)/Decimal(6)
        z_next = zn + dt*(v1 + 2*v2 + 2*v3 + v4)/Decimal(6)
        tyz_vals.append([t_next,y_next,z_next])

    return tyz_vals



tyz_vals = RK4_euler(1e-2, [0,1,0], 1001)

# print("interp ", get_approx(tyz_vals))
# print("målet: ", mp.pi)
print("Root 1: ", root_data[-2])
print("Root 2: ", root_data[-1])
print("Difference between root approxiations: ", root_data[-1]-root_data[-2])