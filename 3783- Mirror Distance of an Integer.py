class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        r = str(n)
        rev = ""
        for i in range(len(r)-1,-1,-1):
            rev = rev + r[i]
        return abs(n-int(rev))   