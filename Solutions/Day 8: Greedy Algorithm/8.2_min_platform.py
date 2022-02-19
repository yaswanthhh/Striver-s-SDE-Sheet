class Solution:    
    
    def minimumPlatform(self,n,arr,dep):
        arr.sort()
        dep.sort()
        max, ctr, d = 0, 0, 0
        for i in range(n):
            while d < i and dep[d] < arr[i]:
                ctr -= 1
                d += 1
            ctr += 1
            if max<ctr:
                max = ctr
        return max
