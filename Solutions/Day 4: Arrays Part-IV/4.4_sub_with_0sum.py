class Solution:
    def maxLen(self, n, a):
        d = {}
        sum = 0
        maxl = 0
        for i in range(n):
            sum += a[i]
            if sum == 0:
                if maxl < i:
                    maxl = i+1
            elif sum in d:
                if maxl < i - d[sum]:
                    maxl = i - d[sum]
            else:
                d[sum] = i
        return maxl
