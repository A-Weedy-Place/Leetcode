class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = [int(i) for i in str(n)]
        n.sort()
        return n[-1] * n[-2]