#pang
import matplotlib.pyplot as plt

def f(C,x, y):
    return C * y ** 2

    

def euler(C, step_size, f, starty, startx, stopx):
    dx = step_size
    n = round(abs(stopx - startx) / dx)
    x = [startx]
    y = [starty]
    for k in range(n):
        next_x = x[-1]+dx
        next_y = y[-1] + dx*f(C,x[-1], y[-1])
        x.append(next_x)
        y.append(next_y)
    return x, y


def runge_kutta(C, step_size, f, starty, startx, stopx):
    dx = step_size
    x = [startx]
    y = [starty]
    while x[-1] < stopx:
        k1 = dx * f(C, x[-1], y[-1])
        k2 = dx * f(C, x[-1] + dx / 2, y[-1] + k1 / 2)
        k3 = dx * f(C, x[-1] + dx / 2, y[-1] + k2 / 2)
        k4 = dx * f(C, x[-1] + dx, y[-1] + k3)
        next_y = y[-1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        next_x = x[-1] + dx
        x.append(next_x)
        y.append(next_y)
    return x, y

def warmup():
    N = 50
    x_values,y_values = euler(1,0.01,f,N/100,0,2) # smäller när x=2
    plt.plot(x_values,y_values, label="Euler")
    plt.show()

def plot_for_different_C():
    Cs= [1, 10, 50, 100, 250, 500, 1000, 2000]
    epsilon = -1e-3
    for C in Cs:
        x_values, y_values = euler(C,0.1,f,epsilon,0,1000)
        print(y_values[-1])
        plt.plot(x_values, y_values, label=f"C = {C}")
    plt.title("y' = Cy^2 med eulerforward")
    plt.legend()
    plt.grid(True)
    plt.show()


plot_for_different_C()
