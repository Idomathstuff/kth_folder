import math
from decimal import Decimal, getcontext

getcontext().prec = 30

def f(t, x, y):
    return -y

def g(t, x, y):
    return x

def RK4_2d(tn, xn, yn, h):
    miu1 = h * Decimal(f(tn, xn, yn))
    v1 = h * Decimal(g(tn, xn, yn))
    miu2 = h * Decimal(f(tn + h/Decimal(2), xn + miu1/Decimal(2), yn + v1/Decimal(2)))
    v2 = h * Decimal(g(tn + h/Decimal(2), xn + miu1/Decimal(2), yn + v1/Decimal(2)))
    miu3 = h * Decimal(f(tn + h/Decimal(2), xn + miu2/Decimal(2), yn + v2/Decimal(2)))
    v3 = h * Decimal(g(tn + h/Decimal(2), xn + miu2/Decimal(2), yn + v2/Decimal(2)))
    miu4 = h * Decimal(f(tn + h, xn + miu3, yn + v3))
    v4 = h * Decimal(g(tn + h, xn + miu3, yn + v3))

    x_next = Decimal(xn + (miu1 + 2*miu2 + 2*miu3 + miu4)/Decimal(6))
    y_next = Decimal(yn + (v1 + 2*v2 + 2*v3 + v4)/Decimal(6))

    return x_next, y_next

def interpolation(t1, t2, y1, y2):
    a = Decimal(y2 - y1)/Decimal(t2 - t1)
    b = Decimal(y1 - t1*a)
    return Decimal(-b/a)

# Variables
tau = Decimal('1e-20')
h1 = Decimal('1e-1')
xn = Decimal('0')
yn = Decimal('1')
tn = Decimal('0')

root_list = []

# Finding roots
while tn <= 1002 + h1:  # Loop until just past 1000
    x_next, y_next = RK4_2d(tn, xn, yn, h1)
    if (y_next < Decimal(0)) != (yn < Decimal(0)):  # Check for a root
        root = interpolation(tn, tn + h1, yn, y_next)
        root_list.append((root, abs(root - 1000)))  # Store root and its distance from 1000
    tn += h1
    xn = x_next
    yn = y_next

# Find the root closest to 1000
root_closest_to_1000 = min(root_list, key=lambda x: x[1])[0]  # Select the root with the smallest distance to 1000
print("Root closest to 1000 is at t =", root_closest_to_1000)