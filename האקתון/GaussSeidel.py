# https://github.com/nuhferjc/gauss-seidel/blob/master/gaussseidel.py
def gaussSeidel(A, b, x, N, tol):
    maxIterations = 1000000
    xprev = [0.0 for i in range(N)]
    for i in range(maxIterations):
        for j in range(N):
            xprev[j] = x[j]
        for j in range(N):
            summ = 0.0
            for k in range(N):
                if k != j:
                    summ = summ + A[j][k] * x[k]
            x[j] = (b[j] - summ) / A[j][j]
        diff1norm = 0.0
        oldnorm = 0.0
        for j in range(N):
            diff1norm = diff1norm + abs(x[j] - xprev[j])
            oldnorm = oldnorm + abs(xprev[j])
        if oldnorm == 0.0:
            oldnorm = 1.0
        norm = diff1norm / oldnorm
        if (norm < tol) and i != 0:
            print("Sequence converges to [", end="")
            for j in range(N - 1):
                print(x[j], ",", end="")
            print(x[N - 1], "]. Took", i + 1, "iterations.")
            return
    print("Doesn't converge.")


A = [[0.00979566, 0.00678165, 0.00678165, 0.0051862],
     [0.00678165, 0.00979566, 0.0051862, 0.00678165],
     [0.00678165, 0.0051862, 0.00979566, 0.00678165],
     [0.0051862, 0.00678165, 0.00678165, 0.00979566]]
b = [1250.0, 1550, 1100, 1400]
guess = [0.0, 0.0, 0.0, 0.0]

gaussSeidel(A, b, guess, 4, 0.00000000000001)
