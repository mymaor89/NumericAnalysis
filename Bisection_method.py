# שיטת החציה
import sympy
from sympy.parsing.sympy_parser import parse_expr


def bisection(a, b, y, eps):
    iteration = 1
    while b - a > eps:
        m = (a + b) / 2
        f_m = y.evalf(subs={x: m})
        print("iteration: ", iteration, " m = ", m)
        if f_m * f_a > 0:  # התעלם מחצי שמאלי
            a = m
        else:
            b = m  # התעלם מחצי ימני
        iteration += 1
    return m


x1 = float(input('choose x1 '))
x2 = float(input('choose x2 '))
x = sympy.Symbol('x')
formula = parse_expr(input('type function '), evaluate=False)
epsilon = float(input('choose epsilon '))
f_a = formula.evalf(subs={x: x1})
f_b = formula.evalf(subs={x: x2})
if f_a * f_b == 0:
    if f_a == 0:
        print("x = ", a)
    elif f_b == 0:
        print("x = ", b)
elif f_a * f_b < 0:
    print("solution is: ", bisection(x1, x2, formula, epsilon))
else:
    print("No roots in the given interval")
