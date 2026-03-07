class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        num1, num2 = 0,0
        x = 1
        while x<=n:
            if x%m == 0:
                num2 += x
            else:
                num1 += x
            x += 1
        return num1-num2