class Solution(object):
    def rotate(self, matrix):
        for i in range(len(matrix)):
            for j in range (i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in matrix:
            i.reverse()
