import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

a = np.array(np.random.beta(2,2,50))
b = np.array(np.random.beta(2,2,50))

plt.scatter(a,b)
plt.scatter(a[0],b[0], color="green", marker="o", label="starting point")
plt.scatter(a[-1],b[-1], color="red", marker="o", label="end")

for i in range(len(a) - 1):
    ax.annotate('', xy=(a[i + 1], b[i + 1]), xytext=(a[i], b[i]),arrowprops=dict(arrowstyle='->', lw=1))
ax.legend()
plt.show()