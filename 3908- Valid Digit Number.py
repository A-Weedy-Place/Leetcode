class Solution(object):
    def validDigit(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: bool
        """
        n = str(n)
        if n[0] == str(x):
            return False
        for i in n:
            if i == str(x):
                return True
        return False 
    