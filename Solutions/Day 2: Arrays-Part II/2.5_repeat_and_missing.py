class Solution:
    def repeatedNumber(self, A):
        n = len(A)
        x = sum(A) - sum(set(A))
        k = sum(A) - int(n*(n+1)/2)
    
        return [x,x-k]
