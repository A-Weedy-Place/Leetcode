class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = [0] * n
        if n == 1:
            return 1
        x[0] = 1
        x[1] = 2
        for i in range(2,n):
            x[i] = x[i-1]+x[i-2]
        return x[-1]