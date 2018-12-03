from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot


# https://www.quantstart.com/articles/Jacobi-Method-in-Python-and-NumPy

def jacobi(A, b, N=25, x=None):
    """Solves the equation Ax=b via the Jacobi iterative method."""
    # Create an initial guess if needed
    if x is None:
        x = zeros(len(A[0]))

    # Create a vector of the diagonal elements of A
    # and subtract them from A
    D = diag(A)
    R = A - diagflat(D)

    # Iterate for N times
    for i in range(N):
        x = (b - dot(R, x)) / D
    return x


A = array([[0.00979566, 0.00678165, 0.00678165, 0.0051862],
           [0.00678165, 0.00979566, 0.0051862, 0.00678165],
           [0.00678165, 0.0051862, 0.00979566, 0.00678165],
           [0.0051862, 0.00678165, 0.00678165, 0.00979566]])
b = array([1250.0, 1550, 1100, 1400])
guess = array([0.0, 0.0, 0.0,0.0])

sol = jacobi(A, b, N=25, x=guess)

print("A:")
pprint(A)

print("b:")
pprint(b)

print("x:")
pprint(sol)
