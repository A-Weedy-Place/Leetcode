class Solution(object):
    def removeZeros(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = str(n)
        x = ""
        for i in n:
            if i != "0":
                x += i
        return int(x)