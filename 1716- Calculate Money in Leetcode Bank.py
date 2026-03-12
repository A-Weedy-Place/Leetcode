class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        x = 0
        while True:
            for i in range(7):
                x += 1
                n -= 1
                total += x
                if n == 0:
                    return total
            x -= 6