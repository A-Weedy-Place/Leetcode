class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        s = 0
        for i in x:
            s += int(i)
        if int(x) % s == 0:
            return s
        else:
            return -1   