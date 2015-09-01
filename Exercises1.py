__author__ = 'andrewwhiter'

# CHALLENGE 1:
# Find the positive factor pairs of a positive integer without opposite combination
# e.g. FactorPairs(6) -> [[1,6], [2,3]]    note that [3,2] and [6,1] are not included
# for the integers 1 to 12 we get
# 1  :  [[1, 1]]
# 2  :  [[1, 2]]
# 3  :  [[1, 3]]
# 4  :  [[1, 4], [2, 2]]
# 5  :  [[1, 5]]
# 6  :  [[1, 6], [2, 3]]
# 7  :  [[1, 7]]
# 8  :  [[1, 8], [2, 4]]
# 9  :  [[1, 9], [3, 3]]
# 10  :  [[1, 10], [2, 5]]
# 11  :  [[1, 11]]
# 12  :  [[1, 12], [2, 6], [3, 4]]

# def FactorPairs(m):
#     if m==1:
#         return [[1,1]]
#     else:
#         factors = [1,m]
#         factorPairs = [[1,m]]
#         for i in range(2,m//2+1):
#             if m%i == 0 and m//i not in factors:
#                 factors.append(i)
#                 factorPairs.append([[i,m//i]])
#         return factorPairs

# def FactorPairs(m):
#     factorPairs = [[1,m]]
#     for i in range(2,m//2+1):
#         if m%i == 0 and i <= m//i:
#             factorPairs.append([i,m//i])
#     return factorPairs

def FactorPairs(m):
    return [[i, m//i] for i in range(1,m//2+(2 if m==1 else 1)) if m%i==0 and i <= m//i]


# for i in range(1,31):
#     print(i, " : ", FactorPairs(i))

# CHALLENGE 2:
# now extend this to give all positive and negative factor combinations
# for the integers -4 to +4 we get
# -4  :  [[-1, 4], [-2, 2], [1, -4], [2, -2]]
# -3  :  [[-1, 3], [1, -3]]
# -2  :  [[-1, 2], [1, -2]]
# -1  :  [[-1, 1], [1, -1]]
# 0  :  []
# 1  :  [[1, 1], [-1, -1]]
# 2  :  [[1, 2], [-1, -2]]
# 3  :  [[1, 3], [-1, -3]]
# 4  :  [[1, 4], [2, 2], [-1, -4], [-2, -2]]

def AllFactorPairs(m):
    if m>0:
        return FactorPairs(m)+[[-f1,-f2] for f1, f2 in FactorPairs(m)]
    elif m<0:
        return [[-f1,f2] for f1, f2 in FactorPairs(-m)]+[[f1,-f2] for f1, f2 in FactorPairs(-m)]
    else:
        return []

# for i in range(-10,11):
#     print(i, " : ", AllFactorPairs(i))

# CHALLENGE 3:
# Now write a function to factorise a simple quadratic equation whose roots are positive or negative integers
# ie. find r1 and r2 such that (x+r1)(x+r2) = x^2 + bx + c, where r1, r2, b, c are all integers
# Hint: r1 and r2 should be a factor pair of the integer c
# eg FindIntegerRoots(b=-4, c=3) -> [-1,-3]   for the factorisation x^2 -4x + 3 = (x-1)(x-3)


def FindIntegerRoots(b, c):
    for pair in AllFactorPairs(c):
        if sum(pair) == b:
            return pair

for b in range (-4,5):
    for c in range (-4,5):
        roots = FindIntegerRoots(b,c)
        if roots != []:
            print("x^2+{}x+{} = (x+{})(x+{})".format(b,c,*roots).replace("+-","-"))

from sympy import *
x = symbols('x')
init_printing()
print(x^2+3x-5)


