class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        xlen = len(matrix[0])
        ylen = len(matrix)
        
        x0 = []
        y0 = []
        for i in range (ylen):
            for j in range (xlen):
                if matrix[i][j] == 0:
                    x0.append(i) 
                    y0.append(j)
                    
        for i in range (ylen):
            for j in range (xlen):
                if i in x0 or j in y0:
                    matrix[i][j] = 0
