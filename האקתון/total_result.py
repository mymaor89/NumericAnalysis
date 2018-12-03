import sympy
from sympy.parsing.sympy_parser import parse_expr
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot

k = 3.75
miu = 0.00373
c = 0.6844
h = 150
N = 2
area_length = 200
m = [1250, 1550, 1100, 1400]
x = []
D = array([[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]])

# R_i_j_1_and_2 = 180.277
# R_i_j_3 = 206.15

R = array([[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]])
for i in range(4):
    R[i][i] = h
R[0][1] = 180.277
R[0][2] = 180.277
R[0][3] = 206.15
R[1][0] = 180.277
R[1][2] = 206.15
R[1][3] = 180.277
R[2][0] = 180.277
R[2][1] = 206.15
R[2][3] = 180.277
R[3][0] = 206.15
R[3][1] = 180.277
R[3][2] = 180.277

for i in range(4):
    for j in range(4):
        D[i][j] = c * (1 + k * h) * 2.71828182846 ** (-miu * h) / R[i][j] ** 2
pprint(D)
