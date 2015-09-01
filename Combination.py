__author__ = 'andrewwhiter'

'''
Find all combinations of r items from a list of n items
Number of combinations = n! / r!(n-r)!
eg
>>> Combinations([1, 2, 3], 2]
>>> [[1,2],[1,3],[2,3]]
'''

def combination(inlist, r):
    if len(inlist) < r:
        raise Exception("combination: r({}) is greater than length of inlist({})".format(r,len(inlist)))
    elif len(inlist) == r:
        return [inlist]
    elif r==1:
        return [[item] for item in inlist]
    else:
        return [[inlist[0]] + c for c in combination(inlist[1:],r-1)] + combination(inlist[1:],r)


if __name__ == '__main__':
    ans = combination(list(range(6)), 4)
    print ("no of combinations = ",len(ans))
    print ("combinations:\n", ans)