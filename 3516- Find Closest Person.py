class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        x = abs(z-x)
        y = abs(z-y)
        if x == y:
            return 0
        elif x > y:
            return 2
        else:
            return 1
        