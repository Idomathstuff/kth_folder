import numpy as np
import matplotlib.pyplot as plt
G = 6.67430e-11  # Gravitationskonstanten 
M = 1.989e30    # mass of sun kg
m_j = 1.898e27 # mass of jupiter
m_e = 5.97e24 # mass of earth
AU = 1.496e11 # astronomical unit
X0_e = [AU, 0, 0, 2.978e4]
X0_j = [5*AU, 0 ,0, 1.307e4]

time_step = 60*60*24

def ode_func(X_e,X_j):
    x_e ,y_e, vx_e, vy_e = X_e
    x_j, y_j, vx_j, vy_j = X_j
    r_e = np.linalg.norm([x_e,y_e])
    r_j = np.linalg.norm([x_j,y_j])
    r_e_to_j = np.linalg.norm([x_e-x_j,y_e-y_j])
    ax_e = -x_e*G*M/r_e**3 -(x_j-x_e)*G*m_j/r_e_to_j**3
    ay_e = -y_e*G*M/r_e**3 -(y_j-y_e)*G*m_j/r_e_to_j**3
    ax_j = -x_j*G*M/r_j**3 -(x_e-x_j)*G*m_j/r_e_to_j**3
    ay_j = -y_j*G*M/r_j**3 -(y_e-y_j)*G*m_j/r_e_to_j**3
    x_e_prime = vx_e + ax_e*time_step
    y_e_prime = vy_e + ay_e*time_step
    x_j_prime = vx_j + ax_j*time_step
    y_j_prime = vy_j + ay_j*time_step

    X_e_derivs = [x_e_prime,y_e_prime,ax_e,ay_e]
    X_j_derivs = [x_j_prime,y_j_prime,ax_j,ay_j]
    return X_e_derivs,X_j_derivs

def euler(X0_e,X0_j):
    X_e = np.array(X0_e)
    X_j = np.array(X0_j)
    X_e_values = []
    X_j_values = []
    n = 366
    for i in range(n):
        X_e_values.append(X_e)
        X_j_values.append(X_j)
        X_e_derivs,X_j_derivs = ode_func(X_e,X_j)
        X_e += time_step*np.array(X_e_derivs)
        X_j += time_step*np.array(X_j_derivs)
    return np.array(X_e_values),np.array(X_j_values)

X_e_values,X_j_values = euler(X0_e,X0_j)

print(X_e_values)
# print()

x_e_values, y_e_values = X_e_values[:, 0], X_e_values[:, 1]
x_j_values, y_j_values = X_j_values[:, 0], X_j_values[:, 1]

# print(x_e_values)
# plt.plot(x_e_values, y_e_values, label='Earth')
# plt.plot(x_j_values, y_j_values, label='Jupiter')
