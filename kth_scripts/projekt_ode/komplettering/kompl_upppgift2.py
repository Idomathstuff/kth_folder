

#I think this is a cute solution, although I'm not sure if we are allowed to do it like this...
# Code Copied and modified from Stack Overflow

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

def solve_diff_eq(C, epsilon, t_max, h):
    # Define my differential equation
    def f(t, y):
        return C * y**2

    # Initialize arrays for t and y values
    t_values = np.arange(0, t_max, h)
    y_values = []

    y = epsilon

    for t in t_values:
        y_values.append(y)
        y_next = y + h * f(t, y)

        # Check for overflow and limit the value of y
        if abs(y_next) > 1e10:
            y_next = np.sign(y_next) * 1e10

        y = y_next

    return t_values, y_values

# Initial conditions
t_start = 100
t_stop = 1000
N = 10000  # Number of steps
h = (t_stop - t_start) / N

# Define the epsilon value and C values
epsilon = -1e-3
C_values = [10, 50, 100, 500]

# Plot the solutions
plt.figure(figsize=(8, 6))

for C in C_values:
    t_values, y_values = solve_diff_eq(C, epsilon, t_stop, h)
    plt.plot(t_values, y_values, label=f'C = {C}')

plt.axhline(0, color='gray', linestyle='--')
plt.xlabel('Time (t)')
plt.ylabel('y(t)')
plt.title("Numerical Solution of y' = Cy^2")
plt.legend()
plt.grid(True)
plt.show()

