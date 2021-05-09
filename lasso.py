import cvxpy as cp 

def lasso(A, y):
    m, n = A.shape
    print(m,n)
    x = cp.Variable((n, 1))
    objective = cp.Minimize(cp.sum_squares(A @ x - y) + cp.norm(x, 1))
    constraints = [x >= 0]
    p = cp.Problem(objective, constraints)
    p.solve(solver='SCS', eps=1e-5)
    # p.solve()

    return x.value