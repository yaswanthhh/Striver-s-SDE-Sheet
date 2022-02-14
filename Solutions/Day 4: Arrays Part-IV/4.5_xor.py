#Source: https://www.interviewbit.com/problems/subarray-with-given-xor/
from collections import defaultdict

class Solution:
    def solve(self, A, B):
        prevXOR = dict()
        currXOR = 0
        prevXOR[0] = 1
        cnt = 0
        for a in A:
            currXOR = currXOR ^ a
            if (currXOR ^ B) in prevXOR:
                cnt += prevXOR[currXOR ^ B]
            if currXOR in prevXOR:
                prevXOR[currXOR] += 1
            else:
                prevXOR[currXOR] = 1
        return cnt
