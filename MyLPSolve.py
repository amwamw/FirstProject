__author__ = 'andrewwhiter'

# The idea with this example is to show how a brute force algorithm might be developed
# from scratch to solve Linear Programming models

import numpy as np
from prettytable import PrettyTable   # may need to install this
from pprint import pprint
from itertools import combinations
import time


def matstr(mat):
    p = PrettyTable()
    for row in mat:
        p.add_row(row)
    return p.get_string(header=False, border=False)

def addNonNegConstraints(A,b):
    rows, cols = np.shape(A)
    I = np.eye(cols)      # creates an Identity matrix (noVars x noVars)
    A = np.bmat("A;I")
    b = np.append(b,[0 for _ in range(cols)])
    return A,b

def findCornerPointSolutions(A,b):
    '''
    corner points are found by solving combination of the boundary line/plane constraints
    when there are n decision variables need to find all combinations of n constraints out of the set of all constraints
    including the non-neg ones
    uses the combinations function from the itertools package
    uses linalg.solve function from numpy
    :param A:
    :param b:
    :return: a list of corner point solutions - each consisting of the constraints from A and b that form the point
             and the solution at that point
    '''
    noconstraints, novars = np.shape(A)
    cps = []
    for constraint_set in combinations(range(noconstraints),novars):
        cpA = np.bmat([[A[i]]for i in constraint_set])
        cpb = np.array([b[i] for i in constraint_set])
        try:
            sol = np.linalg.solve(cpA,cpb)
            if isFeasibleCP(sol, A, b):
                cps += [[cpA,cpb,sol]]           # only add the solution when one can be found and FEASIBLE
        except:
            pass
    return cps




def isFeasibleCP(sol, A, b):
    '''
    assumes A & b hold the full set of boundary constraints INCLUDING the non-zero decision variable constraints
    :param sol:  a solution list of decision variable values
    :param A:
    :param b:
    :return:
    '''
    if min(sol)<0: return False
    else:
        rows, cols = np.shape(A)
        for i in range(rows-cols):     # rows-cols ensures only the less-than-equal constraints are considered - not the non-zero ones
            if np.dot(A[i],sol)>b[i]: return False
        else:
            return True


def FindBestCPF(cps, c):
    bestsol = np.dot(c,cps[0][2])
    at = [cps[0][2]]
    for i in range(2,len(cps)):
        nextsol = np.dot(c,cps[i][2])
        if abs(nextsol-bestsol)<1e-5:
            at.append(cps[i][2])
        elif nextsol>bestsol:
            bestsol = nextsol
            at = [cps[i][2]]
    return bestsol, at




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
    print ("A:\n",A)
    b = np.array([4, 7, 5])
    print ("b:\n",b)
    A,b = addNonNegConstraints(A,b)
    print ("A+non-neg:\n",A)
    print ("b+non-neg:\n",b)
    cps = findCornerPointSolutions(A,b)
    print("no of corner point feasible solutions = ", len(cps) )
    # pprint(cps)
    c = np.array([2, 3, 2])
    sol, at = FindBestCPF(cps, c)
    print("optimal solution = ",sol , " with ", len(at), " corner points")
    print("solutions: ", at)
    print("--- %s seconds ---" % (time.time() - start_time))

    print("\n\nAIR CARGO OPTIMSATION PROBLEM\n")
    start_time = time.time()
    A = np.mat('''1	 0	 0	 1	 0	 0	 1	 0	 0	 1	 0	 0;
 0	 1	 0	 0	 1	 0	 0	 1	 0	 0	 1	 0;
 0	 0	 1	 0	 0	 1	 0	 0	 1	 0	 0	 1;
1	 1	 1	 0	 0	 0	 0	 0	 0	 0	 0	 0;
 0	 0	 0	1	 1	 1	 0	 0	 0	 0	 0	 0;
 0	 0	 0	 0	 0	 0	1	 1	 1	 0	 0	 0;
 0	 0	 0	 0	 0	 0	 0	 0	 0	1	 1	 1;
 500	 0	 0	 700	 0	 0	 600	 0	 0	 400	 0	 0;
 0	 500	 0	 0	 700	 0	 0	 600	 0	 0	 400	 0;
 0	 0	 500	 0	 0	 700	 0	 0	 600	 0	 0	 400''')
    print ("A:\n",A)
    b = np.array([12,18,10,20,16,25,13,7000,9000,5000])
    print ("b:\n",b)
    A,b = addNonNegConstraints(A,b)
    print ("A+non-neg:\n",A)
    print ("b+non-neg:\n",b)
    cps = findCornerPointSolutions(A,b)
    print("no of corner point feasible solutions = ", len(cps) )
    # pprint(cps)
    c = np.array([320,320,320,400,400,400,360,360,360,290,290,290])
    sol, at = FindBestCPF(cps, c)
    print("optimal solution = ",sol , " at ", len(at), " corner points")
    print("solutions: ", np.mat(at))
    print("--- %s seconds ---" % (time.time() - start_time))


