import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.arange(0.0, 2.0, 0.01)
y = x ** 3 - np.cos(x)
# s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(x, y)

ax.set(xlabel='x', ylabel='f(x)',
       title='Secant method')
ax.grid()
plt.show()
