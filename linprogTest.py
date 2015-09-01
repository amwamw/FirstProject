__author__ = 'andrewwhiter'


from scipy.optimize import linprog

'''
linprog(method=’Simplex’)

scipy.optimize.linprog(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=None, method='simplex', callback=None,
    options={'disp': False, 'bland': False, 'tol': 1e-12, 'maxiter': 1000})

Solve the following linear programming problem via a two-phase simplex algorithm.

MINMIZE: c^T * x

subject to: A_ub * x <= b_ub
            A_eq * x == b_eq


Returns:
A scipy.optimize.OptimizeResult consisting of the following fields:
x : ndarray
    The independent variable vector which optimizes the linear
    programming problem.
slack : ndarray
    The values of the slack variables.  Each slack variable corresponds
    to an inequality constraint.  If the slack is zero, then the
    corresponding constraint is active.
success : bool
    Returns True if the algorithm succeeded in finding an optimal
    solution.
status : int
    An integer representing the exit status of the optimization::
     0 : Optimization terminated successfully
     1 : Iteration limit reached
     2 : Problem appears to be infeasible
     3 : Problem appears to be unbounded
nit : int
    The number of iterations performed.
message : str
    A string descriptor of the exit status of the optimization.
'''

import numpy as np
import time

if __name__ == '__main__':

    print("\n\nPROBLEM FROM SIMPLEX.PY\n")
    start_time = time.time()

    """
    max z = 2x + 3y + 2z
    st
    2x + y + z <= 4
    x + 2y + z <= 7
    z          <= 5
    x,y,z >= 0
    """
    A = np.mat("2 1 1;1 2 1;0 0 1")
    b = np.array([4, 7, 5])
    c = np.array([-2, -3, -2])

    # alternatively can use normal lists as inputs for A, b, c:
    # A=[[2,1,1],[1,2,1],[0,0,1]]
    # b=[4, 7, 5]
    # c=[-2, -3, -2]

    sol = linprog(c,A_ub=A, b_ub=b,bounds=(0,None),options={"disp": True})
    print(sol)

    print("--- %s seconds ---" % (time.time() - start_time))

    print("\n\nAIR CARGO OPTIMSATION PROBLEM\n")
    start_time = time.time()
    A = np.mat('''
 1	 0	 0	 1	 0	 0	 1	 0	 0	 1	 0	 0;
 0	 1	 0	 0	 1	 0	 0	 1	 0	 0	 1	 0;
 0	 0	 1	 0	 0	 1	 0	 0	 1	 0	 0	 1;
 1	 1	 1	 0	 0	 0	 0	 0	 0	 0	 0	 0;
 0	 0	 0	1	 1	 1	 0	 0	 0	 0	 0	 0;
 0	 0	 0	 0	 0	 0	1	 1	 1	 0	 0	 0;
 0	 0	 0	 0	 0	 0	 0	 0	 0	1	 1	 1;
 500	 0	 0	 700	 0	 0	 600	 0	 0	 400	 0	 0;
 0	 500	 0	 0	 700	 0	 0	 600	 0	 0	 400	 0;
 0	 0	 500	 0	 0	 700	 0	 0	 600	 0	 0	 400''')
    b = np.array([12,18,10,20,16,25,13,7000,9000,5000])
    c = np.array([320,320,320,400,400,400,360,360,360,290,290,290])

    sol = linprog(c*-1,A_ub=A, b_ub=b,bounds=(0,None),options={"disp": True})
    print(sol)
    print("--- %s seconds ---" % (time.time() - start_time))
