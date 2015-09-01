__author__ = 'andrewwhiter'

# Bug fix: if 'lhs[i] == 0' should be 'lhs[i] less than equal 1e-5'

# from __future__ import division
from numpy import *
# from fractions import Fraction

from prettytable import PrettyTable   # may need to install this

class Tableau:

    def __init__(self, obj):
        self.obj = [1] + obj
        self.rows = []
        self.cons = []

    def add_constraint(self, expression, value):
        self.rows.append([0] + expression)
        self.cons.append(value)

    def _pivot_column(self):
        low = 0
        idx = 0
        for i in range(1, len(self.obj)-1):
            if self.obj[i] < low:
                low = self.obj[i]
                idx = i
        if idx == 0: return -1
        return idx

    def _pivot_row(self, col):
        rhs = [self.rows[i][-1] for i in range(len(self.rows))]
        lhs = [self.rows[i][col] for i in range(len(self.rows))]
        ratio = []
        for i in range(len(rhs)):
            if lhs[i] <= 1e-5: # Bug fix  == 0:
                ratio.append(99999999 * abs(max(rhs)))
                continue
            ratio.append(rhs[i]/lhs[i])
        return argmin(ratio)

    def display(self):
        # print ('\n', matrix([self.obj] + self.rows))
        p = PrettyTable()
        for row in ([self.obj] + self.rows):
            p.add_row(row)
        print(p.get_string(header=False, border=False))

    def _pivot(self, row, col):
        e = self.rows[row][col]
        self.rows[row] /= e
        print("dividing row {} by {}:".format(row+2,e))
        self.display()
        for r in range(len(self.rows)):
            if r == row: continue
            self.rows[r] = self.rows[r] - self.rows[r][col]*self.rows[row]
            print("   making zero in row {} col {}:".format(r+2,col+1))
            self.display()
        self.obj = self.obj - self.obj[col]*self.rows[row]

    def _check(self):
        if min(self.obj[1:-1]) >= 0: return 1
        return 0

    def solve(self):

        # build full tableau
        for i in range(len(self.rows)):
            self.obj += [0]
            ident = [0 for r in range(len(self.rows))]
            ident[i] = 1
            self.rows[i] += ident + [self.cons[i]]
            self.rows[i] = array(self.rows[i], dtype=float)
        self.obj = array(self.obj + [0], dtype=float)

        # solve
        self.display()
        while not self._check():
            c = self._pivot_column()
            r = self._pivot_row(c)
            self._pivot(r,c)
            print('\npivot column: {}\npivot row: {}'.format(c+1,r+2))
            self.display()

if __name__ == '__main__':

    """
    max z = 2x + 3y + 2z
    st
    2x + y + z <= 4
    x + 2y + z <= 7
    z          <= 5
    x,y,z >= 0
    """

    t = Tableau([-2,-3,-2])
    t.add_constraint([2, 1, 1], 4)
    t.add_constraint([1, 2, 1], 7)
    t.add_constraint([0, 0, 1], 5)

    t.solve()
