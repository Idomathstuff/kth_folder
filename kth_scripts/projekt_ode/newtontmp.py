import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Konstanter
G = 6.67430e-11  # Gravitationskonstanten (m^3 kg^-1 s^-2)
M = 1.989e30    # Massan av solen (kg)

# System av differentialekvationer
def system(Y, t):
    x, y, vx, vy = Y
    r = np.sqrt(x**2 + y**2)
    ax = -G * M * x / r**3
    ay = -G * M * y / r**3
    return [vx, vy, ax, ay]

# Initialvärden
x0 = 1.496e11    # 1 AU i meter
y0 = 0
vx0 = 0
vy0 = 29.78e3    # Jordens genomsnittliga orbitalhastighet (m/s)

Y0 = [x0, y0, vx0, vy0]

# Tidsintervall
t = np.linspace(0, 365*24*3600, 1000)  # Ett år i sekunder

# Lös systemet
sol = odeint(system, Y0, t)

# Plotta
plt.figure(figsize=(10, 6))
plt.plot(sol[:, 0], sol[:, 1], label="Planetens bana")
plt.plot(0, 0, 'yo', label="Solen")
plt.title("Planetens bana runt solen")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
