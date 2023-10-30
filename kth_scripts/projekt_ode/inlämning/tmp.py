import math
import matplotlib.pyplot as plt
import numpy as np
from mpmath import mp
mp.dps = 21  # Set the desired number of decimal places
from decimal import Decimal, getcontext
getcontext().prec = 30

def ff(arr):
    x, y, z = arr[0], arr[1], arr[2]
    x_prime = 1
    y_prime = z
    z_prime = -y
    return np.array([x_prime, y_prime, z_prime])




def g(t, x, y):
    return x

def f(t, x, y):
    return -y

def RK4_euler():
    pass

def RK4_2d(tn, xn, yn, h):



    miu1, v1 = h * Decimal(f(tn, xn, yn)), h * Decimal(g(tn, xn, yn))
    miu2, v2 = h * Decimal(f(tn + h/Decimal(2), xn + miu1/Decimal(2), yn + v1/Decimal(2))), h * Decimal(g(tn + h/Decimal(2), xn + miu1/Decimal(2), yn + v1/Decimal(2)))
    miu3, v3 = h * Decimal(f(tn + h/Decimal(2), xn + miu2/Decimal(2), yn + v2/Decimal(2))), h * Decimal(g(tn + h/Decimal(2), xn + miu2/Decimal(2), yn + v2/Decimal(2)))
    miu4, v4 = h * Decimal(f(tn + h, xn + miu3, yn + v3)), h * Decimal(g(tn + h, xn + miu3, yn + v3))

    x_next = Decimal(xn + (miu1 + 2*miu2 + 2*miu3 + miu4)/Decimal(6))
    y_next = Decimal(yn + (v1 + 2*v2 + 2*v3 + v4)/Decimal(6))

    return x_next, y_next

def interpolation(t1, t2, y1, y2):
    a = Decimal(y2 - y1)/Decimal(t2 - t1)
    b =Decimal(y1 - t1*a)
    return Decimal(-b/a)



tau = Decimal('1e-20')
h1 = Decimal('1e-4')
xn = Decimal('0')
yn = Decimal('1')
tn = Decimal('0')

while yn > 0:
    x_next, y_next = RK4_2d(tn, xn, yn, h1)
    if (y_next < Decimal(0)) != (yn < Decimal(0)):
        ans = interpolation(tn, tn + h1, yn, y_next)
        break
    tn += h1
    xn = x_next
    yn = y_next



print("       ",round(2*ans,20))
print("målet: ", mp.pi)
