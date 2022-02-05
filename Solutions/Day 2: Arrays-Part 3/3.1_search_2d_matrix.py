class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in matrix:
            if i[len(matrix[0])-1] >= target:
                for j in i:
                    if j == target:
                        return True
                return False
        return False
