#https://gist.github.com/aurelienpierre/1d9826e7db078e048bf437e516a7a4b2
from sympy import Symbol, simplify, lambdify
import numpy as np
import matplotlib.pyplot as plt
from functools import reduce
import operator


def interpolate_lagrange(x, x_values, y_values):
    """
    x : value at which to evaluate y, should be between min and max x_values
    x_values: list or numpy array containing values of x
    y_values: list or numpy array contaning values of y
    """

    def _basis(j):
        p = [(x - x_values[m]) / (x_values[j] - x_values[m]) for m in range(k) if m != j]
        return reduce(operator.mul, p)

    assert len(x_values) != 0 and (
            len(x_values) == len(y_values)), 'x and y cannot be empty and must have the same length'
    k = len(x_values)
    return sum(_basis(j) * y_values[j] for j in range(k))


x = Symbol('x')
poly = simplify(interpolate_lagrange(x, [2, 3, 6], [-3.5, 1.25, 4.1]))
print(str(poly))
x1 = np.linspace(-1, 2, 100)
y1 = lambdify(x, poly)(x1)

fig, ax = plt.subplots()
ax.plot(x1, y1)
ax.scatter([2, 3, 6], [-3.5, 1.25, 4.1], c='r')
plt.show()
