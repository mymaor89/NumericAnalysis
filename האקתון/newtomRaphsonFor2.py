# ניטון רפסון
import sympy
from sympy.parsing.sympy_parser import parse_expr


def derivative(y, x1):
    return y.diff(x).evalf(subs={x: x1})


def evaluate(y, x1):
    return y.evalf(subs={x: x1})


def newton(y, x1, eps):
    iteration = 1
    h = evaluate(y, x1) / derivative(y, x1)
    while abs(h) >= eps:
        h = evaluate(y, x1) / derivative(y, x1)
        print("iteration: ", iteration, "f(x)= ", evaluate(y, x1))
        x1 = x1 - h
        h = evaluate(y, x1) / derivative(y, x1)
        iteration += 1
    return x1


x0 = float(input('choose x0 '))
x = sympy.Symbol('x')
# formula = parse_expr(input('type function '), evaluate=False)
formula = parse_expr(str(x ** 3 + 2 * (x ** 2) + 10 * x - 20))
epsilon = float(input('choose epsilon '))
solution = newton(formula, x0, epsilon)
print("solution is: ", solution)
print("Half the root is: ", solution / 2)
