# שיטת המיתר
import sympy
from sympy.parsing.sympy_parser import parse_expr
import matplotlib.pyplot as plt
import numpy as np


def secant(a, b, y, eps, max_iter):
    f_a = y.evalf(subs={x: a})
    f_b = y.evalf(subs={x: b})
    if f_a * f_b >= 0:
        print("Secant method fails.")
        return
    iteration = 1
    a_n = a
    b_n = b
    while iteration <= max_iter:  # and abs(xn_1 - xn) > eps:
        f_a = y.evalf(subs={x: a_n})
        f_b = y.evalf(subs={x: b_n})
        if f_a * f_b >= 0:
            print("Something bad had happened")
            return
        line = (f_b - f_a) / (b_n - a_n) * (z - a_n) + f_a
        ax.plot(z, line)
        m_n = a_n - f_a * (b_n - a_n) / (f_b - f_a)
        print("iteration: ", iteration, "m= ", m_n, "a =", a_n, " b = ", b_n)
        f_m = y.evalf(subs={x: m_n})
        iteration += 1
        if f_a * f_m < 0:
            b_n = m_n
        elif f_m * f_b < 0:
            a_n = m_n
        elif f_m == 0:
            print("exact solution: ", m_n)
        else:
            print("Secant method fails.")
            return None
    m_n = a_n - f_a * (b_n - a_n) / (f_b - f_a)
    f_m = y.evalf(subs={x: m_n})
    ax.annotate('Root',
                xy=(m_n, f_m), xycoords='data',
                xytext=(-50, 30), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"))
    return m_n


x1 = float(input('choose x1 '))
x2 = float(input('choose x2 '))
x = sympy.Symbol('x')
m = int(input('choose max iterations '))
# formula = parse_expr(input('type function '), evaluate=False)
formula = parse_expr(str(x ** 3 + 2 * (x ** 2) + 10 * x - 20))
epsilon = float(input('choose epsilon '))
z = np.arange(0.0, 2.0, 0.01)
y = z ** 3 + 2 * (z ** 2) + 10 * z - 20
fig, ax = plt.subplots()
ax.plot(z, y)
result = secant(x1, x2, formula, epsilon, m)
ax.set(xlabel='x', ylabel='f(x)',
       title='Secant method ' + 'f(x)= ' + formula.__str__())
ax.grid()
plt.show()
print("root/2 is: ", result/2)
