class Solution(object):        
    def generate(self, numRows):
        pascals_triangle = []
        for i in range(numRows):
            temp = []
            for j in range(0, i+1):
                if j > i-j:
                    j = i-j
                res = 1
                for l in range(j):
                    res *= (i-l)
                    res //= l+1
                temp.append(res)
            pascals_triangle.append(temp)
        return pascals_triangle
