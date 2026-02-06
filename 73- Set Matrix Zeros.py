class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range (m):
            for j in range (n):
                if matrix[i][j] == 0:
                    for x in range (n):
                        if matrix[i][x] != 0:
                            matrix[i][x] = 999
                    for y in range (m):
                        if matrix[y][j] != 0:
                            matrix[y][j] = 999
        for i in range (m):
            for j in range (n):
                if matrix[i][j] == 999:
                    matrix[i][j] = 0