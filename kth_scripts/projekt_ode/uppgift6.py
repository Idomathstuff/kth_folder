import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
G = 6.67430e-11  # Gravitationskonstanten 
M = 1.989e30    # mass of sun kg
m_j = 1.898e28 # mass of jupiter
m_j = 1.898e29 # mass of jupiter

m_e = 5.97e24 # mass of earth
m_s = 2e4 # mass of space ship
AU = 1.496e11 # astronomical unit

X0_e = np.array([-AU, 0, 0, 2.978e4]) # initial x,y,vx,vy
X0_j = np.array([3*AU, 0 ,0, 1.307e4])
X0_s = np.array([-1.1*AU, 0, 0, -3.5e4]) # ändra initial hastighet för rymdskeppet för att lämna solsystemet
time_step = 60*60*24 

def ode_func(X_e,X_j,X_s):
    x_e ,y_e, vx_e, vy_e = X_e
    x_j, y_j, vx_j, vy_j = X_j
    x_s, y_s, vx_s, vy_s = X_s
    
    r_e =np.sqrt(x_e**2+y_e**2)
    r_j = np.sqrt(x_j**2+y_j**2)
    r_e_to_j = np.sqrt((x_e-x_j)**2+(y_e-y_j)**2)
    r_s = np.sqrt(x_s**2+y_s**2)
    r_s_to_j = np.sqrt((x_s-x_j)**2+(y_s-y_j)**2)
    r_s_to_e = np.sqrt((x_s-x_e)**2+(y_s-y_e)**2)
    
    ax_e = -x_e*G*M/r_e**3 -(x_j-x_e)*G*m_j/r_e_to_j**3
    ay_e = -y_e*G*M/r_e**3 -(y_j-y_e)*G*m_j/r_e_to_j**3
    ax_j = -x_j*G*M/r_j**3 -(x_e-x_j)*G*m_e/r_e_to_j**3
    ay_j = -y_j*G*M/r_j**3 -(y_e-y_j)*G*m_e/r_e_to_j**3
    ax_s = -x_s*G*M/r_s**3 -(x_e-x_s)*G*m_e/r_s_to_e**3 -(x_j-x_s)*G*m_j/r_s_to_j**3
    ay_s = -y_s*G*M/r_s**3 -(y_e-y_s)*G*m_e/r_s_to_e**3 -(y_j-y_s)*G*m_j/r_s_to_j**3
    
    # if np.abs(r_s - r_j) < 1.1 * r_j and np.sqrt(vx_s**2 + vy_s**2) < 10e3:
    #     vx_s += 5e3
    #     vy_s += 2e3

    x_e_prime = vx_e + ax_e*time_step
    y_e_prime = vy_e + ay_e*time_step
    x_j_prime = vx_j + ax_j*time_step
    y_j_prime = vy_j + ay_j*time_step
    x_s_prime = vx_s + ax_s*time_step
    y_s_prime = vy_s + ay_s*time_step
    
    X_e_derivs = np.array([x_e_prime,y_e_prime,ax_e,ay_e])
    X_j_derivs = np.array([x_j_prime,y_j_prime,ax_j,ay_j])
    X_s_derivs = np.array([x_s_prime, y_s_prime, ax_s, ay_s])
    return X_e_derivs,X_j_derivs,X_s_derivs

def euler(X0_e,X0_j,X0_s):
    X_e = np.array(X0_e)
    X_j = np.array(X0_j)
    X_s = np.array(X0_s)
    x_e_values = []
    y_e_values = []
    x_j_values = []
    y_j_values = []
    x_s_values = []
    y_s_values = []
    n = 5000
    for i in range(n):
        x_e_values.append(X_e[0])
        y_e_values.append(X_e[1])
        x_j_values.append(X_j[0])
        y_j_values.append(X_j[1])
        x_s_values.append(X_s[0])
        y_s_values.append(X_s[1])
        X_e_derivs,X_j_derivs,X_s_derivs = ode_func(X_e,X_j,X_s)
        X_e += time_step*np.array(X_e_derivs)
        X_j += time_step*np.array(X_j_derivs)
        X_s += time_step*np.array(X_s_derivs)

        # state = True
        # if np.sqrt((x_s_values[-1]-x_j_values[-1])**2+(y_s_values[-1]-y_j_values[-1])**2)<np.sqrt((X_s[0]-X_j[0])**2 + (X_s[1]-X_j[1])**2) and state:
            # state=False
            # X_s[3]+=2e3
    return x_e_values,y_e_values, x_j_values,y_j_values, x_s_values,y_s_values


x_e_values, y_e_values, x_j_values, y_j_values, x_s_values, y_s_values = euler(X0_e,X0_j,X0_s)



fig, ax = plt.subplots()
plt.plot(x_e_values,y_e_values, color = "cyan")
plt.plot(x_j_values,y_j_values, color = "orange")
plt.plot(x_s_values,y_s_values,marker='o',markersize=0.1)
plt.scatter(0,0, color="yellow")

earth, = ax.plot([], [], 'o', color='cyan', markersize=5)
jupiter, = ax.plot([], [], 'o', color='orange', markersize=5)
spaceship, = ax.plot([], [], 'o', color='blue', markersize=5)
sun = ax.plot(0, 0, 'yo', markersize=5)
ax.set_xlim(-8 * AU, 8 * AU)
ax.set_ylim(-8 * AU, 8 * AU)


def init():
    earth.set_data([], [])
    jupiter.set_data([], [])
    spaceship.set_data([], [])
    return earth, jupiter, spaceship


def animate(i):
    x_e, y_e, x_j, y_j, x_s, y_s = x_e_values[i], y_e_values[
        i], x_j_values[i], y_j_values[i], x_s_values[i], y_s_values[i]
    earth.set_data(x_e, y_e)
    jupiter.set_data(x_j, y_j)
    spaceship.set_data(x_s, y_s)
    return earth, jupiter, spaceship


ani = FuncAnimation(fig, animate, init_func=init,
                    frames=len(x_e_values), repeat=False, blit=True, interval=0.0001)


plt.show()
