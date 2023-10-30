import numpy as np
import matplotlib.pyplot as plt

from tabulate import tabulate

plt.style.use('seaborn-darkgrid')

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

def analytical_solution(x, starty):
    return starty * np.exp(x)

def plot_global_fel_plots():
    N = 50
    results = []
    k_values = range(9,10)
    for k in k_values:
        final_y_analytical = analytical_solution(2**k, N)
        x_euler, y_euler = euler(0.01, f, N, 0, 2**k)
        global_difference = [abs(final_y_analytical-y_euler[i]) for i in range(len(y_euler))]
        # plt.plot(x_euler,y_euler)
        plt.plot(x_euler, abs(analytical_solution(np.array(x_euler), N)-np.array(y_euler)))
        plt.yscale('log')
        # plt.xscale('log')
        # plt.scatter(x_euler, global_difference)
    plt.show()

def plot_local_fel_with_k():
    N = 50
    results = []
    k_values = range(1, 10)
    for k in k_values:
        x_euler, y_euler = euler(0.01, f, N, 0, 2 ** k)
        final_y_euler = y_euler[-1]
        try:
            x_rk4, y_rk4 = runge_kutta(0.01, f, N, 0, 2 ** k)
            final_y_rk4 = y_rk4[-1]
        except Exception:
            final_y_rk4 = "N/A"

        analytical_y = analytical_solution(2 ** k, N)

        results.append([k, final_y_euler, final_y_rk4, analytical_y])

    k_values = [2**result[0] for result in results]
    difference_values = [abs(result[1] - result[3]) for result in results]
    plt.plot(k_values, difference_values, linestyle='-')
    plt.yscale('log')
    plt.xlabel('$x_{\t{final}}=2^k$')
    plt.ylabel('$|y_{Euler}(2^k) - y_{Analytical}(2^k)|$')
    plt.title('Fel termen av euler metod vs. $2^k$')
    plt.show()


def generate_latex_table():
    N = 50
    results = []
    k_values = range(1, 10)
    for k in k_values:
        x_euler, y_euler = euler(0.01, f, N, 0, 2 ** k)
        final_y_euler = y_euler[-1]
        try:
            x_rk4, y_rk4 = runge_kutta(0.01, f, N, 0, 2 ** k)
            final_y_rk4 = y_rk4[-1]
        except Exception:
            final_y_rk4 = "N/A"  # Placeholder for expensive or non-converging cases
        analytical_y = analytical_solution(2 ** k, N)
        results.append([k, final_y_euler, final_y_rk4, analytical_y])
    table = tabulate(results, headers=["k", "Final y (Euler)", "Final y (RK4)", "Analytical y"], tablefmt="latex_raw")
    print(table)

# plot_local_fel_with_k()