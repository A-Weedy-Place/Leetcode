class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        x = 0
        for i in range(1,n+1):
            if n % i == 0:
                x += 1
                if x == k:
                    return i
        return -1