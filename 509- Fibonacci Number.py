class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [0,1]
        if n == 0:
            return 0
        for i in range(n-1):
            f.append(f[-1]+f[-2])
        return f[-1]