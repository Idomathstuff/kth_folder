#existense men inte entydighet
import numpy as np
import matplotlib.pyplot as plt
import time
plt.style.use('seaborn-darkgrid')
def tic():
    return time.time()

def toc(start_time):
    end_time = time.time()
    return end_time - start_time

def y(x,c):
    if x>-c:
        return ((x+c)/2)**2
    else:
        return -((x+c)/2)**2

def f(x, y):
    return float(np.sqrt(abs(y)))

def euler(step_size, f, starty, startx, stopx):
    dx = step_size
    n = round(abs(stopx - startx) / dx)
    x = [startx]
    y = [starty]
    for k in range(n):
        next_x = x[-1]+dx
        next_y = y[-1]+dx*f(x[-1],y[-1])
        x.append(next_x)
        y.append(next_y)
    return x,y


def runge_kutta(step_size, f, start_y, start_x, stop_x):
    dx = step_size
    n = round(abs(stop_x - start_x) / dx)
    x = [start_x]
    y = [start_y]
    for i in range(n):
        if i == 0:
            continue
        k1 = dx* f(x[-1], y[-1])
        k2 = dx*f(x[-1] + 0.5*dx, y[-1] + 0.5*k1)
        k3 = dx *f(x[-1] + 0.5*dx, y[-1] + 0.5*k2)
        k4 = dx *f(x[-1] + dx, y[-1] + k3)
        next_y = y[-1] + (k1 + 2*k2 + 2*k3 + k4) / 6
        next_x = x[-1]+dx
        x.append(next_x)
        y.append(next_y)
    return x,y

x1, y1 = euler(0.011, f, -1, -1, 5)
def get_interval(x_values,y_values):
    n_steps = len(x_values)
    for i in range(1,n_steps):
        if y_values[i-1]<0 and y_values[i]>0:
            lower_bound = x_values[i-1]
            upper_bound = x_values[i]
            return lower_bound, upper_bound

def plot_interval_against_step_size():
    step_size_arr = [2**(-i) for i in range(1,12)]
    interval_lengths_arr = []
    for step_size in step_size_arr:
        x_values, y_values = euler(step_size, f, -1, -1, 5)
        lower_bound, upper_bound = get_interval(x_values, y_values)
        interval_lengths_arr.append(upper_bound - lower_bound)

    log_step_size_arr= [np.log2(step) for step in step_size_arr]
    log_interval_lengths_arr = [np.log2(length) for length in interval_lengths_arr]
    plt.title("Interval against step size")
    plt.xlabel("$|h|$")
    plt.ylabel("$|(x_0+h)-(x_0-h)|$")
    plt.scatter(step_size_arr, interval_lengths_arr)
    plt.show()
# plot_interval_against_step_size()

# print(get_interval(x1,y1))

# plt.grid(True)
# plt.scatter(x1,y1, marker=".", label=r"numerisk lösning, $h=0.1$")
# plt.plot(x1,[y(np.array(x),-1) for x in x1],color="orange", label=r"analytisk lösning")
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.show()

def make_inf_sol_demo():
    dt = 0.1
    a = 5
    x0 = -a-10
    y0 = 0
    f = lambda x: (x/2)**2
    x_values = np.array([x0+dt*i for i in range(300)])
    y_values = []
    for x in x_values:
        if x < -a:
            y_values.append(-f(x+a))
        elif x>a:
            y_values.append(f(x-a))
        else:
            y_values.append(0)
    plt.plot(x_values, y_values)
    plt.scatter(-a,0)
    plt.scatter(a,0)

    # Add labels to the scatter points
    plt.text(-a, 0, '-a', fontsize=12, ha='right', va='bottom')
    plt.text(a, 0, '+a', fontsize=12, ha='left', va='bottom')
    plt.show()

make_inf_sol_demo()




