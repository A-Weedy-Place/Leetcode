class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n >= 10:  # reduce n to a single digit
            total = 0
            while n > 0:
                total += (n % 10) ** 2
                n //= 10
            n = total
        
        return n == 1 or n == 7