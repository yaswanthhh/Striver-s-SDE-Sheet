import operator as op
from functools import reduce

class Solution(object):
    def uniquePaths(self, m, n):
        r = 0
        N = n + m - 2
        r = m - 1
        res = 1
        r = min(r, N-r)
        numer = reduce(op.mul, range(N, N-r, -1), 1)
        denom = reduce(op.mul, range(1, r+1), 1)
        return numer // denom 
