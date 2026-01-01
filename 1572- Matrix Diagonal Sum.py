class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n = 0
        m = len(mat) - 1
        sum = 0
        for i in range(len(mat)):
            if n != m:
                sum += mat[i][n] + mat[i][m]
            else:
                sum += mat[i][n]
            n += 1
            m -= 1
        return sum